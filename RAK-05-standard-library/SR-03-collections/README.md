# SR-03: High-Performance Data (Collections) [x] Complete

> **"A list is just the beginning. The 'collections' module is where Python's data engineering power truly resides."**

Sub-Rak ini mengeksplorasi modul **`collections`**, arsenal utama Python untuk menangani struktur data tingkat lanjut dengan performa tinggi. Kita akan membedah bagaimana mengganti `list` dan `dict` standar dengan kontainer yang lebih efisien — seperti `deque` untuk antrean $O(1)$ dan `defaultdict` untuk pengelompokan data instan.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Counters_Deques](./BK-01_Counters_Deques/)** | Freq & Queues | Bedah analisis frekuensi dan antrean ujung-ganda yang cepat. |
| **[BK-02_Advanced_Dicts](./BK-02_Advanced_Dicts/)** | Grouping & Layers | Bedah `defaultdict` dan `ChainMap` untuk konfigurasi berlapis. |
| **[BK-03_Named_Containers](./BK-03_Named_Containers/)** | Light Objects | Bedah `namedtuple` sebagai alternatif kelas yang hemat memori. |

---

## 🎯 Key Learning Goals
- Memahami beda performa antara **$O(n)$** (List pop-left) vs **$O(1)$** (Deque pop-left).
- Mampu melakukan analisis frekuensi data secara instan menggunakan `Counter`.
- Menguasai teknik pengelompokan data tanpa `KeyError` melalui `defaultdict`.
- Memahami strategi manajemen konfigurasi bertingkat menggunakan `ChainMap`.
- Mengoptimalkan penggunaan memori untuk kontainer data sederhana via `namedtuple`.

---

## 🧪 Prasyarat Teknis
- Pemahaman Built-in Types (List, Dict, Tuple).
- Pengetahuan dasar Kompleksitas Algoritma (Notasi Big O).

---

## ⏭️ Next Step
Setelah menguasai struktur data berperforma tinggi, mari kita pelajari cara mengolah aliran data masif secara hemat memori melalui **[SR-04: Lazy Data Pipelines (Itertools)](../SR-04-itertools/)**.

---
*Back to [Rak-05 Standard Library](../README.md)*
