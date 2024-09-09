{
    # App Information
    'name': 'Setu College Management',
    'version': '16.0',
    'category': 'college',

    # Author
    'author': 'Setu Consulting Services Pvt. Ltd.',
    'maintainer': 'Setu Consulting Services Private Limited',
    'website': 'http://www.setuconsulting.com/',

    # Dependencies
    'depends': ['mail'],

    'summary': """This module is college management""",

    'support': 'support@setuconsulting.com',

    'description': """This module is college management 1""",

    'data': [
        'security/ir.model.access.csv',
        'views/setu_college_views.xml',
        'views/setu_professor_views.xml',
        'views/setu_candidate_views.xml',
        'views/setu_book_views.xml',
        'views/setu_book_issue_views.xml',
        'views/setu_subject_views.xml'
    ],

    # Technical
    'installable': True,
    'auto_install': False,
    'application': True
}