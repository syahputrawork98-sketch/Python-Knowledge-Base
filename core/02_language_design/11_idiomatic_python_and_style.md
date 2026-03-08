# Idiomatic Python and Style

Chapter Code: CORE-02-11
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Intermediate
Estimated Time: 45 menit teori + 35 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas apa yang dimaksud "idiomatic Python": cara menulis kode yang terasa natural bagi ekosistem Python, mudah dibaca tim lain, dan konsisten dengan praktik yang direkomendasikan (terutama PEP 8).

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-10
- memahami fungsi, class dasar, exception, dan module import
- memahami dasar type hint dan standard library umum

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| idiomatic Python | gaya penulisan yang sesuai kebiasaan komunitas Python | list comprehension seperlunya |
| style guide | pedoman konsistensi penulisan kode | PEP 8 |
| readability | kemudahan kode dipahami pembaca | nama fungsi deskriptif |
| explicitness | niat kode jelas, tidak tersembunyi | guard clause, named argument |
| refactor | perubahan struktur internal tanpa ubah perilaku | pecah fungsi panjang |

## Tujuan Besar

Membantu pembaca menulis kode Python yang bersih, konsisten, dan mudah dipelihara, sekaligus mampu membedakan gaya idiomatik yang sehat dari "gaya pintar" yang sulit dirawat.

## Tujuan Kecil

- menerapkan pola idiomatic Python pada kasus umum
- menghindari anti-pattern style yang memperberat maintenance
- membangun dasar argumentasi saat code review

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- menulis fungsi yang mengikuti style Pythonic secara konsisten
- refactor kode non-idiomatic menjadi lebih jelas
- menjelaskan keputusan style berbasis readability dan maintainability

## Peruntukan

Bab ini digunakan saat:

- melakukan code review harian
- menyiapkan standar coding guideline tim
- merapikan modul lama agar lebih mudah dibaca

## Bukan Peruntukan

Bab ini bukan untuk:

- pembahasan seluruh aturan PEP 8 secara lengkap
- perdebatan style subjektif tanpa konteks kebutuhan tim
- optimisasi performa rendah-level berbasis microbenchmark

## Analogi

Idiomatic style seperti tata bahasa baku. Anda tetap bisa dipahami dengan gaya acak, tapi komunikasi jadi lebih lambat dan rawan salah tafsir.

## Miskonsepsi Umum

- Miskonsepsi: "Pythonic berarti kode sesingkat mungkin."
  Klarifikasi: Pythonic menekankan kejelasan intent, bukan minim karakter.

- Miskonsepsi: "Kalau linter hijau, style sudah bagus."
  Klarifikasi: linter penting, tapi tidak menggantikan desain fungsi, naming, dan alur logika yang sehat.

- Miskonsepsi: "Style itu urusan kosmetik."
  Klarifikasi: style yang baik menurunkan beban kognitif dan biaya maintenance.

## Konsep Inti

### 1. Prinsip Dasar

Prinsip praktis idiomatic Python:

1. Use clear names
Nama fungsi/variabel harus menyampaikan intent bisnis.

2. Prefer simple flow
Gunakan guard clause untuk menghindari nested logic berlapis.

3. Use Python features responsibly
Comprehension, unpacking, dan context manager dipakai saat memperjelas kode, bukan untuk pamer trik.

4. Keep functions focused
Satu fungsi, satu tanggung jawab utama.

### 2. Dampak Praktis

Penerapan idiomatik memberi dampak nyata:

- review lebih cepat karena pola kode familiar
- onboarding developer baru lebih mudah
- refactor lebih aman karena struktur fungsi jelas
- bug lebih cepat ditemukan dari intent yang terbaca

Checklist refactor menuju idiomatic style:

1. apakah nama sudah menjelaskan tujuan
2. apakah alur logika terlalu dalam dan bisa diringkas
3. apakah ada fitur Python yang bisa membuat kode lebih jelas
4. apakah perubahan tetap menjaga perilaku asli

## Diagram

![Big picture Idiomatic Python and Style](assets/11_idiomatic_python_and_style.svg)

Caption: Diagram memperlihatkan hubungan antara prinsip idiomatic style dan dampaknya terhadap kualitas kolaborasi tim.

### Legenda Diagram

- 1: prinsip style Pythonic
- 2: penerapan pada struktur kode
- 3: dampak ke readability dan maintenance

## Contoh Kode (Benar)

```python
from pathlib import Path
from tempfile import TemporaryDirectory


def load_usernames(file_path: str) -> list[str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


with TemporaryDirectory() as temp_dir:
    users_path = Path(temp_dir) / "users.txt"
    users_path.write_text("alice\nbob\n\ncharlie\n", encoding="utf-8")
    print(load_usernames(str(users_path)))
```

Expected output:

```text
['alice', 'bob', 'charlie']
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
def load(file):
    f = open(file)
    data = []
    for x in f.readlines():
        if x.strip() != "":
            data.append(x.strip())
    f.close()
    return data
```

Masalah:

- nama fungsi/parameter terlalu umum
- tidak memakai context manager (`with`)
- style kondisi verbose dan kurang idiomatik

Perbaikan:

```python
from pathlib import Path


def load_usernames(file_path: str) -> list[str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]
```

## Catatan Praktis

- ikuti PEP 8 sebagai baseline konsistensi
- pakai comprehension jika hasilnya tetap mudah dibaca
- pilih `with` untuk resource management (file, lock, connection)
- hindari nama singkat tanpa konteks (`x`, `tmp`, `data` berlebihan)
- gabungkan formatter + linter + review manusia untuk kualitas style

## Latihan

### Dasar

Refactor satu fungsi non-idiomatic di proyek Anda agar menggunakan nama yang lebih jelas dan context manager jika relevan.

### Menengah

Ambil satu loop klasik, ubah menjadi list/dict comprehension yang tetap terbaca. Bandingkan mana yang lebih jelas.

### Mini Challenge

Buat file `student_report.py` berisi:

- fungsi load data siswa dari file teks
- fungsi hitung rata-rata nilai
- fungsi format output laporan

Syarat:

- gunakan naming deskriptif
- gunakan `with` untuk file handling
- tambahkan minimal 5 test case
- tulis 5-8 kalimat trade-off style yang Anda pilih (ringkas vs jelas)

## Checklist Lulus Bab

- [ ] memahami prinsip utama idiomatic Python
- [ ] mampu refactor kode non-idiomatic ke versi lebih jelas
- [ ] menyelesaikan mini challenge dan test
- [ ] mampu memberi alasan style decision saat code review

## Peta Keterkaitan

- Bab sebelumnya: 10_backward_compatibility_and_peps.md
- Bab berikutnya: 12_language_design_tradeoffs.md
- Keterkaitan lintas buku Core: CORE-15 (code quality), CORE-14 (testing)

## Ringkasan

- idiomatic Python adalah cara menulis yang natural, jelas, dan konsisten
- style yang baik mempercepat kolaborasi serta menurunkan biaya maintenance
- fitur bahasa Python dipakai untuk memperjelas, bukan memperumit
- keputusan style harus selalu ditimbang dengan readability tim

## FAQ Singkat

1. Apakah harus selalu pakai comprehension?
   Jawaban singkat: tidak; pakai hanya jika membuat intent lebih jelas.
2. Apakah PEP 8 wajib 100%?
   Jawaban singkat: jadikan baseline kuat; deviasi boleh jika ada alasan jelas dan konsisten.
3. Bagaimana menyeimbangkan style dan performa?
   Jawaban singkat: mulai dari style yang jelas, lalu optimasi berdasarkan data profiling nyata.

## Referensi

- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
- PEP 20 (Zen of Python): https://peps.python.org/pep-0020/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
