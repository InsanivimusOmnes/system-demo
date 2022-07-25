from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    number = fields.Char(string="Number", compute="_compute_number", store=True)

    # @profile
    @api.depends("order_id.order_line", "sequence")
    def _compute_number(self):
        """Compute sequence number for orders lines"""
        orders = self.mapped("order_id")
        for order in orders:
            for seq, rec in enumerate(
                order.order_line.sorted(key=lambda r: r.sequence), 1
            ):
                rec.number = seq
