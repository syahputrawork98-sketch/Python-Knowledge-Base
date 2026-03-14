# 02_baca_arsip.py
# Simulasi Membaca Buku: Mengambil data dari harddisk

print("=== SISTEM PEMBACAAN ARSIP ===")

try:
    # Membuka file dengan mode 'r' (Read) - mode default jika tidak ditulis
    with open("catatan_saya.txt", "r", encoding="utf-8") as file:
        # Membaca seluruh isi sekaligus
        konten = file.read()
        
    print("Isi file ditemukan:")
    print("-" * 30)
    print(konten)
    print("-" * 30)

except FileNotFoundError:
    print("Error: File 'catatan_saya.txt' belum dibuat.")
    print("Silakan jalankan skrip '01_tulis_catatan.py' terlebih dahulu!")
