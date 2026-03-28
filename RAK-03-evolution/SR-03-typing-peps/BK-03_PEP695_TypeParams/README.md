# BK-03: PEP 695 (Type Parameter Syntax) [x] Complete

> **"PEP 695 makes generics a first-class citizen of Python syntax."**

Buku ini membedah **PEP 695**, yang memperkenalkan **Type Parameter Syntax** di Python 3.12. Kita akan mempelajari bagaimana proposal ini merevolusi cara kita menulis kode generik dan alias tipe melalui kata kunci baru `type`, menggantikan metode lama yang bertele-tele.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [PEP 695 -- Type Parameter Syntax](https://peps.python.org/pep-0695/)
- **Strategic Blueprint**: [RAK-03 Evolution](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-03-evolution/README.md)

---

## 🧠 The Essence (Narrative)
Secara historis, mendefinisikan kelas atau fungsi generik di Python membutuhkan impor manual `TypeVar` dan pewarisan eksplisit dari `Generic[T]`. Masalahnya adalah **Kebisingan Sintaksis** (Syntax Noise) — deklarasi generik menjadi panjang dan sulit dibaca. PEP 695 mengusulkan solusi di tingkat **Sintaksis Deklaratif**. Dengan menggunakan kurung siku `[T]` langsung setelah nama fungsi atau kelas, serta memperkenalkan pernyataan `type` sebagai alias resmi, Python 3.12 menjadikan generik jauh lebih intuitif dan bersih.

---

## 🎨 Visual Logic (Generic Syntax Evolution)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Pre312[Legacy: TypeVar + Generic] -- Verbose --> Post312[Modern: Bracketed TypeParams]
    Post312 -- PEP 695 --> FirstClassSytax[Clean & Intuitive]
    style Post312 fill:#3776AB,stroke:#333,color:#fff
```

---

## 🛠️ Comparison: Problems -> Solutions

### ❌ The "Verbose" Problem (Pre-3.12)
```python
from typing import TypeVar, Generic
T = TypeVar("T")

class Stack(Generic[T]):
    def push(self, item: T): ...
```

### ✅ The "Modern" Solution (3.12+)
```python
class Stack[T]:
    def push(self, item: T): ...

# Type Alias modern
type Point = tuple[float, float]
```

---

## ⚠️ Pitfalls
- **Python Version**: PEP 695 **HANYA** tersedia di Python 3.12 ke atas. Menggunakannya di versi Python 3.11 atau lebih lama akan menyebabkan fatal `SyntaxError`.
- **Import Conflicts**: Pastikan Anda tidak memiliki variabel atau modul lama bernama `type` di dalam skrip Anda, meskipun `type` di sini adalah kata kunci baru yang dioptimalkan oleh parser Python 3.12. Untuk menjaga kompatibilitas ke belakang (Backwards Compatibility), gunakan gaya lama jika pustaka Anda harus mendukung Python < 3.12.

---
*Back to [SR-03 Type System Evolution](../README.md)*
