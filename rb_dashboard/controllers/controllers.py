# -*- coding: utf-8 -*-
# from odoo import http


# class RbDashboard(http.Controller):
#     @http.route('/rb_dashboard/rb_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rb_dashboard/rb_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rb_dashboard.listing', {
#             'root': '/rb_dashboard/rb_dashboard',
#             'objects': http.request.env['rb_dashboard.rb_dashboard'].search([]),
#         })

#     @http.route('/rb_dashboard/rb_dashboard/objects/<model("rb_dashboard.rb_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rb_dashboard.object', {
#             'object': obj
#         })
