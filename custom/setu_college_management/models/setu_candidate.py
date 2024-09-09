from odoo import models,fields
import datetime


class SetuCandidate(models.Model):
    _name = "setu.candidate"
    _rec_name = "name"
    _description = "Candidate Register"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Candidate Name", required=True, help="Enter Candidate Name", tracking=True)
    roll_no = fields.Integer("Roll No")
    year = fields.Integer("Year")
    subject = fields.Char("Subject")
    # professor_id = fields.Many2one('setu.professor', default= lambda self: self.env['setu.professor'].search([('id', '=', '1')]))
    professor_id = fields.Many2one('setu.professor')
    college_professor_ids = fields.Many2many('setu.professor', 'professor_candidate_rel',
                                             'candidate_id','professor_id')
    # book_issue_ids = fields.Many2many('setu.book.issue', 'candidate_book_issue_rel', 'book_issue_id', 'candidate_id')