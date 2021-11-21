from odoo import http

class HomeController(http.Controller):
    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('tubes_si.sale_list')

    @http.route('/pesan', auth='public',type='http', website=True)
    def pesanan(self, **kw):
        return http.request.render('tubes_si.pesan')

    @http.route('/cekpesanan', auth='public', website=True)
    def cekpesanan(self, **post):
        if 'id_pesanan' in post: 
            id_pesanan = post.get('id_pesanan')
            result = ( http.request.env["tubes_si.pesanan"].sudo().search([("id_pesanan", "=", id_pesanan)]) )
            if len(result) == 0:
                result = 'Pesanan tidak ditemukan'
            else:
                result = result.id_pesanan

            return http.request.render('tubes_si.cekpesanan',{
                'pesanan': result
            })
        else:
            return http.request.render('tubes_si.cekpesanan')

    @http.route('/detail', auth='public', website=True)
    def detail(self, **kw):
        return http.request.render('tubes_si.detail')