# 02_pola_detektif.py
# Pola Pencarian: Menyisir data sampai ketemu target

print("=== SISTEM SCANNER DAFTAR HADIR ===")

daftar_hadir = ["Budi", "Siti", "Ahmad", "Dewi", "Bambang"]
target = "Dewi"

# 1. Gunakan 'Flag' (Penanda)
ketemu = False
posisi = -1

# 2. Mulai menyisir
print(f"Mencari '{target}' dalam daftar...")

for index, nama in enumerate(daftar_hadir):
    if nama == target:
        ketemu = True
        posisi = index
        break  # Rahasia efisiensi: Berhenti jika sudah ketemu!

# 3. Laporkan hasil
if ketemu:
    print(f"DITEMUKAN! {target} ada di urutan nomor {posisi + 1}.")
else:
    print(f"TIDAK ADA: Nama {target} tidak terdaftar hari ini.")
