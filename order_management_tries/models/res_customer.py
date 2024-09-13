from odoo.exceptions import UserError

from odoo import models, fields, api


class Customer(models.Model):
    _name = "res.customer"
    _rec_name = "name"
    _order = "name"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _sql_constraints = [
        ('unique_pan_number',
         'UNIQUE (pan_number)',
         'Pan Number should be unique.'),
    ]

    name = fields.Char(string="Customer Name", required=True, help="Enter Customer Name", tracking=True)
    address = fields.Text("Address")
    pan_number = fields.Char("Pan Number")

    order_ids = fields.One2many('sales.order', 'customer_id', string='Orders')
    salesman_names = fields.Char(string='Salesman Names', compute='_compute_salesman_names', store=True)


    @api.depends('order_ids.salesman_id')
    def _compute_salesman_names(self):
        for customer in self:
            salesman_names = set(order.salesman_id.name for order in customer.order_ids if order.salesman_id)
            customer.salesman_names = ', '.join(salesman_names)


    @api.constrains('name', 'address')
    def check_unique_name(self):
        for record in self:
            existing_record = self.search(
                [('id', '!=', record.id), ('name', '=', record.name), ('address', '=', record.address)])
            if existing_record:
                raise UserError('Name & Address combination should be unique.')


    @api.model
    def create(self, vals):
        names = vals.get('name') + " [" + vals.get('pan_number') + "]"
        vals['name'] = names
        return super(Customer, self).create(vals)

    # if super will be called before modifying data then it will create data and it will not update field in vals


    # def write(self, vals):
    #     for record in self:
    #         names = record.name.split(" ")[0] + " [" + vals.get('pan_number') + "]"
    #         vals['name'] = names
    #         return super(SetuCustomer, self).write(vals)


    def write(self, vals):
        # res = super(SetuCustomer, self).write(vals)
        for record in self:
            if vals.get('pan_number'):
                names = record.name.split(" ")[0] + " [" + vals.get('pan_number') + "]"
            elif vals.get('name'):
                names = vals.get('name').split(" ")[0] + " [" + record.pan_number + "]"
            else:
                names = record.name.split(" ")[0] + " [" + record.pan_number + "]"
            vals['name'] = names
            return super(Customer, self).write(vals)


    # duplicate creator method override
    # # Here its upon us weather we want to use decorator or not
    # # @api.returns('self', lambda value: value.id)
    # def copy(self, default={}):
    #     print(self)
    #     default['pan_number'] = "copy (" + self.pan_number + ")"
    #     default['name'] = "copy (" + self.name + ")"
    #     res = super(Customer, self).copy(default=default)
    #     res.address = "Same as main"
    #     return res


    # delete record method override
    # def unlink(self):
    #     print("self statement", self)
    #     for cus in self:
    #         if cus.pan_number.endswith("123"):
    #             raise UserError("You can't delete this %s customer"%cus.name)
    #     res = super(Customer, self).unlink()
    #     print("Return statement", res)
    #     return res


    # out of 3 name_create only first one is working properly and that also with static value for pan number

    # @api.model
    # def name_create(self, name):
    #     print("Self",self)
    #     print("Salesman Name",name)
    #     res = self.create({'name':name,'pan_number':name+"123"})
    #     print("res",res)
    #     print("res.name_get()[0]",res.name_get()[0])
    #     return res.name_get()[0]

                # or

    # @api.model
    # def name_create(self, name, pan_number):
    #     pan_number = name+"123"
    #     print("name_create calling ............ !!")
    #     return super(Customer,self).name_create(name,pan_number)

                # or

    # @api.model
    # def name_create(self, name, pan_number):
    #     # name = name + " [" + name + "123]"
    #     # pan_number = name + "123"
    #     res = super(Customer, self).name_create(name, pan_number)
    #     # pan_number = name + "123"
    #     print("name_create calling ............ !!", res)
    #     return res


    # @api.model
    # def default_get(self, field_list=[]):
    #     print(field_list)
    #     res = super(Customer,self).default_get(field_list)
    #     res['name'] = "Default_check"
    #     res['pan_number'] = "Default_check123"
    #     print(res)
    #     return res


    # Browse Method
    # # This method can be checked out in console or can be directly applied to get record-set in return as it is not over-riding in example
    # # Also here it's not example with method definition and it is using odoo's pre-defined in-built method
    # # Here it will all work on id
    # cust_obj = self.env['Customer']
    #
    # 1) cust_obj.browse()
    # --> Customer()
    #
    # 2) cust_obj.browse(3)
    # --> Customer(3, )      ---  record-set of ID - 3
    #
    # 3) cust_list = cust_obj.browse(3)
    #    cust_list
    # --> Customer(3, )
    #    cust_list.name
    # --> CDE [CDE123]
    # cust_list.pan_number
    # --> CDE123
    #
    # 4) cust_obj.browse([3,4,5])
    # --> Customer(3, 4, 5)
    #
    # 5) for cust in cust_obj.browse([3,4,5])
    #         cust
    # --> Customer(3, )
    #     Customer(4, )
    #     Customer(5, )
    #
    # 6) #consider that customer with id 2 does not exist
    #     for cust in cust_obj.browse([1,2,3,4,5])
    #         if cust.exists():
    #             cust
    #         else:
    #             print(cust,"Not Found")
    # --> Customer(1, )
    #     Customer(2, )Not Found
    #     Customer(3, )
    #     Customer(4, )
    #     Customer(5, )


    # Search Method
    # cust_obj = self.env['res.customer']
    # cust_obj.search([])
    # ---> res.customer(1, 2, 3, 4, 5, 6, 7, 17, 18, 30)
    # len(cust_obj.search([]))
    # ---> 10
    # cust_obj.search([('id','=',3)])
    # ---> res.customer(3, )
