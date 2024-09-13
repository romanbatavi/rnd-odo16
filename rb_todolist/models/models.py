# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rb_todolist(models.Model):
#     _name = 'rb_todolist.rb_todolist'
#     _description = 'rb_todolist.rb_todolist'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
