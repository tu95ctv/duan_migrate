# -*- coding: utf-8 -*-
{
    'name': "tonkho",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of Duan migrate
    """,

    'author': "My Company duan migrate",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],
    #'css': ['static/src/css/style.css'], 
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
#         'views/tonkho.xml',
#         'views/stock_picking.xml',
#         'views/tonkho_stock.xml',
        'views/stock_quant.xml',
        'report/pick_operation_report.xml',
        
        #'views/assets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}