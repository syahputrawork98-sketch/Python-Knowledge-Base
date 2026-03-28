# CH-02: Special Methods (Magic Methods) [x] Complete

> **"Dunder methods are the hooks that connect your custom objects to the built-in behaviors of Python."**

Bab ini membedah **Special Methods** — sering disebut **Magic Methods** atau **Dunder** (*Double Underscore*). Kita akan mempelajari bagaimana cara membuat objek kustom Anda bisa dijumlahkan, dibandingkan, atau direpresentasikan sebagai string secara elegan.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - Data Model: Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Metode spesial bukanlah metode yang Anda panggil secara langsung. Python memanggilnya di balik layar saat Anda melakukan operasi tertentu pada objek. Contohnya, saat Anda memanggil `len(obj)`, Python sebenarnya memanggil `obj.__len__()`. Saat Anda melakukan `obj1 + obj2`, Python memanggil `obj1.__add__(obj2)`. Inilah yang memungkinkan **Operator Overloading** — memberikan arti baru bagi operator standar pada objek buatan Anda.

---

## 🎨 Visual Logic (Magic Interaction)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    User([Syntax: a + b]) -- triggers --> P[Dunder Method: __add__]
    User([Syntax: print(a)]) -- triggers --> S[Dunder Method: __str__]
    User([Syntax: len(a)]) -- triggers --> L[Dunder Method: __len__]
    style P fill:#3776AB,stroke:#333,color:#fff
    style S fill:#3776AB,stroke:#333,color:#fff
    style L fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Essential Magic Methods

1. **`__str__`**: Representasi string yang ramah pengguna (untuk `print()`).
2. **`__repr__`**: Representasi string untuk pengembang/debugging (tujuannya adalah untuk menduplikasi pembuatan objek).
3. **`__len__`**: Digunakan oleh fungsi `len()`.
4. **`__add__` / `__sub__`**: Digunakan untuk operator `+` dan `-`.

---

## ⚠️ Pitfalls
- **`__str__` vs `__repr__` Confusion**: Ingatlah bahwa `__repr__` adalah "cadangan" bagi `__str__`. Jika Anda hanya mendefinisikan `__repr__`, Python akan menggunakannya untuk `print()` juga. Namun jika sebaliknya, `print()` akan menggunakan `__str__` tetapi representasi internal (misal dalam list) tetap menggunakan `__repr__` asli.
- **Overloading Everything**: Jangan berlebihan dalam melakukan *operator overloading*. Jika penambahan dua objek tidak memiliki makna logis yang jelas di dunia nyata (misal: `AlatTulis + Kertas`), lebih baik gunakan metode biasa yang dinamai dengan jelas.

---
*Back to [BK-03 Encapsulation & Special Methods](../README.md)*
