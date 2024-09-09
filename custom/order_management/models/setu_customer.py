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
    # salesman_ids = fields.Many2many('setu.salesman','customer_salesman_rel','salesman_id','customer_id')
    salesman_id = fields.Many2one('setu.salesman',"Salesman")


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
            return super(SetuCustomer, self).write(vals)

























    # def write(self, vals):
    #     res = super(SetuCustomer, self).write(vals)
    #     if vals.get('name'):
    #         self.update_name_name()
    #     elif vals.get('pan_number'):
    #         self.update_name_pan_number()
    #
    #     return res
    #
    # def update_names_name(self):
    #     for record in self:
    #         record.name = record.name.split(" ")[0] + " [" + record.pan_number + "]"
    #
    # def update_name_pan_number(self):
    #     for record in self:
    #         record.name = record.name.split(" ")[0] + " [" + record.pan_number + "]"
    #
    # def update_name_other(self):
    #     for record in self:
    #         record.name = record.name.split(" ")[0] + " [" + record.pan_number + "]"