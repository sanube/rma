# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Warranty Date on Lot/Serial Numbers',
    'summary': 'Add warranty date to stock production lot',
    'version': '11.0.0.0.1',
    'license': 'AGPL-3',
    'author': 'Open Source Integrators, Odoo Community Association (OCA)',
    'category': 'Stock',
    'website': 'https://github.com/OCA/rma',
    'depends': [
        'product_warranty',
        'stock',
    ],
    'data': [
        'views/stock_production_lot.xml',
    ],
    'application': False,
    'development_status': 'Beta',
    'maintainers': [
        'osi-scampbell',
        'max3903',
    ]
}
