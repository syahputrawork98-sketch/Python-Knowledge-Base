# The Great Rift: Perpecahan Python 2 vs Python 3

**"We wanted to fix the mistakes of the past, and many of us are still paying for it."**
*The Great Rift adalah pelajaran terbesar dalam sejarah pengembangan bahasa pemrograman modern.*

> [!IMPORTANT]
> **Source Link**: [PEP 3000 -- Python 3000](https://peps.python.org/pep-3000/) | [PEP 3131 -- Supporting Non-ASCII Identifiers](https://peps.python.org/pep-3131/)

---

## 1. Definisi & Konsep (The Logic)

**The Great Rift** adalah nama tidak resmi untuk periode 2008–2020 dimana Python 2 dan Python 3 hidup berdampingan dalam ekosistem yang terpecah. Python 3.0 dirilis Desember 2008 dengan tujuan mulia: menjadi versi Python yang "bersih" dan konsisten. Namun konsekuensinya adalah **breaking change terbesar dalam sejarah bahasa pemrograman mainstream**.

### Perubahan Paling Kritis (Yang Menciptakan Rift)

| Area | Python 2 | Python 3 | Dampak |
|---|---|---|---|
| **String** | `str` = bytes, `unicode` terpisah | `str` selalu Unicode, `bytes` terpisah | Semua string-handling harus ditulis ulang |
| **`print`** | Statement: `print "hello"` | Function: `print("hello")` | Semua script lama langsung rusak |
| **`input()`** | Mengevaluasi ekspresi (danger!) | Selalu mengembalikan string | Breaking change pada security model |
| **Integer Division** | `5 / 2 = 2` (truncate) | `5 / 2 = 2.5` (float) | Bug numerik tersembunyi di code base lama |
| **`range()`** | Mengembalikan list (memory hog) | Mengembalikan iterator (lazy) | Perubahan perilaku diam-diam (*silent*) |

### Terminologi Utama (Senior Terms)

| Istilah | Makna |
|---|---|
| **`__future__` imports** | Mekanisme migrasi gradual — memungkinkan Python 2 untuk "meminjam" fitur Python 3 (`from __future__ import print_function`). |
| **`2to3` tool** | Automated refactoring script dari CPython team untuk membantu migrasi. |
| **PyPI Wheel** | Format distribusi yang memungkinkan library untuk menerbitkan versi terpisah untuk Py2 dan Py3 secara bersamaan. |
| **EOL (End of Life)** | Python 2 secara resmi mati pada **1 Januari 2020** — 12 tahun perjuangan transisi. |

---

## 2. Rasionalitas (Why & How?)

### Mengapa Guido Memilih Breaking Change Daripada Evolusi Gradual?

Masalah string duality di Python 2 adalah *systemic bug, bukan cosmetic bug*. Setiap kali developer mencampur `str` dan `unicode`, mereka mendapat `UnicodeDecodeError` yang sulit di-debug. Ini adalah sumber bug #1 di aplikasi Python skala besar (web scraping, database, networking).

Solusi gradual tidak mungkin: untuk memperbaiki string handling, seluruh interpreter, parser, dan standard library harus konsisten. Tidak ada cara untuk "setengah-setengah" mengubah fondasi.

Ini adalah penerapan ekstrem dari Zen Python: **"Now is better than never. Although never is often better than *right* now."** — Paradoks yang Guido selesaikan dengan memilih jangka panjang.

### Biaya Nyata vs Keuntungan Nyata

**Biaya:**
- ~12 tahun fragmentasi ekosistem.
- Ribuan jam kerja developer untuk migrasi.
- Beberapa library besar (seperti NumPy) harus mempertahankan dua codebase.

**Keuntungan:**
- Python 3 adalah platform yang jauh lebih stabil untuk distributed system.
- Unicode-by-default membuat Python menjadi pilihan utama untuk NLP dan internasional apps.
- Konsistensi bahasa meningkat drastis — tidak ada lagi "jebakan" konversi implisit.

### Analogi Mendalam: Renovasi Gedung Bersejarah

The Great Rift seperti merenovasi **Gedung Bersejarah yang Masih Berpenghuni**. Anda tahu fondasinya retak (string duality), tapi Anda tidak bisa mengosongkan gedung sekaligus — ribuan bisnis beroperasi di sana. Anda harus membangun fondasi baru di sebelahnya, sambil terus melayani penghuni lama, selama 12 tahun. Menyakitkan, mahal, tapi hasilnya adalah gedung yang bisa berdiri 50 tahun lagi.

---

## 3. Warisan Struktural

The Great Rift meninggalkan beberapa pola di CPython modern:

- **PEP proses yang lebih ketat** — Setiap breaking change kini harus melalui Deprecation Period minimal 2 versi.
- **`__future__` module** menjadi standar untuk preview fitur baru.
- **Semantic Versioning awareness** — Python sekarang lebih berhati-hati tentang minor vs major changes.

---

> [!NOTE]
> **Pengecualian "Nil Content"**: Materi historis naratif. Mekanisme internal Unicode di CPython (`CPython/Objects/unicodeobject.c`) akan dibahas di **RAK-06 (Interpreters)**.

---
*Back to [BK-01_Genesis](../README.md)*
