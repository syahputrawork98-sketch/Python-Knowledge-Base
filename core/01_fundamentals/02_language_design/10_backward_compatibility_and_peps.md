# Backward Compatibility and PEPs

Chapter Code: CORE-02-10
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Intermediate
Estimated Time: 50 menit teori + 40 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas bagaimana Python menyeimbangkan dua kebutuhan yang sering bertentangan: menjaga kompatibilitas kode lama (backward compatibility) dan tetap berevolusi melalui perubahan bahasa. PEP (Python Enhancement Proposal) menjadi mekanisme utama untuk mendiskusikan dan meresmikan perubahan tersebut.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-09
- memahami dasar versioning dan API function/module
- memahami warning dan exception dasar

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| backward compatibility | kemampuan versi baru tetap menjalankan kode lama | fungsi lama masih bekerja |
| breaking change | perubahan yang membuat kode lama gagal | parameter wajib baru tanpa default |
| deprecation | fase transisi sebelum fitur lama dihapus | `DeprecationWarning` |
| migration path | langkah berpindah dari API lama ke API baru | alias fungsi + panduan update |
| PEP | dokumen proposal resmi evolusi Python | PEP 8, PEP 20, PEP 484 |

## Tujuan Besar

Membantu pembaca merancang perubahan kode/API secara aman dan terukur, serta memahami mengapa proses evolusi Python sangat menekankan kompatibilitas.

## Tujuan Kecil

- membedakan perubahan kompatibel vs breaking
- menerapkan pola deprecation bertahap pada API
- membaca PEP sebagai sumber keputusan desain

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- mengidentifikasi risiko breaking change sebelum rilis
- menulis migration path sederhana untuk API internal
- menggunakan PEP relevan sebagai acuan argumen teknis

## Peruntukan

Bab ini digunakan saat:

- mengubah API library internal tim
- menyusun release note dan rencana migrasi
- meninjau proposal perubahan arsitektur/module publik

## Bukan Peruntukan

Bab ini bukan untuk:

- membahas governance Python secara historis lengkap
- merinci seluruh proses formal PEP dari awal sampai akhir
- menggantikan strategi release management organisasi secara penuh

## Analogi

Backward compatibility seperti renovasi jalan utama kota: perubahan harus memungkinkan kendaraan lama tetap lewat sambil menyiapkan jalur baru yang lebih baik.

## Miskonsepsi Umum

- Miskonsepsi: "Kalau desain baru lebih bagus, langsung ganti total."
  Klarifikasi: tanpa transisi, biaya migrasi pengguna bisa sangat besar.

- Miskonsepsi: "Deprecation warning cuma gangguan."
  Klarifikasi: warning adalah alat komunikasi penting untuk menurunkan risiko perubahan.

- Miskonsepsi: "PEP hanya penting untuk core developer Python."
  Klarifikasi: developer aplikasi tetap diuntungkan karena PEP menjelaskan alasan dan dampak fitur bahasa.

## Konsep Inti

### 1. Prinsip Dasar

Empat prinsip perubahan kompatibel:

1. Prefer additive change
Tambahkan API baru sebelum menghapus yang lama.

2. Deprecate before remove
Berikan warning dan waktu transisi yang jelas.

3. Document migration path
Sediakan langkah konkret berpindah API agar pengguna tidak menebak.

4. Use standards as reference
Rujuk PEP/dokumen resmi agar keputusan tidak berbasis opini semata.

### 2. Dampak Praktis

Jika prinsip ini dipakai, tim akan mendapatkan:

- rollout fitur baru lebih aman
- gangguan produksi lebih kecil saat upgrade
- komunikasi antar tim lebih jelas melalui release note
- kepercayaan pengguna internal/eksternal lebih tinggi

Checklist sebelum mengubah API publik:

1. apakah ini breaking change
2. apakah ada fallback/compat layer sementara
3. apakah warning dan dokumentasi migrasi sudah tersedia
4. apakah test mencakup jalur API lama dan baru selama transisi

## Diagram

![Big picture Backward Compatibility and PEPs](assets/10_backward_compatibility_and_peps.svg)

Caption: Diagram menunjukkan alur perubahan dari proposal (PEP/policy) ke deprecation bertahap hingga migrasi aman.

### Legenda Diagram

- 1: kebutuhan perubahan
- 2: evaluasi dampak kompatibilitas
- 3: rollout bertahap + migrasi

## Contoh Kode (Benar)

```python
import warnings


def calculate_total_v2(price: float, tax_rate: float = 0.11) -> float:
    return price + (price * tax_rate)


def calculate_total(price: float) -> float:
    warnings.warn(
        "calculate_total() is deprecated; use calculate_total_v2(price, tax_rate)",
        DeprecationWarning,
        stacklevel=2,
    )
    return calculate_total_v2(price)


with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always", DeprecationWarning)
    total = calculate_total(100_000)

print(caught[0].message)
print(total)
```

Expected output:

```text
calculate_total() is deprecated; use calculate_total_v2(price, tax_rate)
111000.0
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
# versi lama tiba-tiba dihapus tanpa fase transisi

def calculate_total_v2(price: float, tax_rate: float) -> float:
    return price + (price * tax_rate)
```

Masalah:

- caller lama langsung error karena signature berubah
- tidak ada jalur migrasi yang jelas
- memperbesar risiko gangguan saat deploy

Perbaikan:

```python
import warnings


def calculate_total_v2(price: float, tax_rate: float = 0.11) -> float:
    return price + (price * tax_rate)


def calculate_total(price: float) -> float:
    warnings.warn(
        "calculate_total() is deprecated; use calculate_total_v2(price, tax_rate)",
        DeprecationWarning,
        stacklevel=2,
    )
    return calculate_total_v2(price)
```

## Catatan Praktis

- hindari breaking change mendadak pada API yang sudah dipakai luas
- gunakan `DeprecationWarning` dengan pesan migrasi yang jelas
- tentukan batas waktu transisi dan komunikasikan sejak awal
- sertakan contoh before/after di release note
- jadikan PEP relevan sebagai rujukan keputusan desain

## Latihan

### Dasar

Tambahkan wrapper deprecated untuk satu fungsi lama di proyek Anda dan tampilkan warning yang informatif.

### Menengah

Buat rencana migrasi 3 langkah untuk perubahan signature fungsi yang sudah dipakai banyak modul.

### Mini Challenge

Buat file `pricing_api.py` berisi:

- fungsi lama `get_price_total(price)`
- fungsi baru `get_price_total_v2(price, tax_rate=0.11)`
- warning deprecation pada fungsi lama

Tambahkan minimal 5 test case (termasuk jalur kompatibilitas lama), lalu tulis 5-8 kalimat strategi transisi yang Anda pilih.

## Checklist Lulus Bab

- [ ] memahami perbedaan additive vs breaking change
- [ ] mampu menerapkan deprecation bertahap
- [ ] menyelesaikan mini challenge dan test
- [ ] mampu menggunakan PEP sebagai acuan argumentasi teknis

## Peta Keterkaitan

- Bab sebelumnya: 09_batteries_included_mindset.md
- Bab berikutnya: 11_idiomatic_python_and_style.md
- Keterkaitan lintas buku Core: CORE-13 (packaging/release), CORE-14 (testing)

## Ringkasan

- backward compatibility adalah strategi penting menjaga stabilitas ekosistem
- perubahan API idealnya additive lalu deprecate sebelum remove
- PEP memberi kerangka keputusan desain yang transparan dan terdokumentasi
- migrasi yang jelas menurunkan risiko teknis dan biaya adopsi

## FAQ Singkat

1. Apakah semua breaking change harus dihindari?
   Jawaban singkat: tidak selalu, tapi harus terencana, terdokumentasi, dan diberi jalur migrasi.
2. Kapan warning deprecation sebaiknya dipasang?
   Jawaban singkat: segera saat API pengganti stabil tersedia.
3. Kenapa perlu baca PEP untuk developer aplikasi?
   Jawaban singkat: agar paham alasan fitur/perubahan dan bisa mengambil keputusan implementasi yang lebih tepat.

## Referensi

- PEP Index: https://peps.python.org/
- PEP 387 (Backwards Compatibility): https://peps.python.org/pep-0387/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
