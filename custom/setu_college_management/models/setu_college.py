from odoo import models,fields
import datetime


class SetuCollege(models.Model):
    _name = "setu.college"
    _rec_name = "name"
    _description = "College Management"
    _order = "college_no"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="College Name",required=True,help="Enter College Name", tracking=True)
    college_no = fields.Integer(string="College No",copy=False, tracking=True, skip_locked=True)
    average_fees = fields.Float(string="Average Fees")
    international = fields.Boolean(string="International or Not",default=True)
    medium = fields.Selection(selection=[('english', 'English'),
                                ('hindi', 'Hindi')],
                                required=True,default='english')
    register_date = fields.Date(string="Registration Date",default=datetime.datetime.today(),readonly=True)


    # form_time = fields.Datetime(string="Current Date and Time",default=datetime.datetime.now(),readonly=True)