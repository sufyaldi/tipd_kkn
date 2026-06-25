# -*- coding: utf-8 -*-
from odoo import models, fields

class KknSupervisor(models.Model):
    _name = 'tipd_kkn.supervisor'
    _description = 'Dosen Pembimbing Lapangan'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Dosen (DPL)', required=True, domain=[('is_company', '=', False)])
    nip = fields.Char(string='NIP / NIDN', related='partner_id.ref', readonly=False, store=True)
    
    group_ids = fields.One2many('tipd_kkn.group', 'supervisor_id', string='Kelompok Bimbingan')
    program_id = fields.Many2one('tipd_kkn.program', string='Program KKN')

    def action_create_user(self):
        for record in self:
            if not record.nip:
                continue
                
            # Cek apakah user sudah ada
            user = self.env['res.users'].sudo().search([('login', '=', record.nip)], limit=1)
            if not user:
                # DPL masuk ke grup Internal User (agar bisa akses backend) dan grup DPL KKN
                group_internal = self.env.ref('base.group_user')
                group_dpl = self.env.ref('tipd_kkn.group_kkn_supervisor')
                
                user_name = record.partner_id.name or record.nip
                user = self.env['res.users'].sudo().create({
                    'name': user_name,
                    'login': record.nip,
                    'password': record.nip,
                    'partner_id': record.partner_id.id,
                    'groups_id': [(6, 0, [group_internal.id, group_dpl.id])],
                })
