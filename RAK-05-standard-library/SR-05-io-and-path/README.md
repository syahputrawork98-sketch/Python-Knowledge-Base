# SR-05: Modern File System (Pathlib & I/O) [x] Complete

> **"A path is a contract between your code and the operating system. Pathlib makes that contract elegant."**

Sub-Rak ini membedah arsenal modern Python untuk manipulasi sistem berkas (**File System**). Kita akan mempelajari bagaimana meninggalkan paradigma lama berbasis string (`os.path`) dan beralih ke manipulasi berbasis objek menggunakan `pathlib`. Selain itu, kita akan membedah stream memori (`io`) dan manajemen file sementara yang aman (`tempfile`).

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Pathlib_Objects](./BK-01_Pathlib_Objects/)** | Path Objects | Bedah manipulasi jalur lintas-platform dan operator `/`. |
| **[BK-02_File_Streams](./BK-02_File_Streams/)** | RAM & Temp Streams | Bedah `io.StringIO` dan manajemen `tempfile` yang aman. |

---

## 🎯 Key Learning Goals
- Memahami beda antara **Object-oriented Paths** vs **String-based Paths**.
- Mampu melakukan manipulasi jalur file yang aman secara lintas-platform.
- Menguasai teknik pencarian file rekursif menggunakan `rglob`.
- Mampu mensimulasikan file di memori (`StringIO`) untuk keperluan pengujian.
- Menguasai manajemen pembersihan file otomatis melalui `tempfile`.

---

## 🧪 Prasyarat Teknis
- Pemahaman Context Managers (RAK-04 SR-02).
- Pengetahuan DASAR tentang hirarki direktori (Root, Parent, Child).

---

## ⏭️ Next Step
Setelah menguasai manipulasi file fisik, mari kita beralih ke struktur data terstruktur yang hemat kode di **[SR-07: Structured Data Models (Dataclasses)](../SR-07-typing/)**.

---
*Back to [Rak-05 Standard Library](../README.md)*
