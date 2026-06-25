# -*- coding: utf-8 -*-
from odoo import models, fields

class KknLocation(models.Model):
    _name = 'tipd_kkn.location'
    _description = 'Lokasi Posko KKN'

    name = fields.Char(string='Nama Posko/Lokasi', required=True)
    description = fields.Text(string='Deskripsi')
    
    # Geographic Master Data Relational Fields
    village_id = fields.Many2one('tipd_kkn.village', string='Desa/Kelurahan')
    district_id = fields.Many2one('tipd_kkn.district', related='village_id.district_id', string='Kecamatan', store=True)
    regency_id = fields.Many2one('tipd_kkn.regency', related='district_id.regency_id', string='Kabupaten/Kota', store=True)
    province_id = fields.Many2one('tipd_kkn.province', related='regency_id.province_id', string='Provinsi', store=True)
    
    address = fields.Text(string='Alamat Lengkap')
    map_url = fields.Char(string='Google Maps URL')
    latitude = fields.Float(string='Latitude', digits=(10, 7))
    longitude = fields.Float(string='Longitude', digits=(10, 7))

    group_ids = fields.One2many('tipd_kkn.group', 'location_id', string='Kelompok KKN')
