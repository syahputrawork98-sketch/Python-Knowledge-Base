# 03_pola_ayakan.py
# Pola Penyaringan: Mengambil yang 'lolos sensor' saja

print("=== SISTEM SELEKSI NILAI LULUS ===")

semua_nilai = [45, 88, 70, 55, 92, 60, 30]
ambang_batas = 65

print(f"Daftar Nilai: {semua_nilai}")
print(f"Ambang Batas Kelulusan: {ambang_batas}")

# 1. Siapkan 'Wadah Baru' (Ayakan)
daftar_lulus = []

# 2. Proses penyaringan
for nilai in semua_nilai:
    if nilai >= ambang_batas:
        daftar_lulus.append(nilai)

# 3. Hasil
print("-" * 30)
print(f"NILAI YANG LULUS: {daftar_lulus}")
print(f"Jumlah yang lulus: {len(daftar_lulus)} dari {len(semua_nilai)} siswa.")
