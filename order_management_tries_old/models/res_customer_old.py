from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime


class Customer(models.Model):
    _name = "res.customer"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _sql_constraints = [
        ('unique_pan_number',
         'UNIQUE (pan_number)',
         'Pan Number should be unique.'),
    ]

    name = fields.Char(string="Customer Name", required=True, help="Enter Customer Name", tracking=True)
    address = fields.Text("Address")
    pan_number = fields.Char("Pan Number")

    order_ids = fields.One2many('sales.order', 'customer_id', string='Orders')
    salesman_names = fields.Char(string='Salesman Names', compute='_compute_salesman_names', store=True)

    @api.depends('order_ids.salesman_id')
    def _compute_salesman_names(self):
        for customer in self:
            salesman_names = set(order.salesman_id.name for order in customer.order_ids if order.salesman_id)
            customer.salesman_names = ', '.join(salesman_names)


    @api.constrains('name', 'address')
    def check_unique_name(self):
        for record in self:
            existing_record = self.search(
                [('id', '!=', record.id), ('name', '=', record.name), ('address', '=', record.address)])
            if existing_record:
                raise UserError('Name & Address combination should be unique.')


    @api.model
    def create(self, vals):
        names = vals.get('name') + " [" + vals.get('pan_number') + "]"
        vals['name'] = names
        return super(Customer, self).create(vals)

    # if super will be called before modifying data then it will create data and it will not update field in vals


    # def write(self, vals):
    #     for record in self:
    #         names = record.name.split(" ")[0] + " [" + vals.get('pan_number') + "]"
    #         vals['name'] = names
    #         return super(SetuCustomer, self).write(vals)


    def write(self, vals):
        # res = super(SetuCustomer, self).write(vals)
        for record in self:
            if vals.get('pan_number'):
                names = record.name.split(" ")[0] + " [" + vals.get('pan_number') + "]"
            elif vals.get('name'):
                names = vals.get("name").split(" ")[0] + " [" + record.pan_number + "]"
            else:
                names = record.name.split(" ")[0] + " [" + record.pan_number + "]"
            vals['name'] = names
            return super(Customer, self).write(vals)
