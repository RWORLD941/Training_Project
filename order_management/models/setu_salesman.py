from odoo import models,fields
import datetime


class SetuSalesman(models.Model):
    _name = "setu.salesman"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Salesman",required=True,help="Enter Sales Person Name", tracking=True)

    order_ids = fields.One2many('setu.order','salesman_id')
    # customer_ids = fields.Many2many('setu.customer','customer_salesman_rel','customer_id','salesman_id')
    # customer_ids = fields.One2many('setu.customer','salesman_id')
    # customer_id = fields.Many2one('setu.order','salesman_id')
