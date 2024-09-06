from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime


class SetuCustomer(models.Model):
    _name = "setu.customer"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _sql_constraints = [
        ('unique_pan_number',
         'UNIQUE (pan_number)',
         'Pan Number should be unique.'),
    ]

    name = fields.Char(string="Customer Name",required=True,help="Enter Customer Name", tracking=True)
    address = fields.Text("Address")
    pan_number = fields.Char("Pan Number")

    order_ids = fields.One2many('setu.order','customer_id')
    salesman_ids = fields.Many2many('setu.salesman','customer_salesman_rel','salesman_id','customer_id')



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
        return super(SetuCustomer, self).create(vals)


    def write(self, vals):

        for record in self:
            names = record.name.split(" ")[0] + " [" + vals.get('pan_number') + "]"
            vals['name'] = names
        return super(SetuCustomer, self).write(vals)
