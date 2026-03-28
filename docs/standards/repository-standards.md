# Repository Standards: Hierarchy & Conventions

Dokumen ini mengatur struktur fisik, penamaan, dan mekanisme pelacakan status di Python Knowledge Base sesuai dengan **Unified Gold Standard**.

---

## 🌐 0. Hubungan Blueprint vs Workspace

Repositori ini (Workspace) adalah **Laboratorium Teknis** yang harus selalu selaras dengan **Strategic Blueprint** (Peta Induk).

- **Blueprint (Strategic)**: Menyimpan konteks industri, posisi dalam Learning Matrix, dan arah strategis.
- **Workspace (Operational)**: Menyimpan detail spesifikasi, internal CPython, dan kode pembuktian lab.
- **Tautan Induk**: [Strategic Blueprint: Python](file:///i:/Workspace/Workspace-Syahputrawork/learning-matrix-blueprint/01-Language-Hubs/Python-Knowledge-Base.md)

---

## 🏛️ 1. Hirarki 6-Level (Universe Standard)

Sistem ini mengikuti hirarki kedalaman yang konsisten untuk seluruh repositori:

| Tingkatan | Nama | Analogi | Prefix | Contoh Direktori |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1** | **Root** | Library Hub | `/` | `/` |
| **Level 2** | **Rak** | Domain Utama | `RAK-` | `RAK-01-anatomy/` |
| **Level 3** | **Sub-Rak** | Track Spesifik | `SR-` | `SR-01-essence/` |
| **Level 4** | **Buku** | Koleksi Terpadu | `BK-` | `BK-01_Philosophy/` |
| **Level 5** | **Bab** | Materi Inti | `CH-` | `CH-01_ZenOfPython/` |
| **Level 6** | **Section** | Detail Halaman | `SEC-` | `SEC-01_Introduction/` |

> [!IMPORTANT]
> **Pengecualian RAK-01**: Menggunakan **Flat Structure** (RAK > BK > CH > SEC) dengan melompati Level 3 (SR) untuk efisiensi naratif. RAK lain tetap menggunakan struktur lengkap.

---

## 📏 2. Konvensi Penamaan

| Elemen | Aturan | Contoh |
| :--- | :--- | :--- |
| **Rak & Sub-Rak** | `kebab-case` dengan prefix `RAK-` atau `SR-`. | `RAK-04-core-mechanics` |
| **Buku, Bab, Section** | Prefix (BK/CH/SEC) + `_` + Name Slug. | `CH-01_BytecodeInterpreter` |
| **Lab Praktis** | Prefix numerik 2-digit berurutan dengan ekstensi `.py`. | `01_ref_counting.py` |

---

## 🏗️ 3. Struktur Internal Unit (Level 5 & 6)

Setiap folder Bab (**CH**) atau Section (**SEC**) wajib memiliki struktur minimal:
```text
CH- atau SEC-/
├── README.md        <- Materi teks inti & diagram Mermaid inline (PPM V4).
├── examples/        <- Kode lab fungsional .py (Wajib untuk materi teknis).
└── assets/          <- Media statis eksternal (Opsional).
```

---

## 🔄 4. Protokol Pembaruan Status (Bubbling Up)

Progress pengerjaan repositori dihitung secara otomatis dari unit terkecil:

1.  **Level Bab/Section**: Status dicatat di `README.md` lokal (`[ ] Draft`, `[/] Partial`, `[x] Complete`).
2.  **Level Buku/Sub-Rak**: Persentase penyelesaian = `(Σ Complete) / (Total Unit)`.
3.  **Global Status**: Dashboard utama berada pada file `status.md` di root repositori.

---

## 🪞 5. Prinsip "Digital Mirroring"

Hierarki ini mencerminkan struktur sumber primer (docs.python.org / PEPs) secara **1:1**. Jika sumber menuntut kedalaman lebih (misal: sub-clause spesifikasi), gunakan Level 6 (**SEC**) untuk menjaga integritas struktur utama.
