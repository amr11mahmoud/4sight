# -*- coding: utf-8 -*-
# from odoo import http


# class DevCase2(http.Controller):
#     @http.route('/dev_case_2/dev_case_2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev_case_2/dev_case_2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev_case_2.listing', {
#             'root': '/dev_case_2/dev_case_2',
#             'objects': http.request.env['dev_case_2.dev_case_2'].search([]),
#         })

#     @http.route('/dev_case_2/dev_case_2/objects/<model("dev_case_2.dev_case_2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev_case_2.object', {
#             'object': obj
#         })
