# Copyright 2024 manoel-roberto
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Maua Books',
    'description': """
        Integração entre o cadastro de clientes e produtos""",
    'version': '16.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'manoel-roberto',
    'website': 'https://github.com/manoel-roberto',
    'depends': [
        'base',
        'product',
    ],
    'data': [
        #'security/product_product.xml',
        #'security/res_partner.xml',
        #
        'views/main_menu.xml',
        'views/product_product.xml',
        'views/res_partner.xml',
    ],
    'demo': [
        #'demo/product_product.xml',
        #'demo/res_partner.xml',
    ],
}
