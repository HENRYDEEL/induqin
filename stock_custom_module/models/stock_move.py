from odoo import models, fields
from odoo.addons import decimal_precision as dp

class StockMove(models.Model):
    _inherit='stock.move'

    product_uom_qty = fields.Float(
        'Initial Demand',
        digits=(16,5),
        default=0.0, required=True, states={'done': [('readonly', True)]},
        help="This is the quantity of products from an inventory "
             "point of view. For moves in the state 'done', this is the "
             "quantity of products that were actually moved. For other "
             "moves, this is the quantity of product that is planned to "
             "be moved. Lowering this quantity does not generate a "
             "backorder. Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.")

    reserved_availability = fields.Float(
        'Quantity Reserved', compute='_compute_reserved_availability',
        digits=(16,5),
        readonly=True, help='Quantity that has already been reserved for this move')

    quantity_done = fields.Float('Quantity Done', compute='_quantity_done_compute',  digits=(16,5), inverse='_quantity_done_set')


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    product_uom_qty = fields.Float(
        'Reserved', default=0.0, digits=(16,5),
        copy=False, required=True)
    qty_done = fields.Float('Done', default=0.0,  digits=(16,5), copy=False)