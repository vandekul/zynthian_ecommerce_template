# -*- coding: utf-8 -*-
# Copyright 2015 Tecnativa - Jairo Llopis
# Copyright 2016 Tecnativa - Vicent Cubells
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import http
from openerp.http import request
from openerp.sql_db import TestCursor
from openerp import SUPERUSER_ID
from openerp.addons.website_sale.controllers.main import website_sale
import logging

_logger = logging.getLogger(__name__)

class website_sale_mandatory_mod(website_sale):
    
    @http.route(['/shop/confirm_order'], type='http', auth="public", website=True)
    def confirm_order(self, **post):
        self.mandatory_billing_fields  = ["name", "email", "phone", "street2", "city", "country_id", "zip"]
        self.optional_billing_fields   = ["vat","street", "state_id"]
        self.mandatory_shipping_fields = ["name", "email", "phone", "street2", "city", "country_id", "zip"]
        self.optional_shipping_fields  = ["state_id"]
        return super(website_sale_mandatory_mod,self).confirm_order(**post)

class RequireLegalTermsToCheckout(website_sale):
    def checkout_parse(self, address_type, data, remove_prefix=False,
                       *args, **kwargs):
        """Require accepting legal terms to buy."""
        result = (super(RequireLegalTermsToCheckout, self).
                  checkout_parse(address_type, data, remove_prefix,
                                 *args, **kwargs))

        # Avoid PhantomJS errors in test mode
        if (not isinstance(request.env.cr, TestCursor) and
                address_type == "billing"):
            result["accepted_legal_terms"] = (
                bool(request.params.get("accepted_legal_terms")))

        return result

    def checkout_form_save(self, checkout, *args, **kwargs):
        """Do not use accepting legal terms to save and get metadata"""
        res = super(RequireLegalTermsToCheckout, self).checkout_form_save(
            checkout, *args, **kwargs)
        if "accepted_legal_terms" in checkout:
            _logger.info("request.context: %s",request.context)
            del checkout["accepted_legal_terms"]
            user_obj = request.env['res.users']
            order = request.website.sale_get_order(
                force_create=1, context=request.context)
            partner_id = request.env['res.partner']
            if request.uid != request.website.user_id.id:
                partner_id = user_obj.browse(request.uid).partner_id
            elif order.partner_id:
                user_ids = user_obj.with_context(
                    dict(request.context, active_test=False)).search(
                    [("partner_id", "=", order.partner_id.id)])
                if not user_ids or request.website.user_id.id not in user_ids:
                    partner_id = order.partner_id
            if partner_id:
                environ = request.httprequest.headers.environ
                metadata = "Website legal terms acceptance metadata:<br/>"
                metadata += "<br/>".join(
                    "%s: %s" % (val, environ.get(val)) for val in (
                            "REMOTE_ADDR",
                            "HTTP_USER_AGENT",
                            "HTTP_ACCEPT_LANGUAGE",
                        )
                    )
                website_user = (request.website.salesperson_id.id or
                                SUPERUSER_ID)
                partner_id.sudo(website_user).message_post(body=metadata)
        return res

    def checkout_form_validate(self, data, *args, **kwargs):
        error, error_message = (super(RequireLegalTermsToCheckout, self).checkout_form_validate(data, *args, **kwargs))

        # If it is ``None``, then there is no need to check it
        if data.get("accepted_legal_terms") is False:
            error["accepted_legal_terms"] = 'missing'
            error_message.append('Acceptance legal terms required')
            #_logger.info('errors[accepted_legal_terms] = %s', errors["accepted_legal_terms"])

        return error, error_message
