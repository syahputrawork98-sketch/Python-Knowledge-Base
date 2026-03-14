# 02_kordinat_tuple.py
# Simulasi Kotak Segel: Data Permanen (Immutable)

print("=== REKAMAN KORDINAT (TUPLE) ===")

# Definisi: Memakai tanda kurung ()
# Anggaplah ini kordinat harta karun yang tidak boleh digeser
lokasi_harta = (-6.208, 106.845)

print(f"Lokasi Target: {lokasi_harta}")

# 1. Mencoba mengubah (Akan ERROR jika diaktifkan)
# lokasi_harta[0] = -7.0 
# Pesan: TypeError: 'tuple' object does not support item assignment

# 2. Teknik Unpacking (Membongkar kotak)
lintang, bujur = lokasi_harta
print(f"Terbongkar -> Lintang: {lintang}, Bujur: {bujur}")

# 3. Tuple 1 Item (Jebakan Batman)
bukan_tuple = (10)   # Ini dianggap Integer biasa oleh Python
adalah_tuple = (10,) # WAJIB tanda koma untuk 1 item
print(f"Tipe (10) : {type(bukan_tuple)}")
print(f"Tipe (10,): {type(adalah_tuple)}")
