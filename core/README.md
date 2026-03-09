# Core Python

Bagian ini adalah rak fondasi Python di dalam Python Knowledge Universe.

Fokus utamanya adalah memahami bagaimana Python bekerja, bukan hanya cara menulis sintaks. Setelah menyelesaikan Core, pembaca akan lebih siap masuk ke jalur spesialisasi seperti web development, data science, machine learning, AI engineering, dan automation.

## Untuk Siapa Bagian Ini

- pemula yang ingin jalur belajar Python yang runtut
- developer yang ingin merapikan fondasi konsep Python
- pembaca yang ingin memahami behavior Python secara internal

## Cara Membaca Core

Ada dua mode penggunaan:

1. Jalur berurutan: baca dari buku 01 sampai 15 untuk membangun fondasi penuh.
2. Jalur referensi: lompat ke buku tertentu saat butuh topik spesifik.

## Peta 15 Buku Core

| No | Buku | Tujuan Utama | Status |
|---|---|---|---|
| 01 | Python Basics | Menguasai sintaks, struktur dasar, dan pola pemrograman awal | In Progress |
| 02 | Language Design | Memahami filosofi dan prinsip desain bahasa Python | Planned |
| 03 | Execution Model | Memahami alur eksekusi kode Python | Planned |
| 04 | Object Model | Memahami sistem object, type, dan attribute | Planned |
| 05 | Memory Management | Memahami referensi objek dan manajemen memori | Planned |
| 06 | Modules and Import System | Memahami modularisasi dan mekanisme import | Planned |
| 07 | Standard Library | Menguasai library bawaan Python yang esensial | Planned |
| 08 | File System and IO | Mengelola file, path, stream, dan operasi IO | Planned |
| 09 | Networking | Dasar komunikasi jaringan dengan Python | Planned |
| 10 | Concurrency | Dasar thread, process, dan parallel execution | Planned |
| 11 | Async Programming | Dasar event loop, coroutine, dan asyncio | Planned |
| 12 | Testing | Dasar pengujian unit, integrasi, dan strategi validasi | Planned |
| 13 | Packaging | Dasar distribusi package dan metadata proyek | Planned |
| 14 | Virtual Environments | Manajemen environment dan dependency proyek | Planned |
| 15 | Tooling | Ekosistem alat bantu development Python modern | Planned |

## Struktur Direktori

```text
core/
|
|-- 01_python_basics/
|-- 02_language_design/
|-- 03_execution_model/
|-- 04_object_model/
|-- 05_memory_management/
|-- 06_modules_import_system/
|-- 07_standard_library/
|-- 08_file_system_io/
|-- 09_networking/
|-- 10_concurrency/
|-- 11_async_programming/
|-- 12_testing/
|-- 13_packaging/
|-- 14_virtual_environments/
`-- 15_tooling/
```

Setiap direktori merepresentasikan satu buku utama.

## Learning Path Rekomendasi

### Jalur Pemula

1. 01_python_basics
2. 02_language_design
3. 03_execution_model
4. 04_object_model
5. 05_memory_management
6. 06_modules_import_system
7. 07_standard_library
8. 08_file_system_io
9. 09_networking
10. 10_concurrency
11. 11_async_programming
12. 12_testing
13. 13_packaging
14. 14_virtual_environments
15. 15_tooling

### Jalur Intermediate

1. 03_execution_model
2. 04_object_model
3. 05_memory_management
4. 06_modules_import_system
5. 11_async_programming
6. 13_packaging
7. 15_tooling

## Prasyarat Sebelum Masuk Specializations

- sudah menyelesaikan minimal buku 01, 06, 07, 12, 13, dan 14
- mampu membaca dokumentasi resmi Python
- mampu menjalankan project dengan virtual environment

## Standar Kualitas Konten per Buku

- setiap buku memiliki `README.md` sebagai peta materi
- materi turunan menggunakan urutan numerik (`01_`, `02_`, dst)
- contoh kode harus runnable dan jelas output/perilakunya
- konsep penting wajib menyertakan referensi resmi
- gunakan istilah konsisten dengan `docs/glossary.md`

## Kebijakan Aset Visual (Core)

- jangan membuat aset visual (`assets/*.svg`) di awal saat konten buku masih berkembang
- selesaikan dulu konten buku sampai status draft final (content lock) per bab atau per buku
- lakukan review pedagogi dan konsistensi istilah sebelum desain visual
- setelah konten stabil, baru buat diagram spesifik per bab berdasarkan konsep final
- hindari template visual generik yang tidak merepresentasikan konsep bab secara akurat

## Progress Tracker

| Status | Arti |
|---|---|
| Planned | Topik sudah didefinisikan, konten belum ditulis |
| In Progress | Konten sedang ditulis atau direview |
| Published | Konten siap digunakan |
| Revision | Konten sudah ada tetapi perlu pembaruan |

## Kontribusi ke Bagian Core

- Panduan global: `docs/contribution-guide.md`
- Panduan khusus Core: `core/docs/CONTRIBUTING.md`

## Referensi

Materi Core Python dirancang berdasarkan sumber utama:
- Python Official Documentation
- Python Language Reference
- Python Standard Library Documentation
- Python Enhancement Proposals (PEP)
- sumber kode CPython
