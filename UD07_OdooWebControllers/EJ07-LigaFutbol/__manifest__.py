# -*- coding: utf-8 -*-
{
    'name': "Gestionar liga de futbol",  # Titulo del módulo
    'summary': "Gestionar una liga de futbol :) (Version avanzada)",  # Resumen de la funcionaliadad
    'description': """
    Gestor de Liga de futbol (Version avanzada)
    ==============
    """,

    #Indicamos que es una aplicación
    'installable': True,
    'application': True,
    'author': "Marcos Zahonero",
    'website': "http://prueba.es",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'report/liga_partido_report.xml',
        'views/liga_partido.xml',
        'views/liga_equipo.xml',
        'views/liga_equipo_clasificacion.xml',
        'report/liga_equipo_clasificacion_report.xml',
        'wizard/liga_equipo_wizard.xml',
        'wizard/liga_crear_partido_wizard.xml'
    ],
    'controllers': [
        'controllers/liga_partido_controller.py',
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
