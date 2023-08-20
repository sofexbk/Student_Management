import datetime

from odoo import api,fields,models
from datetime import date
import datetime

class Student(models.Model):
    _name="student"
    _description="student_Management"
    _rec_name="first_name"

    cne= fields.Char(string="CNE")
    first_name=fields.Char(string="First Name")
    second_name=fields.Char(string="Second Name")
    email=fields.Char(string="Email")
    date_birth=fields.Date(string ="Date of birth")
    image=fields.Image(string="Image")
    age=fields.Char(compute="_compute_age",string="Age")
    student_course_note_ids = fields.One2many('student.course.note','student_id', string="Notes")
    text_note =fields.Text(string="Text Note")

    student_state=fields.Selection([
         ('failed', 'Failed'),
         ('pass', 'Pass'),
         ('not_assigned', 'Not Assigned'),
         ] ,string="State",default="not_assigned",readonly="True")

    @api.depends("date_birth")
    def _compute_age(self):
        for record in self:
            if record.date_birth:
                today = date.today()
                birth_date = record.date_birth
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = str(age)
            else:
                record.age = ""

    @api.model
    def create(self,vals):
        return super(Student,self).create(vals)

    def wizard_action(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Validate Result',
            'view_mode': 'form',
            'res_model': 'student.wizard',
            'context': {'default_student_id': self.id, 'default_text_note': self.text_note,'default_student_state':self.student_state},
            'view_id': self.env.ref('module_v1.view_student_wizard_form').id,
            'target': 'new',
        }







