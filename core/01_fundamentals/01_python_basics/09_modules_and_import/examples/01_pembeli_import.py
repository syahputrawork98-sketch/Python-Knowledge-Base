# 01_pembeli_import.py
# Simulasi Pemesanan Kargo: Cara mengimpor dan menggunakan module

# 1. Cara Pertama: Import Utuh (Satu Kotak)
import toko_alat

# 2. Cara Kedua: Import Spesifik (Kurir Khusus)
from toko_alat import hitung_harga_obeng

print(f"Selamat datang di {toko_alat.NAMA_TOKO}")

# Menggunakan alat dari kotak utuh
total_palu = toko_alat.hitung_harga_palu(3)
print(f"Harga 3 Palu: Rp {total_palu:,}")

# Menggunakan alat yang dipesan spesifik
total_obeng = hitung_harga_obeng(5)
print(f"Harga 5 Obeng: Rp {total_obeng:,}")
