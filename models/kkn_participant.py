# -*- coding: utf-8 -*-
from odoo import models, fields

class KknParticipant(models.Model):
    _name = 'tipd_kkn.participant'
    _description = 'Peserta KKN'
    _inherit = ['mail.thread']
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Mahasiswa', required=True, tracking=True, domain=[('is_company', '=', False)])
    name = fields.Char(string='Nama Mahasiswa', required=True, tracking=True)
    nim = fields.Char(string='NIM', required=True, tracking=True)
    gender = fields.Selection([('m', 'Laki-Laki'), ('f', 'Perempuan')], string='Jenis Kelamin')
    phone = fields.Char(string='Nomor Telepon')
    
    # Academic Data
    faculty_id = fields.Many2one('tipd_kkn.faculty', string='Fakultas')
    study_program_id = fields.Many2one('tipd_kkn.study_program', string='Program Studi', domain="[('faculty_id', '=', faculty_id)]")
    
    group_id = fields.Many2one('tipd_kkn.group', string='Kelompok KKN', tracking=True)
    program_id = fields.Many2one('tipd_kkn.program', string='Program KKN', tracking=True)
    
    faculty = fields.Char(string='Fakultas')
    major = fields.Char(string='Program Studi')
    
    status = fields.Selection([
        ('registered', 'Terdaftar'),
        ('active', 'Aktif'),
        ('withdrawn', 'Mengundurkan Diri'),
        ('completed', 'Selesai')
    ], string='Status Peserta', default='registered', tracking=True)
    
    grade_ids = fields.One2many('tipd_kkn.grade', 'participant_id', string='Nilai')

    def action_validate(self):
        for record in self:
            if not record.nim:
                continue
                
            # Create or find user for this participant
            user = self.env['res.users'].sudo().search([('login', '=', record.nim)], limit=1)
            if not user:
                # Get the portal group
                portal_group = self.env.ref('base.group_portal')
                
                user_name = record.name or record.partner_id.name or record.nim
                user = self.env['res.users'].sudo().create({
                    'name': user_name,
                    'login': record.nim,
                    'password': record.nim,
                    'partner_id': record.partner_id.id,
                    'group_ids': [(6, 0, [portal_group.id])],
                })
            
            record.status = 'active'
