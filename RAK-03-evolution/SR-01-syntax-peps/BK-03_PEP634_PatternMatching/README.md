# BK-03: PEP 634 (Structural Pattern Matching) [x] Complete

> **"Structural Pattern Matching is the bridge between Python's flexibility and Functional Programming's rigor."**

Buku ini membedah **PEP 634**, yang memperkenalkan **Structural Pattern Matching** (`match` dan `case`) di Python 3.10. Kita akan mempelajari bagaimana fitur ini bukan sekadar pengganti *switch-case*, melainkan alat yang kuat untuk mengekstraksi data dan memproses logika bercabang secara deklaratif.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [PEP 634 -- Structural Pattern Matching Specification](https://peps.python.org/pep-0634/)
- **Strategic Blueprint**: [RAK-03 Evolution](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-03-evolution/README.md)

---

## 🧠 The Essence (Narrative)
Sejak awal, Python hanya mengandalkan `if-elif-else` untuk percabangan logika. Masalah muncul saat kita harus menangani data yang memiliki "bentuk" beragam, seperti pesan API (JSON) atau struktur pohon. PEP 634 mengusulkan solusi di tingkat **Struktur**. Dengan `match-case`, Anda tidak hanya membandingkan nilai, tetapi juga memeriksa "bentuk" atau tipe data objek tersebut secara rekursif. Ini menjerakan kode yang jauh lebih bersih dibandingkan pemeriksaan manual yang bertele-tele.

---

## 🎨 Visual Logic (Matching Pipeline)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph TD
    Input[Data Entry] --> Match{match data:}
    Match -- case [x, y] --> Seq[List with 2 items]
    Match -- case {"status": 200} --> Map[Success Dict]
    Match -- case int() --> Type[Integer input]
    Match -- case _ --> Default[Catch-all]
    style Match fill:#3776AB,stroke:#333,color:#fff
    style Default fill:#ccc,stroke:#333,color:#666
```

---

## 🛠️ Comparison: Problems -> Solutions

### ❌ The "Brittle" Problem (Nested If)
```python
if isinstance(data, list) and len(data) == 2:
    process_point(data[0], data[1])
elif isinstance(data, dict) and "id" in data:
    process_id(data["id"])
```

### ✅ The "Matching" Solution (3.10+)
```python
match data:
    case [x, y]:
        process_point(x, y)
    case {"id": user_id}:
        process_id(user_id)
```

---

## ⚠️ Pitfalls
- **Python Version**: Structural Pattern Matching **HANYA** tersedia di Python 3.10 ke atas. Menggunakannya di versi Python 3.9 atau lebih lama akan menyebabkan fatal `SyntaxError`.
- **Soft Keywords**: `match` dan `case` adalah "soft keywords". Artinya, Anda masih bisa menggunakan variabel bernama `match` di bagian lain kode Anda, namun sangat disarankan untuk menghindarinya agar tidak membingungkan pembaca kode.

---
*Back to [SR-01 Syntax Evolution](../README.md)*
