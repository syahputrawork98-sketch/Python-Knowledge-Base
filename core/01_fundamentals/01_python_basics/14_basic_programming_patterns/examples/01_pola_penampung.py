# 01_pola_penampung.py
# Pola Akumulator: Mengumpulkan hasil ke satu tempat (Ember)

print("=== PENGHITUNG TOTAL BELANJA ===")

# Daftar harga barang yang dibeli
keranjang = [15000, 25000, 5000, 45000]

# 1. Inisialisasi 'Ember' di luar loop
total_harga = 0

# 2. Iterasi untuk memasukkan data ke ember
for harga in keranjang:
    total_harga += harga  # Akumulasi
    print(f"Menambahkan Rp {harga:,} ... Subtotal: Rp {total_harga:,}")

print("-" * 30)
print(f"TOTAL AKHIR: Rp {total_harga:,}")

# Bonus: Rata-rata (menggunakan akumulator hasil pembagian)
rata_rata = total_harga / len(keranjang)
print(f"Rata-rata Harga per Barang: Rp {rata_rata:,.2f}")
