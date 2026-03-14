# 01_sistem_tilang.py
# Simulasi Persimpangan: Deteksi Kecepatan Kendaraan

print("=== SISTEM DETEKSI KECEPATAN OTOMATIS ===")

kecepatan = float(input("Masukkan kecepatan kendaraan (km/jam): "))

# 1. Gerbang if (Kondisi Utama)
if kecepatan > 100:
    print("STATUS: PELANGGARAN BERAT!")
    print("Mobil Anda terdeteksi melaju sangat kencang. Tilang otomatis diproses.")

# 2. Gerbang elif (Kondisi Alternatif)
elif kecepatan > 80:
    print("STATUS: PERINGATAN.")
    print("Anda sedikit melewati batas. Harap kurangi kecepatan.")

# 3. Gerbang else (Kondisi Sisa)
else:
    print("STATUS: AMAN.")
    print("Selamat berkendara dengan tertib.")

print("\n(Hanya satu gerbang yang bisa dilalui oleh mobil Anda hari ini)")
