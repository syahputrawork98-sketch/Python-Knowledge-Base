# SR-06: Standard Concurrency (Asyncio & Threads) [x] Complete

> **"Concurrency is not Parallelism. One is about dealing with many things at once; the other is about doing many things at once."**

Sub-Rak ini membedah arsenal konkurensi bawaan Python yang paling kritis. Kita akan mempelajari bagaimana **`asyncio`** merevolusi cara kita menangani ribuan koneksi jaringan dengan efisiensi tinggi, serta bagaimana **`threading`** tetap menjadi pilihan utama untuk eksekusi tugas I/O sinkron yang memblokir.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Asyncio_Internals](./BK-01_Asyncio_Internals/)** | Event Loop | Bedah Co-operative multitasking dan `async/await`. |
| **[BK-02_Low_Level_Threading](./BK-02_Low_Level_Threading/)** | OS Threads | Bedah Pre-emptive multitasking, Locks, dan Queues. |

---

## 🎯 Key Learning Goals
- Memahami beda antara **Co-operative Multitasking** (Asyncio) vs **Pre-emptive Multitasking** (Threads).
- Mampu membangun aplikasi network-heavy menggunakan **Event Loop** asinkron.
- Menguasai teknik sinkronisasi memori bersama menggunakan **Lock** (Gembok).
- Mampu melakukan komunikasi antar-thread yang aman melalui **Queue**.
- Memahami keterbatasan **GIL (Global Interpreter Lock)** pada eksekusi multi-thread.
- Mampu memilih mesin eksekusi yang tepat antara Asyncio, Threads, atau Multiprocessing.

---

## 🧪 Prasyarat Teknis
- Pemahaman Generator & Coroutines (RAK-04 SR-06).
- Pengetahuan DASAR tentang I/O Bound vs CPU Bound.

---

## ⏭️ Next Step
Selamat! Anda telah menyelesaikan seluruh pilar **RAK-05: Standard Library**. Semua arsenal bawaan Python kini telah terdokumentasi dengan standar tertinggi (**GS-7**). Mari kita berikan sentuhan akhir (Audit Final) pada RAK ini.

---
*Back to [Rak-05 Standard Library](../README.md)*
