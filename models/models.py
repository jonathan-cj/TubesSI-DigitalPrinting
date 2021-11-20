# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pesanan(models.Model):
    _name = 'tubes_si.pesanan'
    _description = 'Pesanan digital printing'

    id_pesanan = fields.Char(string='ID Pesanan')
    waktu_pesanan = fields.Datetime(string='Waktu Pemesanan', default=fields.Datetime.now())
    id_jenis = fields.Many2one('tubes_si.digitalprinting', string='ID Jenis')
    nama_pemesan = fields.Char(string='Nama Pemesan')
    email_pemesan = fields.Char(string='Email Pemesan')
    no_hp_pemesan = fields.Char(string='Nomor Telepon Pemesan')
    jumlah_pesanan = fields.Integer(string='Jumlah Pesanan')
    deskripsi_pesanan = fields.Char(string='Deskripsi Pesanan')
    file_pesanan = fields.Image(string='File Pesanan')
    bukti_pembayaran = fields.Image(string='Bukti Pembayaran')
    status = fields.Char(string='Status Pesanan')

    
class DigitalPrinting(models.Model):
    _name = 'tubes_si.digitalprinting'
    _description = 'Jenis digital printing'

    id_jenis = fields.Char(string='ID Jenis Digital Printing')
    nama = fields.Char(string='Nama Digital Printing')
    deskripsi = fields.Char(string='Deskripsi Digital Printing')
    harga = fields.Integer(string='Harga Digital Printing')
