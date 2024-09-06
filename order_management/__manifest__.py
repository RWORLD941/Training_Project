{
    # App Information
    'name': 'Order Management',
    'version': '1.1',
    'category': 'Sales',
    'sequence': 1,

    # Author
    'author': 'Setu Consulting Services Pvt. Ltd.',
    'maintainer': 'Setu Consulting Services Private Limited',
    'website': 'http://www.setuconsulting.com/',

    # Dependencies
    'depends': ['mail'],

    'summary': "Order Management System",

    'description': "This is order management system software",

    'data': [
        'security/ir.model.access.csv',
        "views/setu_customer_views.xml",
        "views/setu_order_views.xml",
        "views/setu_salesman_views.xml",
    ],

    # Technical

}