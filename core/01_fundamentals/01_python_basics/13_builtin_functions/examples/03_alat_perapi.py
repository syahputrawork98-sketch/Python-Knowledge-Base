# 03_alat_perapi.py
# Simulasi Alat Perapi: Bermain dengan Urutan

print("=== SISTEM PENATAAN RAK ===")

# Rak yang berantakan
rak_buku = ["Geografi", "Astronomi", "Biologi", "Fisika"]
print(f"Rak Awal: {rak_buku}")

# 1. sorted() - Membuat tatanan baru tanpa merusak aslinya
rak_rapi = sorted(rak_buku)
print(f"Rak Rapi (Sorted)     : {rak_rapi}")
print(f"Rak Asli (Tetap)      : {rak_buku} <-- Masih berantakan!")

# 2. reversed() - Membalik urutan (menghasilkan objek khusus)
rak_terbalik = list(reversed(rak_buku))
print(f"Rak Terbalik (Reversed): {rak_terbalik}")

# 3. any() & all() - Pengecekan Kualitas
pemeriksaan = [True, True, False]
print(f"\nStatus Pemeriksaan: {pemeriksaan}")
print(f"Apakah ADA yang lulus? : {any(pemeriksaan)}")
print(f"Apakah SEMUA lulus?     : {all(pemeriksaan)}")
