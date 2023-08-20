{
    "name": "Stage_Module",
    "version": "16.0.1.0.0",
    "website":"Odoo_student",
    "summary":"Odoo 16 developement",
    "author": "Soufian Bouktaib",
    "category": "Management/differents",
    "installable": True,
    "depends": [
         'base'
    ],
    "data": [
        'views/main_view.xml',
        'security/ir.model.access.csv',
        'report/student_details_template.xml',
        'report/report.xml',
        'views/course_view.xml',
        'views/res_partner_inherit.xml',
        'views/student_note.xml',
        'wizard/student_view.xml'
    ],
}