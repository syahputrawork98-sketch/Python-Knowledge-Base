# SR-02: Functional Optimization (Functools) [x] Complete

> **"Functools is the bridge between pure functional logic and Python's pragmatic execution."**

Sub-Rak ini mengeksplorasi modul **`functools`**, arsenal utama Python untuk melakukan optimasi pemanggilan fungsi dan komposisi tingkat tinggi. Kita akan membedah bagaimana teknik **Memoization** dapat mempercepat algoritma rekursif ribuan kali lipat, serta bagaimana **Functional Composition** membantu kita membangun kode yang lebih DRY (*Don't Repeat Yourself*).

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Memoization](./BK-01_Memoization/)** | Speed & Cache | Bedah `lru_cache` dan `@cache` untuk optimasi rekursif. |
| **[BK-02_Composition](./BK-02_Composition/)** | Functional Tools | Bedah `partial` dan `@wraps` untuk spesialisasi fungsi. |

---

## 🎯 Key Learning Goals
- Memahami konsep **Memoization** dan algoritma **LRU (Least Recently Used)**.
- Mampu mengoptimalkan algoritma rekursif berat tanpa mengubah struktur logika utama.
- Menguasai teknik **Currying** sederhana menggunakan `partial`.
- Memahami pentingnya pelestarian metadata fungsi menggunakan `@wraps`.
- Mampu membedakan kapan harus menggunakan cache memori vs komputasi ulang.

---

## 🧪 Prasyarat Teknis
- Pemahaman Functions & Decorators (RAK-02 SR-07).
- Pengetahuan dasar tentang Rekursi.

---

## ⏭️ Next Step
Setelah menguasai optimasi fungsi, mari kita beralih ke struktur data tingkat lanjut untuk performa tinggi di **[SR-03: High-Performance Data (Collections)](../SR-03-collections/)**.

---
*Back to [Rak-05 Standard Library](../README.md)*
