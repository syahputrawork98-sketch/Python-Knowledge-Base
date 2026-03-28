# BK-02: File Streams (io & tempfile) [x] Complete

> **"Data is a river. File streams are the pipes that direct it, whether in RAM or on Disk."**

Buku ini membedah **File Streams** menggunakan modul `io` (untuk manipulasi data di memori selayaknya file) dan modul `tempfile` (untuk manajemen berkas sementara yang aman). Kita akan mempelajari bagaimana mensimulasikan file untuk unit testing dan menjaga sistem tetap bersih dari sampah file temporer.

---

## 🌐 Source Hub (Authority)
- **Primary Source**: [Python Docs - io (Core tools for working with streams)](https://docs.python.org/3/library/io.html)
- **Strategic Blueprint**: [RAK-05 Standard Library](file:///i:/Workspace/Workspace-Syahputrawork/01-Language-Hubs-Workspace/Python-Knowledge-Base/RAK-05-standard-library/README.md)

---

## 🧠 The Essence (Narrative)
Kadang kita memiliki data dalam string yang ingin kita proses seolah-olah ia berasal dari sebuah file (misal: untuk dikirim ke fungsi yang hanya menerima objek file). Menggunakan **`io.StringIO`** dan **`io.BytesIO`**, kita bisa membuat "file virtual" di dalam RAM. Selain itu, saat melakukan pemrosesan data besar yang butuh penyimpanan sementara di disk, **`tempfile`** memastikan bahwa file-file tersebut diciptakan dengan nama acak yang aman dan akan dihapus secara otomatis saat tidak lagi digunakan — mencegah penumpukan sampah di direktori `/tmp`.

---

## 🎨 Visual Logic (Stream Processing)

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#3776AB', 'primaryTextColor': '#fff', 'lineColor': '#FFD43B'}}}%%
graph LR
    String[Raw String/Bytes] -- io.StringIO --> VFile[Virtual File in RAM]
    VFile -- processed by --> Logic[App Logic]
    Logic -- saves to --> TFile[tempfile: Auto-deleted]
    style VFile fill:#3776AB,stroke:#333,color:#fff
    style TFile fill:#FFD43B,stroke:#333,color:#000
```

---

## 🛠️ Implementation: Virtual Files & Safe Temps
```python
import io
import tempfile

# 1. StringIO: Mensimulasikan File (Ideal untuk Unit Test)
stream = io.StringIO("Line 1\nLine 2")
for line in stream:
    print(f"Reading from RAM: {line.strip()}")

# 2. tempfile: File Sementara yang Aman
with tempfile.NamedTemporaryFile(mode='w+', suffix='.log') as tmp:
    tmp.write("Pesan rahasia sementara...")
    tmp.seek(0)
    print(f"Temporary Path: {tmp.name}")
    print(tmp.read())
# File otomatis terhapus saat keluar dari blok 'with'
```

---

## ⚠️ Pitfalls
- **Seeking**: Saat menulis ke stream (seperti `StringIO` atau `BytesIO`), kursor berada di akhir data. Jika Anda ingin membaca kembali apa yang baru ditulis, Anda **wajib** memanggil `.seek(0)` untuk mengembalikan kursor ke awal.
- **Binary vs Text**: `StringIO` hanya untuk string (Teks). Jika data Anda adalah citra atau binari mentah, gunakan `BytesIO`.
- **Tempfile Persistence**: Jika Anda ingin file sementara tetap ada (misal: untuk debugging), Anda bisa mengatur `delete=False` pada `NamedTemporaryFile`, namun ingat bahwa Anda bertanggung jawab menghapusnya secara manual nanti.

---
*Back to [SR-05 I/O & Path](../README.md)*
