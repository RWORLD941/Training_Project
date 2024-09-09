from odoo import fields, models

class SchoolProfile(models.Model):
    _name = "school.profile"

    def get_default_rank(self):
        if 1==1:
            return 200
        else:
            return 100

    def get_default_date(self):
        return fields.Date.today()

    name = fields.Char(string="School Name",help="This is school name",size=20,
                       trim=False,required=True,default="School Name")
    email = fields.Char(string="Email")
    phone = fields.Integer("Phone", required=1)
    is_virtual_class = fields.Boolean("Virtual Class Support?",default=True)
    school_rank = fields.Integer("Rank", default=lambda lm:lm.get_default_rank())
    result = fields.Float("Result",digits=(2,3))
    address = fields.Text("Address",trim=True)
    establish_date = fields.Date("Establish Date", default=lambda dt:dt.get_default_date(), readonly=True)
    open_date = fields.Datetime("Open Date",default=fields.Datetime.now(),required=True)
    school_type = fields.Selection([('public','Public School'),('private','Private School')],"School Type",default='private')
    school_type2 = fields.Selection([('public', 'Public School'), ('private', 'Private School')], "School Type")
    documents = fields.Binary("Documents")
    document_name = fields.Char("File Name")
    school_image = fields.Image("Upload School Image",max_width=100,max_height=100)

    school_description = fields.Html("Description")
    school_description2 = fields.Html("Description", default="This is <b>School.")

    # student_id = fields.One2many




    # phone = fields.Integer("Phone", selection=[('+91', '+91'),
    #                                            ('+1', '+1')], size=10)
    # fields.Selection(["+91","+91"],["+1","+1"]) +

    # read_only = fields.Char("Read Only",readonly=True,default="Read Only Example")
