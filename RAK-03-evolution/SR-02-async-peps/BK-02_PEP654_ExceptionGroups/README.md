# BK-02: PEP 654 (Exception Groups) [x] Complete

> **"When multiple tasks fail concurrently, we shouldn't just record the first failure; we should handle them all."**

Buku ini membedah **PEP 654**, yang memperkenalkan **Exception Groups** dan sintaksis **`except*`** di Python 3.11. Kita akan mempelajari bagaimana Python berevolusi untuk menangani kegagalan massal dalam eksekusi konkuren tanpa kehilangan informasi error penting.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [PEP 654 -- Exception Groups and except*](https://peps.python.org/pep-0654/)
- **Strategic Blueprint**: [RAK-03 Evolution](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-03-evolution/README.md)

---

## 🧠 The Essence (Narrative)
Sejak awal, Python berasumsi satu `try` menghasilkan paling banyak satu `except`. Masalah muncul pada pemrograman asinkron tingkat lanjut: jika kita menjalankan 10 tugas secara paralel dan 3 di antaranya gagal, mana yang harus kita tangkap? PEP 654 mengusulkan solusi di tingkat **Agregasi**. Dengan `ExceptionGroup`, Python dapat membungkus beberapa eksepsi sekaligus. Pasangannya, sintaksis `except*`, memungkinkan Anda menangkap tipe error tertentu dari dalam grup tersebut secara selektif tanpa menghentikan penangkapan tipe error lain.

---

## 🎨 Visual Logic (Exception Group Handling)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Group[ExceptionGroup: msg] -- contains --> E1[ValueError]
    Group -- contains --> E2[TypeError]
    Group -- contains --> E3[KeyError]
    Group --> Handle{except* ValueError:}
    Handle -- Match --> Action1[Handle ValueError]
    Handle -- Remaining --> Rest[Group {TypeError, KeyError}]
    style Group fill:#3776AB,stroke:#333,color:#fff
    style Rest fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Comparison: Problems -> Solutions

### ❌ The "Incomplete" Problem (Pre-3.11)
```python
# Hanya menangkap satu error pertama, yang lain hilang
try:
    await asyncio.gather(task1(), task2())
except Exception as e:
    print(f"Caught one: {e}")
```

### ✅ The "Aggregate" Solution (3.11+)
```python
# Menangani semua error berdasarkan tipenya dari dalam grup
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task1())
        tg.create_task(task2())
except* ValueError as eg:
    print(f"Handled all ValueErrors in group")
except* TypeError as eg:
    print(f"Handled all TypeErrors in group")
```

---

## ⚠️ Pitfalls
- **Python Version**: Exception Groups dan `except*` **HANYA** tersedia di Python 3.11 ke atas. Menggunakannya di versi Python 3.10 atau lebih lama akan menyebabkan fatal `SyntaxError`.
- **Async Dependency**: Walaupun bisa digunakan secara sinkron, fitur ini lebih banyak ditemukan dalam konteks asinkron (`asyncio.TaskGroup`). Pastikan Anda memahami dasar asinkron (SR-02 BK-01) sebelum menggunakan fitur ini secara efektif.

---
*Back to [SR-02 Async & Concurrency](../README.md)*
