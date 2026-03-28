# BK-02: Aggregation (zip, enumerate, sorted) [x] Complete

> **"Aggregation is the art of combining separate signals into a single, meaningful melody."**

Buku ini membedah trio maut agregasi data di Python: **`zip()`**, **`enumerate()`**, dan **`sorted()`**. Kita akan mempelajari bagaimana fungsi-fungsi bawaan ini mempermudah pengelolaan banyak koleksi sekaligus dengan sintaksis yang bersih dan efisien.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - Built-in Functions](https://docs.python.org/3/library/functions.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Mengelola banyak koleksi data secara terpisah seringkali merepotkan. Python menawarkan solusi agregat tingkat tinggi:
1.  **`zip(*iterables)`**: Menggabungkan beberapa koleksi menjadi satu aliran "pasangan" (Tuples).
2.  **`enumerate(iterable)`**: Memberikan "counter" otomatis pada setiap elemen dalam loop.
3.  **`sorted(iterable, key=func)`**: Mengurutkan data menggunakan algoritma **Timsort** yang sangat cepat tanpa merubah urutan asli data.
Ketiganya dirancang agar meminimalkan jumlah baris kode yang Anda tulis sekaligus memaksimalkan keterbacaan struktur data Anda.

---

## 🎨 Visual Logic (Aggregation Mapping)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    A1[Names: A, B, C]
    A2[Scores: 80, 90, 85]
    A1 & A2 -- zip --> Z[Result: (A,80), (B,90), (C,85)]
    Z -- enumerate --> E[Result: (0,(A,80)), (1,(B,90)), ...]
    style Z fill:#3776AB,stroke:#333,color:#fff
    style E fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation: The Aggregation Chain
```python
names = ["Alice", "Bob"]
scores = [95, 88]

for i, (name, score) in enumerate(zip(names, scores)):
    print(f"{i+1}. {name}: {score}")
```

---

## ⚠️ Pitfalls
- **The Shortest Wins**: Dalam `zip()`, jika salah satu koleksi lebih pendek dari yang lain, Python akan berhenti di elemen terakhir dari koleksi terpendek tersebut. Sisa elemen di koleksi panjang akan diabaikan. Jika Anda butuh semua elemen, gunakan `itertools.zip_longest`.
- **Memory Cost of Sorting**: Gunakan `sorted()` untuk menghasilkan list baru tanpa mengubah data asli. Namun ingat, `sorted()` **BUKAN** iterator; ia akan memakan memori untuk menyimpan seluruh hasil urutan di RAM. Jika data sangat besar, pertimbangkan menggunakan sortir disk-based.
- **Unzipping**: Mengetahui cara memasangkan data dengan `zip(*data)` (Unzipping) adalah teknik pro yang sering terabaikan namun sangat berguna untuk memisahkan kembali kolom data.

---
*Back to [SR-01 Builtins](../README.md)*
