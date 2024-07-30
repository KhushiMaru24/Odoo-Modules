# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Cryptocurrency Data',
    'version': '1.0.0',
    'sequence':-100,
    'category': 'cryptocurrency',
    'summary': 'Cryptocurrency website data stored',
    'description':"""""",
    'depends': ['base','om_hospital','point_of_sale'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/crypto_view.xml',
        'views/pos_custom_template.xml',
    ],
    'demo': [],
    'installation': True,
    'auto_install': False,
     'point_of_sale.assets':[
            '/om_hospital/static/src/js/pos_custom.js',
     ],
    'licence': 'LGPL-3',
    'application': True,

}
