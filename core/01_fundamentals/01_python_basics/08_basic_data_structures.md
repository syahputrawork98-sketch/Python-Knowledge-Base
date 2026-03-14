# Basic Data Structures

Chapter Code: CORE-01-08
Book Code: CORE-01
Version: v0.2.8
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 50 menit teori + 45 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas struktur data bawaan Python yang paling sering dipakai: `list`, `tuple`, `set`, dan `dict`. Kamu akan belajar kapan masing-masing struktur digunakan, operasi dasar yang umum, serta kesalahan praktis yang sering terjadi.

## Prasyarat Spesifik Bab

- memahami `04_basic_data_types.md`
- memahami `05_operators_and_expressions.md`
- memahami `07_functions.md`

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| list | koleksi berurutan dan mutable | `[1, 2, 3]` |
| tuple | koleksi berurutan dan immutable | `(1, 2, 3)` |
| set | koleksi tanpa urutan, unik | `{1, 2, 3}` |
| dict | pasangan key-value | `{"name": "Ayu"}` |
| indexing | akses elemen berdasarkan posisi | `items[0]` |
| slicing | ambil sebagian data berurutan | `items[1:4]` |

## Tujuan Besar

Membekali pembaca kemampuan memilih struktur data yang tepat untuk penyimpanan dan pemrosesan data sehari-hari dalam Python.

## Tujuan Kecil

- membedakan karakteristik list, tuple, set, dan dict
- melakukan operasi dasar tambah/ubah/hapus data
- melakukan iterasi pada struktur data
- memilih struktur data sesuai kebutuhan kasus

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- mengelola sekumpulan data dalam program
- memproses data berulang dengan loop
- membangun representasi data sederhana (profil, daftar tugas, dsb.)

## Bukan Peruntukan

Bab ini bukan untuk:

- struktur data custom kompleks
- optimasi algoritma tingkat lanjut

## Analogi

Struktur data seperti jenis lemari penyimpanan: list itu rak fleksibel, tuple itu kotak segel, set itu daftar unik tanpa duplikasi, dict itu map label-ke-nilai.

## Miskonsepsi Umum

- Miskonsepsi: set mempertahankan urutan seperti list.
  Klarifikasi: set fokus pada keunikan elemen, bukan urutan indeks.

- Miskonsepsi: tuple dan list sama saja.
  Klarifikasi: tuple immutable, list mutable.

## Konsep Inti

### 1. List dan Tuple

```python
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits[0])
print(fruits[1:3])

point = (10, 20)
print(point[0])
```

`list` cocok untuk data yang sering berubah, `tuple` untuk data tetap.

### 2. Set

```python
tags = {"python", "api", "python", "backend"}
print(tags)

tags.add("learning")
print("api" in tags)
```

Set otomatis menghapus duplikasi.

### 3. Dictionary

```python
user = {
    "name": "Ayu",
    "age": 21,
    "active": True,
}

print(user["name"])
user["city"] = "Bandung"
print(user)
```

Dict cocok untuk data terstruktur berbasis key-value.

### 4. Iterasi Dasar

```python
numbers = [1, 2, 3]
for n in numbers:
    print(n)

for key, value in user.items():
    print(key, value)
```

## Diagram

![Big picture Basic Data Structures](assets/08_basic_data_structures.svg)

Caption: Diagram memperlihatkan perbedaan peran list, tuple, set, dan dict dalam penyimpanan data.

### Legenda Diagram

- kotak biru: jenis struktur data
- kotak tengah: operasi umum
- kotak hijau: hasil penggunaan

## Contoh Kode (Benar)

```python
tasks = ["belajar", "latihan", "review"]
profile = {"name": "Raka", "level": "beginner"}

for task in tasks:
    print(task)

print(profile["name"])
```

Expected output:

```text
belajar
latihan
review
Raka
```

## Pitfall Umum

Akses key dict yang tidak ada:

```python
user = {"name": "Ayu"}
print(user["age"])
```

Perbaikan:

```python
user = {"name": "Ayu"}
print(user.get("age", "unknown"))
```

Mengubah tuple secara langsung:

```python
point = (1, 2)
point[0] = 10
```

Perbaikan:

```python
point = (1, 2)
point = (10, point[1])
print(point)
```

## Catatan Praktis

- gunakan list saat data perlu update dinamis
- gunakan tuple untuk data yang seharusnya tetap
- gunakan set untuk cek keunikan/membership cepat
- gunakan dict untuk data berlabel jelas

## Latihan

### Dasar

Buat list berisi 5 nama, lalu tampilkan nama pertama dan terakhir.

### Menengah

Buat dict profil pengguna (`name`, `age`, `city`) dan cetak semua key-value.

### Mini Challenge

Buat aplikasi mini todo list sederhana dengan list dan dict (tiap task punya `title` dan `done`).

## Checklist Lulus Bab

- [ ] memahami perbedaan list, tuple, set, dict
- [ ] bisa melakukan operasi dasar setiap struktur
- [ ] bisa iterasi data dengan loop
- [ ] menyelesaikan mini challenge

## Peta Keterkaitan

- Bab sebelumnya: `07_functions.md`
- Bab berikutnya: `09_modules_and_import.md`
- Keterkaitan lintas buku Core: `CORE-06` (Modules and Import System)

## Ringkasan

- Python menyediakan struktur data dasar dengan karakteristik berbeda.
- Pemilihan struktur data yang tepat memengaruhi kejelasan dan keandalan kode.
- List/dict paling umum, tetapi tuple/set sangat penting pada konteks tertentu.

## FAQ Singkat

1. Kapan pilih list vs tuple?
   Jawaban singkat: list untuk data mutable, tuple untuk data tetap.
2. Kapan pakai set?
   Jawaban singkat: saat butuh data unik dan cek membership cepat.
3. Kenapa dict sangat sering dipakai?
   Jawaban singkat: karena representasi key-value cocok untuk banyak data dunia nyata.

## Referensi

- Python Tutorial (Data Structures): https://docs.python.org/3/tutorial/datastructures.html
- Python Standard Types: https://docs.python.org/3/library/stdtypes.html
- Python `dict` docs: https://docs.python.org/3/library/stdtypes.html#dict

