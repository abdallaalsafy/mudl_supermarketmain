# -*- coding: utf-8 -*-
{
    'name': "SuperMarket Main",
    'summary': """
        """,
    'description': """
        Small supermarket management project without relying on non-essential Odoo modules
    """,
    'author': "abdalla alsafy",
    'website': "http://www.facebook.com/abdalla6alsafy",
    'category': 'Uncategorized',
    'version': '13.0.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'my_data/sequence.xml',
        'views/customers.xml',
        'views/mandoops.xml',
        'views/classes.xml',
        'views/goods.xml',
        'views/buys_goods.xml',
        'views/stores.xml',
        'views/stores_goods.xml',
        'views/zepoons.xml',
        'views/places.xml',
        'views/streets.xml',
        'views/buys.xml',
        'views/vws_bbacks.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
