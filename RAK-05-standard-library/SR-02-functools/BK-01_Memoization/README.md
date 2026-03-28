# BK-01: Memoization (lru_cache & cache) [x] Complete

> **"Memoization is the art of never solving the same problem twice."**

Buku ini membedah **Memoization**, teknik optimasi yang menyimpan hasil pemanggilan fungsi yang mahal dan mengembalikannya secara instan saat argumen yang sama diberikan kembali. Kita akan menggunakan `lru_cache` sebagai senjata utama untuk mempercepat algoritma komputasi di Python.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - functools (Higher-order functions)](https://docs.python.org/3/library/functools.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Beberapa fungsi, terutama yang bersifat rekursif (seperti kalkulasi Fibonacci atau pencarian path), seringkali menghitung hal yang sama berulang kali. `lru_cache` (Least Recently Used) bertindak sebagai buku catatan pintar. Ia menyimpan hasil kalkulasi dalam memori. Jika kapasitas penuh, ia akan menghapus hasil yang paling jarang digunakan. Sejak Python 3.9, tersedia juga `@cache` yang merupakan versi `lru_cache` dengan kapasitas tak terbatas, sangat berguna untuk fungsi yang hasil uniknya tidak terlalu banyak namun sering dipanggil.

---

## 🎨 Visual Logic (LRU Cache Strategy)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Call[Function Call: f(x)] --> Check{Is x in Cache?}
    Check -- Yes --> Return[Return Cached Result]
    Check -- No --> Execute[Execute Logic]
    Execute --> Store[Store result in Cache]
    Store --> Return
    style Check fill:#3776AB,stroke:#333,color:#fff
    style Return fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation: Recursive Optimization
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

# Tanpa cache: Eksponensial (Lambat)
# Dengan cache: Linear (Sangat Cepat)
```

---

## ⚠️ Pitfalls
- **Mutable Arguments**: Argumen fungsi yang didekorasi dengan `lru_cache` **harus bersifat Hashable** (seperti string, int, tuple). Anda tidak bisa mengirim `list` atau `dict` sebagai argumen karena mereka tidak bisa di-hash untuk menjadi key di cache.
- **Memory Bloat**: Jika `maxsize` disetel ke `None` (atau menggunakan `@cache`), cache akan tumbuh selamanya selama program berjalan. Pastikan memori Anda cukup atau gunakan batas yang masuk akal.
- **Side Effects**: Jangan mem-memoize fungsi yang memiliki efek samping (misal: menulis ke file atau database). Cache hanya menyimpan nilai kembali, ia tidak akan menjalankan ulang "efek samping" tersebut saat data diambil dari cache.

---
*Back to [SR-02 Functools](../README.md)*
