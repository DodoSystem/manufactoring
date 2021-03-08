{
    'name': "DDS - SK/CZ lokalizácia - Sklad",
    'summary': """
        Dodo Systems - SK/CZ lokalizácia - Sklad""",
    'description': """
        Dodo Systems - SK/CZ lokalizácia - Sklad
    """,
    'author': "Dodo Systems s.r.o.",
    'website': "http://www.dodosys.sk/",
    'category': 'Localization',
    'version': '1.4',
    'data': [        
        'report/report_deliveryslip.xml',
        'views/stock_picking_views.xml',
    ],
    'depends': ['base', 'dds_localization_sk', 'stock', 'web'],    
    'installable': True,    
    'application': False,
    'auto_install': False,
}