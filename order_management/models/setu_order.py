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
    product = fields.Selection([('laptop', 'Laptop'),
                                ('mouse', 'Mouse'),
                                ('keyboard', 'Keyboard'),
                                ('pendrive', 'Pendrive'),
                                ('ssd', 'SSD'),
                                ('cable', 'Cable'),
                                ('table', 'Table')], "Product", required=True)
    price = fields.Float("Price",digits=(7,3),required=True)
    quantity = fields.Integer("Quantity",required=True)
    # bill_total = fields.Float("Total Bill Amount",default=lambda ba:ba.get_bill_total())
    bill_total = fields.Float("Total Bill Amount")


    customer_id = fields.Many2one('setu.customer', "Customer")
    salesman_id = fields.Many2one('setu.salesman', "Salesman")





    # bill_total = fields.Float("Total Bill Amount")
    #
    # @api.onchange('price', 'quantity')
    # def get_bill_total(self):
    #     self.bill_total = self.price * self.quantity




    # math = fields.Integer(string="Math")
    # english = fields.Integer(string="English")
    # science = fields.Integer(string="Science")
    # gujarati = fields.Integer(string="Gujarati")
    # hindi = fields.Integer(string="Hindi")
    # percentage = fields.Float(string="Percentage")
    #
    def button_bill_total(self):
        for record in self:
            total = record.price * record.quantity
            record.bill_total = total



