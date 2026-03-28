# CH-01: Lists (The Dynamic Array) [x] Complete

> **"A list is more than an array; it is a self-growing container of pointers."**

Bab ini membedah **`list`** dalam Python — struktur data paling serbaguna yang bersifat **Mutable** dan **Ordered**. Kita akan membongkar bagaimana Python mengelola pertumbuhan ukuran list secara dinamis di balik layar.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - Lists](https://docs.python.org/3/library/stdtypes.html#lists)
- **CPython Source**: [Objects/listobject.c](https://github.com/python/cpython/blob/main/Objects/listobject.c)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
List dalam Python bukanlah *Linked List*, melainkan **Dynamic Array**. Di level C, list adalah array dari pointer (`PyObject** ob_item`). Keunikan utamanya adalah **Over-allocation**: saat Anda melakukan `.append()`, Python tidak hanya memesan satu slot memori tambahan, tapi beberapa sekaligus. Strategi ini memastikan bahwa penambahan elemen rata-rata memiliki kecepatan **O(1)** (Amortized Constant Time).

---

## 🎨 Visual Logic (List Growth Strategy)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    A["List Object (Size 4/4)"] -- Append New --> B["Resize Event"]
    B --> C["New Allocation (Size 4/8)"]
    C --> D["Amortized O(1) Push"]
    style B fill:#FFD43B,stroke:#333,color:#000
    style C fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Performance Matrix (Big O)

| Operation | Complexity | Note |
| :--- | :--- | :--- |
| `append()` | **O(1)** | Amortized constant time. |
| `pop()` | **O(1)** | Menghapus dari akhir sangat cepat. |
| `insert(i, v)` | **O(n)** | Membutuhkan pergeseran seluruh elemen di kanannya. |
| `remove()` | **O(n)** | Harus mencari elemen terlebih dahulu. |

---

## ⚠️ Pitfalls
- **`insert(0, val)` Trap**: Melakukan insert di indeks 0 pada list besar sangat lambat (O(n)). Jika Anda sering menambah/hapus dari depan, gunakan `collections.deque`.
- **Reference Sharing**: Hati-hati saat melakukan `[ [] ] * 5`. Ini akan membuat list yang berisi 5 referensi ke **list yang sama**, bukan 5 list baru yang independen.

---
*Back to [BK-01 Sequences](../README.md)*
