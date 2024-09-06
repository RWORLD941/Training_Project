from odoo import models,fields
import datetime


class SetuState(models.Model):
    _name = "setu.state"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="State",required=True,help="Enter State Name", tracking=True)

    country_id = fields.Many2one('setu.country')