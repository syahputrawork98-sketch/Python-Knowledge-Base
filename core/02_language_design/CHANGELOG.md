# CHANGELOG

Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08

## 2026-03-08
- Changed: Regenerasi seluruh aset visual `core/02_language_design/assets/*.svg` agar tiap bab memiliki label konsep yang spesifik dan konsisten.
- Reason: Menghapus template generik/emoji yang berisiko tidak konsisten saat render lintas environment dan meningkatkan relevansi visual per bab.
- Impact: Diagram Buku CORE-02 kini lebih stabil (ASCII-safe), lebih mudah dibaca, dan selaras dengan fokus materi tiap chapter.

## 2026-03-08
- Changed: Tindak lanjut review pedagogi pada `CORE-02-10`, `CORE-02-09`, dan `CORE-02-01` (output deprecation dibuat eksplisit, kalibrasi difficulty, dan penyeragaman tuntutan mini challenge).
- Reason: Menutup gap konsistensi pembelajaran antar bab dan meningkatkan kejelasan demonstrasi konsep.
- Impact: Bab backward compatibility lebih demonstratif, level kesulitan bab batteries-included lebih selaras dengan latihan, dan baseline evaluasi mini challenge antar bab lebih konsisten.

## 2026-03-08
- Changed: Perbaikan hasil review konten pada `CORE-02-10`, `CORE-02-09`, dan `CORE-02-11` (jalur deprecation diperjelas dan contoh file I/O dibuat tanpa artefak lokal).
- Reason: Menutup temuan quality review agar demonstrasi konsep akurat dan contoh lebih aman dijalankan berulang.
- Impact: Contoh backward compatibility kini benar-benar memanggil API deprecated; contoh stdlib/style tetap runnable tanpa meninggalkan file sementara di workspace.

## 2026-03-08
- Changed: Quality pass pada contoh kode `CORE-02-09` dan `CORE-02-11` agar runnable secara mandiri (self-contained) tanpa file prasyarat manual.
- Reason: Mengurangi friction pembaca saat mencoba contoh langsung dan meningkatkan konsistensi pengalaman belajar.
- Impact: Contoh praktik di dua bab tersebut kini bisa dijalankan langsung dengan output yang tetap sesuai.

## 2026-03-08
- Changed: Sinkronisasi metadata level buku setelah seluruh bab `CORE-02-01` s.d. `CORE-02-12` selesai diisi ke status draft.
- Reason: Menutup fase pengisian konten awal agar status versi dan progres buku konsisten lintas dokumen.
- Impact: `README` dan `CHANGELOG` kini merepresentasikan kondisi terbaru Buku CORE-02 secara akurat (`v0.2.1`, draft complete).

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-11` (`11_idiomatic_python_and_style.md`) dari template menjadi materi penuh.
- Reason: Menuntaskan urutan penulisan per topik pada area praktik style Pythonic dan standar kode yang maintainable.
- Impact: Bab idiomatic style kini siap dipakai untuk latihan refactor, code review, dan penyusunan guideline coding tim.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-10` (`10_backward_compatibility_and_peps.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan penulisan per topik pada area strategi evolusi API, kompatibilitas mundur, dan proses perubahan berbasis PEP.
- Impact: Bab backward compatibility kini siap dipakai untuk latihan deprecation bertahap, migration path, dan argumentasi desain yang lebih kuat.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-09` (`09_batteries_included_mindset.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan urutan penulisan per topik pada area pengambilan keputusan penggunaan standard library vs dependency eksternal.
- Impact: Bab batteries-included kini siap dipakai untuk latihan evaluasi dependency dan desain solusi berbasis stdlib yang terukur.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-08` (`08_errors_as_part_of_design.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan urutan penulisan per topik pada area desain error handling dan kontrak exception.
- Impact: Bab error design kini siap dipakai untuk latihan fail-fast, exception contract, dan peningkatan kualitas debugging.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-07` (`07_duck_typing_and_protocols.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan urutan penulisan per topik pada aspek fleksibilitas desain antarkomponen di Python.
- Impact: Bab duck typing kini siap dipakai untuk latihan desain kontrak berbasis perilaku, pengurangan coupling, dan kemudahan testing.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-06` (`06_mutability_and_object_thinking.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan progres per topik pada area risiko bug paling umum terkait state dan referensi objek.
- Impact: Bab mutability kini siap dipakai untuk latihan desain API aman, pencegahan shared state bug, dan penguatan praktik testing.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-05` (`05_simple_vs_complex.md`) dari template menjadi materi penuh.
- Reason: Menjaga kontinuitas penulisan per topik sekaligus mengisi pilar trade-off inti dalam desain Python.
- Impact: Bab simple vs complex kini siap dipakai untuk latihan identifikasi over-engineering dan refactor kompleksitas.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-04` (`04_consistency_and_practicality.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan urutan penulisan per topik agar prinsip kualitas kode dibangun bertahap dan konsisten.
- Impact: Bab consistency kini siap dipakai untuk acuan standar review tim dan keputusan pragmatis pada implementasi harian.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-03` (`03_readability_and_explicitness.md`) dari template menjadi materi penuh.
- Reason: Menjaga progres penulisan per topik agar fondasi style dan kualitas kode terbentuk sejak bab awal.
- Impact: Bab readability kini siap dipakai untuk latihan code review, refactor naming, dan desain kontrak fungsi.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-02` (`02_the_zen_of_python.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan eksekusi strategi penulisan per topik secara berurutan dari bab awal.
- Impact: Bab Zen of Python kini siap dipakai sebagai kerangka evaluasi style coding dan refactor pada bab berikutnya.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-01` (`01_design_goals_and_philosophy.md`) dari template menjadi materi penuh.
- Reason: Menjalankan strategi penulisan per topik untuk mematangkan isi buku secara bertahap dan terstruktur.
- Impact: Bab pembuka CORE-02 kini siap dijadikan acuan tone, kedalaman, dan pola latihan untuk bab-bab berikutnya.

## 2026-03-08
- Changed: Menyelesaikan draft konten detail `CORE-02-12` (`12_language_design_tradeoffs.md`) dari template menjadi materi penuh.
- Reason: Melanjutkan fase pengisian konten dari struktur awal menuju chapter siap review.
- Impact: Bab penutup CORE-02 kini memiliki pembahasan utuh tentang trade-off desain Python beserta contoh kode, pitfall, latihan, dan checklist.

## 2026-03-08
- Changed: Menyusun ulang struktur buku `02_language_design`, menambahkan 12 bab awal lengkap dengan metadata/template, dan membuat aset visual SVG per bab.
- Reason: Menetapkan fondasi operasional agar penulisan konten detail dapat dilakukan konsisten dan cepat.
- Impact: Buku CORE-02 kini siap masuk fase pengisian konten bab secara bertahap.

## 2026-03-08
- Changed: Inisialisasi struktur awal buku.
- Reason: Menetapkan fondasi dokumentasi dan tracking perubahan.
- Impact: Buku siap menerima pembaruan konten dengan histori yang jelas.
