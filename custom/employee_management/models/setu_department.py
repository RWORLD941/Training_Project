from odoo import models,fields
import datetime


class SetuDepartment(models.Model):
    _name = "setu.department"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Department Name",required=True,help="Enter Department Name", tracking=True)

    employee_ids = fields.One2many('setu.employee','department_id')