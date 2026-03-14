# Errors as Part of Design

Chapter Code: CORE-02-08
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Intermediate
Estimated Time: 45 menit teori + 35 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas error sebagai bagian dari desain API, bukan sekadar kejadian saat runtime. Di Python, cara kita memunculkan, menangkap, dan menyampaikan error sangat memengaruhi kejelasan kontrak fungsi, kualitas debugging, dan keandalan sistem.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-07
- memahami exception dasar (`try`, `except`, `raise`)
- memahami fungsi dan type hint sederhana

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| fail-fast | gagal secepat mungkin saat kondisi invalid terdeteksi | validasi input di awal fungsi |
| exception contract | jenis error yang mungkin muncul dari sebuah API | `ValueError` untuk input invalid |
| error propagation | aliran error ke lapisan atas jika tidak ditangani lokal | raise ulang dari service ke controller |
| error context | informasi tambahan agar debugging mudah | pesan error menyertakan field bermasalah |
| custom exception | exception khusus domain bisnis | `PaymentValidationError` |

## Tujuan Besar

Membantu pembaca merancang penanganan error yang eksplisit, konsisten, dan informatif agar sistem lebih mudah diuji dan dirawat.

## Tujuan Kecil

- membedakan error yang harus ditangani lokal vs diteruskan
- menulis pesan error yang actionable
- menghindari anti-pattern seperti `except Exception` tanpa alasan

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- mendefinisikan exception contract untuk fungsi penting
- merancang jalur error yang dapat diprediksi
- memperbaiki kode yang menelan error secara diam-diam

## Peruntukan

Bab ini digunakan saat:

- merancang fungsi/service untuk dipakai modul lain
- menyusun standar error handling tim
- memperbaiki bug yang sulit dilacak karena error message buruk

## Bukan Peruntukan

Bab ini bukan untuk:

- membahas observability stack secara penuh (logging/metrics/tracing)
- membahas internals exception object secara low-level
- menggantikan desain arsitektur reliability skala enterprise

## Analogi

Error handling seperti alarm kebakaran. Alarm yang jelas dan tepat waktu membantu respons cepat. Alarm yang dimatikan diam-diam membuat masalah kecil berubah jadi insiden besar.

## Miskonsepsi Umum

- Miskonsepsi: "Error harus selalu ditangkap agar aplikasi tidak crash."
  Klarifikasi: tidak semua error harus ditelan; banyak error lebih aman diteruskan setelah diberi konteks.

- Miskonsepsi: "Pesan error tidak penting, yang penting tipe exception."
  Klarifikasi: pesan error menentukan seberapa cepat orang bisa memperbaiki masalah.

- Miskonsepsi: "`except Exception` aman untuk berjaga-jaga."
  Klarifikasi: penangkapan terlalu luas sering menyembunyikan bug serius.

## Konsep Inti

### 1. Prinsip Dasar

Empat prinsip desain error yang sehat:

1. Validate early
Periksa input di awal agar kegagalan terjadi dekat sumber masalah.

2. Raise specific exception
Gunakan tipe exception yang tepat untuk menjaga kontrak API tetap jelas.

3. Add useful context
Sertakan informasi field/kondisi yang relevan di pesan error.

4. Catch only what you can handle
Tangkap error hanya jika Anda bisa memulihkan, menerjemahkan, atau menambah konteks yang bernilai.

### 2. Dampak Praktis

Penerapan prinsip ini memberi dampak langsung:

- debugging lebih cepat
- test error path lebih mudah ditulis
- integrasi antar modul lebih aman karena kontrak error jelas
- incident production lebih mudah ditriase

Checklist desain error untuk fungsi publik:

1. input invalid apa saja yang mungkin terjadi
2. exception apa yang akan dipakai untuk tiap kasus
3. pesan error apakah jelas dan actionable
4. lapisan mana yang bertanggung jawab menangkap error

## Diagram

![Big picture Errors as Part of Design](assets/08_errors_as_part_of_design.svg)

Caption: Diagram memperlihatkan bagaimana desain error yang baik menghubungkan validasi, exception contract, dan respons sistem.

### Legenda Diagram

- 1: validasi dan deteksi masalah
- 2: raise/catch sesuai kontrak
- 3: dampak ke keandalan dan maintainability

## Contoh Kode (Benar)

```python
class PaymentValidationError(ValueError):
    pass


def validate_payment(amount: float, currency: str) -> None:
    if amount <= 0:
        raise PaymentValidationError("amount must be > 0")
    if currency not in {"IDR", "USD"}:
        raise PaymentValidationError("currency must be IDR or USD")


def create_payment(amount: float, currency: str) -> str:
    validate_payment(amount, currency)
    return "payment_created"


print(create_payment(150_000, "IDR"))
```

Expected output:

```text
payment_created
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
def create_payment(amount, currency):
    try:
        if amount <= 0:
            raise ValueError("invalid")
        return "payment_created"
    except Exception:
        return None
```

Masalah:

- menelan semua error dan kehilangan konteks
- kontrak return tidak konsisten (`str` atau `None`)
- caller sulit membedakan validasi gagal vs bug internal

Perbaikan:

```python
class PaymentValidationError(ValueError):
    pass


def create_payment(amount: float, currency: str) -> str:
    if amount <= 0:
        raise PaymentValidationError("amount must be > 0")
    if currency not in {"IDR", "USD"}:
        raise PaymentValidationError("currency must be IDR or USD")
    return "payment_created"
```

## Catatan Praktis

- selalu prioritaskan exception spesifik daripada generik
- jangan gunakan sentinel value (`None`, `False`) untuk menutupi error tanpa kontrak jelas
- log di boundary aplikasi, bukan di semua lapisan
- tulis test untuk jalur gagal, bukan hanya jalur sukses
- jika menerjemahkan error lintas layer, pertahankan konteks penting

## Latihan

### Dasar

Buat fungsi validasi email yang me-raise `ValueError` dengan pesan berbeda untuk input kosong dan format salah.

### Menengah

Refactor fungsi yang menggunakan `except Exception` menjadi penanganan exception spesifik dengan pesan yang lebih informatif.

### Mini Challenge

Buat file `order_service.py` berisi:

- custom exception `OrderValidationError`
- fungsi validasi `order_id`, `quantity`, dan `price`
- fungsi `create_order` yang memanggil validasi

Tambahkan minimal 6 test case (3 sukses, 3 gagal), lalu tulis 5-8 kalimat tentang keputusan exception contract yang Anda pilih.

## Checklist Lulus Bab

- [ ] memahami error sebagai bagian kontrak API
- [ ] mampu menulis exception spesifik dan pesan actionable
- [ ] menyelesaikan mini challenge beserta test
- [ ] mampu membedakan kapan menangkap vs meneruskan error

## Peta Keterkaitan

- Bab sebelumnya: 07_duck_typing_and_protocols.md
- Bab berikutnya: 09_batteries_included_mindset.md
- Keterkaitan lintas buku Core: CORE-12 (reliability), CORE-14 (testing)

## Ringkasan

- error handling adalah keputusan desain, bukan sekadar teknis runtime
- exception contract yang jelas meningkatkan prediktabilitas API
- pesan error yang baik mempercepat debugging dan review
- anti-pattern menelan error diam-diam harus dihindari

## FAQ Singkat

1. Apakah semua error harus jadi custom exception?
   Jawaban singkat: tidak; gunakan exception bawaan jika cukup jelas, custom exception saat butuh konteks domain.
2. Kapan sebaiknya menangkap exception?
   Jawaban singkat: saat Anda bisa memulihkan, menerjemahkan, atau menambah konteks yang berguna.
3. Bolehkah return `None` saat gagal?
   Jawaban singkat: boleh jika kontraknya eksplisit; untuk kegagalan validasi umumnya exception lebih jelas.

## Referensi

- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
- Built-in Exceptions: https://docs.python.org/3/library/exceptions.html
- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
