# Rak 04: Core Mechanics (Mekanisme Internal)

> **"Python's real power lies not in its syntax, but in its Data Model."**

Rak ini membedah **Python Data Model** — lapisan protokol (`__dunder__` methods) yang menjadi tulang punggung semua objek Python. Memahami rak ini adalah perbedaan antara programmer Python dan *arsitek* Python.

## 🏗️ Struktur Sub-Rak

| Sub-Rak | Fokus | Konsep Utama |
| :--- | :--- | :--- |
| [SR-01-data-model](./SR-01-data-model/) | Fondasi Objek Python | `PyObject`, `__repr__`, `__eq__`, `__hash__` |
| [SR-02-protocols](./SR-02-protocols/) | Protokol Standar | Iterator, Iterable, Context Manager |
| [SR-03-descriptors](./SR-03-descriptors/) | Descriptor Protocol | `__get__`, `__set__`, property, classmethod |
| [SR-04-metaclasses](./SR-04-metaclasses/) | Kelas dari Kelas | `type`, `__new__`, `__init_subclass__` |
| [SR-05-memory](./SR-05-memory/) | Memori & GC | Reference counting, Cyclic GC, `weakref` |

## 🎯 Key Goals
- Memahami *mengapa* `a + b` bekerja — bagaimana `__add__` dipanggil oleh evaluator.
- Mampu membuat objek yang berperilaku seperti built-in types.
- Mengerti lifecycle objek Python dari kreasi hingga dealokasi.

---
- `[ ] Planned`: Menunggu pengisian konten.

*Back to [Library Root](../README.md)*
