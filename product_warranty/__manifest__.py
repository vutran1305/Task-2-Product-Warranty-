# -*- coding: utf-8 -*-
{
    'name': "Product Warranty",

    'summary': """
       Product Sale""",

    'description': """
        Product Warranty
    """,

    'author': "Vu Tran",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale','contacts'],

    # always loaded
    'data': [
        'views/product_warranty_action_check_warranty.xml',
         'views/product_warranty_inherit.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/product_warranty_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
