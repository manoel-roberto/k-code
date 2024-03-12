# Copyright 2024 manoel-roberto
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    is_publisher = fields.Boolean("É editor")
    is_author = fields.Boolean("é autor")

    author_book_ids = fields.Many2many(
        comodel_name="product.product",
        relation="book_author_rel",
        column1="author_id",
        column2="product_id",
        domain=[('is_book', '=', True)],
    )

    editor_book_ids = fields.One2many(
        comodel_name='product.product',
        inverse_name='editor_id',
        string='Livors',
        required=False,
        domain=[('is_book', '=', True)],
    )
