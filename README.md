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
- menjadi dokumentasi yang terus berkembang
- menjadi dasar untuk website pembelajaran Python

## Struktur Pengetahuan

Repository ini dirancang dengan analogi sebuah perpustakaan, di mana struktur tertata dari tingkat yang luas hingga ke materi spesifik (Perpustakaan -> Rak -> Sub-Rak -> Buku -> Bab).

Repository ini dibagi menjadi dua **Rak** utama.

### 1. Rak Core (`core/`)

Core adalah rak fondasi. Rak ini dibagi lagi menjadi beberapa **Sub-Rak** (Fase) untuk memandu perjalanan belajar:

1. **01_fundamentals**: Pemahaman dasar tentang bahasa (`01_python_basics`, `02_language_design`)
2. **02_advanced_concepts**: Konsep mendalam di balik layar (`01_execution_model`, `02_object_model`, `03_memory_management`)
3. **03_system_and_io**: Interaksi program dengan sistem operasi (`01_modules_import_system`, `02_file_system_io`, `03_networking`)
4. **04_concurrency**: Eksekusi paralel dan asynchronous (`01_concurrency`, `02_async_programming`)
5. **05_ecosystem_and_tooling**: Perangkat pengembangan dunia nyata (`01_standard_library`, `02_testing`, `03_packaging`, `04_virtual_environments`, `05_tooling`)

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
