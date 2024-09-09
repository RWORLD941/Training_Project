from odoo import models,fields
import datetime


class SetuBook(models.Model):
    _name = "setu.book"
    _rec_name = "name"
    _description = "Book Records"
    _order = "id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Book Name", required=True, tracking=True)
    number = fields.Integer("Book Number")
    # subject = fields.Char("Subject Name")
    version = fields.Integer("Printing Year")
    author = fields.Char("Author Name")
    price = fields.Float("Book Price")
    branch = fields.Integer("Branch Name")


    subject_id = fields.Many2one('setu.subject')
    # issue_ids = fields.Many2many('setu.book.issue','book_book_issue_rel','book_issue_id','book_id')