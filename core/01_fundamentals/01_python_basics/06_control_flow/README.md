# Bab 06: Control Flow

Chapter Code: CORE-01-06
Version: Core.Fundamentals.01.01-draft
Last Updated: 2026-03-14
Status: Draft

> **Deskripsi Singkat**: Bab ini membahas jantung logika pemrograman: bagaimana Python membuat keputusan menggunakan percabangan (`if`) dan mengulang tugas menggunakan perulangan (`for`, `while`).

## 1. Analogi (Pendekatan Konsep)

### Analogi Singkat
> "Control Flow adalah **Papan Petunjuk Jalan** di dalam kode Anda. Ia menentukan apakah mobil (eksekusi program) harus belok kanan, kiri, atau berputar-putar di bundaran sampai bensin (kondisi) habis."

### Analogi Panjang / Cerita (Menavigasi Kota Python)
Bayangkan eksekusi program Anda adalah sebuah mobil yang melaju di jalan raya. Tanpa *Control Flow*, mobil hanya bisa lurus terus sampai menabrak dinding (ujung file).

- **`if`, `elif`, `else` (Persimpangan Tiket)**: Bayangkan ada gerbang tol. Petugas bertanya: "Jika (`if`) Anda punya Kartu VIP, silakan lewat jalur kanan. Atau jika (`elif`) Anda punya Kartu Member, lewat jalur tengah. Selain itu (`else`), lewatlah jalur kiri yang macet." Hanya satu jalur yang dipilih, dan mobil tidak bisa melewati dua jalur sekaligus.
- **`for` loop (Bus Wisata Halte)**: Ini adalah bus yang sudah punya daftar tujuan pasti di peta (List). Bus akan berhenti di Halte A, menurunkan penumpang, lalu otomatis maju ke Halte B, dan seterusnya. Bus akan berhenti dengan sendirinya jika daftar di peta sudah habis dikunjungi.
- **`while` loop (Bundaran Tanpa Ujung)**: Ini adalah mobil yang terjebak di **Bundaran (Roundabout)**. Mobil akan terus berputar-putar SELAMA lampu indikator di dashboard masih berwarna Hijau (`True`). Begitu lampu berubah Merah (`False`), mobil baru diperbolehkan keluar dari putaran. Bahayanya: jika lampu tidak pernah Merah, mobil akan berputar selamanya (*Infinite Loop*).
- **`break` & `continue` (Aksi Darurat)**:
    - **`break`**: "Hentikan mobil sekarang juga dan keluar dari jalan tol!" (Keluar paksa dari loop).
    - **`continue`**: "Lewati rest area ini, jangan berhenti, langsung gas ke halte berikutnya!" (Melewati sisa kode di loop saat ini dan lanjut ke iterasi selanjutnya).

## 2. Istilah Kunci (Key Terms)

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| Conditional | Pengecekan kondisi yang menghasilkan True atau False | `if x > 10:` |
| Iteration | Satu kali putaran atau satu langkah dalam perulangan | Putaran ke-1 dalam `for` |
| Iterable | Obyek yang bisa dijalani elemennya satu per satu | `list`, `string`, `range` |
| Infinite Loop | Perulangan yang tidak pernah berhenti karena kondisinya selalu True | `while True:` |
| Clause | Bagian atau blok dari sebuah pernyataan kontrol alur | Blok di bawah `else` |

## 3. Konsep Utama

### A. Percabangan Bertingkat (`if-elif-else`)
Python mengevaluasi kondisi dari atas ke bawah. Begitu satu kondisi `True`, blok di bawahnya dijalankan, dan Python mengabaikan sisa rantai `elif` atau `else` di bawahnya.

```python
skor = 85
if skor >= 90:
    print("Grade A")
elif skor >= 80:
    print("Grade B") # Ini yang dijalankan
else:
    print("Grade C")
```

### B. Perulangan `for` (Pasti & Terukur)
Gunakan `for` jika Anda tahu persis berapa banyak item yang ingin diproses. Fungsi `range(start, stop)` adalah alat pembantu paling populer untuk menciptakan deretan angka halte.

```python
# Berhenti di angka 0 sampai 4 (5 tidak termasuk)
for i in range(5):
    print(f"Langkah ke-{i}")
```

### C. Perulangan `while` (Berdasarkan Syarat)
Gunakan `while` jika Anda tidak tahu kapan tugas akan selesai, tapi Anda tahu syarat apa yang membuatnya harus berhenti.

```python
bensin = 3
while bensin > 0:
    print("Mobil melaju...")
    bensin -= 1  # Penting: kurangi agar tidak putar selamanya!
print("Bensin habis. Berhenti.")
```

### D. Pengendali Loop: `break` dan `continue`
- `break`: Membatalkan seluruh sisa perulangan.
- `continue`: Membatalkan putaran *saat ini* dan langsung loncat ke putaran berikutnya.
- `pass`: Tidak melakukan apa-apa (hanya sebagai penanda tempat agar tidak Error jika blok masih kosong).

## 4. Visualisasi Analogi

![Big Picture Control Flow - Navigasi Jalan Raya](assets/06_control_flow.svg)

## 5. Di Balik Layar (Under the Hood)
Di tingkat mesin (Bytecode), Python tidak benar-benar memiliki konsep "perulangan" yang puitis. Ia menggunakan instruksi **`POP_JUMP_IF_FALSE`** atau **`JUMP_ABSOLUTE`**. Saat interpreter sampai di ujung blok `while`, ia hanya diperintah untuk "Loncat kembali ke baris nomor X". Jika syaratnya sudah salah, ia diperintah "Loncat Lewati baris Y sampai Z". Komputer hanya terus-menerus melakukan lompatan baris berdasarkan hasil evaluasi True/False.

## 6. Peringatan / Jebakan Umum (Gotchas)
- **Infinite Loop**: Sering terjadi pada `while` karena lupa memperbarui variabel penentu kondisi di dalam blok (seperti lupa `i += 1`).
- **Off-by-One Error**: Saat memakai `range(5)`, ingatlah bahwa Python berhenti *sebelum* angka 5. Jadi ia hanya mencetak 0, 1, 2, 3, 4.
- **Modifikasi List**: Hindari menghapus item dari list saat Anda sedang melakukan `for item in my_list`. Hal ini akan membuat indeks Python berantakan dan melewatkan beberapa item. **Solusi**: Gunakan salinan list `for item in my_list.copy()`.

## 7. Referensi Kode Praktik
Silakan eksekusi simulasi jalan raya di folder `examples/`:
- `01_sistem_tilang.py`: Logika `if-elif-else` deteksi kecepatan.
- `02_absensi_bus.py`: Iterasi list menggunakan `for`.
- `03_pom_bensin.py`: Pengisian bensin menggunakan `while`.
- `04_pintu_darurat.py`: Demonstrasi `break` dan `continue`.

## 8. Latihan (Validasi)
- [ ] Buatlah `for` loop yang mencetak angka genap saja dari 1 sampai 20. (Petunjuk: Gunakan operator `%` atau langkah di `range`).
- [ ] Buatlah sebuah `while` loop yang terus meminta input nama dari user, dan hanya boleh berhenti jika user mengetik kata "selesai".
- [ ] Prediksi: Apa hasil dari kode ini?
  ```python
  for i in range(3):
      if i == 1:
          continue
      print(i)
  ```
