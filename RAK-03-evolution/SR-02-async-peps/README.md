# SR-02: Async & Concurrency Evolution [x] Complete

> **"Asynchronous programming is the key to building high-performance, I/O-bound applications in modern Python."**

Sub-Rak ini mengeksplorasi transformasi dramatis dalam paradigma konkurensi Python. Kita akan membedah bagaimana Python berpindah dari ketergantungan pada generator ke sintaksis native `async/await`, hingga kemampuan menangani banyak kegagalan sekaligus melalui sistem agregasi error yang revolusioner.

---

## 🌍 Landscape (Daftar Buku)

| Buku | Fokus | Deskripsi |
| :--- | :--- | :--- |
| **[BK-01_PEP492_AsyncAwait](./BK-01_PEP492_AsyncAwait/)** | Native Syntax | Transisi ke coroutine native (Py 3.5+). |
| **[BK-02_PEP654_ExceptionGroups](./BK-02_PEP654_ExceptionGroups/)** | Error Handling | Penanganan banyak error via `except*` (Py 3.11+). |

---

## 🎯 Key Learning Goals
- Memahami beda antara **Generator-based Coroutines** vs **Native Coroutines**.
- Mampu mengimplementasikan pola **Non-blocking I/O** menggunakan `async` dan `await`.
- Menguasai teknik pengolahan kegagalan massal dalam konkurensi via **Exception Groups**.
- Memahami evolusi model eksekusi asinkron Python dari waktu ke waktu.

---

## 🧪 Prasyarat Teknis
- Pemahaman dasar Control Flow (SR-04) dan Exception Handling (SR-08) di RAK-02 Foundation.
- Instalasi Python 3.11+ sangat disarankan untuk memahami fitur Exception Groups secara utuh.

---

## ⏭️ Next Step
Setelah menguasai evolusi konkurensi, mari kita beralih ke perjalanan Python menjadi bahasa yang lebih aman dan terstruktur melalui **[SR-03: Type System Evolution](../SR-03-typing-peps/README.md)**.

---
*Back to [Rak-03 Evolution](../README.md)*
