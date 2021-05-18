{
    'name': "Zynthian Ecommerce Template",
    'version': '1.0',
    'category' : 'Website',
    'website' : 'http://www.zynthian.org',
    'summary': 'Form ecommerce modification',
    'description': """
        Modification of:

        - website_sale.checkout (checkout.html) --> checkout_extend.xml
            [--Delete fields: VAT number and Company Name ] -> Active again 1/10/20
            --Delete State/Province field
            --Delete Billing Address (it will be the same than Shipping Address)
            --Delete Sign In Button
            [-- Prepared Invoice Required Info but not active, only VAT number that must be deleted from shipping form, it includes javaScript]

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
            * 1/10/20 : Not imported total_exend.xml

        - website_sale.wizard_checkout
            --Modify literal Shipping&Billing by Shipping Address

        - website_sale.product_categories_extend
            -- Delete "All products" tag
            -- Add List Categories for small devices

        - website_sale.product_extend
            -- Delete conditions of shipping

        - website_sale.cart_lines_extend
            -- Delete product description

        - assets.xml
            -- Edit ecommerce style

        - Acceptance policy included and also mandatory an required fiels to be validate from the form
            --  /controllers/main.py
        Important:
        - Desactivar la vista Shipping Country and states (manualment de moment)
        - Desactivar la vista Product Categories (website_sale.products_categories, manualment)
        """,
    'author': 'mumaker',
    'depends': ['website'],
    'data': [
        'views/shopping_cart_extend.xml',
        'views/checkout_extend.xml',
        'views/payment_extend.xml',
        'views/wizard_checkout_extend.xml',
        'views/product_categories_extend.xml',
        'views/product_extend.xml',
        'views/cart_lines_extend.xml',
        'views/reusable_templates.xml',
        'views/website_legal_footer_extend.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
