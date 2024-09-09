from odoo import models, fields


class SetuCollege(models.Model):
    _inherit = 'setu.college'

    college_expire_date = fields.Date(string="College Expire Date")
    state = fields.Selection(selection=[('gujarat','Gujarat'),('delhi','Delhi')],string="Select State")
    college_closed = fields.Boolean(string="College Closed")