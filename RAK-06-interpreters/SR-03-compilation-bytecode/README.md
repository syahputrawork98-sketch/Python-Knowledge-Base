# SR-03: Compilation & Bytecode (The Instruction Factory) [x] Complete

> **"Code is an idea; Bytecode is the command; Execution is the result."**

Sub-Rak ini membedah **Pabrik Instruksi CPython**, proses transformasi pohon logika (AST) menjadi urutan instruksi tingkat rendah (Opcodes) yang dapat dimengerti oleh Mesin Virtual. Kita akan mempelajari bagaimana compiler memetakan cakupan variabel melalui Symbol Table dan memancarkan aliran bytecode ke dalam struktur **Code Object**.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Bytecode_Emitter](./BK-01_Bytecode_Emitter/)** | Instruction Generation | Bedah transformasi AST ke Opcode di `Python/compile.c`. |
| **[BK-02_Symbol_Table](./BK-02_Symbol_Table/)** | Static Scoping | Bedah manajemen cakupan variabel di `Python/symtable.c`. |

---

## 🎯 Key Learning Goals
- Memahami struktur internal **Code Object** (`co_code`, `co_consts`, `co_names`).
- Mampu membaca instruksi bytecode menggunakan modul `dis`.
- Memahami bagaimana compiler menentukan cakupan variabel secara statis melalui **Symbol Table**.
- Mengenali alasan kegagalan cakupan seperti `UnboundLocalError` di level compiler.
- Memahami peran optimasi konstanta (Peephole optimization) pada level bytecode.

---

## 🧪 Prasyarat Teknis
- Pemahaman AST (RAK-06 SR-02).
- Pengetahuan DASAR tentang Konsep Kompilasi (Source -> Intermediate).

---

## ⏭️ Next Step
Setelah kita memiliki aliran instruksi bytecode, mari kita pelajari bagaimana jantung mesin Python mengeksekusinya secara fisik melalui loop evaluasi di **[SR-04: Evaluation Loop](../SR-04-eval-loop/)**.

---
*Back to [RAK-06 Interpreters](../README.md)*
