# 03_tambah_log.py
# Simulasi Menambah Catatan: Menggunakan mode 'a' (Append)

import datetime

print("=== SISTEM PENCATATAN LOG (APPEND) ===")

waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
pesan_log = f"Akses program pada: {waktu_sekarang}\n"

# Membuka file dengan mode 'a' (Append)
# Tidak menghapus isi lama, justru menambah di baris paling bawah.
with open("riwayat_akses.log", "a", encoding="utf-8") as log_file:
    log_file.write(pesan_log)

print("Berhasil menambahkan baris log baru ke 'riwayat_akses.log'.")
print("Cobalah jalankan skrip ini berkali-kali dan lihat isinya bertambah!")
