from odoo import models,fields,api
import datetime


class Order(models.Model):
    _name = "sales.order"
    _rec_name = "number"
    _order = "number"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    number = fields.Integer("Order No.", required=True)
    product = fields.Selection([('laptop', 'Laptop'),
                                ('mouse', 'Mouse'),
                                ('keyboard', 'Keyboard'),
                                ('pendrive', 'Pendrive'),
                                ('ssd', 'SSD'),
                                ('cable', 'Cable'),
                                ('table', 'Table')], "Product", required=True)
    price = fields.Float("Price", digits=(7, 3), required=True)
    quantity = fields.Integer("Quantity", required=True)
    bill_total = fields.Float("Total Bill Amount",default=lambda ba:ba.get_bill_total())

    customer_id = fields.Many2one('res.customer', string='Customer')
    salesman_id = fields.Many2one('res.salesman', string='Salesman')

    # customer_name = fields.Char(string='Customer Name', related='customer_id.name', store=True)
    # salesman_name = fields.Char(string='Salesman Name', related='salesman_id.name', store=True)

    # bill_total = fields.Float("Total Bill Amount")

    @api.onchange('price', 'quantity')
    def get_bill_total(self):
        self.bill_total = self.price * self.quantity