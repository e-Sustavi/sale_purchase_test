from odoo import models,api


class DupSale(models.Model):
    _inherit = 'sale.order.line'

# Function describes Duplication
    @api.multi
    def action_copy(self):
        self.copy(default={'order_id': self.order_id.id})
