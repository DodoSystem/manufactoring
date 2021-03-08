{
    'name': "DDS - SK/CZ lokalizácia",
    'summary': """
        Dodo Systems - SK/CZ lokalizácia""",
    'description': """
        Dodo Systems - SK/CZ lokalizácia
    """,
    'author': "Dodo Systems s.r.o.",
    'website': "http://www.dodosys.sk/",
    'category': 'Localization',
    'version': '2.15',
    'data': [        
        'views/account_move_views.xml',
        'views/res_partner_views.xml',
        'views/account_payment_view.xml',
        'views/sale_views.xml',
        'views/res_company_views.xml',
        'views/purchase_views.xml',    
        'views/sale_portal_templates.xml',          
        'report/report_templates.xml',
        'report/report_invoice.xml',
        'report/sale_report_templates.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_quotation_templates.xml',
    ],
    'depends': ['base', 'account', 'purchase', 'sale', 'web'],    
    'installable': True,    
    'application': False,
    'auto_install': False,
}