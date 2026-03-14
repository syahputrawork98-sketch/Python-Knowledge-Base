# 01_pembagi_aman.py
# Simulasi Jaring Pengaman: Menangani pembagian nol & salah input

print("=== SISTEM PEMBAGIAN AMAN ===")

try:
    # Blok 'try': Zona Eksperimen Berisiko
    pembilang = float(input("Masukkan angka yang ingin dibagi: "))
    panyebut = float(input("Masukkan angka pembagi: "))
    
    hasil = pembilang / panyebut

except ZeroDivisionError:
    # Tim Pemadam untuk Api Spesifik: Pembagian Nol
    print("\n[ALARM]: Terjadi korsleting! Tidak boleh membagi dengan nol.")
    hasil = "Tak Terhingga"

except ValueError:
    # Tim Pemadam untuk Api Spesifik: Bukan Angka
    print("\n[ALARM]: Bahan baku salah! Harap masukkan angka, bukan huruf.")
    hasil = "Error"

else:
    # Dijalankan HANYA jika tidak ada alarm kebakaran
    print("\n[LAPORAN]: Eksperimen sukses tanpa percikan api.")

finally:
    # Selalu dijalankan: Mematikan lampu ruangan
    print("[PROTOKOL]: Membersihkan meja kerja...")

print(f"\nHasil akhir Eksperimen: {hasil}")
