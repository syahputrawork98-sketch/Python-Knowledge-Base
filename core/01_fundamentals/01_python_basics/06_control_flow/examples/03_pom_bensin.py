# 03_pom_bensin.py
# Simulasi Bundaran: Terus berjalan selama kondisi True

print("=== PENGISIAN BBM OTOMATIS ===")

kapasitas_maks = 5.0
tangki_saat_ini = 0.0

# Selama tangki belum penuh (Kondisi True)
# Kita terus berada di dalam 'bundaran' perulangan
while tangki_saat_ini < kapasitas_maks:
    tangki_saat_ini += 1.2
    
    # Mencegah angka melampaui batas untuk tampilan
    if tangki_saat_ini > kapasitas_maks:
        tangki_saat_ini = kapasitas_maks

    print(f"Sedang mengisi... [{tangki_saat_ini:.1f} / {kapasitas_maks} Liter]")

print("KLIK! Tangki Penuh. Silakan keluar dari bundaran pengisian.")
