# -*- coding: utf-8 -*-
{
    'name': "randomimagemarcos",

    'summary': "Genera imágenes aleatorias en Odoo usando un Web Controller",

    'description': """
Genera imágenes aleatorias en Odoo usando un Web Controller hecho por Marcos Zahonero.
    """,

    'author': "Marcos Zahonero",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
    'installable': True,
    'application': False,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

