from odoo import api, fields, models

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    rango = fields.Char()
    fecha_limite = fields.Date()
    no_de_factura = fields.Date()