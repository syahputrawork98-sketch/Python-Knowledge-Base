# SR-04: Lazy Data Pipelines (Itertools) [x] Complete

> **"Itertools is the secret weapon for handling big data with small memory."**

Sub-Rak ini mengeksplorasi modul **`itertools`**, arsenal utama Python untuk melakukan pemrosesan data secara "malas" (*Lazy Evaluation*). Kita akan membedah bagaimana membangun pipa data (*Data Pipelines*) yang mampu menangani jutaan elemen tanpa menghabiskan RAM, serta teknik kombinatorial untuk menyingkirkan loop bersarang yang lambat.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_Infinite_Iterables](./BK-01_Infinite_Iterables/)** | Generations | Bedah `count`, `cycle`, dan `repeat` untuk stream tak terbatas. |
| **[BK-02_Combinatorics](./BK-02_Combinatorics/)** | Math Patterns | Bedah `product`, `permutations`, dan `combinations`. |
| **[BK-03_Pipeline_Tools](./BK-03_Pipeline_Tools/)** | Flows | Bedah `chain`, `islice`, dan `groupby` untuk pemrosesan aliran. |

---

## 🎯 Key Learning Goals
- Memahami prinsip **Lazy Evaluation** untuk penghematan memori ekstrem.
- Mampu menghasilkan aliran data (IDs, cycles) secara dinamis tanpa batas RAM.
- Menguasai teknik eliminasi **Nested Loops** menggunakan perkalian Cartesian (`product`).
- Memahami beda matematis antara **Permutations** vs **Combinations** dalam dataset.
- Mampu menyambung (`chain`) dan memotong (`islice`) iterator tanpa menyalin data.
- Menguasai pengelompokan data agregat menggunakan `groupby` (dengan syarat Sortir).

---

## 🧪 Prasyarat Teknis
- Pemahaman Iterator Dasar (RAK-04 SR-02).
- Pengetahuan Dasar Agregasi (RAK-05 SR-01).

---

## ⏭️ Next Step
Setelah menguasai aliran data di memori, mari kita tantang diri kita untuk mengelola file fisik secara modern di **[SR-05: Modern File System (Pathlib)](../SR-05-io-and-path/)**.

---
*Back to [Rak-05 Standard Library](../README.md)*
