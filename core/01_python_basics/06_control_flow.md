# Control Flow

Chapter Code: CORE-01-06
Book Code: CORE-01
Version: v0.2.6
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 45 menit teori + 40 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas bagaimana Python menentukan jalur eksekusi program berdasarkan kondisi dan perulangan. Kamu akan mempelajari `if/elif/else`, `for`, `while`, serta kontrol tambahan seperti `break`, `continue`, dan `pass`.

## Prasyarat Spesifik Bab

- memahami `02_python_syntax.md`
- memahami `04_basic_data_types.md`
- memahami `05_operators_and_expressions.md`

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| branching | percabangan alur berdasarkan kondisi | `if score >= 75:` |
| loop | perulangan eksekusi blok kode | `for x in items:` |
| iterator | objek yang menghasilkan item satu per satu | hasil `range(5)` |
| break | menghentikan loop lebih awal | `if done: break` |
| continue | loncat ke iterasi berikutnya | `if skip: continue` |

## Tujuan Besar

Membekali pembaca kemampuan mengendalikan alur program sehingga program dapat merespons kondisi data secara dinamis.

## Tujuan Kecil

- menulis percabangan dengan kondisi yang jelas
- memilih loop yang tepat (`for` vs `while`)
- menggunakan `break` dan `continue` dengan benar
- menghindari infinite loop sederhana

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- perlu keputusan berbasis kondisi
- perlu memproses data berulang
- perlu menghentikan proses berdasarkan syarat tertentu

## Bukan Peruntukan

Bab ini bukan untuk:

- optimasi algoritma kompleks
- pembahasan async flow atau concurrency

## Analogi

Control flow seperti navigasi di persimpangan jalan: kondisi menentukan belok kiri/kanan, loop seperti memutar rute sampai tujuan tercapai.

## Miskonsepsi Umum

- Miskonsepsi: `for` selalu lebih baik dari `while`.
  Klarifikasi: pilih berdasarkan kebutuhan; `for` untuk iterasi koleksi, `while` untuk kondisi dinamis.

- Miskonsepsi: `break` dan `continue` membuat kode selalu buruk.
  Klarifikasi: keduanya valid jika dipakai terukur dan meningkatkan kejelasan alur.

## Konsep Inti

### 1. Percabangan dengan `if/elif/else`

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"

print(grade)
```

### 2. Perulangan dengan `for`

```python
names = ["Ayu", "Budi", "Cici"]
for name in names:
    print(f"Halo, {name}")
```

`for` cocok untuk mengiterasi list, tuple, dict, string, atau `range()`.

### 3. Perulangan dengan `while`

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

Pastikan kondisi berhenti jelas agar tidak infinite loop.

### 4. `break`, `continue`, dan `pass`

```python
for n in range(1, 6):
    if n == 2:
        continue
    if n == 5:
        break
    print(n)
```

- `continue`: lewati iterasi saat ini
- `break`: keluar dari loop
- `pass`: placeholder blok kosong sementara

## Diagram

![Big picture Control Flow](assets/06_control_flow.svg)

Caption: Diagram menggambarkan alur keputusan (branching) dan perulangan (loop) hingga program mencapai kondisi selesai.

### Legenda Diagram

- kotak biru: kondisi atau aksi
- panah: arah alur eksekusi
- kotak hijau: output/akhir proses

## Contoh Kode (Benar)

```python
numbers = [1, 2, 3, 4, 5]
even_total = 0

for n in numbers:
    if n % 2 == 0:
        even_total += n

print(even_total)
```

Expected output:

```text
6
```

## Pitfall Umum

Infinite loop karena lupa update kondisi:

```python
x = 1
while x <= 3:
    print(x)
```

Perbaikan:

```python
x = 1
while x <= 3:
    print(x)
    x += 1
```

Pitfall percabangan bertumpuk tak jelas:

```python
if a > 0:
    if a > 10:
        print("besar")
```

Perbaikan (lebih jelas):

```python
if a > 10:
    print("besar")
elif a > 0:
    print("positif")
```

## Catatan Praktis

- tulis kondisi yang eksplisit dan mudah dibaca
- hindari nesting terlalu dalam; pecah ke fungsi jika perlu
- gunakan guard clause saat memungkinkan

## Latihan

### Dasar

Buat percabangan yang menentukan kategori umur (`anak`, `remaja`, `dewasa`).

### Menengah

Gunakan `for` untuk menghitung total nilai dari list angka.

### Mini Challenge

Buat program menu sederhana menggunakan `while` yang berjalan sampai user memilih keluar.

## Checklist Lulus Bab

- [ ] menulis `if/elif/else` dengan benar
- [ ] membedakan penggunaan `for` dan `while`
- [ ] menggunakan `break`/`continue` secara tepat
- [ ] menghindari infinite loop dasar

## Peta Keterkaitan

- Bab sebelumnya: `05_operators_and_expressions.md`
- Bab berikutnya: `07_functions.md`
- Keterkaitan lintas buku Core: `CORE-03` (Execution Model)

## Ringkasan

- Control flow mengatur urutan eksekusi berdasarkan kondisi dan iterasi.
- `if/elif/else` untuk keputusan, `for`/`while` untuk pengulangan.
- Kejelasan kondisi dan titik berhenti loop adalah kunci kode yang aman.

## FAQ Singkat

1. Kapan pakai `for` dan kapan `while`?
   Jawaban singkat: `for` saat jumlah iterasi berbasis koleksi/range, `while` saat berbasis kondisi.
2. Apakah `break` itu jelek?
   Jawaban singkat: tidak, selama dipakai untuk menyederhanakan alur secara jelas.
3. Kenapa loop saya tidak berhenti?
   Jawaban singkat: biasanya kondisi berhenti tidak pernah menjadi `False`.

## Referensi

- Python Tutorial (More Control Flow Tools): https://docs.python.org/3/tutorial/controlflow.html
- Python Language Reference (`if`, `while`, `for`): https://docs.python.org/3/reference/compound_stmts.html
- Built-in `range()`: https://docs.python.org/3/library/stdtypes.html#ranges

