from odoo import models, fields

class Subject(models.Model):
    _name = 'subject'
    _description = 'Subject'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)