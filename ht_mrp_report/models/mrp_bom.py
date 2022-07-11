from odoo import fields, models, api


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    formula_name = fields.Char(string='Nombre de fórmula')
    procedimiento_para_la_fabricacion = fields.Html(string='Procedimiento Para La Fabricación')