# Design Goals and Philosophy

Chapter Code: CORE-02-01
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Basic
Estimated Time: 35 menit teori + 25 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas tujuan desain utama Python dan filosofi yang mengarahkan keputusan sintaks, standar library, serta gaya menulis kode. Intinya: Python dirancang agar manusia lebih cepat memahami kode, tanpa mengabaikan kebutuhan implementasi praktis.

## Prasyarat Spesifik Bab

- memahami variabel, kontrol alur, fungsi, dan module dasar dari CORE-01
- pernah membaca kode Python sederhana (script kecil)
- siap membandingkan beberapa gaya penulisan kode

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| design goal | sasaran utama saat merancang bahasa | readability, productivity |
| philosophy | prinsip berpikir yang memandu keputusan | explicit is better than implicit |
| practicality | keputusan yang memprioritaskan manfaat nyata | fitur sederhana yang sering dipakai |
| consistency | pola yang seragam agar mudah diprediksi | aturan penamaan dan struktur serupa |
| maintainability | kemudahan merawat kode jangka panjang | kode mudah dibaca tim lain |

## Tujuan Besar

Membangun fondasi cara berpikir agar pembaca memahami "mengapa" di balik gaya Python, bukan sekadar mengikuti gaya secara mekanis.

## Tujuan Kecil

- mengenali tujuan desain utama Python
- memahami hubungan filosofi bahasa dengan keputusan coding
- menerapkan prinsip dasar untuk menulis kode lebih jelas

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menjelaskan minimal 3 design goal Python
- memberi alasan kenapa satu gaya kode lebih dipilih daripada gaya lain
- menulis ulang kode sederhana menjadi lebih terbaca

## Peruntukan

Bab ini digunakan saat:

- ingin memahami pondasi mental model Python
- memulai standar gaya coding di tim
- melakukan code review untuk kualitas keterbacaan

## Bukan Peruntukan

Bab ini bukan untuk:

- membahas detail internal implementasi CPython
- membahas optimisasi performa tingkat lanjut
- menggantikan dokumentasi API spesifik library

## Analogi

Desain bahasa mirip desain rambu lalu lintas. Rambu yang konsisten membuat semua orang lebih cepat mengambil keputusan dengan risiko salah lebih kecil.

## Miskonsepsi Umum

- Miskonsepsi: "Python itu mudah, jadi desainnya tidak penting."
  Klarifikasi: justru karena mudah dipakai banyak orang, desain harus kuat agar kode tetap konsisten.

- Miskonsepsi: "Yang penting program jalan."
  Klarifikasi: program yang jalan hari ini bisa mahal dirawat besok jika intent tidak jelas.

- Miskonsepsi: "Filosofi bahasa hanya teori."
  Klarifikasi: filosofi langsung memengaruhi API design, error handling, dan style tim.

## Konsep Inti

### 1. Prinsip Dasar

Tujuan desain Python secara praktis bisa dirangkum sebagai berikut:

1. Keterbacaan sebagai prioritas
Kode dibaca jauh lebih sering daripada ditulis ulang. Karena itu, kejelasan menjadi target utama.

2. Kesederhanaan yang realistis
Python mendorong solusi sederhana, tetapi tetap menerima kompleksitas jika memang dibutuhkan masalah nyata.

3. Konsistensi antarpola
Struktur yang seragam mengurangi beban kognitif saat berpindah antar modul/proyek.

4. Produktivitas developer
Bahasa didesain untuk membantu penyelesaian masalah bisnis/ilmiah lebih cepat, bukan memaksa detail teknis rendah-level dari awal.

### 2. Dampak Praktis

Di pekerjaan harian, filosofi ini terlihat pada:

- penamaan variabel/fungsi yang deskriptif
- struktur fungsi ringkas dengan satu tanggung jawab
- penggunaan fitur idiomatik seperlunya (bukan demi terlihat pintar)
- komentar seperlunya, fokus menjelaskan alasan, bukan mengulang kode

Aturan kerja sederhana:

1. tulis versi paling jelas
2. cek lewat test/review
3. rapikan jika ada pengulangan
4. optimasi hanya setelah ada bukti kebutuhan

## Diagram

![Big picture Design Goals and Philosophy](assets/01_design_goals_and_philosophy.svg)

Caption: Diagram menunjukkan alur dari tujuan desain bahasa ke dampak nyata pada keputusan coding sehari-hari.

### Legenda Diagram

- 1??: tujuan desain utama
- 2??: prinsip filosofi yang memandu
- 3??: konsekuensi pada gaya coding

## Contoh Kode (Benar)

```python
def send_welcome_email(user_email: str, user_name: str) -> str:
    if not user_email:
        raise ValueError("user_email must not be empty")
    return f"Hi {user_name}, welcome to Python Knowledge Universe!"


print(send_welcome_email("user@example.com", "Syahputra"))
```

Expected output:

```text
Hi Syahputra, welcome to Python Knowledge Universe!
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
def f(a, b):
    if a == "":
        return None
    return "Hi " + b
```

Masalah:

- nama fungsi/parameter tidak jelas
- kontrak fungsi tidak konsisten (`None` atau `str` tanpa penjelasan)
- intent bisnis sulit dibaca reviewer

Perbaikan:

```python
def send_welcome_email(user_email: str, user_name: str) -> str:
    if not user_email:
        raise ValueError("user_email must not be empty")
    return f"Hi {user_name}, welcome to Python Knowledge Universe!"
```

## Catatan Praktis

- pilih nama yang menjelaskan niat, bukan singkatan prematur
- buat fungsi kecil dengan tanggung jawab jelas
- hindari logika bercabang panjang dalam satu blok
- gunakan exception dengan pesan yang actionable
- konsistensi style lebih penting daripada preferensi personal

## Latihan

### Dasar

Cari satu fungsi di kode Anda yang namanya terlalu umum (`process`, `handle`, `run`) lalu usulkan nama yang lebih spesifik.

### Menengah

Refactor fungsi dengan lebih dari 20 baris menjadi 2-3 fungsi kecil tanpa mengubah output.

### Mini Challenge

Buat file `greeting.py` berisi:

- satu fungsi validasi input nama
- satu fungsi pembuat pesan sambutan
- satu fungsi orchestrator pemanggil keduanya

Tambahkan minimal 4 test case sederhana dan tulis 5-8 kalimat tentang trade-off yang Anda ambil (ringkas vs jelas).

## Checklist Lulus Bab

- [ ] memahami design goal utama Python
- [ ] mampu menjelaskan dampak filosofi pada kode nyata
- [ ] menyelesaikan mini challenge dengan output benar
- [ ] dapat memutuskan gaya kode berbasis kejelasan

## Peta Keterkaitan

- Bab sebelumnya: tidak ada (bab pembuka)
- Bab berikutnya: 02_the_zen_of_python.md
- Keterkaitan lintas buku Core: CORE-01 (syntax), CORE-03 (execution model)

## Ringkasan

- Python dirancang untuk membantu manusia memahami kode lebih cepat
- filosofi bahasa memengaruhi keputusan coding harian
- kejelasan intent adalah modal utama maintainability
- keputusan teknis yang baik dimulai dari design goal yang benar

## FAQ Singkat

1. Apakah selalu salah menulis kode pendek?
   Jawaban singkat: tidak; pendek boleh selama intent tetap jelas.
2. Kenapa harus peduli naming sejak awal?
   Jawaban singkat: naming buruk adalah sumber biaya maintenance yang besar.
3. Apa hubungan filosofi dengan performa?
   Jawaban singkat: filosofi menentukan default yang aman dibaca; optimasi dilakukan terukur saat dibutuhkan.

## Referensi

- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
- PEP 20 (Zen of Python): https://peps.python.org/pep-0020/
- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
