# SR-04: Evaluation Loop (The Brain Hub) [x] Complete

> **"Code is an static idea; the Evaluation Loop is its dynamic life."**

Sub-Rak ini membedah **Jantung Eksekusi CPython**, proses di mana bytecode yang telah dikompilasi benar-benar dijalankan secara fisik oleh mesin virtual. Kita akan mengeksplorasi file paling legendaris dalam sejarah Python: `ceval.c`, dan memahami bagaimana paradigma **Stack Machine** menggerakkan setiap baris kode Anda.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Ceval_Anatomy](./BK-01_Ceval_Anatomy/)** | The Great Switch | Bedah jantung `_PyEval_EvalFrameDefault` di `Python/ceval.c`. |
| **[BK-02_Stack_Machine](./BK-02_Stack_Machine/)** | Execution Frame | Bedah mekanisme PUSH/POP pada stack PVM dan struktur frame. |

---

## 🎯 Key Learning Goals
- Memahami alur kerja **Fetch-Decode-Execute** di dalam `ceval.c`.
- Mampu menjelaskan bagaimana Python beroperasi sebagai **Stack-based VM**.
- Memahami struktur **PyFrameObject** dan fungsinya sebagai konteks eksekusi.
- Mengenali letak pemeriksaan sintak sistem (seperti GIL check) di dalam loop utama.
- Memahami alasan teknis di balik batas kedalaman rekursi Python.

---

## 🧪 Prasyarat Teknis
- Pemahaman Opcodes & Bytecode (RAK-06 SR-03).
- Pengetahuan DASAR tentang penggunaan Stack (LIFO: Last In First Out).

---

## ⏭️ Next Step
Setelah kita memahami bagaimana instruksi dijalankan, mari kita membedah fondasi atomik dari semua objek Python melalui kacamata C di **[SR-05: Object C-API](../SR-05-object-c-api/)**.

---
*Back to [RAK-06 Interpreters](../README.md)*
