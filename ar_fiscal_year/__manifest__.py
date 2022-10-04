# -*- coding: utf-8 -*-
{
    'name': "ar_fiscal_year",

    'summary': """
       """,

    'description': """
       add fiscal years, lock date
    """,

    'author': "Arados Software",
    'website': "http://www.arados-so.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '15.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/change_lock_date.xml',
        'views/fiscal_year.xml',
        'views/templates.xml',
        'views/settings.xml',
    ],

}
