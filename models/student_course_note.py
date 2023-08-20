from odoo import api,fields,models
from datetime import date
import datetime

class StudentCourseNote(models.Model):
    _name="student.course.note"
    _description="student_course_note"

    name=fields.Char(string="Student Note")
    course_id=fields.Many2one("course.course",string="Course_Id",ondelete='cascade')
    course_code=fields.Char(related='course_id.course_code')
    student_id=fields.Many2one("student",string="Student_id",ondelete='cascade')
