{
    # App Information
    'name': 'School Students',
    'version': '1.1',
    'category': 'Students',
    'sequence': 1,

    # Author
    'author': 'Setu Consulting Services Pvt. Ltd.',
    'maintainer': 'Setu Consulting Services Private Limited',
    'website': 'http://www.setuconsulting.com/',

    # Dependencies
    'depends': ['setu_college_management','school'],

    'summary': "School Student Management System",

    'support': 'support@weblearns.com',

    'description': "This is school student management system software",

    'data': [
        'security/ir.model.access.csv',
        "views/school_student_view.xml",
        "views/setu_college_views.xml",
             ],

    # Technical

}