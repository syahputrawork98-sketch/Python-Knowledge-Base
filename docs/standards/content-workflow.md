# Content Workflow: Research & Writing (PPM V4)

Dokumen ini mengatur alur kerja pembuatan materi, mulai dari riset spesifikasi Python hingga penulisan narasi yang memenuhi standar **8-Point Gold Standard**.

---

## 🛡️ 1. Rule 0: Discussion-First Protocol (Pre-Execution)

Sebelum AI melakukan penulisan atau restrukturisasi file apapun, AI **WAJIB** melalui gerbang diskusi:

1.  **AI Research**: AI mencari sumber primer (docs.python.org / PEPs / CPython Source) yang relevan.
2.  **AI Proposal**: AI mengajukan tautan (URL) dan alasan pemilihan di chat.
3.  **Wait for "Eksekusi"**: AI dilarang menulis sebelum User memberikan persetujuan eksplisit.

---

## ✍️ 2. Tahapan PPM (Prosedur Penulisan Materi) V4

Setiap penyusunan materi wajib mengikuti 5 tahapan representasi:

### Tahap 1: Source Alignment & Judul
Header materi dengan metafora/analogi + Link spesifik langsung ke dokumentasi resmi atau PEP terkait.

### Tahap 2: Konsep & Esensi (Definisi & Rasionalitas)
Definisi formal, "Why & How" (Alasan fitur diciptakan), dan Analogi Model Mental Pythonic.

### Tahap 3: Visualisasi Sistem (Mermaid)
Diagram Mermaid **inline** (bukan file eksternal) untuk memetakan alur bytecode atau struktur objek.

### Tahap 4: Mekanisme Pembuktian (Algoritma Detil)
Detail balik layar bagaimana CPython mengeksekusi kode (Evaluation Loop / C-API logic).

### Tahap 5: Multi-file Lab Praktis (Examples)
Referensikan ke skrip di folder `examples/` yang memverifikasi teori di atas secara fungsional.

---

## 🏛️ 3. Adaptive Gold Standard (4 Pilar + X Modul)

Untuk menjaga kualitas premium, setiap unit (`README.md`) menggunakan struktur **4 Pilar Inti (Wajib)** dan **Modul Kontekstual (Pilihan)** sesuai tipe materinya.

### A. 4 Pilar Inti (Wajib di Setiap Unit)
1.  **Header (Identity)**: Judul Kinetik + Badge Status (`Draft`, `Partial`, `Complete`).
2.  **🌐 Source Hub (Authority)**: Tautan balik ke Blueprint Induk & Sumber Primer (PEP/Official Docs).
3.  **The Essence (Narrative)**: Deskripsi logika, sejarah, atau rasionalitas dalam bentuk naratif.
4.  **Visual Logic (Mermaid)**: Representasi grafis wajib (Flowchart, Memory Map, atau Bytecode Flow) secara **inline**.

### B. Modul Kontekstual (Pilihan Sesuai Kebutuhan)
- **🌍 Landscape**: Pemetaan navigasi unit di bawahnya (Gunakan untuk Level 2-4).
- **🧪 The Lab (Specimens)**: Referensi ke kode praktis di folder `examples/`.
- **⚙️ Spec-Internals**: Bedah algoritma CPython atau mekanisme engine mendalam.
- **⚠️ Pitfalls**: Mitigasi kesalahan umum dan mitos teknologi Python.

---

## 📜 4. Klasifikasi Unit Materi
1.  **N-Type (Narrative)**: Fokus pada Sejarah/Filosofi. (Gunakan: Core + Landscape + Pitfalls).
2.  **C-Type (Conceptual)**: Fokus pada Sintaks/API Dasar. (Gunakan: Core + The Lab + Pitfalls).
3.  **S-Type (Spec-Rigor)**: Fokus pada Mekanika Internal (C-API/VM). (Gunakan: Core + Spec-Internals + The Lab).
