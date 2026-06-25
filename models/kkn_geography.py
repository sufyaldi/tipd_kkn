# -*- coding: utf-8 -*-
from odoo import models, fields

class KKNProvince(models.Model):
    _name = 'tipd_kkn.province'
    _description = 'Provinsi'

    name = fields.Char(string='Nama Provinsi', required=True)
    regency_ids = fields.One2many('tipd_kkn.regency', 'province_id', string='Kabupaten/Kota')


class KKNRegency(models.Model):
    _name = 'tipd_kkn.regency'
    _description = 'Kabupaten/Kota'

    name = fields.Char(string='Nama Kabupaten/Kota', required=True)
    province_id = fields.Many2one('tipd_kkn.province', string='Provinsi', required=True, ondelete='cascade')
    district_ids = fields.One2many('tipd_kkn.district', 'regency_id', string='Kecamatan')


class KKNDistrict(models.Model):
    _name = 'tipd_kkn.district'
    _description = 'Kecamatan'

    name = fields.Char(string='Nama Kecamatan', required=True)
    regency_id = fields.Many2one('tipd_kkn.regency', string='Kabupaten/Kota', required=True, ondelete='cascade')
    village_ids = fields.One2many('tipd_kkn.village', 'district_id', string='Desa/Kelurahan')


class KKNVillage(models.Model):
    _name = 'tipd_kkn.village'
    _description = 'Desa/Kelurahan'

    name = fields.Char(string='Nama Desa/Kelurahan', required=True)
    district_id = fields.Many2one('tipd_kkn.district', string='Kecamatan', required=True, ondelete='cascade')
    postal_code = fields.Char(string='Kode Pos')
