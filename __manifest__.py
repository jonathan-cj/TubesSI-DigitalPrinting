# -*- coding: utf-8 -*-
{
    'name': "Cats",
    'summary': 'Module Odoo untuk menyimpan data digital printing.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan data digital printing CV Andika Megah Jaya.',
    'sequence': -100,
    'author': "Tim G03",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cats_trees.xml',
        'views/cats_menus.xml',
        'views/cats_forms.xml',
        'views/index.xml'
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
