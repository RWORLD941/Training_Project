from odoo import models,fields
import datetime


class SetuCountry(models.Model):
    _name = "setu.country"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Country",required=True,help="Enter Country Name", tracking=True)

    state_ids = fields.One2many('setu.state','country_id')