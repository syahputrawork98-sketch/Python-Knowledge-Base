# SR-05: Object C-API (The Atomic Base Hub) [x] Complete

> **"Everything is an object, and every object is a pointer to a C struct."**

Sub-Rak ini membedah **Fondasi Atomik** dari setiap entitas dalam Python. Kita akan meninggalkan dunia dinamis Python sejenak untuk melihat bagaimana objek-objek tersebut didefinisikan secara fisik di level memori menggunakan bahasa C. Kita akan membedah rahasia di balik `PyObject` dan `PyTypeObject`.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_PyObject_Struct](./BK-01_PyObject_Struct/)** | Atomic Base | Bedah struktur data `PyObject` dan `ob_refcnt`. |
| **[BK-02_Type_Objects](./BK-02_Type_Objects/)** | Blueprints | Bedah `PyTypeObject` dan mekanisme slot metode C. |

---

## 🎯 Key Learning Goals
- Memahami struktur data fisik dari **PyObject** di level memori C.
- Mampu menjelaskan mekanisme **Reference Counting** dari perspektif C-struct.
- Memahami bagaimana **ob_type** menghubungkan instans dengan perilakunya.
- Mengenali peran **tp_slots** dalam memetakan metode Python ke fungsi C.
- Memahami keterbatasan fisik pewarisan di level interpreter (Memory Layout).

---

## 🧪 Prasyarat Teknis
- Pemahaman Stack & Evaluation Loop (RAK-06 SR-04).
- Pengetahuan DASAR tentang Pointer Merujuk ke Alamat Memori (C Pointers).

---

## ⏭️ Next Step
Setelah kita memahami fondasi objek yang statis, mari kita melompat ke masa depan Python dan melihat bagaimana mesin ini dioptimalkan secara dinamis melalui **[SR-06: Modern Internals (JIT & No-GIL)](../SR-06-modern-internals/)**.

---
*Back to [RAK-06 Interpreters](../README.md)*
