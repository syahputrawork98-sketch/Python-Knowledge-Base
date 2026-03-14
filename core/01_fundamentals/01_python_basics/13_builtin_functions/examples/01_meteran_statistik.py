# 01_meteran_statistik.py
# Simulasi Sabuk Alat Tukang: Menggunakan Meteran dan Alat Hitung

print("=== GUDANG MATERIAL TUKANG ===")

# Tumpukan material (Koleksi data)
berat_kayu = [12.5, 8.2, 15.0, 9.7, 11.1]

# 1. len() - Seperti Meteran: Menghitung jumlah kayu
jumlah_kayu = len(berat_kayu)
print(f"Jumlah Balok Kayu: {jumlah_kayu} buah")

# 2. max() & min() - Mencari yang paling ekstrem
paling_berat = max(berat_kayu)
paling_ringan = min(berat_kayu)
print(f"Balok Paling Berat : {paling_berat} kg")
print(f"Balok Paling Ringan: {paling_ringan} kg")

# 3. sum() - Menghitung total berat sekaligus
total_berat = sum(berat_kayu)
print(f"Total Berat Seluruhnya: {total_berat} kg")

# Bonus: Menghitung rata-rata secara manual gabungan alat
rata_rata = total_berat / jumlah_kayu
print(f"Rata-rata Berat Kayu: {rata_rata:.2f} kg")
