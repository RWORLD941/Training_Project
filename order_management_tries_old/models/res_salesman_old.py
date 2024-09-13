from odoo import models,fields,api
import datetime


class Salesman(models.Model):
    _name = "res.salesman"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Salesman", required=True, help="Enter Sales Person Name", tracking=True)
    # address = fields.Char(string='Address')
    # department = fields.Char(string='Department')
    # product = fields.Char(string='Product')

    order_ids = fields.One2many('sales.order', 'salesman_id', string='Orders')
    customer_names = fields.Char(string='Customer Names', compute='_compute_customer_names', store=True)

    @api.depends('order_ids.customer_id')
    def _compute_customer_names(self):
        for salesman in self:
            customer_names = set(order.customer_id.name for order in salesman.order_ids if order.customer_id)
            salesman.customer_names = ', '.join(customer_names)