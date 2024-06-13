from odoo import models, fields

class Grade(models.Model):
    _name = 'grade'
    _description = 'Grade'

    student_id = fields.Many2one('student', string='Student', required=True)
    subject_id = fields.Many2one('subject', string='Subject', required=True)
    grade = fields.Float(string='Grade', required=True)
    semester = fields.Selection([
        ('Fall 2022', 'Fall 2022'),
        ('Spring 2023', 'Spring 2023'),
        ('Fall 2023', 'Fall 2023'),
        ('Spring 2024', 'Spring 2024'),
    ], 'Semester', required=True)