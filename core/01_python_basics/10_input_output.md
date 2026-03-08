# Input and Output

Chapter Code: CORE-01-10
Book Code: CORE-01
Version: v0.3.0
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 45 menit teori + 40 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas mekanisme input dan output dasar pada program Python berbasis command line. Kamu akan belajar menerima data dari pengguna, mengubah tipe input, memformat output, dan melakukan validasi sederhana agar program lebih aman dipakai.

## Prasyarat Spesifik Bab

- memahami `04_basic_data_types.md`
- memahami `05_operators_and_expressions.md`
- memahami `06_control_flow.md`

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| input | data masuk dari pengguna | `input("Nama: ")` |
| output | data keluar ke layar/file | `print("Halo")` |
| prompt | pesan sebelum input diisi | `"Masukkan umur: "` |
| parsing | konversi string ke tipe lain | `int(raw_age)` |
| formatting | pengaturan tampilan output | `f"Umur: {age}"` |
| validation | pengecekan data input | `if age >= 0` |

## Tujuan Besar

Membantu pembaca membangun interaksi pengguna dasar yang benar, jelas, dan tahan terhadap input tidak valid.

## Tujuan Kecil

- menggunakan `input()` dan `print()` secara efektif
- memahami bahwa hasil `input()` selalu string
- melakukan parsing ke `int`/`float` dengan aman
- memformat output agar informatif
- menulis validasi input sederhana

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- membuat program interaktif di terminal
- menerima data pengguna untuk diproses
- menampilkan hasil proses secara rapi

## Bukan Peruntukan

Bab ini bukan untuk:

- antarmuka GUI/web
- serialisasi data kompleks atau protocol IO lanjutan

## Analogi

Input/output seperti percakapan dua arah: program bertanya (prompt), pengguna menjawab (input), program merespons (output).

## Miskonsepsi Umum

- Miskonsepsi: `input()` langsung menghasilkan angka jika user mengetik angka.
  Klarifikasi: `input()` selalu menghasilkan string; perlu konversi.

- Miskonsepsi: validasi input tidak penting untuk program kecil.
  Klarifikasi: tanpa validasi, program mudah error pada input tak terduga.

## Konsep Inti

### 1. Input Dasar dengan `input()`

```python
name = input("Masukkan nama: ")
print("Halo,", name)
```

### 2. Parsing Tipe Data

```python
raw_age = input("Masukkan umur: ")
age = int(raw_age)
print(f"Tahun depan umurmu: {age + 1}")
```

Untuk angka pecahan gunakan `float()`.

### 3. Formatting Output

```python
name = "Ayu"
score = 88.5

print(f"Nama: {name} | Nilai: {score:.1f}")
```

### 4. Validasi Input Sederhana

```python
raw = input("Masukkan jumlah item: ")
if raw.isdigit():
    qty = int(raw)
    print(f"Jumlah valid: {qty}")
else:
    print("Input harus berupa angka bulat non-negatif")
```

## Diagram

![Big picture Input and Output](assets/10_input_output.svg)

Caption: Diagram memperlihatkan alur prompt -> input pengguna -> parsing/validasi -> output hasil.

### Legenda Diagram

- kotak biru: sumber input
- kotak tengah: proses validasi/parsing
- kotak hijau: output valid atau pesan error

## Contoh Kode (Benar)

```python
name = input("Nama: ")
raw_price = input("Harga: ")
raw_qty = input("Jumlah: ")

if raw_price.replace('.', '', 1).isdigit() and raw_qty.isdigit():
    price = float(raw_price)
    qty = int(raw_qty)
    total = price * qty
    print(f"{name}, total belanja kamu: Rp {total:,.2f}")
else:
    print("Input harga/jumlah tidak valid")
```

Expected output (contoh):

```text
Ayu, total belanja kamu: Rp 150,000.00
```

## Pitfall Umum

Lupa parsing input angka:

```python
a = input("A: ")
b = input("B: ")
print(a + b)
```

Perbaikan:

```python
a = int(input("A: "))
b = int(input("B: "))
print(a + b)
```

Parsing langsung tanpa penanganan:

```python
age = int(input("Umur: "))
```

Perbaikan (defensif):

```python
raw = input("Umur: ")
if raw.isdigit():
    age = int(raw)
    print(age)
else:
    print("Umur harus angka")
```

## Catatan Praktis

- selalu anggap input pengguna bisa salah
- gunakan prompt yang jelas dan spesifik
- pisahkan proses: ambil input -> validasi -> konversi -> proses -> output
- gunakan f-string untuk output agar lebih terbaca

## Latihan

### Dasar

Buat program yang meminta nama dan kota, lalu tampilkan kalimat sapaan.

### Menengah

Buat kalkulator BMI sederhana dari input tinggi dan berat.

### Mini Challenge

Buat program kasir mini: input beberapa item (nama, harga, qty), hitung subtotal, dan tampilkan ringkasan transaksi dengan format rapi.

## Checklist Lulus Bab

- [ ] memahami alur input -> validasi -> output
- [ ] bisa parsing string ke int/float dengan aman
- [ ] bisa memformat output dengan f-string
- [ ] menyelesaikan mini challenge

## Peta Keterkaitan

- Bab sebelumnya: `09_modules_and_import.md`
- Bab berikutnya: `11_file_handling.md`
- Keterkaitan lintas buku Core: `CORE-08` (File System and IO)

## Ringkasan

- `input()` mengembalikan string, sehingga parsing sering diperlukan.
- Output yang baik membantu pengguna memahami hasil proses.
- Validasi input adalah langkah wajib untuk mencegah error runtime sederhana.

## FAQ Singkat

1. Kenapa angka dari input tidak bisa langsung dihitung?
   Jawaban singkat: karena input berupa string, harus dikonversi dulu ke angka.
2. Lebih baik validasi sebelum atau sesudah parsing?
   Jawaban singkat: validasi format dasar dulu, lalu parsing.
3. Kapan perlu pakai `try/except` untuk input?
   Jawaban singkat: saat validasi string saja tidak cukup dan konversi bisa gagal.

## Referensi

- Python Built-in Functions (`input`, `print`): https://docs.python.org/3/library/functions.html
- Python Tutorial (Input and Output): https://docs.python.org/3/tutorial/inputoutput.html
- Python String Format Spec: https://docs.python.org/3/library/string.html#format-specification-mini-language

