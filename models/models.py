# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pesanan(models.Model):
    _name = 'tubes_si.pesanan'
    _description = 'Pesanan digital printing'

    waktu_pesanan = fields.Datetime(string='Waktu Pemesanan', default=fields.Datetime.now())
    id_jenis = fields.Many2one('tubes_si.digitalprinting', string='ID Jenis', required=True, ondelete='cascade')
    nama_pemesan = fields.Char(string='Nama Pemesan')
    email_pemesan = fields.Char(string='Email Pemesan')
    no_hp_pemesan = fields.Char(string='Nomor Telepon Pemesan')
    alamat_pemesan = fields.Char(string='Alamat Pemesan')
    jumlah_pesanan = fields.Integer(string='Jumlah Pesanan')
    deskripsi_pesanan = fields.Char(string='Deskripsi Pesanan')
    file_pesanan = fields.Binary("Image",help='File Pesanan')
    bukti_pembayaran = fields.Binary("Image",help='Bukti Pembayaran')
    status = fields.Char(string='Status Pesanan')

    
class DigitalPrinting(models.Model):
    _name = 'tubes_si.digitalprinting'
    _description = 'Jenis digital printing'

    nama = fields.Char(string='Nama Digital Printing')
    deskripsi = fields.Char(string='Deskripsi Digital Printing')
    harga = fields.Integer(string='Harga Digital Printing')
