# -*- coding: utf-8 -*-
{
    'name': "Empresa Repartidores",
    'summary': "Gestión de repartimientos para una empresa de repartidores",

    'description': """
Gestión de repartimientos para una empresa de repartidores hecho y mantenido por Marcos Zahonero.
    """,

    'author': "Marcos Zahonero",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
    'installable': True,
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/wizard_repartimiento_views.xml',
        'views/report_repartimientos_pendientes.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

