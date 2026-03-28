# SR-01: Source Anatomy (The Machine Room Peta) [x] Complete

> **"Mastering Python starts with knowing where the bricks are laid in C."**

Sub-Rak ini membedah **Anatomi Fisik** dari repositori kode sumber CPython. Kita akan melakukan dekonstruksi terhadap struktur folder utama seperti `Include/`, `Objects/`, dan `Python/` untuk memahami bagaimana ribuan file C terorganisir menjadi mesin eksekusi yang kuat.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Labirinto_CPython](./BK-01_Labirinto_CPython/)** | Folder Hierarchy | Navigasi hirarki folder utama CPython (Include, Objects, Python). |
| **[BK-02_Build_System](./BK-02_Build_System/)** | Build Engine | Bedah proses kompilasi dari source (`configure`, `make`). |

---

## 🎯 Key Learning Goals
- Memahami tanggung jawab setiap folder utama dalam repositori CPython.
- Mampu menemukan definisi struct inti seperti `PyObject` di dalam file header C.
- Memahami letak implementasi tipe data bawaan (List, Dict, Str) di dalam `Objects/`.
- Menguasai alur pembangunan interpreter Python dari kode sumber (Drafting/Building).
- Mampu membedakan antara library standar berbasis Python (`Lib/`) vs berbasis C (`Modules/`).

---

## 🧪 Prasyarat Teknis
- Pemahaman Dasar Sistem Operasi (File System, Directories).
- Pengetahuan SANGAT DASAR tentang bahasa C (untuk membaca nama file).

---

## ⏭️ Next Step
Setelah kita memahami letak komponen fisik mesin, mari kita pelajari bagaimana mesin tersebut memproses teks kode Anda menjadi pohon sintaks di **[SR-02: Parsing & AST](../SR-02-parsing-ast/)**.

---
*Back to [RAK-06 Interpreters](../README.md)*
