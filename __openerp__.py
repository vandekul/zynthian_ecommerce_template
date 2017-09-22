{
    'name': "Zynthian Ecommerce Template",
    'version': '1.0',
    'category': 'custom, website',
    'summary': 'Form ecommerce modification',
    'description': """
        Modification of:

        - website_sale.checkout (checkout.html) --> checkout_extend.xml
        -- Delete fields: VAT number and Company Name
        -- Delete Billing Address (it will be the same than Shipping Addpress)
        
        - website_sale.payment (payment.html) --> payment_extend.xml
            -- Change product layout  
            -- Delete showing Billing Address
            -- Show Delivey Address
        
        - website_sale.cart (shopping_cart.html) --> shopping_cart_extend.xml
            -- Delete Policies and Secure Payment
        
        -- website_sale.total (total.html) --> total_extend.xml / delivery_extend.xml
            -- Delete Taxes field

        """,
    'author': 'mumaker',
    'depends': ['website'],
    'data': [
        'views/checkout_extend.xml',
        'views/payment_extend.xml',
        'views/shopping_cart_extend.xml',
        'views/total_extend.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}