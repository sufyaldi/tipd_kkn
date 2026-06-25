# -*- coding: utf-8 -*-
from odoo import models, fields

class KKNFaculty(models.Model):
    _name = 'tipd_kkn.faculty'
    _description = 'Fakultas'

    name = fields.Char(string='Nama Fakultas', required=True)
    code = fields.Char(string='Kode Fakultas')
    study_program_ids = fields.One2many('tipd_kkn.study_program', 'faculty_id', string='Program Studi')


class KKNStudyProgram(models.Model):
    _name = 'tipd_kkn.study_program'
    _description = 'Program Studi'

    name = fields.Char(string='Nama Program Studi', required=True)
    code = fields.Char(string='Kode Program Studi')
    faculty_id = fields.Many2one('tipd_kkn.faculty', string='Fakultas', required=True, ondelete='cascade')
