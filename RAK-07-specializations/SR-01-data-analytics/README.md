# SR-01: Modern Data Stack (The Analytics Engine) [x] Complete

> **"Speed is not just a feature; it's a structural requirement for modern engineering."**

Sub-Rak ini membedah **Mesin Analisis Modern** dalam ekosistem Python. Kita akan meninggalkan keterbatasan Pandas tradisional untuk mengeksplorasi **Polars** dan **DuckDB**—tulang punggung pemrosesan data berperforma tinggi yang didesain untuk menangani dataset raksasa dengan efisiensi memori maksimal (Apache Arrow).

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Polars_Mastery](./BK-01_Polars_Mastery/)** | Data Engine | Bedah manipulasi data berbasis Rust/SIMD dan Lazy API. |
| **[BK-02_DuckDB_OLAP](./BK-02_DuckDB_OLAP/)** | In-Process SQL | Bedah kueri SQL analitik super cepat tanpa server. |

---

## 🎯 Key Learning Goals
- Memahami perbedaan fundamental antara eksekusi **Eager** (Pandas) vs **Lazy** (Polars).
- Menguasai teknik manipulasi data skala besar (Jutaan baris) di dalam memori terbatas.
- Mampu mengintegrasikan kueri SQL kompleks langsung pada Dataframe via **DuckDB**.
- Memahami format memori **Apache Arrow** sebagai penyimpan data lintas-platform.
- Mampu memilih tool yang tepat (Polars vs DuckDB) berdasarkan karakteristik task.

---

## 🧪 Prasyarat Teknis
- Pemahaman Logika Dataframe DASAR (RAK-05 SR-03).
- Pengetahuan SANGAT DASAR tentang Kueri SQL (SELECT, GROUP BY).

---

## ⏭️ Next Step
Setelah kita menguasai akselerasi data mentah, mari kita pelajari bagaimana data tersebut digunakan untuk melatih kecerdasan buatan di **[SR-02: AI & ML Engineering](../SR-02-machine-learning/)**.

---
*Back to [RAK-07 Specializations](../README.md)*
