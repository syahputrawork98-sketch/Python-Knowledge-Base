# CHANGELOG

> Format berdasarkan panduan versi internal (`Rak.SubRak.Buku.Revisi`).

**Book Code:** CORE-01
**Current Version:** Core.Fundamentals.01.00
**Last Updated:** 2026-03-14

---

## [Unreleased]
*Catatan perubahan yang sedang dikerjakan ("Draf") dan belum dirilis secara resmi.*

---

## [Core.Fundamentals.01.00] - 2026-03-14
### Ditambahkan
- **Bab 14 (`14_basic_programming_patterns`):** Penulisan draf materi pola pemrograman dasar menggunakan Analogi "Buku Resep & Cetak Biru Logika". Membahas pola-pola esensial seperti *Accumulator*, *Filtering*, *Searching*, dan *Counting*.
- **Bab 13 (`13_builtin_functions`):** Penulisan draf materi fungsi bawaan menggunakan Analogi "Sabuk Alat Tukang Ahli". Membahas alat ukur (`len`, `sum`), alat identifikasi (`type`, `dir`), serta alat perulangan modern (`range`, `enumerate`, `zip`).
- **Bab 12 (`12_exception_handling`):** Penulisan draf materi sistem keamanan menggunakan Analogi "Manajemen Krisis Gedung". Membahas penggunaan `try`, `except`, `else`, `finally`, dan cara melempar error manual dengan `raise`.
- **Bab 11 (`11_file_handling`):** Penulisan draf materi interaksi file menggunakan Analogi "Sekretaris Digital & Lemari Arsip". Membahas siklus `open-work-close`, mode file (`r, w, a`), kekuatan `with`, dan mekanisme *buffering*.
- **Bab 10 (`10_input_output`):** Penulisan draf materi interaksi terminal menggunakan Analogi "Meja Resepsionis". Membahas `input()`, `print()`, f-string, dan validasi tipe data dasar.
- **Bab 09 (`09_modules_and_import`):** Penulisan draf materi modularitas menggunakan Analogi "Ekspedisi Logistik Kargo". Membahas cara pemecahan file (`import`), struktur folder (`package`), peran `__init__.py`, serta rahasia identitas `__name__`.
- **Bab 08 (`08_basic_data_structures`):** Penulisan draf materi struktur data menggunakan Analogi "Manajemen Gudang Pusat". Menjelaskan perbedaan fungsional antara `list`, `tuple`, `set`, dan `dict`, beserta mekanisme internal *Hash Table*.
- **Bab 07 (`07_functions`):** Penulisan draf materi fungsi menggunakan metafora "Stasiun Masak/Pabrik Mini". Membahas anatomi `def`, perbedaan parameter vs argumen, kekuatan `return`, serta isolasi variabel (*Scope*).
- **Bab 06 (`06_control_flow`):** Penulisan draf materi kendali alur menggunakan Analogi "Navigasi Jalan Raya". Menjelaskan `if/else` sebagai persimpangan, `for` sebagai bus wisata, dan `while` sebagai bundaran. Dilengkapi 4 skrip simulasi sistem lalu lintas.
- **Bab 05 (`05_operators_and_expressions`):** Penulisan ulang materi operator menggunakan metafora "Alat Masak & Hierarki Resep". Mencakup detail *precedence*, *short-circuit logic*, dan mekanisme internal *dunder methods* secara konseptual.
- **Bab 04 (`04_basic_data_types`):** Ditulis ulang seutuhnya menggunakan Analogi "Wadah Kemasan Pasar". Menambahkan tabel Istilah Kunci lengkap dan demonstrasi interaktif penggunaan inspektur obyek `type()` serta trik konversi paksa (*Type Casting*). Disertai satu diagram SVG pengolahan *parsing* data.
- **Bab 03 (`03_variables_and_names`):** Ditulis ulang seutuhnya dengan implementasi Analogi Gudang & Stiker Label. Menyertakan bab komprehensif tentang teori *Name Binding*, konsep mutable vs immutable, bahaya aliasing, serta visual SVG arsitektur objek.
- **Bab 02 (`02_python_syntax`):** Ditulis ulang seutuhnya; materi difokuskan pada penguasaan pemehaman indentasi 4 spasi, statement tunggal, blok kode, dan sintaks komentar `#`. Dilengkapi diagram visual "Tata Bahasa Python" dan dua berkas contoh.
- **Bab 01 (`01_getting_started`):** Ditulis ulang seutuhnya menggunakan format Bab Folder, Analogi Ganda (Pendek/Panjang), dan pemecahan file instruksi REPL vs Script ke dalam `examples/`.

---

## [v0.3.5] - 2026-03-08
- Changed: Menambahkan section `Hasil Belajar` pada seluruh bab 01-14, memperbaiki urutan prasyarat di `11_file_handling.md`, dan menambahkan catatan alasan penggunaan referensi non-resmi di bab 14.
- Reason: Menutup temuan review agar seluruh bab selaras dengan standar wajib pada `core/docs/CONTRIBUTING.md`.
- Impact: Konsistensi pedagogi dan kepatuhan struktur buku meningkat sehingga buku siap masuk tahap commit.

## 2026-03-08
- Changed: Mendesain ulang seluruh aset SVG bab 01-14 dengan visual map yang lebih jelas dan menambahkan emoji sebagai anchor pembelajaran.
- Reason: Meningkatkan keterbacaan visual serta diferensiasi identitas tiap bab agar lebih mudah dipahami.
- Impact: Materi visual buku 01 sekarang lebih kuat untuk mendukung pemahaman konsep inti di setiap bab.

## 2026-03-08
- Changed: Menulis konten nyata untuk `14_basic_programming_patterns.md` meliputi pola IPO, guard clause, accumulator, refactor fungsi kecil, pitfall, dan mini challenge end-to-end.
- Reason: Mengganti placeholder bab 14 agar buku ditutup dengan pola integrasi konsep yang dapat langsung dipraktikkan.
- Impact: Bab penutup Python Basics kini menjadi jembatan praktis menuju mini project yang lebih utuh.

## 2026-03-08
- Changed: Menulis konten nyata untuk `13_builtin_functions.md` mencakup built-in penting (len/sum/min/max/enumerate/zip/map/filter), pitfall, dan latihan.
- Reason: Mengganti placeholder bab 13 agar pembaca dapat menulis kode lebih idiomatik dengan toolkit bawaan Python.
- Impact: Pemahaman utilitas inti Python meningkat dan mengurangi kode manual berulang.

## 2026-03-08
- Changed: Menulis konten nyata untuk `12_errors_and_exceptions.md` meliputi try/except/else/finally, raise, handling spesifik, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 12 agar pembaca mampu membuat program yang lebih robust saat terjadi error runtime.
- Impact: Fondasi reliability aplikasi Python meningkat sebelum masuk pola pemrograman akhir.

## 2026-03-08
- Changed: Menulis konten nyata untuk `11_file_handling.md` meliputi mode file, context manager, encoding, operasi baca/tulis, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 11 agar pembaca siap mengelola data berbasis file dengan aman.
- Impact: Materi I/O buku 1 kini lebih lengkap dan siap dipakai untuk latihan data persistence dasar.

## 2026-03-08
- Changed: Menulis konten nyata untuk `10_input_output.md` meliputi input(), output formatting, parsing tipe, validasi input, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 10 agar pembaca siap membangun program interaktif berbasis terminal.
- Impact: Sepuluh bab awal Python Basics kini mencakup fondasi interaksi pengguna yang lebih lengkap.

## 2026-03-08
- Changed: Menulis konten nyata untuk `09_modules_and_import.md` meliputi konsep module, pola import, package dasar, `__main__`, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 09 agar pembaca siap mengorganisasi kode lintas file secara modular.
- Impact: Sembilan bab awal Python Basics kini membentuk fondasi coding terstruktur untuk proyek sederhana.

## 2026-03-08
- Changed: Menulis konten nyata untuk `08_basic_data_structures.md` meliputi list, tuple, set, dict, operasi dasar, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 08 agar pembaca siap bekerja dengan koleksi data sebelum masuk modul/import.
- Impact: Delapan bab awal Python Basics kini mencakup fondasi data dan alur pemrograman yang lebih lengkap.

## 2026-03-08
- Changed: Menulis konten nyata untuk `07_functions.md` mencakup definisi fungsi, parameter/argumen, return, default argument, scope dasar, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 07 agar pembaca siap menulis kode modular dan reusable.
- Impact: Tujuh bab awal Python Basics kini membentuk fondasi coding praktis yang lebih lengkap.

## 2026-03-08
- Changed: Menulis konten nyata untuk `06_control_flow.md` mencakup percabangan, loop, break/continue/pass, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 06 agar pembaca memiliki fondasi alur eksekusi sebelum masuk ke fungsi.
- Impact: Enam bab awal Python Basics kini siap sebagai jalur belajar dasar yang lebih stabil.

## 2026-03-08
- Changed: Menulis konten nyata untuk `05_operators_and_expressions.md` mencakup operator aritmatika, perbandingan, logika, precedence, pitfall, dan latihan.
- Reason: Mengganti placeholder bab 05 agar pembaca siap masuk ke kontrol alur dengan fondasi expression yang kuat.
- Impact: Lima bab awal Python Basics kini membentuk jalur konsep dasar yang lebih utuh.

## 2026-03-08
- Changed: Menulis konten nyata untuk `04_basic_data_types.md` meliputi tipe data dasar, casting, truthiness, pitfall, latihan, dan FAQ.
- Reason: Mengganti placeholder bab 04 agar fondasi manipulasi nilai sebelum operator/ekspresi menjadi kuat.
- Impact: Empat bab awal Python Basics kini siap dipakai sebagai jalur belajar berurutan.

## 2026-03-08
- Changed: Menulis konten nyata untuk `03_variables_and_names.md` termasuk name binding, mutable vs immutable, aliasing, latihan, dan FAQ.
- Reason: Mengganti placeholder bab 03 agar transisi dari syntax ke model objek dasar menjadi jelas.
- Impact: Tiga bab awal Python Basics kini operasional dan saling terhubung secara konseptual.

## 2026-03-08
- Changed: Menulis konten nyata untuk `02_python_syntax.md` termasuk konsep syntax, indentation, contoh runnable, pitfall, latihan, dan FAQ.
- Reason: Mengganti placeholder bab 02 agar pembahasan sintaks dasar siap dipelajari setelah bab pembuka.
- Impact: Jalur belajar Python Basics kini memiliki dua bab awal yang sudah operasional.

## 2026-03-08
- Changed: Menulis konten nyata untuk `01_getting_started.md` termasuk konsep inti, contoh kode runnable, latihan, FAQ, dan perbaikan format markdown.
- Reason: Mengganti placeholder agar bab pembuka siap dipelajari dan menjadi acuan kualitas untuk bab berikutnya.
- Impact: Bab pertama Python Basics kini dapat digunakan langsung sebagai materi belajar.

## 2026-03-08
- Changed: Menambahkan 14 file bab awal menggunakan template resmi Core dan melengkapi 14 diagram SVG per bab di folder `assets/`.
- Reason: Menyiapkan struktur buku yang siap ditulis detail dan sesuai standar pedagogi + visual.
- Impact: Buku `01_python_basics` sekarang memiliki kerangka operasional lengkap untuk kontribusi bertahap.

## 2026-03-08
- Changed: Inisialisasi struktur awal buku.
- Reason: Menetapkan fondasi dokumentasi dan tracking perubahan.
- Impact: Buku siap menerima pembaruan konten dengan histori yang jelas.

