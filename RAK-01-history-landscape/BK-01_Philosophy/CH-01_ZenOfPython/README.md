# Zen of Python: Ontologi Desain Bahasa

**"Explicit is better than implicit."**
*Prinsip ini memiliki konsekuensi teknis langsung, bukan sekadar estetika kode.*

> [!IMPORTANT]
> **Source Link**: [PEP 20 -- The Zen of Python](https://peps.python.org/pep-0020/)

---

## 1. Definisi & Konsep (The Logic)

**PEP 20** bukan sekedar sajak gaya. Ia adalah **Ontologi Desain** yang mendikte bagaimana CPython dibangun dan bagaimana fitur-fitur baru dievaluasi di Steering Council. Setiap prinsip dalam Zen memiliki **konsekuensi implementasi teknis** yang dapat dilacak di source code CPython itu sendiri.

Jalankan `import this` di interpreter manapun untuk membacanya. Prinsip-prinsip tersebut sengaja disimpan dalam sebuah modul bernama `this.py` yang full dengan "kode yang buruk" sebagai lelucon meta, namun outputnya adalah keindahan.

### Terminologi Utama (Senior Terms)

| Istilah | Makna Teknis |
| :--- | :--- |
| **Orthogonality** | Fitur-fitur bahasa tidak saling tumpang tindih. Satu cara untuk setiap konsep. |
| **Duck Typing** | Fokus pada *protokol/perilaku* objek (`__iter__`, `__len__`) bukan hierarki kelas statis. Langsung dari Zen: "If it walks like a duck..." |
| **EAFP** | *Easier to Ask Forgiveness than Permission* — Gaya Python yang lebih memilih `try/except` daripada `if isinstance(...)`. |
| **Namespace** | "Namespaces are one honking great idea" — Zen secara eksplisit memodelkan Python's scoping rules (LEGB). |

---

## 2. Rasionalitas (Why & How?)

### Mengapa "Explicit > Implicit" Berdampak pada Compiler?

Di CPython, ini berarti Python **menolak konversi tipe otomatis**. Coba `"3" + 3` di Python — Anda mendapatkan `TypeError`. Di JavaScript atau C, operasi ini "berhasil" dengan hasil yang mungkin tidak terduga. Python memilih untuk *meledak dengan keras* (raise exception) daripada menebak maksud programmer.

Ini bukan overhead — ini adalah **Design Constraint** yang memastikan bytecode yang dihasilkan oleh compiler dapat diprediksi dan dianalisis secara statis.

### Mengapa "There Should Be One Obvious Way" Berdampak pada Stdlib?

Python secara aktif **mendepresiasi modul redundan**. Daftar panjang yang dihapus di Python 3 (`cPickle` → `pickle`, `urllib2` → `urllib.request`) adalah bukti nyata bahwa Zen bukan sekadar retorika. Setiap duplikasi di standard library adalah "technical debt" yang harus dilunasi.

### Analogi Mendalam: Arsitektur vs Improvisasi

Jika bahasa lain bertindak seperti musisi jazz yang berimprovisasi (implicit, flexible, unpredictable), Python adalah **Konduktor Orkestra Klasik**. Setiap pemain (developer) harus mengikuti partitur (explicit code). Jika ada bagian yang ambigu, konduktor berhenti dan meminta klarifikasi — bukan menebak nada berikutnya.

---

## 3. Implikasi Arsitektural (The Internals)

Prinsip Zen juga **mempengaruhi arsitektur CPython secara langsung**:

- **"Special cases aren't special enough to break the rules"** → Menjadi alasan mengapa `list`, `tuple`, dan `dict` semuanya diimplementasikan melalui protokol Python yang sama, bukan dengan jalur kode khusus.
- **"Errors should never pass silently"** → Menjadi fondasi *exception propagation model* di CPython's evaluation loop (`ceval.c`).
- **"In the face of ambiguity, refuse the temptation to guess"** → Inilah mengapa Python 3 memisahkan `bytes` dan `str` secara total, sebuah breaking change deliberate.

---

> [!NOTE]
> **Pengecualian "Nil Content"**: Unit ini murni bersifat filosofis/arsitektural. Pembuktian teknis `Duck Typing` (via `__dunder__` protokol) akan dibahas mendalam di **RAK-04 (Core Mechanics)**.

---
*Back to [BK-01_Philosophy](../README.md)*
