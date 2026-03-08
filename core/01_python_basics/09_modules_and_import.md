# Modules and Import

Chapter Code: CORE-01-09
Book Code: CORE-01
Version: v0.2.9
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 45 menit teori + 40 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas cara memecah kode Python ke beberapa file (module) dan cara memakainya dengan `import`. Kamu akan memahami pola import yang umum, struktur package dasar, penggunaan alias, serta praktik agar kode tetap rapi dan mudah dirawat.

## Prasyarat Spesifik Bab

- memahami `07_functions.md`
- memahami `08_basic_data_structures.md`
- memahami alur eksekusi dari `06_control_flow.md`

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| module | file Python yang bisa diimpor | `math_utils.py` |
| import | mekanisme menggunakan module lain | `import math` |
| package | folder berisi modul-modul terkait | `utils/` |
| namespace | ruang nama untuk mencegah bentrok identifier | `math.sqrt` |
| alias import | nama singkat untuk module/simbol | `import numpy as np` |
| entry point | titik awal eksekusi script | `if __name__ == "__main__":` |

## Tujuan Besar

Membantu pembaca menyusun kode menjadi modul terpisah agar proyek lebih terstruktur, reusable, dan mudah dikembangkan.

## Tujuan Kecil

- memahami perbedaan `import x` vs `from x import y`
- menggunakan alias import dengan tepat
- membuat module sederhana sendiri
- memahami fungsi `if __name__ == "__main__":`
- menghindari masalah import path dasar

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- kode sudah terlalu panjang dalam satu file
- ingin memisahkan fungsi per tanggung jawab
- ingin menggunakan modul bawaan atau modul buatan sendiri

## Bukan Peruntukan

Bab ini bukan untuk:

- internals import system CPython tingkat lanjut
- packaging/distribution lanjutan (akan dibahas di buku lain)

## Analogi

Module itu seperti lemari arsip per kategori. Import adalah cara mengambil berkas yang kamu butuhkan tanpa mencampur semua berkas dalam satu map besar.

## Miskonsepsi Umum

- Miskonsepsi: `from module import *` aman untuk pemula.
  Klarifikasi: wildcard import membuat namespace tidak jelas dan berisiko bentrok nama.

- Miskonsepsi: file `.py` otomatis jadi package.
  Klarifikasi: package adalah organisasi folder modul; praktik modern bisa pakai namespace package, namun struktur perlu jelas.

## Konsep Inti

### 1. Pola Import Dasar

```python
import math
print(math.sqrt(25))

from math import pi
print(pi)

import math as m
print(m.ceil(2.1))
```

Gunakan `import module` saat ingin namespace jelas. Gunakan `from ... import ...` saat butuh simbol tertentu.

### 2. Membuat Module Sendiri

Contoh file `math_utils.py`:

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Contoh pemakaian di `main.py`:

```python
import math_utils

print(math_utils.add(2, 3))
print(math_utils.multiply(4, 5))
```

### 3. `if __name__ == "__main__"`

```python
def greet(name):
    return f"Halo, {name}!"

if __name__ == "__main__":
    print(greet("Python"))
```

Blok ini hanya jalan saat file dieksekusi langsung, bukan saat di-import.

### 4. Struktur Package Dasar

```text
project/
|-- app.py
`-- utils/
    |-- __init__.py
    `-- formatter.py
```

Contoh import:

```python
from utils.formatter import to_upper
```

## Diagram

![Big picture Modules and Import](assets/09_modules_and_import.svg)

Caption: Diagram memperlihatkan alur pemisahan kode ke modul dan proses pemanggilan kembali lewat import.

### Legenda Diagram

- kotak biru: file/module sumber
- panah: proses import
- kotak hijau: fungsi/kelas dipakai di modul pemanggil

## Contoh Kode (Benar)

```python
# text_utils.py
def shout(text):
    return text.upper() + "!"

# main.py
from text_utils import shout

print(shout("belajar python"))
```

Expected output:

```text
BELAJAR PYTHON!
```

## Pitfall Umum

Wildcard import:

```python
from math import *
print(sqrt(16))
```

Perbaikan (lebih jelas):

```python
import math
print(math.sqrt(16))
```

Masalah nama file bentrok dengan module standar (`math.py`, `json.py`):

```text
math.py  # file lokal
```

Perbaikan:

- ganti nama file lokal agar tidak bentrok module bawaan
- pastikan struktur folder proyek jelas

## Catatan Praktis

- hindari `import *`
- gunakan nama module deskriptif (`text_utils`, `validators`)
- letakkan import di bagian atas file (kecuali ada alasan khusus)
- kelompokkan import: standard library, third-party, local

## Latihan

### Dasar

Buat module `greetings.py` berisi fungsi `hello(name)`, lalu panggil dari file lain.

### Menengah

Pisahkan fungsi matematika sederhana (`add`, `subtract`) ke module terpisah dan gunakan alias import.

### Mini Challenge

Buat mini project 3 file: `main.py`, `calculator.py`, `formatter.py`, lalu hubungkan dengan import agar aplikasi berjalan modular.

## Checklist Lulus Bab

- [ ] memahami konsep module dan import
- [ ] bisa membuat dan mengimpor module sendiri
- [ ] menggunakan `if __name__ == "__main__":` dengan benar
- [ ] menghindari wildcard import dan bentrok nama modul

## Peta Keterkaitan

- Bab sebelumnya: `08_basic_data_structures.md`
- Bab berikutnya: `10_input_output.md`
- Keterkaitan lintas buku Core: `CORE-06` (Modules and Import System)

## Ringkasan

- Module membantu memecah kode agar rapi dan reusable.
- Import yang jelas menjaga namespace tetap aman dan mudah dibaca.
- Struktur package sederhana memberi fondasi proyek Python yang sehat.

## FAQ Singkat

1. Kapan pakai `import module` vs `from module import func`?
   Jawaban singkat: pakai `import module` untuk kejelasan namespace; pakai `from ... import ...` saat butuh simbol spesifik.
2. Kenapa `if __name__ == "__main__":` penting?
   Jawaban singkat: agar file bisa berfungsi ganda sebagai module dan script eksekusi langsung.
3. Kenapa import saya gagal padahal file ada?
   Jawaban singkat: biasanya karena struktur folder/path atau nama modul bentrok.

## Referensi

- Python Tutorial (Modules): https://docs.python.org/3/tutorial/modules.html
- Python Reference (import statement): https://docs.python.org/3/reference/simple_stmts.html#import
- Python Standard Library (Modules): https://docs.python.org/3/library/modules.html

