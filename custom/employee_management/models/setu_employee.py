from odoo import models,fields
import datetime


class SetuEmployee(models.Model):
    _name = "setu.employee"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Employee Name",required=True,help="Enter Employee Name", tracking=True)
    address = fields.Text("Address",required=True)

    state_id = fields.Many2one('setu.state')
    country_id = fields.Many2one('setu.country')
    department_id = fields.Many2one('setu.department')