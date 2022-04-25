from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_method_id = fields.Many2one('account.payment.method', string='Payment Method')