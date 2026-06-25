# TIPD KKN Management (Odoo 19)

Modul ini adalah *backend engine* (Inti) dari Sistem Informasi Kuliah Kerja Nyata (KKN). Modul ini bertanggung jawab atas seluruh manajemen master data, relasi, dan logika bisnis administrasi KKN.

## Fitur Utama
1. **Master Program KKN**: Mendefinisikan periode/program KKN (Tema, Tahun, Tanggal, dan Status).
2. **Master Lokasi / Posko**: Mengelola data desa, kecamatan, kabupaten, dan provinsi penempatan.
3. **Data Peserta (Mahasiswa)**: Mengelola data mahasiswa yang mendaftar dan mengikuti program KKN.
4. **Data Dosen Pembimbing Lapangan (DPL)**: Mengelola data dosen yang bertugas membimbing di lapangan.
5. **Manajemen Kelompok**: Memetakan mahasiswa ke dalam kelompok beserta DPL dan lokasi pengabdiannya.
6. **Laporan Kegiatan Harian (LKH)**: Mahasiswa dapat mengunggah laporan harian (judul, tanggal, deskripsi, status). Tersedia tampilan **Kanban View**.
7. **Penilaian Akhir**: Fitur bagi DPL untuk memberikan nilai akhir mahasiswa.
8. **Native Odoo Chatter**: Menggunakan *mail.thread* bawaan Odoo untuk aktivitas komentar dan diskusi LKH, menggantikan sistem komentar manual di aplikasi lama.

## Prasyarat Instalasi (Prerequisites)
Sebelum menginstal modul ini, pastikan Anda telah:
1. Menginstal dan mengonfigurasi server **Odoo 19** sebagai *core engine*.
2. Memastikan service PostgreSQL berjalan dan terhubung dengan Odoo.

## Dependensi
- `base`
- `mail`

## Integrasi Portal Web
Jika Anda ingin mahasiswa dan DPL (Dosen) memiliki akses mandiri untuk mengisi form, melihat kelompok, melakukan pendaftaran KKN secara *online*, dan memvalidasi laporan harian *tanpa* perlu masuk ke *Backend Odoo*, pastikan Anda juga menginstal modul **`tipd_kkn_web`** (*Frontend Portal*).

## Panduan Penggunaan Singkat
1. Buka menu **Data Master > Program KKN**. Buat program baru. Klik teks **Aktif** di status bar untuk membuka pendaftaran (agar muncul di portal web).
2. Tentukan **Lokasi/Posko** KKN.
3. Tunggu hingga mahasiswa mendaftar (via portal web) atau input data peserta secara manual di menu **Peserta**.
4. Masuk ke menu **Kelompok**, buat kelompok baru, tetapkan DPL, Lokasi, lalu *Add a line* untuk memasukkan peserta ke dalam kelompok tersebut.
5. Peserta sekarang bisa melaporkan **LKH** dari portal. DPL dapat memvalidasinya.

---
*Developed by SufyALDI & Forum TIPD*
