{
    # App Information
    'name': 'Order Management Tries Old',
    'version': '1.1',
    'category': 'Sales',
    'sequence': 1,

    # Author
    # 'author': 'Setu Consulting Services Pvt. Ltd.',
    # 'maintainer': 'Setu Consulting Services Private Limited',
    # 'website': 'http://www.setuconsulting.com/',

    # Dependencies
    'depends': ['mail'],

    'summary': "Order Management Try and Error",

    'description': "This is order management trial and error system software",

    'data': [
        'security/ir.model.access.csv',
        "views/res_customer_old_views.xml",
        "views/sales_order_old_views.xml",
        "views/res_salesman_old_views.xml",
    ],

    # Technical

}
