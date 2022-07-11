{
    'name': 'Manufacturing Report',
    'version': '14.0',
    'summary': 'Manufacturing Report',
    'description': 'Reports for Manufacturing',
    'category': 'Manufacturing',
    'author': 'Hadoopt Technologies Private Limited',
    'website': 'https://hadoopt.com',
    'depends': [
        'base',
        'mrp'
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/mrp_report.xml',
        'report/production_order_report.xml',
        'views/mrp_production.xml',
        'views/mrp_bom.xml',
    ],
    'installable': True,
    'auto_install': False
}
