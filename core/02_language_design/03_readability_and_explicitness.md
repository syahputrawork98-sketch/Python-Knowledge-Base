# Readability and Explicitness

Chapter Code: CORE-02-03
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Basic
Estimated Time: 40 menit teori + 30 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas bagaimana keterbacaan (readability) dan kejelasan niat (explicitness) menjadi fondasi gaya Pythonic. Fokusnya adalah membuat kode yang mudah dipahami ulang oleh manusia, bukan hanya berjalan benar saat ini.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 dan CORE-02-02
- memahami fungsi, if/for, serta exception dasar
- terbiasa membaca kode Python sederhana sampai menengah

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| readability | kemudahan kode dipahami oleh pembaca | nama variabel yang deskriptif |
| explicitness | niat program ditulis jelas dan tidak samar | validasi input eksplisit |
| implicit behavior | perilaku tersembunyi yang tidak langsung terlihat | fallback diam-diam |
| cognitive load | beban mental saat membaca kode | nested condition berlapis |
| API contract | kesepakatan input/output/error sebuah fungsi | tipe argumen dan exception |

## Tujuan Besar

Membantu pembaca menulis kode yang jelas, dapat diprediksi, dan mudah dirawat tim tanpa mengorbankan produktivitas.

## Tujuan Kecil

- mengenali pola kode yang mudah dibaca vs sulit dibaca
- menerapkan explicitness pada validasi dan error handling
- mengurangi ambiguitas pada desain fungsi sederhana

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- mengidentifikasi masalah readability pada potongan kode nyata
- merancang fungsi dengan kontrak input/output yang jelas
- melakukan refactor untuk menurunkan beban kognitif pembaca

## Peruntukan

Bab ini digunakan saat:

- melakukan code review harian
- menulis API/helper internal tim
- merapikan legacy code agar lebih mudah dipahami

## Bukan Peruntukan

Bab ini bukan untuk:

- optimisasi mikro tingkat mesin
- pembahasan teori compiler atau parser
- perdebatan style tanpa konteks maintainability

## Analogi

Readability seperti rambu jalan yang jelas. Saat rambu ambigu, semua orang tetap bisa sampai tujuan, tapi risiko salah belok dan waktu tempuh meningkat.

## Miskonsepsi Umum

- Miskonsepsi: "Yang penting output benar, readability belakangan."
  Klarifikasi: output benar hari ini tidak menjamin kode mudah diubah besok.

- Miskonsepsi: "Explicit code pasti panjang dan lambat."
  Klarifikasi: explicit tidak selalu panjang; yang penting intent terlihat tanpa menebak.

- Miskonsepsi: "Komentar banyak berarti jelas."
  Klarifikasi: komentar tidak menggantikan nama fungsi/struktur kode yang buruk.

## Konsep Inti

### 1. Prinsip Dasar

Readability dan explicitness biasanya muncul di empat area utama:

1. Naming
Nama fungsi, parameter, dan variabel harus menggambarkan niat, bukan sekadar singkatan.

2. Control flow
Alur logika perlu linear dan mudah diikuti. Hindari percabangan terlalu dalam jika bisa dipisah.

3. API contract
Jelaskan apa yang diterima, dikembalikan, dan kondisi error. Kontrak yang jelas menurunkan salah pakai.

4. Error clarity
Error message harus menjelaskan masalah dan konteks input invalid.

### 2. Dampak Praktis

Dalam proyek nyata, dampaknya terlihat pada:

- onboarding developer baru lebih cepat
- review lebih fokus ke logika bisnis, bukan menebak maksud kode
- bug lebih cepat ditelusuri karena kontrak fungsi jelas
- refactor lebih aman karena perilaku fungsi dapat diprediksi

Checklist cepat saat menulis fungsi:

1. apakah nama fungsi menjawab "fungsi ini melakukan apa"
2. apakah input invalid ditangani eksplisit
3. apakah output konsisten untuk semua cabang
4. apakah error message membantu debugging

## Diagram

![Big picture Readability and Explicitness](assets/03_readability_and_explicitness.svg)

Caption: Diagram memperlihatkan hubungan antara readability, explicitness, dan dampaknya terhadap maintainability.

### Legenda Diagram

- 1: intent bisnis
- 2: keputusan desain kode
- 3: dampak ke kualitas maintenance

## Contoh Kode (Benar)

```python
def calculate_discounted_price(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("price must be >= 0")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


print(calculate_discounted_price(200_000, 15))
```

Expected output:

```text
170000.0
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
def calc(p, d):
    if d > 100:
        return p
    return p - p * d / 100
```

Masalah:

- nama `calc`, `p`, `d` tidak memberi konteks
- validasi tidak lengkap (`d < 0`, `p < 0` tidak ditangani)
- perilaku diam-diam saat `d > 100` membingungkan caller

Perbaikan:

```python
def calculate_discounted_price(price: float, discount_percent: float) -> float:
    if price < 0:
        raise ValueError("price must be >= 0")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount
```

## Catatan Praktis

- utamakan nama yang deskriptif daripada singkat
- hindari hidden fallback yang menyembunyikan error input
- type hint membantu komunikasi kontrak fungsi
- gunakan guard clause untuk memangkas nested logic
- buat satu fungsi untuk satu tanggung jawab

## Latihan

### Dasar

Temukan satu fungsi di proyek Anda yang nama parameternya terlalu singkat. Ubah ke nama yang lebih jelas.

### Menengah

Refactor satu fungsi dengan percabangan bertingkat menjadi guard clause tanpa mengubah output.

### Mini Challenge

Buat file `invoice.py` berisi:

- fungsi hitung subtotal
- fungsi hitung diskon
- fungsi hitung total akhir dengan validasi

Tambahkan minimal 4 test case (termasuk input invalid), lalu tulis 5-8 kalimat alasan desain yang Anda pilih untuk menjaga readability.

## Checklist Lulus Bab

- [ ] mampu membedakan kode implicit vs explicit
- [ ] mampu memperbaiki naming dan kontrak fungsi
- [ ] menyelesaikan mini challenge beserta test
- [ ] dapat menjelaskan dampak readability ke maintenance

## Peta Keterkaitan

- Bab sebelumnya: 02_the_zen_of_python.md
- Bab berikutnya: 04_consistency_and_practicality.md
- Keterkaitan lintas buku Core: CORE-01 (fungsi dasar), CORE-05 (exception lanjut)

## Ringkasan

- readability mempercepat pemahaman tim terhadap kode
- explicitness mengurangi ambiguitas perilaku fungsi
- kontrak API yang jelas memperkecil risiko bug integrasi
- kode yang mudah dibaca lebih murah dirawat dalam jangka panjang

## FAQ Singkat

1. Apakah semua variabel harus panjang?
   Jawaban singkat: tidak; cukup deskriptif dan proporsional terhadap konteks.
2. Kapan boleh one-liner?
   Jawaban singkat: saat intent tetap langsung terbaca tanpa parsing mental tambahan.
3. Kenapa guard clause sering direkomendasikan?
   Jawaban singkat: karena mengurangi nesting dan membuat alur utama lebih jelas.

## Referensi

- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
- PEP 20 (Zen of Python): https://peps.python.org/pep-0020/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
