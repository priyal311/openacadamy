{
    # Name of the module, will be shown in the Apps menu
    'name': 'course',
    'version': '1.0',
    'author': 'Priya',
    'category': 'Custom',
    'summary': 'course Test Module',
    'depends': ['base'],

    # List of XML files for views
    'data': [
        'security/ir.model.access.csv',
        'data/course_model_data.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/course_action.xml',
        'views/course_menu.xml'
        ],


    # Allows the module to be installed
    'installable': True,

    # Marks the module as a standalone application
    'application': True,
}
