# -*- coding: utf-8 -*-
{
    'name': "Digital Printing",
    'summary': 'Module Odoo untuk menyimpan data digital printing.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan data digital printing CV Andika Megah Jaya.',
    'sequence': -100,
    'author': "Tim G03",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/index.xml',
        'views/pesan.xml',
        'views/cekpesanan.xml',
        'views/detail.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
