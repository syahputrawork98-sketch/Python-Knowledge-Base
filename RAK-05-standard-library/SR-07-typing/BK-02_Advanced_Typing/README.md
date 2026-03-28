# BK-02: Advanced Typing (Protocols & Generics) [x] Complete

> **"Typing in Python is not about restriction; it's about documenting the contract between parts of your system."**

Buku ini membedah **Advanced Typing**, fitur utama sistem tipe Python modern untuk mendukung pengembangan skala besar. Kita akan mempelajari **Structural Typing** melalui **`Protocol`**, serta bagaimana membangun komponen yang fleksibel menggunakan **`Generic`**.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - typing (Support for type hints)](https://docs.python.org/3/library/typing.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Secara tradisional, Python menggunakan **Duck Typing** ("Jika ia berjalan seperti bebek, maka ia bebek"). Sejak Python 3.8 (PEP 544), kita bisa memformalkan ini melalui **`Protocol`**. Berbeda dengan pewarisan standar (Nominal Subtyping), `Protocol` menggunakan **Structural Subtyping**. Sebuah kelas dianggap "bertipe X" cukup dengan memiliki metode yang sama, tanpa perlu mewarisi secara eksplisit. Ditambah dengan **`Generic`**, kita bisa membuat fungsi yang bekerja untuk berbagai tipe data namun tetap mempertahankan keamanan tipe.

---

## 🎨 Visual Logic (ABC vs Protocol)

| Aspect | Nominal (ABC) | Structural (Protocol) |
| :--- | :--- | :--- |
| **Inheritance** | Explicit (`is-a`) | Implicit (`has-methods`) |
| **Logic** | Rigid & Defensive | Flexible & Dynamic |
| **Use Case** | Shared Logic/Base Classes | Interfaces / Duck Typing |

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    P[Protocol: 'Drawable'] -- requires --> D[Method: .draw()]
    C1[Circle] -- has --> D
    C2[Square] -- has --> D
    C1 -. satisfies .-> P
    C2 -. satisfies .-> P
    style P fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Implementation: Defining the Contract
```python
from typing import Protocol, runtime_checkable, TypeVar, Generic

# 1. Protocol: Structural Interface
@runtime_checkable # Allows isinstance() checks at runtime
class Drawable(Protocol):
    def draw(self) -> str: ...

# 2. Generic: Type Safety for Multi-types
T = TypeVar("T")
class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

num_box = Box[int](10)
```

---

## ⚠️ Pitfalls
- **Runtime Performance**: Menggunakan `@runtime_checkable` menambah overhead kecil pada `isinstance()` karena Python harus memindai seluruh atribut kelas tersebut setiap kali pengecekan dilakukan. Jangan menggunakannya di dalam loop yang sangat ketat.
- **Protocol vs ABC**: Jangan bingung antara keduanya. Gunakan ABC jika Anda ingin menyediakan implementasi default (metode konkret). Gunakan Protocol jika Anda hanya ingin mendefinisikan "kontrak" tanpa implementasi apa pun.
- **Generic Overuse**: Jangan membuat semuanya generik hanya karena bisa. Seringkali tipe data yang eksplisit lebih mudah dipahami oleh pengembang lain.

---
*Back to [SR-07 Typing](../README.md)*
