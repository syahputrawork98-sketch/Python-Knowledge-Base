# BK-03: Named Containers (namedtuple) [x] Complete

> **"namedtuple gives you the power of a class with the memory footprint of a tuple."**

Buku ini membedah **`namedtuple`**, kontainer data dari modul `collections` yang menggabungkan kemudahan akses atribut kelas dengan efisiensi memori dari Tuple standar. Kita akan mempelajari mengapa ini adalah pilihan utama untuk kontainer data sederhana yang bersifat *immutable*.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - collections (Container datatypes)](https://docs.python.org/3/library/collections.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Tuple standar sangat cepat dan hemat memori, namun sulit dibaca karena pengaksesan dilakukan melalui indeks (misal: `p[0]`, `p[1]`). Apakah `p[0]` itu ID atau Nama? **`namedtuple`** diciptakan untuk menyelesaikan masalah ini. Ia memungkinkan Anda memberi nama pada setiap posisi elemen, sehingga Anda bisa mengaksesnya dengan `p.id` atau `p.name`. Karena `namedtuple` tetaplah sebuah Tuple, ia tidak memiliki `__dict__` per instans, yang bermakna penggunaan memorinya jauh lebih kecil daripada objek kelas standar.

---

## 🎨 Visual Logic (Memory Efficiency Map)

| Type | Access Type | Memory Cost | Mutability |
| :--- | :--- | :--- | :--- |
| **Standard List** | Index | Medium | Mutable |
| **Standard Tuple** | Index | **Low** | Immutable |
| **Class Object** | Name | High | Mutable |
| **namedtuple** | **Name + Index** | **Low** | Immutable |

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    NT[namedtuple: Point] --> X[Attribute: .x]
    NT --> Y[Attribute: .y]
    NT -- also --> IX[Index: [0]]
    style NT fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Implementation: Lightweight Models
```python
from collections import namedtuple

# 1. Deklarasi (Sekali saja)
Point = namedtuple("Point", ["x", "y"])

# 2. Instansiasi
p = Point(x=10, y=20)
print(f"Coordinates: {p.x}, {p.y}")

# 3. Konversi ke Dictionary (Jika butuh ekspor JSON)
print(p._asdict()) # Result: {'x': 10, 'y': 20}
```

---

## ⚠️ Pitfalls
- **Immutability**: Seperti Tuple lainnya, elemen `namedtuple` **tidak bisa diubah** setelah diciptakan. Jika Anda butuh kontainer data yang nilainya bisa dimodifikasi, gunakan `dataclasses` (lihat SR-07) atau kelas standar.
- **Factory Limitation**: Anda tidak bisa mendefinisikan metode khusus atau logika validasi yang kompleks di dalam `namedtuple` semudah di dalam kelas standar (walaupun Anda bisa melakukan *subclassing*).
- **The underscore `_` prefix**: Beberapa metode internal `namedtuple` diawali dengan underscore (misal: `_asdict()`, `_make()`, `_replace()`). Ini dilakukan untuk menghindari konflik nama dengan field yang Anda buat sendiri.

---
*Back to [SR-03 Collections](../README.md)*
