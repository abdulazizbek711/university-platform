from odoo import models, fields

class Timetable(models.Model):
    _name = 'timetable'
    _description = 'Timetable'

    group_id = fields.Many2one('group', string='Group', required=True)
    weekday = fields.Selection([
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ], 'Weekday', required=True)
    period = fields.Selection([
        ('8:30-9:45', '8:30-9:45'),
        ('10:00-11:15', '10:00-11:15'),
        ('11:30-12:45', '11:30-12:45'),
        ('13:30-14:45', '13:30-14:45'),
        ('15:00-16:15', '15:00-16:15'),
        ('16:30-17:45', '16:30-17:45'),
        ('18:00-19:15', '18:00-19:15'),
    ], 'Period', required=True)
    subject_id = fields.Many2one('subject', string='Subject', required=True)