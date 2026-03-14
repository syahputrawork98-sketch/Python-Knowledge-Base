# Simple vs Complex

Chapter Code: CORE-02-05
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Intermediate
Estimated Time: 45 menit teori + 35 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas trade-off antara solusi sederhana dan solusi kompleks dalam Python. Tujuan utamanya bukan menghindari kompleksitas total, tetapi memastikan kompleksitas yang dipakai memang perlu dan memberikan nilai jelas.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-04
- memahami fungsi, class dasar, list/dict comprehension
- memahami error handling dan refactor sederhana

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| simplicity | tingkat kesederhanaan desain dan implementasi | fungsi kecil dengan satu tujuan |
| complexity | jumlah komponen/interaksi yang harus dipahami | banyak cabang kondisi dan abstraction layer |
| accidental complexity | kompleksitas yang muncul karena desain buruk | util generic berlebihan untuk kasus kecil |
| essential complexity | kompleksitas inti dari masalah domain | aturan pricing bertingkat yang memang wajib |
| over-engineering | membangun solusi terlalu berat untuk kebutuhan kecil | membuat framework internal prematur |

## Tujuan Besar

Membantu pembaca membedakan kompleksitas yang sah dengan kompleksitas yang tidak perlu, lalu memilih desain yang tepat untuk konteks proyek.

## Tujuan Kecil

- mengenali sinyal over-engineering pada kode Python
- menyederhanakan alur tanpa menghilangkan kebutuhan bisnis
- menilai kapan abstraksi baru memang layak ditambahkan

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- mengidentifikasi accidental complexity pada contoh kode
- melakukan refactor dari desain terlalu rumit ke versi lebih sederhana
- memberi justifikasi teknis saat memilih pendekatan kompleks

## Peruntukan

Bab ini digunakan saat:

- merancang API/helper baru di project
- memutuskan kapan perlu membuat abstraction layer
- meninjau pull request yang terasa "terlalu pintar"

## Bukan Peruntukan

Bab ini bukan untuk:

- membuktikan bahwa solusi sederhana selalu paling benar
- pembahasan optimisasi performa skala besar secara mendalam
- meniadakan pola desain yang memang diperlukan domain kompleks

## Analogi

Membangun software seperti mengemas barang. Kotak sederhana cukup untuk benda ringan. Untuk barang rapuh dan berat, kemasan lebih kompleks diperlukan. Masalahnya bukan kompleks atau tidak, tapi apakah tingkat kompleksitasnya tepat.

## Miskonsepsi Umum

- Miskonsepsi: "Simple berarti selalu pendek."
  Klarifikasi: simple berarti mudah dipahami dan dipelihara, bukan sekadar sedikit baris.

- Miskonsepsi: "Complex pasti jelek."
  Klarifikasi: beberapa domain memang menuntut kompleksitas esensial.

- Miskonsepsi: "Abstraksi dini menghemat waktu jangka panjang."
  Klarifikasi: abstraksi prematur sering menambah beban perubahan di tahap awal.

## Konsep Inti

### 1. Prinsip Dasar

Gunakan empat pertanyaan untuk menilai desain simple vs complex:

1. Apakah kompleksitas ini berasal dari masalah bisnis atau dari desain kita sendiri?

2. Apakah tim saat ini mampu memahami dan merawat solusi ini?

3. Apakah solusi kompleks ini memberi manfaat terukur (reusability, safety, performance)?

4. Jika kebutuhan berubah, mana yang lebih aman diubah: versi sederhana atau versi kompleks?

Prinsip praktis: mulai dari desain paling sederhana yang benar, lalu naikkan kompleksitas secara bertahap jika dibutuhkan bukti nyata.

### 2. Dampak Praktis

Dalam coding harian, keputusan ini memengaruhi:

- ukuran dan tanggung jawab fungsi
- jumlah abstraction layer
- pola dependency antar modul
- biaya onboarding developer baru

Tanda desain terlalu kompleks:

- satu fitur kecil butuh banyak file/kelas
- nama abstraksi terlalu umum dan sulit ditelusuri
- test sulit ditulis karena banyak coupling
- perubahan kecil memicu efek domino

## Diagram

![Big picture Simple vs Complex](assets/05_simple_vs_complex.svg)

Caption: Diagram memetakan jalur pengambilan keputusan dari solusi sederhana menuju kompleksitas terkontrol jika benar-benar diperlukan.

### Legenda Diagram

- 1: kebutuhan nyata
- 2: evaluasi biaya-manfaat desain
- 3: keputusan level kompleksitas

## Contoh Kode (Benar)

```python
def calculate_shipping_cost(weight_kg: float, is_express: bool) -> float:
    if weight_kg <= 0:
        raise ValueError("weight_kg must be > 0")

    base_cost = 10_000
    extra_weight_cost = max(0, weight_kg - 1) * 2_000
    express_cost = 15_000 if is_express else 0

    return base_cost + extra_weight_cost + express_cost


print(calculate_shipping_cost(2.5, True))
```

Expected output:

```text
28000.0
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
class ShippingCostEngine:
    def __init__(self, strategy_registry, config_provider, feature_flags):
        self.strategy_registry = strategy_registry
        self.config_provider = config_provider
        self.feature_flags = feature_flags

    def run(self, payload):
        # abstraksi terlalu berat untuk aturan biaya sederhana
        pass
```

Masalah:

- banyak abstraksi sebelum kebutuhan nyata muncul
- menaikkan biaya maintenance dan testing
- sulit dipahami developer baru

Perbaikan:

```python
def calculate_shipping_cost(weight_kg: float, is_express: bool) -> float:
    if weight_kg <= 0:
        raise ValueError("weight_kg must be > 0")

    base_cost = 10_000
    extra_weight_cost = max(0, weight_kg - 1) * 2_000
    express_cost = 15_000 if is_express else 0

    return base_cost + extra_weight_cost + express_cost
```

## Catatan Praktis

- mulai dari desain sederhana yang memenuhi kebutuhan saat ini
- tambahkan abstraksi hanya jika ada duplikasi/pola yang stabil
- ukur biaya perubahan, bukan hanya keindahan arsitektur
- hindari class/strategy jika fungsi tunggal sudah cukup jelas
- dokumentasikan alasan saat menaikkan kompleksitas desain

## Latihan

### Dasar

Ambil satu fungsi yang terlalu panjang. Pecah menjadi 2-3 fungsi kecil dengan tanggung jawab jelas.

### Menengah

Temukan satu area over-engineering di proyek Anda dan usulkan versi simplifikasi tanpa mengubah perilaku bisnis.

### Mini Challenge

Buat file `shipping.py` berisi:

- fungsi hitung biaya reguler
- fungsi hitung biaya express
- fungsi orkestrasi total biaya kirim

Tambahkan minimal 5 test case, lalu tulis 5-8 kalimat: kompleksitas apa yang Anda sengaja hindari dan kompleksitas apa yang tetap dipertahankan.

## Checklist Lulus Bab

- [ ] memahami perbedaan accidental vs essential complexity
- [ ] mampu menyederhanakan desain tanpa kehilangan aturan bisnis
- [ ] menyelesaikan mini challenge dan test
- [ ] mampu menjelaskan justifikasi saat memilih solusi kompleks

## Peta Keterkaitan

- Bab sebelumnya: 04_consistency_and_practicality.md
- Bab berikutnya: 06_mutability_and_object_thinking.md
- Keterkaitan lintas buku Core: CORE-04 (object model), CORE-14 (testing)

## Ringkasan

- kesederhanaan adalah default terbaik untuk kebanyakan kasus
- kompleksitas boleh ditambah bertahap saat manfaatnya nyata
- over-engineering memperlambat tim dan menaikkan biaya maintenance
- desain yang baik menjaga keseimbangan antara kebutuhan saat ini dan pertumbuhan masa depan

## FAQ Singkat

1. Kapan saat tepat menambah abstraction layer?
   Jawaban singkat: saat pola kebutuhan sudah berulang dan stabil, bukan saat masih spekulatif.
2. Apakah fungsi panjang selalu buruk?
   Jawaban singkat: tidak selalu, tapi fungsi panjang sering jadi sinyal tanggung jawab bercampur.
3. Bagaimana mencegah over-engineering di tim?
   Jawaban singkat: gunakan prinsip "build for now, design for change" dan validasi lewat review.

## Referensi

- PEP 20 (Zen of Python): https://peps.python.org/pep-0020/
- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
