from odoo import http
import base64

ADMIN_KEY = 'admin'
is_admin = False

class HomeController(http.Controller):
    

    @http.route('/', auth='public', website=True)
    def index(self, **kw):
        global is_admin
        is_admin = False
        return http.request.render('tubes_si.login')

    @http.route('/daftar', auth='public', website=True)
    def daftar(self, **post):
        global is_admin

        jenis_dp = http.request.env['tubes_si.digitalprinting'].sudo().search([])

        if len(post) > 0:
            code = post.get('kode')

            if code == ADMIN_KEY:
                is_admin = True
        
        return http.request.render('tubes_si.sale_list', {
            'is_admin': is_admin,
            'jenis_dp': jenis_dp,
        })

    @http.route('/pesan/<id_jenis>', auth='public', website=True)
    def pesanan(self, id_jenis, **post):
        global is_admin
        result = {}

        produk = http.request.env["tubes_si.digitalprinting"].sudo().search([("id_jenis", "=", id_jenis)])
        if len(post) != 0:
            result['nama_pemesan'] = post.get('nama')
            result['alamat_pemesan'] = post.get('alamat')
            file_input = post.get('choose-file')
            result['file_pesanan'] = file_input.read()
            result['deskripsi_pesanan'] = post.get('catatan')
            bukti_pembayaran = post.get('bukti')
            result['bukti_pembayaran'] = bukti_pembayaran.read()
            result['status'] = 'Dalam Proses Pencetakan'
            result['id_jenis'] = id_jenis

            save = http.request.env['tubes_si.pesanan'].sudo().create(result)

            return http.request.render('tubes_si.pesan', {
                'is_admin': is_admin,
                'pesanan': result, # 'pesanan' ini harus sesuai sama <t t-esc='pesanan' />
                'save': save,
                'produk': produk
            })
        else:
            return http.request.render('tubes_si.pesan', { 'produk': produk })

    @http.route('/cekpesanan', auth='public', website=True)
    def cekpesanan(self, **post):
        global is_admin
        if not is_admin:
            if 'id_pesanan' in post: 
                error = False
                
                id_pesanan = post.get('id_pesanan')
                try:
                    int(id_pesanan)
                except ValueError: 
                    error = 'Pesanan tidak ditemukan'


                if not error:
                    result = ( http.request.env["tubes_si.pesanan"].sudo().search([("id", "=", id_pesanan)]) )                
                    if len(result) != 0:
                        return http.request.render('tubes_si.cekpesanan',{
                            'pesanan': result
                        })
                    else:
                        error = 'Pesanan tidak ditemukan'
                return http.request.render('tubes_si.cekpesanan', {
                    'error': error
                })

            else:
                return http.request.render('tubes_si.cekpesanan')
        else:
            return http.request.render('tubes_si.daftarpesanan')

    @http.route('/detail/<id_jenis>', auth='public', website=True)
    def detail(self, id_jenis, **kw):
        global is_admin
        result = ( http.request.env["tubes_si.digitalprinting"].sudo().search([("id_jenis", "=", id_jenis)]) )
        if len(result) == 0:
            result = 'Jenis produk tidak ditemukan'
        
        return http.request.render('tubes_si.detail', {
            'jenis': result,
            'is_admin': is_admin
        })