from odoo import models, fields

class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    profile_picture = fields.Binary(string='Profile Picture')