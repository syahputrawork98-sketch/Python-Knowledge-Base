# File Handling

Chapter Code: CORE-01-11
Book Code: CORE-01
Version: v0.3.4
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 50 menit teori + 45 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas cara membaca, menulis, dan mengelola file di Python secara aman. Kamu akan belajar mode file, context manager (`with`), encoding, path dasar, serta pola penanganan error sederhana saat bekerja dengan file.

## Prasyarat Spesifik Bab

- memahami `09_modules_and_import.md`
- memahami `10_input_output.md`
- memahami konsep validasi input dasar

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| file mode | cara membuka file | `'r'`, `'w'`, `'a'` |
| context manager | manajemen resource otomatis | `with open(...) as f:` |
| encoding | standar representasi karakter | `encoding='utf-8'` |
| path | alamat file/folder | `data/users.txt` |
| buffer | penyangga I/O sementara | default `open()` |

## Tujuan Besar

Membantu pembaca memproses data berbasis file secara aman, terstruktur, dan minim kebocoran resource.

## Tujuan Kecil

- membuka file dengan mode yang tepat
- membaca dan menulis isi file teks
- memahami kapan pakai `with`
- menangani error file umum
- menggunakan path relatif sederhana

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- menyimpan hasil program ke file
- membaca data dari file teks
- membuat log sederhana berbasis file

## Bukan Peruntukan

Bab ini bukan untuk:

- database management
- file format kompleks tingkat lanjut

## Analogi

File handling seperti meminjam buku perpustakaan: buka buku, baca/tulis seperlunya, lalu tutup dengan benar agar tidak rusak/terkunci.

## Miskonsepsi Umum

- Miskonsepsi: file otomatis tertutup setelah dipakai.
  Klarifikasi: file bisa tetap terbuka jika tidak ditutup dengan benar.

- Miskonsepsi: mode `'w'` menambah isi di akhir.
  Klarifikasi: `'w'` menimpa isi file, untuk menambah gunakan `'a'`.

## Konsep Inti

### 1. Membuka dan Membaca File

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
```

### 2. Menulis dan Menambah File

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Baris pertama\n")

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Baris tambahan\n")
```

### 3. Membaca per Baris

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### 4. Penanganan Error Dasar

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File tidak ditemukan")
```

## Diagram

![Big picture File Handling](assets/11_file_handling.svg)

Caption: Diagram menunjukkan alur open -> read/write -> close saat bekerja dengan file.

### Legenda Diagram

- kotak biru: sumber file/path
- kotak tengah: operasi I/O
- kotak hijau: output data

## Contoh Kode (Benar)

```python
items = ["apel", "jeruk", "mangga"]

with open("items.txt", "w", encoding="utf-8") as f:
    for item in items:
        f.write(item + "\n")

with open("items.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Expected output:

```text
apel
jeruk
mangga
```

## Pitfall Umum

Lupa encoding saat file berisi karakter non-ASCII:

```python
with open("data.txt", "r") as f:
    print(f.read())
```

Perbaikan:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Menimpa file tanpa sadar:

```python
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("new")
```

Perbaikan: gunakan `'a'` jika ingin menambahkan.

## Catatan Praktis

- default ke `with open(...)` untuk keamanan resource
- selalu tentukan `encoding="utf-8"` untuk teks
- pahami beda mode `'w'` vs `'a'`
- simpan path relatif konsisten terhadap root project

## Latihan

### Dasar

Buat file `bio.txt`, tulis 3 baris data diri, lalu baca kembali.

### Menengah

Buat program yang menyalin isi file A ke file B.

### Mini Challenge

Buat simple notes app CLI: tambah catatan dan tampilkan semua catatan dari file.

## Checklist Lulus Bab

- [ ] memahami mode file utama (`r`, `w`, `a`)
- [ ] bisa membaca dan menulis file teks
- [ ] menggunakan `with` secara konsisten
- [ ] menangani `FileNotFoundError` dasar

## Peta Keterkaitan

- Bab sebelumnya: `10_input_output.md`
- Bab berikutnya: `12_errors_and_exceptions.md`
- Keterkaitan lintas buku Core: `CORE-08` (File System and IO)

## Ringkasan

- File handling memungkinkan data program disimpan permanen.
- `with open(...)` adalah pola aman dan direkomendasikan.
- Mode file dan encoding yang tepat mencegah banyak bug I/O.

## FAQ Singkat

1. Kapan pakai `'w'` dan kapan `'a'`?
   Jawaban singkat: `'w'` menimpa, `'a'` menambahkan.
2. Kenapa file harus ditutup?
   Jawaban singkat: agar resource dilepas dan data flush dengan benar.
3. Kenapa perlu `encoding='utf-8'`?
   Jawaban singkat: untuk konsistensi pembacaan/penulisan karakter modern.

## Referensi

- Python Tutorial (Reading and Writing Files): https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- Python `open()` docs: https://docs.python.org/3/library/functions.html#open
- `pathlib` docs: https://docs.python.org/3/library/pathlib.html

