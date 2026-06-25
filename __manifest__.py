# -*- coding: utf-8 -*-
###############################################################################
#
#    TIPD - Total Integrated Platform for Digital-Education.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'TIPD KKN Management',
    'version': '1.0',
    'category': 'Education/KKN',
    'summary': 'Modul untuk Manajemen Kuliah Kerja Nyata (KKN)',
    'description': """
        Sistem Manajemen KKN meliputi:
        - Pengelolaan Program / Periode KKN
        - Pengelolaan Kelompok & Posko
        - Pendaftaran & Pendataan Mahasiswa (Peserta)
        - Dosen Pembimbing Lapangan (DPL)
        - Logbook / Laporan Kegiatan Harian (LKH)
        - Penilaian
    """,
    'author': 'SufyALDI - Forum TIPD',
    'website': '',
    'depends': ['base', 'mail', 'account'],
    'data': [
        'security/kkn_security.xml',
        'security/ir.model.access.csv',
        'data/kkn_master_data.xml',
        'data/kkn_dummy_data.xml',
        'views/kkn_program_views.xml',
        'views/kkn_location_views.xml',
        'views/kkn_master_views.xml',
        'views/kkn_group_views.xml',
        'views/kkn_participant_views.xml',
        'views/kkn_supervisor_views.xml',
        'views/kkn_activity_views.xml',
        'views/kkn_grade_views.xml',
        'views/kkn_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
