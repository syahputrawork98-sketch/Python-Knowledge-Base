# 01_rak_belanja_list.py
# Simulasi Rak Antrean: Mengelola List Belanja

print("=== MANAJEMEN RAK BELANJA (LIST) ===")

# Inisialisasi: Rak awal
rak = ["Susu", "Roti", "Telur"]
print(f"Isi Rak Awal: {rak}")

# 1. Menambah di ujung (Langkah paling umum)
rak.append("Kopi")
print(f"Setelah append: {rak}")

# 2. Menyisipkan di tengah (Indeks 1)
rak.insert(1, "Gula")
print(f"Setelah insert di indeks 1: {rak}")

# 3. Mengganti isi (Mutable)
rak[2] = "Roti Gandum"
print(f"Setelah ganti Roti -> Roti Gandum: {rak}")

# 4. Mengambil item (Pop)
barang_keluar = rak.pop()
print(f"Barang yang diambil: {barang_keluar}")
print(f"Sisa rak sekarang: {rak}")

# 5. Mencari posisi
print(f"Posisi 'Telur' ada di urutan (Indeks): {rak.index('Telur')}")
