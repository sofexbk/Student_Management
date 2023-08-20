from odoo import api,fields,models

class CourseStudent(models.Model):
    _name="course.course"
    _description="course_student"

    name=fields.Char(string="Name")
    professor_id=fields.Many2one('res.partner',string="Prof",domain=[('is_professor','=',True)])
    course_code=fields.Char(string="Course_Code")

