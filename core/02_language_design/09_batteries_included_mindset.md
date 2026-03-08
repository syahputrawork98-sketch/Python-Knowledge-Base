# Batteries-included Mindset

Chapter Code: CORE-02-09
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Intermediate
Estimated Time: 40 menit teori + 30 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas filosofi "batteries included" di Python: bahasa menyediakan standard library yang luas agar banyak kebutuhan umum bisa diselesaikan tanpa menambah dependency eksternal sejak awal.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-08
- memahami module import dasar
- memahami fungsi dan error handling sederhana

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| batteries included | filosofi menyediakan alat bawaan yang cukup lengkap | `json`, `pathlib`, `datetime` |
| standard library | kumpulan modul bawaan Python resmi | `collections`, `itertools`, `logging` |
| third-party package | library dari luar distribusi Python default | `requests`, `pydantic` |
| dependency cost | biaya adopsi library tambahan | maintenance, security update |
| build vs buy | keputusan buat sendiri vs pakai komponen siap pakai | util internal vs paket eksternal |

## Tujuan Besar

Membantu pembaca memilih solusi yang seimbang antara standard library dan third-party package berdasarkan kebutuhan nyata proyek.

## Tujuan Kecil

- mengenali kekuatan standard library untuk use case umum
- mengevaluasi biaya/manfaat dependency tambahan
- menghindari reinventing wheel maupun dependency berlebihan

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menyelesaikan masalah umum dengan modul bawaan Python
- menilai kapan third-party package memang diperlukan
- memberi alasan teknis saat menambah dependency ke project

## Peruntukan

Bab ini digunakan saat:

- memulai fitur baru dengan kebutuhan utility umum
- review proposal penambahan package baru
- menyusun guideline dependency policy tim

## Bukan Peruntukan

Bab ini bukan untuk:

- daftar lengkap seluruh modul standard library
- evaluasi keamanan dependency tingkat enterprise mendalam
- pembahasan packaging/distribution Python yang sangat detail

## Analogi

Batteries-included seperti membeli toolkit rumah. Untuk pekerjaan umum, alat bawaan sudah cukup. Anda beli alat tambahan hanya saat benar-benar dibutuhkan untuk tugas spesifik.

## Miskonsepsi Umum

- Miskonsepsi: "Selalu pakai standard library, jangan third-party."
  Klarifikasi: third-party bisa sangat bernilai jika standard library tidak cukup atau terlalu mahal dikembangkan sendiri.

- Miskonsepsi: "Pakai package populer selalu pilihan terbaik."
  Klarifikasi: popularitas tidak otomatis cocok dengan kebutuhan dan constraints proyek Anda.

- Miskonsepsi: "Dependency itu gratis selama install berhasil."
  Klarifikasi: setiap dependency menambah biaya upgrade, audit, dan troubleshooting.

## Konsep Inti

### 1. Prinsip Dasar

Kerangka pengambilan keputusan sederhana:

1. Start with standard library
Cek dulu apakah kebutuhan bisa dipenuhi modul bawaan dengan kualitas memadai.

2. Evaluate gap clearly
Jika ada gap, tulis spesifik apa yang kurang: performa, fitur, ergonomi, atau reliability.

3. Add third-party intentionally
Tambahkan dependency hanya jika manfaatnya jelas lebih besar dari biaya adopsi.

4. Re-evaluate periodically
Dependency yang dulu relevan bisa jadi tidak perlu lagi setelah kebutuhan berubah.

### 2. Dampak Praktis

Penerapan mindset ini berdampak pada:

- startup project lebih cepat dengan risiko dependency rendah
- onboarding tim lebih mudah karena modul bawaan cenderung familiar
- maintenance lebih stabil karena surface area dependency lebih kecil
- keputusan teknis lebih transparan saat package baru diajukan

Checklist sebelum menambah package baru:

1. apakah ada modul stdlib yang sudah cukup
2. apakah package aktif dirawat dan terdokumentasi
3. apakah tim siap menanggung biaya upgrade jangka panjang
4. apakah manfaat fungsionalnya benar-benar signifikan

## Diagram

![Big picture Batteries-included Mindset](assets/09_batteries_included_mindset.svg)

Caption: Diagram menggambarkan jalur keputusan dari penggunaan standar bawaan menuju adopsi dependency eksternal yang terukur.

### Legenda Diagram

- 1: kebutuhan fitur
- 2: evaluasi stdlib vs external package
- 3: keputusan dependency berbasis biaya-manfaat

## Contoh Kode (Benar)

```python
from pathlib import Path
import json
from tempfile import TemporaryDirectory


def load_settings(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"settings file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


with TemporaryDirectory() as temp_dir:
    settings_path = Path(temp_dir) / "settings.json"
    settings_path.write_text(
        '{"app_name": "Python Knowledge Universe"}',
        encoding="utf-8",
    )
    print(load_settings(str(settings_path)))
```

Expected output:

```text
{'app_name': 'Python Knowledge Universe'}
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
# menambah dependency eksternal untuk parsing json sederhana
# padahal kebutuhan bisa dipenuhi `json` bawaan
import some_json_package


def load_settings(file_path):
    return some_json_package.parse_file(file_path)
```

Masalah:

- menambah beban dependency tanpa manfaat jelas
- menaikkan risiko kompatibilitas dan maintenance
- tim baru perlu belajar API tambahan yang sebenarnya tidak perlu

Perbaikan:

```python
from pathlib import Path
import json


def load_settings(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"settings file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
```

## Catatan Praktis

- bias default: coba stdlib dulu, ukur dulu, baru tambah dependency
- dokumentasikan alasan saat menambah package baru
- batasi dependency pada modul yang benar-benar memberi leverage
- lakukan review berkala untuk menghapus dependency yang tidak lagi dipakai
- jangan reinvent wheel jika stdlib atau package matang sudah memenuhi kebutuhan

## Latihan

### Dasar

Cari satu util di proyek yang bisa diganti dengan standard library (`pathlib`, `collections`, `itertools`, atau `json`).

### Menengah

Buat tabel keputusan untuk satu dependency eksternal: manfaat, risiko, alternatif stdlib, dan keputusan akhir.

### Mini Challenge

Buat file `report_loader.py` yang:

- membaca data JSON dari file
- memvalidasi key wajib (`report_id`, `created_at`)
- mengembalikan ringkasan sederhana

Syarat:

- gunakan hanya standard library
- tambahkan minimal 5 test case
- tulis 5-8 kalimat alasan kenapa stdlib cukup atau tidak cukup untuk kasus Anda

## Checklist Lulus Bab

- [ ] memahami prinsip batteries-included Python
- [ ] mampu mengevaluasi kebutuhan dependency eksternal
- [ ] menyelesaikan mini challenge dengan stdlib
- [ ] mampu memberi justifikasi teknis penambahan package

## Peta Keterkaitan

- Bab sebelumnya: 08_errors_as_part_of_design.md
- Bab berikutnya: 10_backward_compatibility_and_peps.md
- Keterkaitan lintas buku Core: CORE-07 (stdlib), CORE-13 (packaging)

## Ringkasan

- Python menyediakan standard library kuat untuk banyak kebutuhan umum
- dependency eksternal harus dipilih secara sadar, bukan otomatis
- keputusan dependency yang baik menurunkan biaya maintenance
- keseimbangan stdlib dan third-party adalah bagian penting dari desain sistem

## FAQ Singkat

1. Apakah salah memakai third-party package?
   Jawaban singkat: tidak; gunakan saat manfaatnya jelas dan biaya adopsi dapat diterima.
2. Kapan stdlib tidak cukup?
   Jawaban singkat: saat kebutuhan fitur/performa/ergonomi melewati kemampuan praktis stdlib.
3. Bagaimana menghindari dependency bloat?
   Jawaban singkat: terapkan review dependency berkala dan minta justifikasi teknis tiap penambahan package.

## Referensi

- Python Standard Library: https://docs.python.org/3/library/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
- Packaging User Guide: https://packaging.python.org/
