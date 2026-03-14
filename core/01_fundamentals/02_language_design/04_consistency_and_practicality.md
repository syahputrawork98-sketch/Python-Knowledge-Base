# Consistency and Practicality

Chapter Code: CORE-02-04
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Basic
Estimated Time: 40 menit teori + 30 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas dua pilar yang sering berjalan bersama dalam Python: consistency (konsistensi pola) dan practicality (keputusan yang berguna di dunia nyata). Tujuannya agar kode tidak hanya "rapi di teori", tapi juga efektif dipakai tim untuk menyelesaikan masalah.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-03
- memahami fungsi, struktur data dasar, dan exception
- pernah berkolaborasi pada kode yang ditulis lebih dari satu orang

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| consistency | keseragaman pola penulisan agar mudah diprediksi | format naming dan struktur fungsi stabil |
| practicality | keputusan berbasis manfaat nyata | solusi sederhana yang cepat dipelihara |
| convention | kebiasaan standar yang diikuti bersama | snake_case, 4 spasi indent |
| local optimum | solusi terbaik di konteks tertentu | pattern tim untuk modul tertentu |
| maintainability | kemudahan merawat kode jangka panjang | perubahan fitur tanpa banyak regression |

## Tujuan Besar

Membantu pembaca mengambil keputusan desain yang konsisten lintas kodebase sambil tetap pragmatis terhadap deadline, kebutuhan produk, dan kapasitas tim.

## Tujuan Kecil

- memahami kapan konsistensi harus diprioritaskan
- memahami kapan pragmatisme perlu mengalahkan idealisme
- menyusun aturan praktis agar tim punya standar yang operasional

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menerapkan style dan pola yang konsisten di fungsi/modul sederhana
- menjelaskan alasan pragmatis di balik deviasi dari pola umum
- melakukan refactor kecil agar kode lebih seragam tanpa mengganggu perilaku

## Peruntukan

Bab ini digunakan saat:

- membangun coding guideline tim
- melakukan review pada kode yang ditulis banyak kontributor
- memutuskan antara "ideal design" vs "shipping value" secara realistis

## Bukan Peruntukan

Bab ini bukan untuk:

- pembahasan arsitektur enterprise multi-layer secara mendalam
- validasi performa skala besar dengan profiling kompleks
- justifikasi "asal jalan" tanpa standar kualitas minimum

## Analogi

Consistency dan practicality seperti jalur produksi. Standar yang konsisten menjaga kualitas, sementara keputusan praktis memastikan produk tetap keluar tepat waktu.

## Miskonsepsi Umum

- Miskonsepsi: "Konsisten berarti kaku dan anti-perubahan."
  Klarifikasi: konsisten berarti mudah diprediksi; perubahan tetap boleh jika dilakukan seragam dan terdokumentasi.

- Miskonsepsi: "Praktis berarti boleh melanggar semua aturan."
  Klarifikasi: praktis tetap butuh batas. Keputusan cepat tanpa standar hanya memindahkan biaya ke maintenance.

- Miskonsepsi: "Kalau sudah pakai linter, masalah consistency selesai."
  Klarifikasi: linter membantu format, tapi tidak menggantikan keputusan desain API dan struktur logika.

## Konsep Inti

### 1. Prinsip Dasar

Empat prinsip kerja consistency + practicality:

1. Default to convention
Ikuti pola umum tim lebih dulu agar onboarding dan review lebih ringan.

2. Break rule with reason
Jika perlu menyimpang, tulis alasan teknis dan ruang lingkupnya.

3. Optimize for team speed
Pilih pola yang mempercepat pemahaman tim, bukan hanya penulis awal.

4. Minimize surprise
Kode yang baik tidak "mengejutkan" pembaca lewat perilaku tak terduga.

### 2. Dampak Praktis

Dalam pekerjaan harian, dampaknya terlihat di:

- struktur fungsi yang seragam (validasi -> proses utama -> return)
- pola penamaan yang stabil antar modul
- error handling yang konsisten
- keputusan trade-off yang terdokumentasi saat ada pengecualian

Checklist saat review:

1. apakah pola fungsi ini konsisten dengan modul sejenis
2. jika berbeda, apakah alasannya jelas dan valid
3. apakah deviasi ini menambah atau mengurangi beban maintenance
4. apakah perubahan tetap aman untuk tim berikutnya

## Diagram

![Big picture Consistency and Practicality](assets/04_consistency_and_practicality.svg)

Caption: Diagram menampilkan alur keputusan dari standar konsisten menuju hasil praktis yang dapat dipelihara.

### Legenda Diagram

- 1: standar/pola tim
- 2: evaluasi kebutuhan nyata
- 3: keputusan implementasi yang operasional

## Contoh Kode (Benar)

```python
def normalize_phone_number(raw_phone: str) -> str:
    cleaned = raw_phone.strip().replace("-", "").replace(" ", "")
    if not cleaned.isdigit():
        raise ValueError("phone number must contain digits only")
    if len(cleaned) < 10:
        raise ValueError("phone number must be at least 10 digits")
    return cleaned


print(normalize_phone_number("0812-3456-7890"))
```

Expected output:

```text
081234567890
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
def p(x):
    x = x.replace("-", "")
    if len(x) < 10:
        return ""
    return x
```

Masalah:

- nama fungsi/parameter tidak konsisten dengan intent domain
- validasi tidak seragam (kadang return string kosong, bukan error)
- perilaku diam-diam mempersulit debugging caller

Perbaikan:

```python
def normalize_phone_number(raw_phone: str) -> str:
    cleaned = raw_phone.strip().replace("-", "").replace(" ", "")
    if not cleaned.isdigit():
        raise ValueError("phone number must contain digits only")
    if len(cleaned) < 10:
        raise ValueError("phone number must be at least 10 digits")
    return cleaned
```

## Catatan Praktis

- konsistenkan pola return dan exception pada fungsi sejenis
- hindari sentinel value diam-diam (`""`, `None`) tanpa kontrak jelas
- dokumentasikan deviasi dari standard pattern tim
- gunakan tooling (formatter/linter) sebagai baseline, bukan satu-satunya quality gate
- prefer perubahan kecil bertahap untuk legacy code

## Latihan

### Dasar

Temukan 2 fungsi serupa di proyek Anda. Samakan gaya naming dan pola validasinya.

### Menengah

Refactor satu modul kecil agar semua fungsi mengikuti struktur yang sama: validasi, proses utama, return.

### Mini Challenge

Buat file `customer_contact.py` berisi:

- fungsi normalisasi email
- fungsi normalisasi nomor telepon
- fungsi validasi kontak wajib (minimal salah satu terisi)

Tambahkan minimal 4 test case, lalu tulis 5-8 kalimat tentang trade-off antara konsistensi style dan kebutuhan praktis yang Anda ambil.

## Checklist Lulus Bab

- [ ] memahami perbedaan konsistensi dan kekakuan
- [ ] mampu memberi alasan pragmatis untuk deviasi tertentu
- [ ] menyelesaikan mini challenge beserta test
- [ ] mampu menjaga perilaku fungsi tetap dapat diprediksi

## Peta Keterkaitan

- Bab sebelumnya: 03_readability_and_explicitness.md
- Bab berikutnya: 05_simple_vs_complex.md
- Keterkaitan lintas buku Core: CORE-03 (execution model), CORE-14 (testing strategy)

## Ringkasan

- consistency menurunkan beban kognitif tim
- practicality menjaga solusi tetap relevan terhadap kebutuhan nyata
- standar tim yang jelas mempercepat review dan maintenance
- deviasi boleh dilakukan jika ada alasan teknis yang terdokumentasi

## FAQ Singkat

1. Apakah konsistensi berarti semua fungsi harus identik?
   Jawaban singkat: tidak; yang penting pola inti dan kontrak perilaku tetap seragam.
2. Kapan boleh menyimpang dari convention tim?
   Jawaban singkat: saat ada kebutuhan teknis valid dan dampaknya dipahami bersama.
3. Apakah practicality selalu menang atas ideal design?
   Jawaban singkat: tidak; keputusan terbaik menyeimbangkan nilai jangka pendek dan jangka panjang.

## Referensi

- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
- PEP 20 (Zen of Python): https://peps.python.org/pep-0020/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
