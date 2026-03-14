# 03_kantong_unik_set.py
# Simulasi Keranjang Sortir: Keunikan & Operasi Himpunan

print("=== SORTIR TAMU UNDANGAN (SET) ===")

# Data mentah yang kotor (Banyak duplikat)
data_masuk = ["Ana", "Budi", "Ana", "Citra", "Budi", "Dedi"]
print(f"Data Mentah: {data_masuk}")

# 1. Otomatis membersihkan duplikat
tamu_unik = set(data_masuk)
print(f"Tamu Unik: {tamu_unik}")

# 2. Operasi Himpunan
tamu_vip = {"Ana", "Zaka"}
print(f"Tamu VIP: {tamu_vip}")

# IRISAN (Siapa tamu yang juga VIP?)
yang_datang_dan_vip = tamu_unik & tamu_vip
print(f"Tamu VIP yang hadir: {yang_datang_dan_vip}")

# GABUNGAN (Total semua orang unik di database)
semua_orang = tamu_unik | tamu_vip
print(f"Total database orang: {semua_orang}")

# DIFERENSI (Tamu biasa yang bukan VIP)
tamu_biasa = tamu_unik - tamu_vip
print(f"Tamu Biasa (Bukan VIP): {tamu_biasa}")
