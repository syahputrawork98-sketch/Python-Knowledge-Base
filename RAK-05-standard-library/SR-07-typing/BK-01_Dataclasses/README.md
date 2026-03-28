# BK-01: Dataclasses (Boilerplate Reduction) [x] Complete

> **"Explicit is better than implicit, but automated boilerplate is better than manual repetition."**

Buku ini membedah **`dataclasses`**, fitur modern Python (3.7+) yang secara otomatis menghasilkan metode khusus seperti `__init__`, `__repr__`, dan `__eq__`. Kita akan mempelajari bagaimana alat ini membersihkan kode Anda dari ribuan baris boilerplate yang membosankan dan rawan kesalahan.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - dataclasses (Data Classes)](https://docs.python.org/3/library/dataclasses.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Secara tradisional, membuat kelas penyimpan data membutuhkan penulisan `def __init__(self, ...): self.x = x ...` yang sangat repetitif. **`@dataclass`** menggunakan anotas tipe untuk secara otomatis membangun metode tersebut untuk Anda. Selain itu, ia menyediakan fitur canggih seperti `frozen=True` untuk imutabilitas instan dan `field()` untuk kontrol granular terhadap atribut tertentu (misal: menyembunyikan password dari representasi string).

---

## 🎨 Visual Logic (Dataclass vs Manual)

| Fitur | Manual Class | Dataclass |
| :--- | :--- | :--- |
| **`__init__`** | Tulis Manual | **Otomatis** |
| **`__repr__`** | Tulis Manual | **Otomatis** |
| **`__eq__`** | Tulis Manual | **Otomatis** |
| **Type Hints** | Opsional | **Wajib (Pemandu)** |

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    DC[@dataclass] -- 1. Inspects --> Hints[Type Hints: name, age]
    DC -- 2. Generates --> Init[__init__]
    DC -- 2. Generates --> Repr[__repr__]
    DC -- 2. Generates --> Eq[__eq__]
    style DC fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Implementation: Clean Data Models
```python
from dataclasses import dataclass, field

@dataclass(frozen=True) # Immutable!
class User:
    id: int
    name: str
    email: str = "guest@example.com" # Default value
    password: str = field(repr=False) # Hidden from print()

    def __post_init__(self):
        # Validasi setelah inisialisasi otomatis
        if "@" not in self.email:
            raise ValueError("Invalid Email")
```

---

## ⚠️ Pitfalls
- **Default Argument Trap**: Seperti pada fungsi, jangan gunakan objek mutable (seperti `list` atau `dict`) sebagai nilai default secara langsung. Gunakan `field(default_factory=list)`.
- **Mutability by Default**: Berbeda dengan `namedtuple`, dataclass bersifat **mutable** kecuali Anda secara eksplisit menyetel `frozen=True`. Hati-hati saat menggunakannya sebagai key di Dictionary.
- **Type Hint Dependency**: Dataclass **wajib** memiliki anotasi tipe untuk setiap field. Jika Anda lupa memberi tipe (misal: `x = 10` tanpa `: int`), field tersebut tidak akan dianggap sebagai bagian dari dataclass.

---
*Back to [SR-07 Typing](../README.md)*
