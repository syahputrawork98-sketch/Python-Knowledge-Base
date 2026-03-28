# SR-02: Parsing & AST (The Gatekeeper Hub) [x] Complete

> **"A language is defined by its grammar; a program is defined by its tree."**

Sub-Rak ini membedah **Gerbang Depan CPython**, proses transformasi teks mentah kode sumber Anda menjadi struktur fungsional yang disebut **Abstract Syntax Tree (AST)**. Kita akan mempelajari bagaimana parser PEG (Parsing Expression Grammar) modern Python bekerja dan bagaimana ia membersihkan kerumitan sintaks menjadi pohon logika yang murni.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_PEG_Parser](./BK-01_PEG_Parser/)** | Formal Grammar | Bedah algoritma PEG dan `Parser/pegen.c`. |
| **[BK-02_AST_Generation](./BK-02_AST_Generation/)** | Syntax Tree | Bedah transformasi token ke AST Nodes di `Python/ast.c`. |

---

## 🎯 Key Learning Goals
- Memahami alasan transisi Python 3.9+ dari parser LL(1) ke **PEG**.
- Mampu membaca file tata bahasa formal Python (`Grammar/python.gram`).
- Memahami perbedaan antara **Concrete Parse Tree** vs **Abstract Syntax Tree**.
- Menguasai teknik manipulasi AST secara terprogram menggunakan modul `ast`.
- Memahami bagaimana ASDL mendefinisikan struktur data pohon sintaks di level C.

---

## 🧪 Prasyarat Teknis
- Pemahaman Struktur Folder CPython (RAK-06 SR-01).
- Pengetahuan SANGAT DASAR tentang Struktur Data Tree (Nodes, Leaves).

---

## ⏭️ Next Step
Setelah kita memiliki pohon sintaks yang bersih, mari kita pelajari bagaimana pohon tersebut diubah menjadi instruksi bytecode yang dapat dimengerti oleh mesin di **[SR-03: Compilation & Bytecode](../SR-03-compilation-bytecode/)**.

---
*Back to [RAK-06 Interpreters](../README.md)*
