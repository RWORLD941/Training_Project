{
    # App Information
    'name': 'Employee Management',
    'version': '1.1',
    'category': 'Employee',
    'sequence': 1,

    # Author
    'author': 'Setu Consulting Services Pvt. Ltd.',
    'maintainer': 'Setu Consulting Services Private Limited',
    'website': 'http://www.setuconsulting.com/',

    # Dependencies
    'depends': ['mail'],

    'summary': "Employee Management System",

    'description': "This is employee management system software",

    'data': [
        'security/ir.model.access.csv',
        "views/setu_country_views.xml",
        "views/setu_department_views.xml",
        "views/setu_employee_views.xml",
        "views/setu_state_views.xml",
             ],

    # Technical

}