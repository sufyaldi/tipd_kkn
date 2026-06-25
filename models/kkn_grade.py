# -*- coding: utf-8 -*-
from odoo import models, fields, api

class KknGrade(models.Model):
    _name = 'tipd_kkn.grade'
    _description = 'Penilaian Mahasiswa'
    _inherit = ['mail.thread']

    participant_id = fields.Many2one('tipd_kkn.participant', string='Mahasiswa', required=True, tracking=True)
    supervisor_id = fields.Many2one('tipd_kkn.supervisor', string='Penilai (DPL)', required=True, tracking=True)
    
    score = fields.Float(string='Nilai Akhir', compute='_compute_total_score', store=True, tracking=True)
    grade_letter = fields.Char(string='Huruf Mutu', compute='_compute_grade_letter', store=True)
    
    line_ids = fields.One2many('tipd_kkn.grade.line', 'grade_id', string='Rincian Nilai')
    remarks = fields.Text(string='Catatan Penilaian')

    @api.depends('line_ids.total_score')
    def _compute_total_score(self):
        for record in self:
            total = sum(line.total_score for line in record.line_ids)
            record.score = total

    @api.depends('score')
    def _compute_grade_letter(self):
        for record in self:
            if record.score >= 85:
                record.grade_letter = 'A'
            elif record.score >= 70:
                record.grade_letter = 'B'
            elif record.score >= 55:
                record.grade_letter = 'C'
            elif record.score >= 40:
                record.grade_letter = 'D'
            else:
                record.grade_letter = 'E'

class KknGradeComponent(models.Model):
    _name = 'tipd_kkn.grade.component'
    _description = 'Komponen Penilaian'

    name = fields.Char(string='Nama Komponen', required=True)
    weight = fields.Float(string='Bobot (%)', required=True, help='Contoh: 40 untuk 40%')
    description = fields.Text(string='Deskripsi')

class KknGradeLine(models.Model):
    _name = 'tipd_kkn.grade.line'
    _description = 'Detail Nilai Komponen'

    grade_id = fields.Many2one('tipd_kkn.grade', string='Penilaian', required=True, ondelete='cascade')
    component_id = fields.Many2one('tipd_kkn.grade.component', string='Komponen', required=True)
    score = fields.Float(string='Skor (0-100)', required=True)
    weight = fields.Float(string='Bobot (%)', related='component_id.weight', store=True)
    total_score = fields.Float(string='Nilai Terbobot', compute='_compute_total_score', store=True)

    @api.depends('score', 'weight')
    def _compute_total_score(self):
        for record in self:
            record.total_score = (record.score * record.weight) / 100.0
