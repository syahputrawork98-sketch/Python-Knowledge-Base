# Rak 06: Interpreters (The Machine Room)

> **"To truly master Python, you must understand the machine that runs it."**

Rak ini adalah **Ruang Mesin CPython** — membedah seluruh pipeline dari kode sumber hingga eksekusi bytecode. Ini adalah pengetahuan yang membedakan *senior engineer* dari *expert*.

## 🏗️ Struktur Sub-Rak

| Sub-Rak | Fokus | Komponen CPython |
| :--- | :--- | :--- |
| [SR-01-source-anatomy](./SR-01-source-anatomy/) | Peta Repositori | `Include/`, `Objects/`, `Python/` |
| [SR-02-parsing-ast](./SR-02-parsing-ast/) | Token → AST | `Parser/pegen.c`, `ast.c` |
| [SR-03-compilation-bytecode](./SR-03-compilation-bytecode/) | AST → Bytecode | `compile.c`, `symtable.c` |
| [SR-04-eval-loop](./SR-04-eval-loop/) | Evaluation Loop | `ceval.c`, Stack Machine |
| [SR-05-object-c-api](./SR-05-object-c-api/) | Fondasi C-API | `object.h`, `PyObject` |
| [SR-06-modern-internals](./SR-06-modern-internals/) | JIT & No-GIL | Python 3.13+, PEP 703 |

## 🎯 Key Goals
- Mampu membaca bytecode dengan `dis.dis()` dan menjelaskan eksekusinya.
- Mengerti mengapa GIL ada dan bagaimana PEP 703 mencoba mengatasinya.
- Memahami bagaimana `PyObject` menjadi fondasi dari semua tipe Python.

---
- `[x] 100% Complete`: Seluruh 6 Hub (SR-01 s/d SR-06) telah dibangun dengan standar Gold Standard (PPM V4).

*Back to [Library Root](../README.md)*
