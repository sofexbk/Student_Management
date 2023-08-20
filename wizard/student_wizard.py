from odoo import api,fields,models

class StudentValidationWizard(models.TransientModel):
    _name="student.wizard"
    _description="student_wizard"


    student_state =fields.Selection([
         ('not_assigned', 'Not Assigned'),
         ('failed', 'Failed'),
         ('pass', 'Pass')
         ] ,string="State" ,default="not_assigned",required="True")
    student_id=fields.Many2one("student",string="Student_Id")
    text_note =fields.Text(string="Text Note",required="True")

    @api.onchange("student_state")
    def onchage_student_state(self):
            if self.student_state=='pass':
                self.text_note="Student Has validated the year"
            elif self.student_state=='failed' :
                self.text_note = "Student will try again to succeed"
            else:
                self.text_note = ""


    def action_pass(self):
        for rec in self:
          rec.student_id.write({'student_state': rec.student_state ,'text_note': rec.text_note})

    def action_failed(self):
        for rec in self:
            rec.student_id.write({'student_state': rec.student_state ,'text_note': rec.text_note})







