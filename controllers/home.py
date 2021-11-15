from odoo import http


class HomeController(http.Controller):
    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('tubes_si.sale_list')
