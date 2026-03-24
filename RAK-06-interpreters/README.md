# Rak 06: Interpreters (The Machine Room)

> **"To truly master Python, you must understand the machine that runs it."**

Rak ini adalah **Ruang Mesin CPython** — membedah seluruh pipeline dari kode sumber hingga eksekusi bytecode. Ini adalah pengetahuan yang membedakan *senior engineer* dari *expert*.

## 🏗️ Struktur Sub-Rak

| Sub-Rak | Fokus | Komponen CPython |
| :--- | :--- | :--- |
| [SR-01-pipeline](./SR-01-pipeline/) | Tokenisasi → AST | `tokenize`, `ast` module |
| [SR-02-bytecode](./SR-02-bytecode/) | Kompilasi Bytecode | `dis` module, `.pyc`, opcode |
| [SR-03-ceval](./SR-03-ceval/) | Evaluation Loop | `ceval.c`, frame object, stack machine |
| [SR-04-gc](./SR-04-gc/) | Garbage Collector | Reference counting, Cyclic GC, `gc` module |
| [SR-05-gil](./SR-05-gil/) | Global Interpreter Lock | `gil.c`, Thread safety, PEP 703 No-GIL |
| [SR-06-c-api](./SR-06-c-api/) | C Extension API | `PyObject`, `Py_INCREF`, `Py_DECREF` |

## 🎯 Key Goals
- Mampu membaca bytecode dengan `dis.dis()` dan menjelaskan eksekusinya.
- Mengerti mengapa GIL ada dan bagaimana PEP 703 mencoba mengatasinya.
- Memahami bagaimana `PyObject` menjadi fondasi dari semua tipe Python.

---
- `[ ] Planned`: Menunggu pengisian konten.

*Back to [Library Root](../README.md)*
