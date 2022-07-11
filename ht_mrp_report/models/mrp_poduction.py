from odoo import fields, models, api
from odoo.addons.hr_maintenance.models import equipment


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    production_completion = fields.Datetime(string='Fecha de finalización de la producción')
    production_start = fields.Datetime(string='Fecha de fabricacion')
    responsable_de_llenado = fields.Many2one('res.users')
    despacho_de_empaque = fields.Many2one('res.users')
    controlo_pesada = fields.Many2one('res.users', string='Controló Pesada')
    jefe_de_produccion = fields.Many2one('res.users', string='Jefe de produccion')
    recepcion_de_empaque = fields.Many2one('res.users', string='Recepción de empaque')
    responsable_de_fabricacion = fields.Many2one('res.users', string='Responsable de fabricacion/verificacion')
    conclusiones = fields.Text(string='Conclusiones')
    equipment_ids = fields.One2many('mrp.equipment','production_id')


    elaborado_y_modificado_por =  fields.Many2one('res.users')
    revisado_por =  fields.Many2one('res.users')
    aprobado_por =  fields.Many2one('res.users')
    version =  fields.Char()
    elaborado =  fields.Char()
    version_vigente =  fields.Char()

    cantidad_en_unidades = fields.Float()
    cantidad_real = fields.Float()
    cantidad_teorica = fields.Float()
    cantidad_en_unidades_2 = fields.Float()
    repeticiones = fields.Float()


class MrpEquipment(models.Model):
    _name = 'mrp.equipment'

    description = fields.Char()
    si = fields.Char()
    no = fields.Char()
    observaciones = fields.Char()
    production_id = fields.Many2one('mrp.production')