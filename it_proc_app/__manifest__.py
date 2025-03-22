# -*- coding: utf-8 -*-
{
    'name': "it_proc_app",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        'security/it_proc_app_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_inherit_views.xml',
        'report/purchase_order_report.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],


    'application': True,
    'external_dependencies': {
        'python': ['num2words'],
    },
}

