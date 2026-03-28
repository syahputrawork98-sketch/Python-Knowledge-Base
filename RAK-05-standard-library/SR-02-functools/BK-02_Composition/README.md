# BK-02: Composition (partial & wraps) [x] Complete

> **"Functional composition is the art of building specialized tools from generic ones."**

Buku ini membedah **Functional Composition** (Komposisi Fungsi) di Python. Kita akan mempelajari bagaimana menggunakan `partial` untuk memfiksasi argumen fungsi dan mengapa `@wraps` adalah dekorator yang wajib ada di setiap dekorator yang Anda tulis.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - functools (Higher-order functions)](https://docs.python.org/3/library/functools.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Python memungkinkan kita untuk mencampur dan mencocokkan fungsi melalui dua utilitas kritis:
1.  **`partial(func, *args, **kwargs)`**: Memungkinkan Anda "mengunci" beberapa argumen dari sebuah fungsi untuk membuat versi yang lebih spesifik.
2.  **`@wraps(func)`**: Digunakan saat Anda menulis dekorator kustom. Fungsinya adalah menyalin metadata asli (seperti nama fungsi dan dokumentasi) ke fungsi pembungkusnya. Tanpa ini, semua fungsi yang didekorasi akan terlihat seperti "wrapper" di mata sistem introspeksi Python.

---

## 🎨 Visual Logic (Functional Currying)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    Generic[Generic Function: f(a, b)] -- Fixate a=10 --> Partial[Partial Function: g(b)]
    Partial -- Called with b=5 --> Result[Result: f(10, 5)]
    style Partial fill:#3776AB,stroke:#333,color:#fff
    style Result fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation: Specialized Utilities
```python
from functools import partial, wraps

# 1. Partial in Action
int2 = partial(int, base=2)
print(int2('101')) # Result: 5 (Binary conversion)

# 2. Wraps in Action (The Decorator Hero)
def my_decorator(f):
    @wraps(f) # <--- Critical! Preserves metadata.
    def wrapper(*args, **kwargs):
        print("   [LOG] Before execution...")
        return f(*args, **kwargs)
    return wrapper
```

---

## ⚠️ Pitfalls
- **Metadata Loss**: Jika Anda lupa menggunakan `@wraps` di dalam dekorator, maka `my_func.__name__` akan berubah menjadi `wrapper`. Ini akan menghancurkan sistem debugging, dokumentasi otomatis (seperti Sphinx), dan testing framework.
- **Argument Binding**: `partial` melakukan *binding* argumen secara statis saat deklarasi. Hati-hati jika Anda mem-partial fungsi yang bergantung pada variabel dinamis di sekitarnya.
- **Over-specialization**: Jangan gunakan `partial` secara berlebihan untuk setiap variasi fungsi. Terkadang fungsi baru (`def`) dengan default arguments sudah cukup jelas.

---
*Back to [SR-02 Functools](../README.md)*
