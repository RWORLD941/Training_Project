from odoo import models,fields
import datetime


class SetuBookIssue(models.Model):
    _name = "setu.book.issue"
    _rec_name = "number"
    _description = "Book Issue Records"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # candidate = fields.Char(string="Candidate Name", required=True, tracking=True)
    number = fields.Integer("Issue Number")
    # subject = fields.Char("Subject Name")
    date = fields.Date("Issue Date")
    branch = fields.Char("Bookstore Branch Name")

    book_ids = fields.Many2many('setu.book', 'book_book_issue_rel', 'book_id', 'book_issue_id')
    candidate_id = fields.Many2one('setu.candidate', "Candidate")
    # candidate_ids = fields.Many2many('setu.candidate', 'candidate_book_issue_rel', 'candidate_id', 'book_issue_id')
    subject_ids = fields.Many2many('setu.subject', 'subject_book_issue_rel', 'subject_id', 'book_issue_id')