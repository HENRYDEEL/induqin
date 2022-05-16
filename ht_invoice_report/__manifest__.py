{
    "name": "Invoice Report",
    'category': 'Tools',
    'author': 'Hadoopt Technologies Private Limited',
    'website': 'www.hadoopt.com',
    'license': 'AGPL-3',
    'summary': '',
    "depends": [
        "base",
        "sale",
        "account",
        "web"
    ],
    
    'data': [
        'views/account_move.xml',
        'report/invoice_report.xml',
        'report/default_sale_order_report.xml',
        'report/default_invoice_report.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
