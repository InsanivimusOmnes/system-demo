from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    numbers = fields.Char(string="Number", compute="_compute_numbers", store=True)
    sequence_line = fields.Char(
        string="Sequence Line", compute="_compute_sequence_line"
    )

    # @profile
    @api.depends("order_id.order_line", "sequence")
    def _compute_numbers(self):
        orders = self.mapped("order_id")
        for order in orders:
            number = 1
            for rec in order.order_line.sorted(key=lambda r: r.sequence):
                rec.numbers = number
                number += 1

    def _compute_sequence_line(self):
        for index, value in enumerate(self, 1):
            value.sequence_line = index
