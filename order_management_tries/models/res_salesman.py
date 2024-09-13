from odoo import models, fields, api
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


    # currency_id = fields.Many2one("res.currency",default = lambda self:self.env.user.company_id.currency_id)
    currency_id = fields.Many2one('res.currency', required=True, compute = '_compute_currency_id')
    # currency_id = fields.Many2one('res.currency', required=True, default = lambda self:self._compute_currency_id(), store=True)

    order_ids = fields.One2many('sales.order', 'salesman_id', string='Orders')
    customer_names = fields.Char(string='Customer Names', compute='_compute_customer_names', store=True)
    # total_sale = fields.Monetary("Total Sales", compute='_compute_total_sale',
    #                              currency_field=lambda self: self.get_currency_field('res.company'))
    #
    # # env.company.currency_id.id

    total_sale = fields.Monetary("Total Sales", compute='_compute_total_sale')

    @api.depends('order_ids.customer_id')
    def _compute_customer_names(self):
        for salesman in self:
            customer_names = set(order.customer_id.name for order in salesman.order_ids if order.customer_id)
            salesman.customer_names = ', '.join(customer_names)

    # @api.depends('order_ids.bill_total')
    def _compute_total_sale(self):
        self.total_sale = sum(self.order_ids.mapped("bill_total"))

    # @api.depends('currency_id')
    def _compute_currency_id(self):
        self.currency_id = self.env.user.company_id.currency_id
