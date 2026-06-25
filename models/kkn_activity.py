# -*- coding: utf-8 -*-
from odoo import models, fields

class KknActivity(models.Model):
    _name = 'tipd_kkn.activity'
    _description = 'Laporan Kegiatan Harian (LKH)'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Judul Kegiatan', required=True, tracking=True)
    date = fields.Date(string='Tanggal Pelaksanaan', default=fields.Date.context_today, required=True, tracking=True)
    
    group_id = fields.Many2one('tipd_kkn.group', string='Kelompok', required=True, tracking=True)
    participant_id = fields.Many2one('tipd_kkn.participant', string='Dilaporkan Oleh', tracking=True)
    
    description = fields.Html(string='Uraian Kegiatan', required=True)
    image = fields.Image(string='Foto Dokumentasi', max_width=1920, max_height=1920)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Diajukan'),
        ('approved', 'Disetujui DPL'),
        ('rejected', 'Ditolak')
    ], string='Status', default='draft', tracking=True)

    def action_submit(self):
        for record in self:
            record.state = 'submitted'

    def action_approve(self):
        for record in self:
            record.state = 'approved'
            # Cari atau buat blog khusus KKN (gunakan sudo agar DPL tidak terkena limitasi hak akses)
            blog = self.env['blog.blog'].sudo().search([('name', 'ilike', 'Berita KKN')], limit=1)
            if not blog:
                blog = self.env['blog.blog'].sudo().create({
                    'name': 'Berita KKN',
                    'subtitle': 'Publikasi Kegiatan Mahasiswa KKN'
                })
            
            # Buat postingan blog (dengan sudo)
            author_id = self.env.user.partner_id.id
            if record.participant_id and record.participant_id.partner_id:
                author_id = record.participant_id.partner_id.id
                
            # Siapkan data blog
            blog_vals = {
                'name': record.name,
                'subtitle': f'Dilaporkan oleh {record.participant_id.name} ({record.group_id.name}) pada {record.date}',
                'content': record.description,
                'blog_id': blog.id,
                'author_id': author_id,
                'is_published': True,
            }

            # Jika ada gambar dokumentasi, jadikan background cover di Berita Blog
            if record.image:
                import json
                # Format URL standar Odoo untuk memanggil image
                image_url = f"/web/image/tipd_kkn.activity/{record.id}/image"
                cover_properties = {
                    "background-image": f"url('{image_url}')",
                    "background_color_class": "o_cc3",
                    "opacity": "0.5",
                    "resize_class": "o_half_screen_height"
                }
                blog_vals['cover_properties'] = json.dumps(cover_properties)
                
            self.env['blog.post'].sudo().create(blog_vals)

    def action_reject(self):
        for record in self:
            record.state = 'rejected'

    def action_draft(self):
        for record in self:
            record.state = 'draft'
