# Origin & Evolution: Dari ABC hingga AI Lingua Franca

**"Python is an experiment in how little machinery you need to build a powerful system."**
*Memahami sejarah CPython adalah memahami trade-off desain yang masih relevan sampai hari ini.*

> [!IMPORTANT]
> **Source Link**: [The History of Python (Guido van Rossum's Blog)](https://python-history.blogspot.com/) | [Python Release History](https://www.python.org/doc/versions/)

---

## 1. Definisi & Konsep (The Logic)

Python tidak lahir di ruang hampa. Ia lahir pada **Desember 1989** dari kegelisahan Guido van Rossum terhadap bahasa ABC yang ia kerjakan di CWI (Centrum Wiskunde & Informatica), Belanda. Keluhan Guido sederhana: ABC terlalu *closed* — tidak bisa mengakses sistem operasi Amoeba secara langsung.

Solusi Guido: buat bahasa baru yang **C-Extensible by Design** — interpreter bisa dikompilasi sebagai pustaka C (`libpython`), sehingga dapat disematkan ke dalam program manapun. Inilah keputusan arsitektural yang membuat Python masih relevan 35 tahun kemudian.

### Terminologi Utama (Senior Terms)

| Istilah | Konteks Historis |
| :--- | :--- |
| **BDFL** | *Benevolent Dictator For Life* — Peran Guido yang menjamin konsistensi desain Python selama 30 tahun, sebelum ia "pensiun" pada 2018. |
| **The Great Rift** | Pemecahan ekosistem saat Python 3.0 (2008) hadir dengan Unicode-by-default yang tidak kompatibel mundur. Komunitas terpecah selama ~10 tahun. |
| **Steering Council** | Badan 5-orang yang menggantikan BDFL pasca-2019, mengelola PEPs dan arah bahasa secara demokratis. |
| **`libpython`** | Shared library dari CPython yang memungkinkan Python diembed ke dalam aplikasi C/C++ (digunakan oleh Blender, Vim, dll). |

---

## 2. Rasionalitas (Why & How?)

### Mengapa "The Great Rift" (Python 2 → 3) Adalah Keputusan Benar?

Python 2 memiliki dua tipe string: `str` (bytes) dan `unicode`. Pencampurannya menyebabkan ribuan bug produksi yang sulit dilacak. Python 3 memutuskan bahwa **semua string adalah Unicode** — satu kebenaran tunggal. Ini adalah penerapan langsung Zen: "In the face of ambiguity, refuse the temptation to guess."

Biayanya nyata: seluruh ekosistem harus ditulis ulang. Tapi hasilnya juga nyata: Python 3.x adalah platform yang jauh lebih stabil untuk distributed computing, dimana encoding data lintas network adalah fundamental.

### Mengapa CPython (bukan Jython/PyPy) yang Menang?

CPython menang bukan karena tercepat, melainkan karena ia adalah **Reference Implementation** yang memiliki C-API yang stabil. NumPy, SciPy, dan jutaan extension modules ditulis melawan C-API CPython. Ini menciptakan **network effect** yang tidak bisa dikalahkan oleh implementasi alternatif.

### Analogi Mendalam: Jembatan Gantung

Python seperti **Jembatan Gantung Besar** yang direvisi. Pondasinya ditanam dalam di tanah OS/C (versi 1.x). Jalannya kemudian diperlebar untuk ribuan kendaraan industri (versi 2.x). Kemudian datang retrofit besar: seluruh jembatan diawali ulang selama 10 tahun (2008–2020) demi memastikan ia tidak runtuh akibat karat "string duality". Painful, tapi perlu.

---

## 3. Jejak Arsitektur ke Masa Kini

Keputusan desain awal Guido masih terasa langsung di sumber CPython (*cpython/Python/ceval.c*) hari ini:

- **Namespace isolation** yang ketat mencegah global variable pollution.
- **`libpython` as a shared library** memungkinkan Python menjadi scripting engine di Blender, LibreOffice, hingga embedded systems.
- **C-extensibility** adalah alasan mengapa NumPy bisa mengalahkan MATLAB dan mengapa TensorFlow memilih Python sebagai front-end.

---

> [!NOTE]
> **Pengecualian "Nil Content"**: Materi sejarah arsitektural pada level Anatomy. Detail mekanisme C-API (`PyObject`, `Py_INCREF`) akan dibedah secara teknis di **RAK-06 (Interpreters)**.

---
*Back to [BK-01_Philosophy](../README.md)*
