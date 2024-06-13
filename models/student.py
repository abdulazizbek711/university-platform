from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    profile_picture = fields.Binary(string='Profile Picture')