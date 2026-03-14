# Panduan Struktur (Structure Guide)

Proyek **Python Knowledge Universe** disusun dengan analogi **Perpustakaan** untuk memudahkan navigasi konsep mulai dari yang paling luas hingga yang paling spesifik.

Semua penulisan aturan, kerangka, dan penataan menggunakan **Bahasa Indonesia** sebagai standar.

## Analogi Struktur

Berikut adalah pemetaannya ke dalam direktori:

| Tingkatan | Analogi | Contoh Direktori | Keterangan |
| :--- | :--- | :--- | :--- |
| **Level 1** | **Perpustakaan** | `/` (root) | Seluruh sistem proyek. |
| **Level 2** | **Rak (Shelf)** | `core/`, `specializations/` | Pengelompokan besar antara dasar bahasa (core) dan terapan ekosistem (specializations). |
| **Level 3** | **Sub-Rak (Sub-shelf)** | `core/01_fundamentals/` | Fase pembelajaran atau kategori domain (misal: tahap pemahaman dasar, atau domain data science). |
| **Level 4** | **Buku** | `core/01_fundamentals/01_python_basics/` | Kumpulan topik khusus yang dipelajari utuh. |
| **Level 5** | **Bab (Chapter) & Kode** | `01_variables.md`, `examples/` | Materi spesifik. Dibagi antara file teks `.md` dan folder `examples/` untuk sumber kode yang bisa dijalankan. |

## Aturan Pewajiban `README.md`

Guna memudahkan orientasi (agar pembaca tahu mereka sedang ada di "rak" sebelah mana), **setiap direktori (Rak, Sub-Rak, Buku) WAJIB memiliki file `README.md`**.

- **Di level Rak** (`core/README.md`): Menjelaskan tujuan keseluruhan rak ini.
- **Di level Sub-Rak** (`core/01_fundamentals/README.md`): Menjelaskan fase ini, apa sasarannya, dan buku-buku apa yang ada di dalamnya.
- **Di level Buku** (`.../01_python_basics/README.md`): Bertindak sebagai pengantar materi bab-bab di dalam buku tersebut (Mirip Kata Pengantar / Daftar Isi).

## Konvensi Penamaan

1. **Folder / File (selain `README.md`)**: Penamaan menggunakan *snake_case* dengan awalan angka numerik `01_`, `02_`, dst untuk memastikan urutan pembelajaran (contoh: `01_python_basics`, `01_web_development`).
2. **Bab**: Format `.md` dan berurut (contoh: `01_variabel.md`).
3. **Kode Praktik**: Disimpan terpisah di folder `examples/` di dalam buku.

## Templat Buku
Setiap folder Buku baru sebaiknya diatur seperti ini:
```text
<urutan>_<nama_buku>/
|-- README.md        <- Wajib ada. Menjelaskan tentang buku dan daftar bab.
|-- 01_<nama_bab>.md
|-- 02_<nama_bab>.md
`-- examples/        <- Opsional jika buku punya file script.
    `-- script_terkait.py
```
