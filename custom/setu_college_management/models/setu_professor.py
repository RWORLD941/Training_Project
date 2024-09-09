from odoo import models,fields
import datetime


class SetuProfessor(models.Model):
    _name = "setu.professor"
    _rec_name = "name"
    _description = "Professor's Register"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Professor Name",required=True,help="Enter Professor Name", tracking=True)
    avg_salary = fields.Float(string="Average Salary")
    age = fields.Integer("Age")
    subject = fields.Char("Subject")
    college_id = fields.Many2one('setu.college', string="College")
    candidate_ids = fields.One2many('setu.candidate', 'professor_id')
    # eg with in-line tree view
    college_candidate_ids = fields.Many2many('setu.candidate', 'professor_candidate_rel',
                                             'professor_id', 'candidate_id')
    # (oppo table name, new table name, both base table id fields)

    # subject_ids = fields.One2many('setu.subject', 'professor_id')
    # subject_ids = fields.Many2many('setu.subject','professor_subject_rel','subject_id','professor_id')