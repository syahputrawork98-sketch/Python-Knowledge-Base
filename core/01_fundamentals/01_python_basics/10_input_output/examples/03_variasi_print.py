# 03_variasi_print.py
# Simulasi Protokol Pengumuman: Teknik Mempercantik Print

print("=== PROTOKOL PENGUMUMAN ===")

# 1. Menggunakan Separator (sep)
print("Menu Hari Ini:", "Sate", "Gulai", "Rendang", sep=" | ")

# 2. Menggunakan End (end)
print("Sedang Memasak", end="... ")
print("Makanannya Sudah Matang!")

# 3. F-String dengan Perkalian (Alignment)
nama_menu = "Sate Kambing"
harga = 25000

print(f"\n{'BON PESANAN':^30}")
print("-" * 30)
print(f"{nama_menu:<20} Rp {harga:>7,}")
print("-" * 30)
