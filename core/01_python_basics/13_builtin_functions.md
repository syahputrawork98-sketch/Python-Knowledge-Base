# Built-in Functions

Chapter Code: CORE-01-13
Book Code: CORE-01
Version: v0.3.4
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 45 menit teori + 40 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas fungsi bawaan (built-in functions) Python yang paling sering dipakai dalam praktik sehari-hari. Fokusnya pada fungsi untuk konversi data, iterasi, agregasi, inspeksi tipe, dan utilitas dasar agar kode lebih ringkas.

## Prasyarat Spesifik Bab

- memahami `04_basic_data_types.md`
- memahami `07_functions.md`
- memahami `08_basic_data_structures.md`

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| built-in function | fungsi tersedia tanpa import | `len()`, `sum()` |
| iterable | objek yang bisa diiterasi | list, tuple, range |
| callable | objek yang bisa dipanggil seperti fungsi | `print`, custom function |
| predicate | fungsi yang menghasilkan bool | `lambda x: x > 0` |
| casting function | fungsi konversi tipe | `int()`, `str()` |

## Tujuan Besar

Membantu pembaca menggunakan built-in functions secara efektif untuk menulis kode yang lebih sederhana dan idiomatik.

## Tujuan Kecil

- mengenali built-in yang sering dipakai
- memilih fungsi bawaan yang sesuai kasus
- menghindari penamaan variabel yang menimpa built-in
- memakai built-in untuk validasi dan transformasi data sederhana

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- ingin mengurangi kode manual berulang
- butuh operasi cepat pada list/dict/string
- ingin menulis kode Python yang lebih idiomatik

## Bukan Peruntukan

Bab ini bukan untuk:

- pembahasan semua built-in secara exhaustif
- metaprogramming built-in tingkat lanjut

## Analogi

Built-in functions seperti toolkit bawaan di mobil: tidak perlu bawa alat eksternal untuk kebutuhan dasar yang sering muncul.

## Miskonsepsi Umum

- Miskonsepsi: semakin banyak built-in dipakai, kode makin sulit dibaca.
  Klarifikasi: jika dipilih tepat, built-in justru memperjelas intent.

- Miskonsepsi: menamai variabel dengan nama built-in aman.
  Klarifikasi: menimpa nama built-in (`list`, `sum`) bisa bikin bug membingungkan.

## Konsep Inti

### 1. Built-in Konversi dan Inspeksi

```python
raw = "123"
num = int(raw)
text = str(num)

print(type(num))
print(isinstance(num, int))
```

### 2. Built-in Agregasi

```python
scores = [80, 90, 75]
print(len(scores))
print(sum(scores))
print(min(scores), max(scores))
```

### 3. Built-in Iterasi

```python
names = ["Ayu", "Budi", "Cici"]
for i, name in enumerate(names, start=1):
    print(i, name)

ages = [20, 21, 22]
for name, age in zip(names, ages):
    print(name, age)
```

### 4. Built-in Transformasi

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
evans = list(filter(lambda x: x % 2 == 0, numbers))
print(squared, evans)
```

## Diagram

![Big picture Built-in Functions](assets/13_builtin_functions.svg)

Caption: Diagram menunjukkan kategori built-in utama dan alur penggunaannya dalam pemrosesan data.

### Legenda Diagram

- kotak biru: kategori fungsi bawaan
- kotak tengah: input data
- kotak hijau: hasil transformasi/agregasi

## Contoh Kode (Benar)

```python
prices = [12000, 15000, 10000]
qty = [2, 1, 3]

subtotals = [p * q for p, q in zip(prices, qty)]
print("Subtotals:", subtotals)
print("Total:", sum(subtotals))
```

Expected output:

```text
Subtotals: [24000, 15000, 30000]
Total: 69000
```

## Pitfall Umum

Menimpa nama built-in:

```python
list = [1, 2, 3]
print(list("abc"))
```

Perbaikan:

```python
numbers = [1, 2, 3]
print(list("abc"))
```

Menggunakan `map/filter` berlebihan saat list comprehension lebih jelas.

## Catatan Praktis

- prioritaskan built-in sebelum membuat helper function baru
- jangan gunakan nama variabel yang sama dengan built-in
- pakai list comprehension saat lebih terbaca daripada `map/filter`

## Latihan

### Dasar

Gunakan `len`, `sum`, `min`, `max` pada list angka buatanmu.

### Menengah

Gunakan `enumerate` untuk menampilkan daftar menu bernomor.

### Mini Challenge

Buat program ringkasan nilai siswa: hitung rata-rata, nilai tertinggi, nilai terendah, dan status lulus berdasarkan threshold tertentu.

## Checklist Lulus Bab

- [ ] mengenali built-in utama untuk kasus dasar
- [ ] bisa memilih built-in sesuai kebutuhan
- [ ] menghindari shadowing nama built-in
- [ ] menyelesaikan mini challenge

## Peta Keterkaitan

- Bab sebelumnya: `12_errors_and_exceptions.md`
- Bab berikutnya: `14_basic_programming_patterns.md`
- Keterkaitan lintas buku Core: `CORE-07` (Standard Library)

## Ringkasan

- Built-in functions mempercepat pekerjaan umum tanpa import tambahan.
- Pemakaian yang tepat membuat kode lebih ringkas dan ekspresif.
- Hindari menimpa nama built-in untuk menjaga kejelasan kode.

## FAQ Singkat

1. Kapan pakai `map/filter` vs list comprehension?
   Jawaban singkat: pakai yang paling jelas dibaca; seringnya list comprehension lebih eksplisit.
2. Apakah semua built-in harus dihafal?
   Jawaban singkat: tidak, kuasai yang paling sering dipakai dulu.
3. Kenapa `type()` dan `isinstance()` keduanya ada?
   Jawaban singkat: `isinstance()` lebih fleksibel untuk hierarchy class.

## Referensi

- Built-in Functions: https://docs.python.org/3/library/functions.html
- Python Tutorial (Data Structures): https://docs.python.org/3/tutorial/datastructures.html
- Functional Programming HOWTO: https://docs.python.org/3/howto/functional.html

