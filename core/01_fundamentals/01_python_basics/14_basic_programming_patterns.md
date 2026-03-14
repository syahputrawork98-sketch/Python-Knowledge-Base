# Basic Programming Patterns

Chapter Code: CORE-01-14
Book Code: CORE-01
Version: v0.3.4
Last Updated: 2026-03-08
Status: In Progress
Difficulty: Basic
Estimated Time: 55 menit teori + 50 menit praktik

## Bab Ini Tentang Apa

Bab ini merangkum pola pemrograman dasar yang sering muncul dalam proyek Python pemula: input-process-output, validasi, transformasi data, pemisahan fungsi, dan alur program sederhana. Tujuannya agar pembaca bisa menggabungkan seluruh materi bab 01-13 menjadi solusi utuh.

## Prasyarat Spesifik Bab

- memahami bab 01 sampai 13
- mampu membuat fungsi dasar dan loop
- memahami I/O serta exception handling dasar

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| IPO pattern | Input -> Process -> Output | kasir sederhana |
| guard clause | validasi awal untuk keluar cepat | `if not data: return` |
| accumulator | variabel penampung hasil bertahap | `total += value` |
| normalize | menyeragamkan bentuk data input | `strip().lower()` |
| refactor | perbaikan struktur tanpa ubah perilaku | pecah fungsi panjang |

## Tujuan Besar

Membantu pembaca menyusun program kecil end-to-end dengan pola yang rapi, mudah dibaca, dan mudah dirawat.

## Tujuan Kecil

- mengidentifikasi pola dasar dalam problem sederhana
- menggabungkan fungsi, kontrol alur, dan struktur data
- menambah validasi dan handling error dasar
- memecah kode ke bagian modular

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan konsep inti bab dengan kata-kata sendiri
- menjalankan contoh utama tanpa error
- menerapkan konsep bab pada latihan dasar

## Peruntukan
Bab ini digunakan saat:

- membangun mini project CLI
- merapikan kode latihan menjadi struktur lebih baik
- menyiapkan fondasi sebelum masuk topik lanjutan

## Bukan Peruntukan

Bab ini bukan untuk:

- arsitektur software skala besar
- design pattern OOP lanjutan

## Analogi

Pola pemrograman seperti template kerja dapur profesional: urutan langkah konsisten membuat hasil lebih cepat, minim salah, dan mudah direplikasi.

## Miskonsepsi Umum

- Miskonsepsi: pola berarti kode harus kaku dan sama terus.
  Klarifikasi: pola adalah panduan fleksibel, bukan aturan kaku.

- Miskonsepsi: refactor bisa ditunda terus.
  Klarifikasi: refactor ringan sejak awal mengurangi technical debt.

## Konsep Inti

### 1. Pola IPO (Input-Process-Output)

```python
def calculate_total(price, qty):
    return price * qty

price = float(input("Harga: "))
qty = int(input("Qty: "))
print(calculate_total(price, qty))
```

### 2. Validasi + Guard Clause

```python
def set_discount(value):
    if value < 0 or value > 100:
        return "Diskon tidak valid"
    return f"Diskon {value}%"
```

### 3. Pola Accumulator

```python
nums = [2, 4, 6]
total = 0
for n in nums:
    total += n
print(total)
```

### 4. Pola Transformasi Koleksi

```python
raw_names = ["  ayu", "BUDI  ", "cici"]
clean_names = [n.strip().title() for n in raw_names]
print(clean_names)
```

### 5. Refactor ke Fungsi Kecil

```python
def get_input():
    return input("Nama: ").strip()

def greet(name):
    return f"Halo, {name}!"

name = get_input()
print(greet(name))
```

## Diagram

![Big picture Basic Programming Patterns](assets/14_basic_programming_patterns.svg)

Caption: Diagram memperlihatkan kombinasi pola dasar dari input hingga output terstruktur.

### Legenda Diagram

- kotak biru: tahap/pola
- panah: urutan eksekusi
- kotak hijau: hasil akhir program

## Contoh Kode (Benar)

```python
def parse_score(raw):
    if not raw.isdigit():
        raise ValueError("Nilai harus angka")
    score = int(raw)
    if score < 0 or score > 100:
        raise ValueError("Nilai harus 0-100")
    return score

def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    return "C"

raw = input("Masukkan nilai: ")
try:
    score = parse_score(raw)
    print("Grade:", get_grade(score))
except ValueError as e:
    print("Error:", e)
```

Expected output (contoh):

```text
Grade: B
```

## Pitfall Umum

Semua logika dicampur di satu fungsi panjang.

Perbaikan: pecah ke fungsi kecil per tanggung jawab (`parse`, `validate`, `process`, `render`).

Tidak ada validasi sebelum proses utama.

Perbaikan: taruh validasi awal (guard clause) untuk gagal cepat.

## Catatan Praktis

- gunakan nama fungsi yang mencerminkan aksi
- jaga fungsi tetap pendek dan fokus
- tambahkan validasi di pintu masuk data
- cek hasil dengan test manual sederhana per fungsi

## Latihan

### Dasar

Buat program yang menerima 3 angka dan menampilkan total serta rata-rata dengan pola IPO.

### Menengah

Refactor program kalkulator sederhana agar tiap operasi berada di fungsi terpisah.

### Mini Challenge

Bangun mini aplikasi CLI "Student Score Tracker" dengan fitur:
- input data nilai siswa
- validasi nilai
- hitung statistik (rata-rata, min, max)
- tampilkan ringkasan rapi

## Checklist Lulus Bab

- [ ] memahami pola IPO, guard clause, accumulator
- [ ] mampu memecah kode ke fungsi kecil
- [ ] menambahkan validasi dan handling error dasar
- [ ] menyelesaikan mini challenge end-to-end

## Peta Keterkaitan

- Bab sebelumnya: `13_builtin_functions.md`
- Bab berikutnya: tidak ada (penutup buku)
- Keterkaitan lintas buku Core: `CORE-12` (Testing) dan `CORE-15` (Tooling)

## Ringkasan

- Pola dasar membantu menyusun kode yang konsisten dan mudah dirawat.
- Menggabungkan konsep dari bab sebelumnya membuat program lebih utuh.
- Kebiasaan refactor ringan sejak awal mempercepat perkembangan jangka panjang.

## FAQ Singkat

1. Harus selalu pakai semua pola di setiap program?
   Jawaban singkat: tidak, pilih pola yang relevan dengan kompleksitas masalah.
2. Kapan program perlu di-refactor?
   Jawaban singkat: saat mulai sulit dibaca, diuji, atau ditambah fitur.
3. Kenapa bab ini di akhir buku?
   Jawaban singkat: karena bab ini menggabungkan seluruh fondasi bab sebelumnya.

## Referensi

Catatan referensi non-resmi: sumber Real Python digunakan sebagai materi pelengkap praktik refactoring, bukan sumber normatif utama bahasa Python.
- Python Tutorial: https://docs.python.org/3/tutorial/
- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
- Real Python (Refactoring basics, supplementary): https://realpython.com/python-refactoring/

