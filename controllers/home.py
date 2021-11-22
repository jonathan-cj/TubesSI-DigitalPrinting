from odoo import http

ADMIN_KEY = 'admin'

class HomeController(http.Controller):
    is_admin = False

    @http.route('/', auth='public', website=True)
    def index(self, **kw):

        return http.request.render('tubes_si.login')

    @http.route('/login', auth='public', website=True)
    def index(self, **post):
        if len(post) > 0:
            code = post.get('kode')

            if code == ADMIN_KEY:
                self.is_admin = True
                return http.request.render('tubes_si.sale_list', {'is_admin': True})
        return http.request.render('tubes_si.sale_list')

    @http.route('/daftar', auth='public', website=True)
    def daftar(self, **kw):

        # INI CUMA CONTOH!!!
        # jenis_dp ini harusnya ambil dari database
        jenis_dp = http.request.env['tubes_si.digitalprinting'].sudo().search([])
        return http.request.render('tubes_si.sale_list', {
            'jenis_dp': jenis_dp # 'jenis_dp' ini harus sesuai sama <t t-foreach='jenis_dp' .....
        })

    @http.route('/pesan', auth='public', website=True)
    def pesanan(self, **post):
        result = {}
        if len(post) != 0:
            result['nama_pemesan'] = post.get('nama')
            result['alamat_pemesan'] = post.get('alamat')
            # result['ukuran'] = post.get('ukuran')
            result['file_pesanan'] = post.get('choose-file')
            result['deskripsi_pesanan'] = post.get('catatan')
            result['bukti_pembayaran'] = post.get('bukti')
            result['status'] = 'Dalam Proses Pencetakan'

            save = http.request.env['tubes_si.pesanan'].sudo().create(result)

            return http.request.render('tubes_si.pesan', {
                'pesanan': result, # 'pesanan' ini harus sesuai sama <t t-esc='pesanan' />
                'save': save
            })
        else:
            return http.request.render('tubes_si.pesan')

    @http.route('/cekpesanan', auth='public', website=True)
    def cekpesanan(self, **post):
        if 'id_pesanan' in post: 
            
            id_pesanan = post.get('id_pesanan')
            try:
                int(id_pesanan)
                result = ( http.request.env["tubes_si.pesanan"].sudo().search([("id", "=", id_pesanan)]) )
                if len(result) == 0: result = 'Pesanan tidak ditemukan'
                return http.request.render('tubes_si.cekpesanan',{
                    'pesanan': result
                })

            except:            
                return http.request.render('tubes_si.cekpesanan', {
                    'error': "ID Pesanan harus angka"
                })
        else:
            return http.request.render('tubes_si.cekpesanan')

    @http.route('/detail/<id_jenis>', auth='public', website=True)
    def detail(self, id_jenis, **kw):
        result = ( http.request.env["tubes_si.digitalprinting"].sudo().search([("id_jenis", "=", id_jenis)]) )
        if len(result) == 0:
            result = 'Jenis produk tidak ditemukan'
        
        return http.request.render('tubes_si.detail', {
            'jenis': result
        })
    
    @http.route('/addproduct', auth='public', website=True) # mungkin authnya harus diubah jadi user?
    def addproduct(self, **post):
        id_jenis = 0 # harus ambil count dari database terus increment +1
        return http.request.render('tubes_si.addproduct', {
            'id_jenis': id_jenis
        })