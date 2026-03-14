# 04_pola_statistik.py
# Pola Penghitung: Menghitung frekuensi kejadian spesifik

print("=== SISTEM ANALISIS LOG KENDARAAN ===")

# Data kendaraan yang lewat (Log)
log_jalan = ["Motor", "Mobil", "Motor", "Motor", "Truk", "Mobil", "Motor"]

# 1. Inisialisasi penghitung
hitung_motor = 0
hitung_mobil = 0

# 2. Proses perhitungan
for kendaraan in log_jalan:
    if kendaraan == "Motor":
        hitung_motor += 1
    elif kendaraan == "Mobil":
        hitung_mobil += 1

# 3. Hasil Statistik
print(f"Total Kendaraan: {len(log_jalan)}")
print(f"- Jumlah Motor: {hitung_motor}")
print(f"- Jumlah Mobil: {hitung_mobil}")
print(f"- Lainnya     : {len(log_jalan) - (hitung_motor + hitung_mobil)}")
