# Errors and Exceptions

Chapter Code: CORE-01-12
Book Code: CORE-01
Version: v0.3.4
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 50 menit teori + 45 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas cara Python menangani kesalahan melalui exceptions. Kamu akan belajar membedakan syntax error vs runtime exception, memakai `try/except`, `else`, `finally`, serta membuat exception handling yang tepat tanpa menutupi bug.

## Prasyarat Spesifik Bab

- memahami `06_control_flow.md`
- memahami `10_input_output.md`
- memahami `11_file_handling.md`

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| exception | kondisi error saat runtime | `ValueError` |
| traceback | jejak call stack saat error | output error Python |
| try block | blok kode yang dipantau error | `try: ...` |
| except block | penanganan error tertentu | `except ValueError:` |
| finally | blok yang selalu dijalankan | `finally: cleanup()` |
| raise | melempar exception manual | `raise ValueError(...)` |

## Tujuan Besar

Membantu pembaca menulis program yang tahan error dan memberikan respon kegagalan yang jelas.

## Tujuan Kecil

- membaca traceback dasar
- menangani exception spesifik
- menggunakan `else/finally` sesuai kebutuhan
- menghindari `except:` yang terlalu umum
- melempar exception dengan pesan jelas

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- program berinteraksi dengan input pengguna
- program membaca file/network/resource eksternal
- ingin menjaga aplikasi tetap stabil saat error terjadi

## Bukan Peruntukan

Bab ini bukan untuk:

- logging framework lanjutan
- error recovery arsitektur distributed system

## Analogi

Exception handling seperti prosedur darurat: bukan mencegah semua masalah, tapi memastikan saat masalah terjadi, responsnya tertib dan aman.

## Miskonsepsi Umum

- Miskonsepsi: menangkap semua error dengan `except:` adalah solusi terbaik.
  Klarifikasi: terlalu umum dan bisa menyembunyikan bug penting.

- Miskonsepsi: jika pakai `try/except`, program pasti aman.
  Klarifikasi: kualitas handling tergantung exception yang ditangkap dan aksi lanjutannya.

## Konsep Inti

### 1. Struktur `try/except`

```python
try:
    value = int(input("Masukkan angka: "))
    print(value * 2)
except ValueError:
    print("Input harus berupa angka")
```

### 2. `else` dan `finally`

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Pembagian dengan nol")
else:
    print("Hasil:", result)
finally:
    print("Selesai diproses")
```

### 3. Menangkap Beberapa Exception

```python
try:
    data = [1, 2, 3]
    idx = int(input("Index: "))
    print(data[idx])
except ValueError:
    print("Index harus angka")
except IndexError:
    print("Index di luar jangkauan")
```

### 4. `raise` untuk Validasi

```python
def set_age(age):
    if age < 0:
        raise ValueError("Umur tidak boleh negatif")
    return age
```

## Diagram

![Big picture Errors and Exceptions](assets/12_errors_and_exceptions.svg)

Caption: Diagram menunjukkan alur normal vs alur exception dan titik penanganannya.

### Legenda Diagram

- kotak biru: eksekusi normal
- kotak merah: exception muncul
- kotak hijau: handling dan recovery

## Contoh Kode (Benar)

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Tidak bisa membagi dengan nol"

print(divide(10, 2))
print(divide(10, 0))
```

Expected output:

```text
5.0
Tidak bisa membagi dengan nol
```

## Pitfall Umum

Menangkap semua exception tanpa konteks:

```python
try:
    risky()
except:
    print("error")
```

Perbaikan:

```python
try:
    risky()
except ValueError as e:
    print(f"ValueError: {e}")
```

Menelan error tanpa aksi lanjut:

```python
try:
    process()
except Exception:
    pass
```

Perbaikan: log/raise ulang jika perlu.

## Catatan Praktis

- tangkap exception sespesifik mungkin
- gunakan pesan error yang membantu pengguna
- jangan pakai `pass` kecuali ada alasan jelas
- gunakan `finally` untuk cleanup resource

## Latihan

### Dasar

Buat program konversi string ke int dengan handling `ValueError`.

### Menengah

Buat fungsi akses list by index dengan handling `IndexError`.

### Mini Challenge

Buat kalkulator sederhana yang tahan input tidak valid dan pembagian nol, lalu berikan pesan error ramah pengguna.

## Checklist Lulus Bab

- [ ] memahami perbedaan syntax error dan exception runtime
- [ ] mampu menulis `try/except` spesifik
- [ ] menggunakan `else/finally` dengan tepat
- [ ] mampu memakai `raise` untuk validasi

## Peta Keterkaitan

- Bab sebelumnya: `11_file_handling.md`
- Bab berikutnya: `13_builtin_functions.md`
- Keterkaitan lintas buku Core: `CORE-12` (Testing)

## Ringkasan

- Exception handling membuat program lebih robust saat menghadapi kondisi gagal.
- Tangkap exception yang tepat, berikan respon jelas, dan hindari menutupi bug.
- `try/except/else/finally` memberi kontrol lengkap pada alur error.

## FAQ Singkat

1. Kapan pakai `except Exception as e`?
   Jawaban singkat: saat butuh fallback umum, tapi tetap log dan evaluasi detail error.
2. Haruskah semua fungsi pakai `try/except`?
   Jawaban singkat: tidak, gunakan pada area yang memang rentan gagal.
3. Bedanya `raise` dan `print` error?
   Jawaban singkat: `raise` menghentikan alur dengan exception, `print` hanya menampilkan teks.

## Referensi

- Python Tutorial (Errors and Exceptions): https://docs.python.org/3/tutorial/errors.html
- Built-in Exceptions: https://docs.python.org/3/library/exceptions.html
- Exception hierarchy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

