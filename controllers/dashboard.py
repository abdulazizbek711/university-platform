from odoo import http
from odoo.http import request

class DashboardController(http.Controller):

    @http.route('/dashboard', auth='user', website=True)
    def dashboard(self, **kwargs):
        return request.render('platform.dashboard', {})

    @http.route('/profile', auth='user', website=True)
    def profile(self, **kwargs):
        students = request.env['student'].sudo().search([])
        return request.render('platform.student_page', {
            'students': students,
        })

    @http.route('/timetable', auth='user', website=True)
    def timetable(self, **kwargs):
        timetables = request.env['timetable'].sudo().search([])
        return request.render('platform.timetable_page', {
            "timetables": timetables,
        })

    @http.route('/grades', auth='user', website=True)
    def grades(self, **kwargs):
        grades = request.env['grade'].sudo().search([])
        return request.render('platform.grade_page', {
            "grades": grades,
        })

