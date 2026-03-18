# Core Contribution Guide

Panduan ini khusus untuk kontribusi pada sub-rak `core/`.

## Scope

Dokumen ini mengatur:

- struktur folder buku Core
- standar isi dokumen dan kode contoh
- aturan versioning dan changelog
- alur kontribusi dari draft sampai merge
- standar review dan quality gate

Dokumen global tetap berlaku di `docs/contribution-guide.md`.

## Prinsip Dasar

- akurat secara teknis
- konsisten secara struktur
- mudah dipelajari bertahap
- mudah ditelusuri histori perubahannya

## Struktur Wajib Core

Struktur minimum:

```text
core/
|-- README.md
|-- 01_<sub-rak>/
|   |-- README.md
|   `-- 01_<book>/
|       |-- README.md
|       |-- CHANGELOG.md
|       `-- 01_<chapter>/
|           |-- README.md
|           |-- assets/
|           `-- examples/
```

## Konvensi Nama

- folder buku: `NN_<book_slug>` (contoh: `02_language_design`)
- file bab: `NN_<chapter_slug>.md` (contoh: `01_getting_started.md`)
- gunakan snake_case dan ASCII

## Metadata Wajib README Buku

Setiap `core/<book>/README.md` wajib memiliki metadata di bagian atas:

- `Book Code` (contoh: `CORE-02`)
- `Version` (contoh: `v0.1.0`)
- `Last Updated` (format `YYYY-MM-DD`)
- `Status` (`Planned`, `In Progress`, `Published`, `Revision`)

Contoh:

```md
# Language Design

Book Code: CORE-02
Version: v0.1.0
Last Updated: 2026-03-08
Status: Planned
```

## Standar Struktur README Buku

Minimal berisi bagian berikut:

1. Ringkasan buku
2. Tujuan pembelajaran
3. Daftar bab
4. Prasyarat
5. Keterkaitan dengan buku Core lain
6. Referensi utama

## Standar Struktur Bab

Setiap file bab minimal punya:

1. `Tujuan`
2. `Konsep Inti`
3. `Contoh Kode`
4. `Catatan Praktis`
5. `Ringkasan`
6. `Referensi`

Template resmi bab tersedia di root `docs/chapter-template.md`.

## Standar Pedagogi Bab (Wajib)

Setiap bab wajib memuat elemen pedagogi berikut agar mudah dipahami:

1. `Analogi` (Bisa berupa **Analogi Singkat** 1 kalimat, atau **Analogi Panjang** berupa cerita. Gunakan keduanya jika materinya sangat baru dan abstrak, gunakan analogi singkat saja jika materinya sederhana).
2. `Tujuan Besar`
3. `Tujuan Kecil` (3-7 poin terukur)
4. `Peruntukan` (kapan dipakai)
5. `Bukan Peruntukan` (kapan tidak tepat dipakai)
6. `Hasil Belajar` (setelah bab ini, pembaca bisa ...)

## Standar SVG per Bab (Wajib)

Setiap bab wajib memiliki visual `.svg` untuk membantu pemahaman. Namun ada aturan tegas mengenai pembuatannya:

1. **Dilarang menggunakan Template:** Tidak ada template baku untuk SVG. File gambar tidak boleh dibuat kosong di awal.
2. **Dibuat Setelah Teks Selesai:** Gambar `.svg` **hanya boleh di-generate setelah seluruh teks materi bab tersebut selesai ditulis dan disepakati**.
3. **Visualisasi Konteks:** Gambar harus secara langsung merepresentasikan dan memperkuat deskripsi / analogi dari teks yang sudah dibuat sebelumnya.
4. **Penyimpanan:** SVG tersebut disimpan di `assets/` di dalam folder bab terkait (contoh: `01_getting_started/assets/01_getting_started.svg`).
5. **Keterbacaan:** SVG harus di-embed ke dalam `README.md` bab menggunakan format Markdown dengan Alt-Text yang relevan.

Contoh penyisipan akhir (setelah bab selesai ditulis):

```md
![Big picture alur eksekusi Python](assets/03_execution_model.svg)
```

## Standar Kode Contoh

- code block diberi bahasa (misal `python`, `bash`)
- contoh harus runnable dan tidak ambigu
- output penting dijelaskan
- hindari dependency eksternal kecuali dibutuhkan
- jika butuh versi Python spesifik, tulis eksplisit

## Standar Contoh dan Pitfall

Setiap bab minimal memiliki:

- 1 contoh penggunaan benar
- 1 pitfall umum + cara memperbaikinya
- expected output untuk bagian penting
- catatan error yang sering terjadi

## Standar Referensi

Prioritas sumber:

1. Python Official Documentation
2. Python Language Reference
3. Python Standard Library Documentation
4. PEP
5. CPython source (jika relevan)

Jika menggunakan sumber non-resmi, jelaskan alasan penggunaannya.

## Standar Latihan dan Evaluasi

Setiap bab sebaiknya memuat:

1. latihan dasar
2. latihan menengah
3. mini challenge praktik
4. 3 pertanyaan refleksi singkat
5. checklist lulus bab

Contoh checklist lulus bab:

- [ ] memahami konsep inti bab
- [ ] menjalankan seluruh contoh tanpa error
- [ ] menyelesaikan mini challenge
- [ ] mampu menjelaskan analogi dengan bahasa sendiri

## Aturan Versioning Buku

Gunakan semantic versioning ringan:

- `v0.x.y` untuk fase draft
- naikkan `x` jika perubahan struktur besar buku
- naikkan `y` jika update konten minor/perbaikan

Panduan singkat:

- tambah bab baru besar: `v0.1.0` -> `v0.2.0`
- revisi isi bab kecil: `v0.2.0` -> `v0.2.1`

## Aturan CHANGELOG Bertingkat

Level changelog:

- `core/CHANGELOG.md` untuk perubahan lintas buku
- `core/<book>/CHANGELOG.md` untuk perubahan di buku tersebut

## Format Wajib CHANGELOG Buku

Header wajib:

- `Book Code`
- `Version`
- `Last Updated`

Setiap entry wajib:

- `Date`
- `Changed`
- `Reason`
- `Impact`

Contoh:

```md
# CHANGELOG

Book Code: CORE-02
Version: v0.1.0
Last Updated: 2026-03-08

## 2026-03-08
- Changed: Menambah kerangka 8 bab awal.
- Reason: Menetapkan urutan belajar buku.
- Impact: Contributor dapat menulis bab tanpa konflik struktur.
```

## Kapan Harus Update Log

- ubah isi buku -> update `core/<book>/CHANGELOG.md`
- ubah metadata buku (`Version`, `Status`) -> update `core/<book>/CHANGELOG.md`
- ubah struktur lintas buku -> update `core/CHANGELOG.md`
- jika keduanya terjadi -> update keduanya

## Workflow Kontribusi

1. pilih buku target
2. baca `README.md` dan `CHANGELOG.md` buku
3. lakukan perubahan terfokus
4. update changelog yang relevan
5. cek konsistensi link, format, dan istilah
6. ajukan PR dengan ringkasan jelas

## Standar Pull Request untuk Core

PR Core wajib memuat:

1. ringkasan perubahan
2. alasan perubahan
3. file yang terdampak
4. dampak ke pembaca
5. status update changelog

Template ringkas PR:

```md
## Summary
- ...

## Reason
- ...

## Impact
- ...

## Changelog Updated
- [ ] core/<book>/CHANGELOG.md
- [ ] core/CHANGELOG.md (jika lintas buku)
```

## Quality Gate Sebelum Merge

- [ ] metadata `README.md` valid
- [ ] `Version` sinkron dengan `CHANGELOG.md`
- [ ] status buku sesuai kondisi nyata
- [ ] tautan internal valid
- [ ] istilah konsisten dengan `docs/glossary.md`
- [ ] contoh kode terbaca dan runnable
- [ ] SVG bab tersedia sesuai standar
- [ ] elemen pedagogi bab terisi lengkap
- [ ] format markdown rapi

## Definition of Done per Bab

Bab dianggap selesai jika:

- struktur bab lengkap sesuai template
- analogi, tujuan besar, tujuan kecil, dan peruntukan jelas
- minimal 1 diagram `.svg` tersedia dan relevan
- contoh kode benar-benar runnable
- latihan dan checklist evaluasi tersedia
- referensi resmi dicantumkan
- changelog buku diperbarui

## Aturan Emoji (Opsional)

Emoji boleh dipakai untuk membantu navigasi visual, dengan batas:

- tidak menggantikan istilah teknis
- digunakan konsisten di seluruh Core
- gunakan seperlunya (hindari berlebihan)
- tetap jaga keterbacaan dokumen tanpa emoji

## Kriteria Status Buku

- `Planned`: struktur ada, konten inti belum ditulis
- `In Progress`: konten sedang aktif dikembangkan
- `Published`: konten stabil dan siap dipakai belajar
- `Revision`: konten terbit tetapi perlu pembaruan penting

## Larangan Umum

- menghapus metadata wajib README/CHANGELOG
- mengubah `Book Code` buku yang sudah dipakai
- menambah klaim teknis tanpa referensi
- mencampur perubahan lintas banyak buku tanpa alasan jelas

## Kontak Struktur

Untuk perubahan aturan global repository, gunakan `docs/contribution-guide.md`.
Untuk aturan khusus Core, dokumen ini menjadi acuan utama.
