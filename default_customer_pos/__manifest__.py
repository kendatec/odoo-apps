# -*- coding: utf-8 -*-

{
    'name': 'Default Customer in Pos',
    'summary': 'Default Customer in Pos',
    'description': 'A default customer is set for the point of sale.',
    'author': 'Kenda Tec',
    'website': 'https://kendatec.com/',
    "support": "kendatec@gmail.com",
    'version': '13.0.0.1.0',
    'category': 'Point of Sale',
    'depends': ['point_of_sale',
    ],
    'data': [
        'views/pos_config_view.xml',
        'import/import-screens.xml',   
    ],
    'license': "OPL-1",
    'installable': True,
    'application': True,

}