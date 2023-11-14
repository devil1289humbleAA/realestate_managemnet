{
    'name':"Real-Estate Management",
    'version':'14.1.0',
    'depends':['base'],
    'sequence':'1',
    'author':"Asad Ali ",
    'category':'Category',
    'description':"""Real-Estate Management for Axiom World""",
    'data': [
    'security/ir.model.access.csv',
    'views/realestate_menu.xml',
    'views/realestate_views.xml',
    'views/realestate_type.xml',
    'views/realestate_tag.xml',
    'views/realestate_offer.xml',
    'views/res_user.xml',


],

    'installable': True,
    'auto_install': False,
    'application':  True,
}