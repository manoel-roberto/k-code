# Copyright 2024 manoel-roberto
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    is_book = fields.Boolean("É um livro")

    isbn = fields.Char(
        string='ISBN',
        copy=False,
        index=True,
    )

    author_ids = fields.Many2many(
        string="Author",
        comodel_name="res.partner",
        relation="book_author_rel",
        column1="product_id",
        column2="author_id",
        domain=[('is_author', '=', True)],
    )

    editor_id = fields.Many2many(
        string="Editor",
        comodel_name="res.partner",
        domain=[('is_publisher', '=', True)],
    )

    _sql_constraints = [
        ('isbn_uniq', 'unique (isbn)', 'The code of the INBN musy be unique !'),
    ]

    # @api.constrains('isbn')
    # def validate_isbn(self):
    #     for record in self:
    #         valido = is_isbn(record.isbn)
    #         if not valido:
    #             raise Validation("Isbn invalido")
