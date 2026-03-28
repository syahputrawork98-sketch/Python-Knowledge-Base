# SR-06: Modern Internals (JIT & No-GIL) [x] Complete

> **"The future of Python is not about changing the language; it's about changing the machine that runs it."**

Sub-Rak ini membedah **Inovasi Terkini** dalam ekosistem CPython (3.13+). Kita akan mengeksplorasi dua pilar utama yang akan mengubah wajah performa Python selamanya: **JIT (Just-In-Time) Compiler** dan penghapusan Global Interpreter Lock (**Free-threading/No-GIL**).

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_JIT_Internals](./BK-01_JIT_Internals/)** | Dynamic Optimization | Bedah JIT Tier 2 dan teknik Copy-and-Patch. |
| **[BK-02_Free_Threading](./BK-02_Free_Threading/)** | True Parallelism | Bedah PEP 703: Eksekusi multi-core tanpa GIL. |

---

## 🎯 Key Learning Goals
- Memahami arsitektur **Tiered Execution** (Tier 1 vs Tier 2) di Python modern.
- Mampu menjelaskan cara kerja JIT **Copy-and-Patch** pada level tinggi.
- Memahami mekanisme **Biased Reference Counting** untuk mendukung No-GIL.
- Mengenali trade-off performa antara mode standar vs mode JIT/No-GIL.
- Mengetahui cara melakukan build CPython dari sumber untuk mengaktifkan fitur eksperimental.

---

## 🧪 Prasyarat Teknis
- Pemahaman Evaluation Loop & Bytecode (RAK-06 SR-03 & SR-04).
- Pengetahuan tentang Multi-threading (RAK-05 SR-06).

---

## ⏭️ Next Step
Selamat! Anda telah menyelesaikan dekonstruksi terdalam **RAK-06: Interpreters (The Machine Room)**. Semua bagian dari mesin CPython kini telah terdokumentasi dengan standar tertinggi (**GS-7**). Anda kini memiliki pemahaman level "Expert" terhadap Python. Mari kita lanjutkan ke aplikasi industri nyata di **[RAK-07: Specializations](../RAK-07-specializations/)**.

---
*Back to [RAK-06 Interpreters](../README.md)*
