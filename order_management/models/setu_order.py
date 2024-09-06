from odoo import models,fields,api
import datetime


class SetuOrder(models.Model):
    _name = "setu.order"
    _rec_name = "number"
    _order = "number"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # def get_bill_total(self):
        # self.bill_total = self.price * self.quantity

    number = fields.Integer("Order No.",required=True)
    product = fields.Selection([('abc','ABC'),
                                ('pqr','PQR'),
                                ('xyz','XYZ')],"Product",required=True)
    price = fields.Float("Price",digits=(7,3),required=True)
    quantity = fields.Integer("Quantity",required=True)
    # bill_total = fields.Float("Total Bill Amount",default=lambda ba:ba.get_bill_total())

    customer_id = fields.Many2one('setu.customer', "Customer")
    salesman_id = fields.Many2one('setu.salesman', "Salesman")



    # bill_total = fields.Float("Total Bill Amount")
    #
    # @api.onchange('price', 'quantity')
    # def get_bill_total(self):
    #     self.bill_total = self.price * self.quantity