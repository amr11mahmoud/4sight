# -*- coding: utf-8 -*-
# from odoo import http


# class DevCase1(http.Controller):
#     @http.route('/dev_case_1/dev_case_1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_case_1/dev_case_1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_case_1.listing', {
#             'root': '/dev_case_1/dev_case_1',
#             'objects': http.request.env['dev_case_1.dev_case_1'].search([]),
#         })

#     @http.route('/dev_case_1/dev_case_1/objects/<model("dev_case_1.dev_case_1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_case_1.object', {
#             'object': obj
#         })
