# -*- coding: utf-8 -*-
# from odoo import http


# class ItProcApp(http.Controller):
#     @http.route('/it_proc_app/it_proc_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/it_proc_app/it_proc_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('it_proc_app.listing', {
#             'root': '/it_proc_app/it_proc_app',
#             'objects': http.request.env['it_proc_app.it_proc_app'].search([]),
#         })

#     @http.route('/it_proc_app/it_proc_app/objects/<model("it_proc_app.it_proc_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('it_proc_app.object', {
#             'object': obj
#         })

