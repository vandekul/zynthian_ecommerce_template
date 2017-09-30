{
    'name': "Zynthian Ecommerce Template",
    'version': '1.0',
    'category' : 'Website',
    'website' : 'http://www.zynthian.org',
    'summary': 'Form ecommerce modification',
    'description': """
        Modification of:

        - website_sale.checkout (checkout.html) --> checkout_extend.xml
            --Delete fields: VAT number and Company Name
            --Delete Billing Address (it will be the same than Shipping Address)
            --Delete Sign In Button

        - website_sale.payment (payment.html) --> payment_extend.xml
            --Change product layout (table) 
            --Delete showing Billing Address
            --Show Only Delivey Address
            --Included Delivery Method in new template
        
        - website_sale.cart (shopping_cart.html) --> shopping_cart_extend.xml
            -- Delete Policies and Secure Payment
        
        - website_sale.total (total.html) --> total_extend.xml / delivery_extend.xml
            -- Delete Taxes field
	    -- Delete Subtotal field
            -- Included Delivery Costs before Total Costs

        - website_sale.wizard_checkout
            --Modify literal Shipping&Billing by Shipping Address

        Important:
        - Desactivar la vista Shipping Country and states (manualment de moment)
        """,
    'author': 'mumaker',
    'depends': ['website'],
    'data': [
        'views/shopping_cart_extend.xml',
        'views/total_extend.xml',
        'views/checkout_extend.xml',
        'views/payment_extend.xml',
        'views/wizard_checkout_extend.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
