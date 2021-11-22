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
        'views/login.xml',
        'views/list.xml',
        'views/pesan.xml',
        'views/cekpesanan.xml',
        'views/daftarpesanan.xml',
        'views/detail.xml',
        'views/addproduct.xml',
        'views/editproduct.xml',
        'views/detailpesanan.xml'
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
