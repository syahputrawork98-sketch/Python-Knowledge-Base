# Contribution Guide

Terima kasih atas minat kontribusi ke Python Knowledge Universe.

## Jenis Kontribusi

- perbaikan typo dan kejelasan bahasa
- penambahan materi atau contoh kode
- perbaikan struktur dokumen
- pembaruan referensi resmi Python

## Standar Penulisan

- gunakan bahasa yang jelas, ringkas, dan konsisten
- prioritaskan akurasi berdasarkan sumber resmi
- sertakan contoh kode yang mudah diuji
- gunakan penamaan file snake_case

## Struktur Pull Request

Setiap pull request sebaiknya berisi:

1. ringkasan perubahan
2. alasan perubahan
3. dampak ke bagian lain (jika ada)
4. checklist validasi sederhana

## Checklist Sebelum PR

- [ ] tautan internal tidak rusak
- [ ] format markdown rapi
- [ ] istilah konsisten dengan `glossary.md`
- [ ] referensi teknis valid
- [ ] `CHANGELOG.md` yang relevan sudah diperbarui

## Konvensi Konten Core

- `core` dibagi menjadi beberapa Sub-rak (Fase Pembelajaran).
- di dalam Sub-rak terdapat folder-folder yang mewakili satu Buku/topik besar.
- setiap folder (Sub-rak dan Buku) wajib punya `README.md` sebagai peta materi.
- file bab (chapter) wajib berbentuk **folder bab** yang berisi `README.md` teks materinya.

## Konvensi Konten Specialization

- setiap specialization punya README sendiri
- setiap domain specialization berada di `specializations/<domain>/`
- buku di dalam domain menggunakan folder bernomor, contoh `specializations/ai-engineering/01_llm_fundamentals/`
- setiap folder buku wajib punya `README.md` sebagai peta isi buku
- setiap folder buku wajib punya `CHANGELOG.md`
- urutan buku menggunakan prefix numerik (`01_`, `02_`, dst)
- jelaskan prasyarat Core yang dibutuhkan
- bedakan materi konsep, praktik, dan project

## Konvensi Kode Buku

Gunakan kode unik per buku agar tracking perubahan konsisten.

- Core: `CORE-01`, `CORE-02`, ..., `CORE-15`
- Specialization Web: `SPEC-WEB-01`, `SPEC-WEB-02`, ...
- Specialization Data Science: `SPEC-DS-01`, `SPEC-DS-02`, ...
- Specialization Machine Learning: `SPEC-ML-01`, `SPEC-ML-02`, ...
- Specialization AI Engineering: `SPEC-AI-01`, `SPEC-AI-02`, ...
- Specialization Automation: `SPEC-AUTO-01`, `SPEC-AUTO-02`, ...

## Aturan CHANGELOG dan Versioning (Rilis)

Sistem versi pada buku mengikuti alamat penyimpanannya di rak (contoh: `[Rak].[Sub-Rak].[Buku].[Revisi]`).

### Alur Kerja Draft (Unreleased)
Saat materi atau bab baru dari sebuah buku sedang ditulis atau direvisi pelan-pelan, perubahannya dicatat di file `CHANGELOG.md` pada buku tersebut di bawah label khusus `[Unreleased]`. Pada tahap ini, buku belum dianggap "merilis" versi baru.

### Alur Kerja Rilis (Released)
Buku tidak dianggap memiliki versi stabil terbaru hingga mendapat instruksi "Rilis". Saat dirilis, seluruh catatan draf di blok `[Unreleased]` digabung (di-bundle) menjadi versi rilis yang sesungguhnya (misal `v1.1.1.0`), lalu blok `[Unreleased]` dikosongkan kembali untuk memantau pekerjaan tahap selanjutnya.

### Format Entry CHANGELOG Buku
Setiap `CHANGELOG.md` buku wajib mengikuti kerangka dari templat bawaan repository `docs/changelog-template.md`.
Minimal memuat:
- Konstanta `Book Code`
- Status `Current Version` (Sesuai alamat rak)
- Daftar perubahan yang diatur dalam blok `[Unreleased]` maupun Rilis.
