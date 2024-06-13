from odoo import models, fields

class Group(models.Model):
    _name = 'group'
    _description = 'Group'

    name = fields.Char(string='Group Name', required=True)
    section = fields.Char(string='Section')
    teacher_id = fields.Many2one('teacher', string='Group Teacher')