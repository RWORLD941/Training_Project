from odoo import models,fields,api
import datetime


class Order(models.Model):
    _name = "sales.order"
    _rec_name = "number"
    _order = "number"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # _sql_constraints = [
    #     ('unique_number',
    #      'UNIQUE (number)',
    #      'Order Number should be unique.'),
    # ]

    number = fields.Integer("Order No.",readonly=1)
    product = fields.Selection([('laptop', 'Laptop'),
                                ('mouse', 'Mouse'),
                                ('keyboard', 'Keyboard'),
                                ('pendrive', 'Pendrive'),
                                ('ssd', 'SSD'),
                                ('cable', 'Cable'),
                                ('table', 'Table')], "Product", required=True)
    # price = fields.Float("Price", digits=(7, 3), required=True)
    price = fields.Float("Price", compute='_compute_bill_total', store=True)
    quantity = fields.Integer("Quantity", required=True)
    # bill_total = fields.Float("Total Bill Amount")
    bill_total = fields.Float("Total Bill Amount", compute='_compute_bill_total', store=True)


    customer_id = fields.Many2one('res.customer', string='Customer')
    salesman_id = fields.Many2one('res.salesman', string='Salesman')

    # customer_name = fields.Char(string='Customer Name', related='customer_id.name', store=True)
    # salesman_name = fields.Char(string='Salesman Name', related='salesman_id.name', store=True)

    # @api.onchange('price','quantity')
    # def _onchange_bill_total(self):
    #     self.bill_total = self.price * self.quantity

    # @api.depends('price','quantity')
    # def _compute_bill_total(self):
    #     for record in self:
    #         # print('test')
    #         total_bill = record.price * record.quantity
    #         record.bill_total = total_bill

    @api.depends('price', 'quantity','product')
    def _compute_bill_total(self):
        # print("test")
        for record in self:
            if record.product == "laptop":
                record.price = 150000
            elif record.product == "mouse":
                record.price = 525
            elif record.product == "keyboard":
                record.price = 410
            elif record.product == "pendrive":
                record.price = 645
            elif record.product == "ssd":
                record.price = 2487
            elif record.product == "cable":
                record.price = 130
            elif record.product == "table":
                record.price = 6045

            total_bill = record.price * record.quantity
            record.bill_total = total_bill


    # setting order number equal to order id

    # @api.model
    # def create(self,vals):
    #     res = super(Order, self).create(vals)
    #     res.number = res.id
    #     return res

    # also can use search in default_get

    @api.model
    def default_get(self, field_list=[]):
        res = super(Order,self).default_get(field_list)
        order_no = self.env['sales.order'].search([],order="id DESC",limit=1).id
        res["number"] = order_no + 1
        return res
