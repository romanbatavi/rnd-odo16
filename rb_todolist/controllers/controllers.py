# -*- coding: utf-8 -*-
# from odoo import http


# class RbTodolist(http.Controller):
#     @http.route('/rb_todolist/rb_todolist', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rb_todolist/rb_todolist/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rb_todolist.listing', {
#             'root': '/rb_todolist/rb_todolist',
#             'objects': http.request.env['rb_todolist.rb_todolist'].search([]),
#         })

#     @http.route('/rb_todolist/rb_todolist/objects/<model("rb_todolist.rb_todolist"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rb_todolist.object', {
#             'object': obj
#         })
