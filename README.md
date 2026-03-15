# Python Knowledge Universe

Python Knowledge Universe adalah rak buku digital tentang Python yang disusun terstruktur, modular, dan terus berkembang.

Repository ini dirancang sebagai:
- sistem pembelajaran Python
- peta pengetahuan Python
- fondasi website dokumentasi
- portfolio teknikal

Tujuan utamanya adalah membangun struktur pengetahuan Python yang jelas, bertahap, dan mudah dipahami oleh manusia maupun AI.

## Tujuan Proyek

- menyusun pengetahuan Python secara sistematis
- menyediakan jalur belajar Python yang jelas
- menjadi referensi Python jangka panjang
- **menjadi ekosistem hidup (living document) yang terus berkembang mengikuti rilis terbaru Python**
- menjadi dasar untuk website pembelajaran Python

## Struktur Pengetahuan

Repository ini dirancang dengan analogi sebuah perpustakaan, di mana struktur tertata dari tingkat yang luas hingga ke materi spesifik (Perpustakaan -> Rak -> Sub-Rak -> Buku -> Bab).

Repository ini dibagi menjadi dua **Rak** utama.

### 1. Rak Core (`core/`)

Core adalah rak fondasi. Rak ini dibagi lagi menjadi beberapa **Sub-Rak** (Fase) untuk memandu perjalanan belajar:

1. **01_python_basics**: Fondasi paling awal: sintaks, variabel, tipe data, dan kontrol alur.
2. **02_data_and_logic**: Struktur data, fungsi, modularitas, I/O, dan pola pemrograman dasar.
3. **03_object_oriented_programming**: Paradigma pemrograman berbasis objek sebagai jembatan ke Rak 02.
4. **04_language_design**: Filosofi *The Zen of Python*, prinsip desain bahasa, dan kebiasaan *Pythonic*.

### 2. Rak Specializations (`specializations/`)

Specializations adalah rak terapan. Setelah memahami Core Python, pembaca dapat memilih sub-rak domain spesifik:

- `01_web_development`
- `02_data_science`
- `03_machine_learning`
- `04_ai_engineering`
- `05_automation`

## Arsitektur Rak

Model organisasi repository ini:

1. `root` adalah Perpustakaan (Library).
2. `core/` & `specializations/` adalah Rak Utama (Shelf).
3. `core/01_fundamentals/` adalah Sub-Rak (Fase/Domain).
4. `core/01_fundamentals/01_python_basics/` adalah Buku.
5. `.../01_python_basics/01_variables.md` adalah Bab (Chapter).

Setiap sub-rak dan buku di atas akan memiliki file `README.md` tersendiri.

*Untuk aturan rinci penggunaan direktori dan penamaan, silakan baca `docs/structure-guide.md`.*

## Struktur Repository

```text
python-knowledge-universe/
|
|-- README.md
|-- docs/
|   |-- roadmap.md
|   |-- glossary.md
|   |-- structure-guide.md
|   `-- contribution-guide.md
|
|-- core/
|   |-- README.md
|   |-- 01_fundamentals/
|   |-- 02_advanced_concepts/
|   |-- 03_system_and_io/
|   |-- 04_concurrency/
|   `-- 05_ecosystem_and_tooling/
|
`-- specializations/
    |-- README.md
    |-- 01_web_development/
    |-- 02_data_science/
    |-- 03_machine_learning/
    |-- 04_ai_engineering/
    `-- 05_automation/
```

## Cara Menggunakan Repository

### 1. Jalur Belajar Berurutan

Urutan rekomendasi untuk pemula adalah mengikuti urutan nomor pada direktori `core/`. Selesaikan semua buku di sub-rak `01_fundamentals` sebelum berpindah ke `02_advanced_concepts`, dan seterusnya.

Lanjutkan ke bagian `specializations` setelah menyelesaikan `core`.

### 2. Jalur Referensi

Jika sudah familiar dengan Python, pembaca dapat langsung menuju rak, sub-rak, atau buku tertentu sesuai kebutuhan, membaca ringkasan pada `README.md` masing-masing folder.

---

## Katalog & Status Buku

Sebagai proyek yang terus berkembang, tabel ini mencatat versi terkini dari perombakan/penulisan buku yang sedang aktif (Berdasarkan log dari masing-masing folder buku):

| Rak | Buku | Status | Versi Rilis | Terakhir Diperbarui |
| :--- | :--- | :--- | :--- | :--- |
| Core | [01_python_basics](core/01_fundamentals/01_python_basics) | Published | Core.Fundamentals.01.00 | 2026-03-14 |
| Core | [02_data_and_logic](core/01_fundamentals/02_data_and_logic) | Published | Core.Fundamentals.02.00 | 2026-03-14 |
| Core | [03_object_oriented_programming](core/01_fundamentals/03_object_oriented_programming) | Published | Core.Fundamentals.03.01 | 2026-03-15 |
| Core | [04_language_design](core/01_fundamentals/04_language_design) | Draft Complete | Core.Fundamentals.04.00 | 2026-03-14 |
| ... | ... | ... | ... | ... |

*(Tabel di atas akan terus diperbarui secara manual setiap kali ada sebuah buku yang resmi dilabeli "Rilis" dari versi unreleased-nya).*

---

## Status Proyek

- `Planned`: topik direncanakan
- `In Progress`: topik sedang ditulis
- `Published`: topik tersedia
- `Revision`: topik perlu diperbarui

## Kontribusi

Kontribusi terbuka untuk:
- perbaikan dokumentasi
- penambahan topik
- contoh kode
- peningkatan struktur

Lihat panduan kontribusi di `docs/contribution-guide.md`.

## Visi Jangka Panjang

- website dokumentasi Python
- sistem pembelajaran Python
- knowledge base Python
- referensi teknikal Python

## Filosofi Proyek

Belajar Python bukan hanya tentang sintaks, tetapi memahami bagaimana bahasa ini bekerja secara mendalam.

## Author

Project ini dibuat sebagai bagian dari perjalanan belajar dan eksplorasi Python.
