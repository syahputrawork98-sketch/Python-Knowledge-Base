# CH-01: Function Syntax (The Definition) [x] Complete

> **"Functions are the building blocks of abstraction; how you define them determines how predictably they behave."**

Bab ini membedah sintaks definisi fungsi dalam Python menggunakan pernyataan **`def`**. Kita akan mempelajari berbagai cara mengirimkan argumen dan mengapa fleksibilitas Python dalam parameter sangatlah kuat namun membutuhkan disiplin tinggi.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- **Strategic Blueprint**: [RAK-02 Foundation](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🧠 The Essence (Narrative)
Fungsi di Python didefinisikan dengan kata kunci `def`. Kekuatan utamanya terletak pada cara ia menangani parameter. Python mendukung argumen posisional, argumen kata kunci (*keyword arguments*), hingga pengumpulan argumen sisa menggunakan `*args` (untuk list) dan `**kwargs` (untuk dictionary). Parameter dalam Python sebenarnya adalah **pass-by-object-reference**, yang berarti perilaku fungsi bergantung pada apakah objek yang Anda kirimkan bersifat mutabel atau tidak.

---

## 🎨 Visual Logic (Argument Types)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    call([Function Call]) --> P[Positional Args]
    call --> K[Keyword Args]
    call --> V["Variable Args (*args)"]
    call --> KW["Keyword Variable (**kwargs)"]
    style P fill:#3776AB,stroke:#333,color:#fff
    style KW fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Performance & Syntax Matrix

| Feature | Syntax | Usage |
| :--- | :--- | :--- |
| **Positional** | `def f(a, b):` | Urutan sangat menentukan. |
| **Default** | `def f(a=1):` | Nilai cadangan jika argumen tidak dikirim. |
| **Variadic** | `def f(*args):` | Menerima jumlah argumen posisional tak terhingga. |
| **Keyword-Only** | `def f(*, a):` | Memaksa pemanggil menggunakan nama parameter `a`. |

---

## ⚠️ Pitfalls
- **Mutable Default Arguments**: Jangan pernah menggunakan objek mutabel seperti `[]` atau `{}` sebagai nilai default parameter. Nilai default didefinisikan **hanya sekali** saat fungsi dimuat, bukan setiap kali fungsi dipanggil. Ini akan menyebabkan state "bocor" antar panggilan fungsi.
  - *Solusi*: Gunakan `arg=None` lalu inisialisasi di dalam body fungsi.
- **`*args` Order**: Selalu letakkan `*args` sebelum `**kwargs`.

---
*Back to [BK-01 Foundations](../README.md)*
