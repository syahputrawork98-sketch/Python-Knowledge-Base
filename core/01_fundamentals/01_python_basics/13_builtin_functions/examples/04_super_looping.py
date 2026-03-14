# 04_super_looping.py
# Simulasi Mesin Penomeran: Enumerate dan Zip

print("=== MESIN PRODUKSI OTOMATIS ===")

produk = ["Pintu", "Jendela", "Meja"]
harga = [500000, 250000, 150000]

# 1. range() - Mencetak nomor urut manual
print("Daftar Batch:")
for i in range(len(produk)):
    print(f"- Batch {i+1}")

# 2. enumerate() - Menempelkan LABEL NOMOR pada setiap produk
print("\nLabeling Produk:")
for nomor, nama in enumerate(produk, start=1):
    print(f"No. {nomor}: {nama}")

# 3. zip() - Memasangkan Produk dengan Harganya (Seperti Resleting)
print("\nNota Gabungan (Zip):")
for item, price in zip(produk, harga):
    print(f"Barang: {item} | Biaya: Rp {price:,}")

print("\n(Produksi Selesai. Semua alat dikembalikan ke sabuk.)")
