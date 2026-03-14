# Duck Typing and Protocols

Chapter Code: CORE-02-07
Book Code: CORE-02
Version: v0.2.1
Last Updated: 2026-03-08
Status: Draft
Difficulty: Intermediate
Estimated Time: 45 menit teori + 40 menit praktik

## Bab Ini Tentang Apa

Bab ini membahas pendekatan duck typing di Python: objek dinilai dari perilakunya (method/atribut yang tersedia), bukan dari garis keturunan class semata. Bab ini juga memperkenalkan `Protocol` sebagai cara modern untuk membuat kontrak antarkomponen tanpa coupling berlebihan.

## Prasyarat Spesifik Bab

- sudah menyelesaikan CORE-02-01 sampai CORE-02-06
- memahami class, inheritance dasar, dan type hint
- memahami exception handling dan refactor sederhana

## Istilah Kunci

| Istilah | Definisi Singkat | Contoh |
|---|---|---|
| duck typing | pendekatan berbasis perilaku objek | objek apa pun yang punya `.read()` bisa dipakai |
| protocol | kontrak struktur/perilaku tanpa wajib inheritance | `typing.Protocol` |
| structural typing | kecocokan ditentukan dari shape, bukan parent class | punya method yang disyaratkan |
| nominal typing | kecocokan ditentukan dari deklarasi tipe/pewarisan | `isinstance(obj, BaseClass)` |
| loose coupling | ketergantungan antarkomponen rendah | fungsi menerima interface perilaku |

## Tujuan Besar

Membantu pembaca merancang API Python yang fleksibel namun tetap jelas kontraknya, sehingga mudah dikembangkan dan diuji.

## Tujuan Kecil

- memahami kapan duck typing menguntungkan
- menulis kontrak perilaku dengan `Protocol`
- menghindari coupling berlebihan ke class konkret

## Hasil Belajar

Setelah menyelesaikan bab ini, pembaca diharapkan mampu:

- membedakan duck typing, nominal typing, dan structural typing
- mendesain fungsi yang menerima objek berdasarkan kapabilitas
- memakai `Protocol` untuk meningkatkan kejelasan kolaborasi tim

## Peruntukan

Bab ini digunakan saat:

- membuat service/repository abstraction
- menyiapkan kode yang mudah di-mock saat testing
- membangun library internal yang extensible

## Bukan Peruntukan

Bab ini bukan untuk:

- membahas type checker secara penuh dan lanjutan
- menggantikan materi OOP mendalam tentang inheritance tree besar
- pembahasan plugin architecture skala enterprise

## Analogi

Duck typing seperti meminjam charger. Anda tidak peduli merek ponselnya; yang penting konektornya cocok dan bisa mengisi daya.

## Miskonsepsi Umum

- Miskonsepsi: "Duck typing berarti tanpa kontrak sama sekali."
  Klarifikasi: kontrak tetap perlu, hanya bentuknya berbasis perilaku, bukan class induk.

- Miskonsepsi: "Harus selalu pakai inheritance untuk polymorphism."
  Klarifikasi: di Python, banyak kasus lebih sederhana dengan structural typing.

- Miskonsepsi: "Protocol hanya untuk type checker, tidak ada dampak desain."
  Klarifikasi: Protocol memaksa kita merumuskan kontrak yang lebih bersih dan fokus.

## Konsep Inti

### 1. Prinsip Dasar

Empat prinsip desain duck typing yang sehat:

1. Program to behavior, not concrete class
Fungsi menerima objek yang mampu melakukan aksi tertentu.

2. Keep protocol minimal
Definisikan method seminimal mungkin sesuai kebutuhan use case.

3. Fail clearly
Jika kapabilitas tidak ada, error harus jelas dan cepat terlihat.

4. Use Protocol for communication
Gunakan `Protocol` untuk mendokumentasikan kontrak antar modul/tim.

### 2. Dampak Praktis

Dampaknya dalam pengembangan harian:

- komponen lebih mudah ditukar (swap implementation)
- testing lebih ringan karena mock/fake object sederhana
- integrasi lintas modul lebih cepat jika kontrak perilaku jelas
- refactor class internal lebih aman selama kontrak tetap terpenuhi

Checklist saat mendesain fungsi berbasis duck typing:

1. method apa yang benar-benar dibutuhkan fungsi ini
2. apakah kontrak itu sudah ditulis jelas (docstring/type hint/Protocol)
3. apakah error message cukup jelas saat objek tidak kompatibel
4. apakah desain ini mengurangi ketergantungan ke class konkret

## Diagram

![Big picture Duck Typing and Protocols](assets/07_duck_typing_and_protocols.svg)

Caption: Diagram menunjukkan alur dari kontrak perilaku ke desain komponen yang fleksibel dan mudah diuji.

### Legenda Diagram

- 1: kebutuhan perilaku
- 2: definisi protocol/kontrak
- 3: implementasi yang dapat dipertukarkan

## Contoh Kode (Benar)

```python
from typing import Protocol


class Writer(Protocol):
    def write(self, message: str) -> None:
        ...


def send_report(writer: Writer, title: str) -> None:
    writer.write(f"[REPORT] {title}")


class ConsoleWriter:
    def write(self, message: str) -> None:
        print(message)


send_report(ConsoleWriter(), "Monthly Revenue")
```

Expected output:

```text
[REPORT] Monthly Revenue
```

## Pitfall Umum

Contoh kesalahan yang sering terjadi:

```python
class ConsoleWriter:
    def write(self, message: str) -> None:
        print(message)


def send_report(console_writer: ConsoleWriter, title: str) -> None:
    # coupling ke class konkret, susah ditukar implementasinya
    console_writer.write(f"[REPORT] {title}")
```

Masalah:

- fungsi bergantung pada implementasi spesifik
- sulit reuse dengan writer lain (file, network, test double)
- memperbesar biaya perubahan

Perbaikan:

```python
from typing import Protocol


class Writer(Protocol):
    def write(self, message: str) -> None:
        ...


def send_report(writer: Writer, title: str) -> None:
    writer.write(f"[REPORT] {title}")
```

## Catatan Praktis

- gunakan Protocol kecil dan fokus use case
- hindari interface "gemuk" yang memaksa implementasi tidak perlu
- pada boundary publik, type hint + docstring wajib jelas
- pilih duck typing untuk fleksibilitas, pilih class konkret jika domain memang tetap
- validasi runtime tetap penting untuk input eksternal

## Latihan

### Dasar

Buat dua class berbeda (`ConsoleWriter`, `FileWriter`) yang sama-sama punya method `write` dan pakai satu fungsi pengirim laporan yang sama.

### Menengah

Refactor fungsi yang saat ini menerima class konkret menjadi menerima `Protocol` minimal.

### Mini Challenge

Buat file `notifier.py` berisi:

- `Protocol` bernama `Notifier` dengan method `send(message: str) -> None`
- dua implementasi: `EmailNotifier` dan `SmsNotifier`
- satu fungsi `broadcast` yang menerima daftar `Notifier`

Tambahkan minimal 5 test case (termasuk fake notifier untuk testing), lalu tulis 5-8 kalimat tentang trade-off fleksibilitas vs kejelasan kontrak.

## Checklist Lulus Bab

- [ ] memahami konsep duck typing dan structural typing
- [ ] mampu mendefinisikan Protocol yang minimal dan jelas
- [ ] menyelesaikan mini challenge beserta test
- [ ] mampu menjelaskan kapan coupling ke class konkret masih masuk akal

## Peta Keterkaitan

- Bab sebelumnya: 06_mutability_and_object_thinking.md
- Bab berikutnya: 08_errors_as_part_of_design.md
- Keterkaitan lintas buku Core: CORE-06 (typing), CORE-14 (testing)

## Ringkasan

- duck typing menekankan kapabilitas, bukan identitas class
- Protocol membantu mendokumentasikan kontrak perilaku dengan rapi
- desain berbasis perilaku menurunkan coupling dan memudahkan testing
- fleksibilitas tetap harus dijaga dengan kontrak yang eksplisit

## FAQ Singkat

1. Apakah Protocol selalu lebih baik daripada inheritance?
   Jawaban singkat: tidak; gunakan Protocol untuk kontrak perilaku lintas implementasi, inheritance untuk relasi domain yang benar-benar hierarkis.
2. Apakah duck typing berbahaya tanpa type checker?
   Jawaban singkat: bisa, jika kontrak tidak jelas; minimalkan risiko dengan type hint, test, dan error message yang baik.
3. Kapan boleh tetap memakai class konkret sebagai parameter?
   Jawaban singkat: saat kebutuhan memang spesifik ke implementasi tersebut dan kecil kemungkinan ditukar.

## Referensi

- Python Tutorial: https://docs.python.org/3/tutorial/
- Python Language Reference: https://docs.python.org/3/reference/
- `typing.Protocol` docs: https://docs.python.org/3/library/typing.html#typing.Protocol
- PEP 544 (Protocols): https://peps.python.org/pep-0544/
