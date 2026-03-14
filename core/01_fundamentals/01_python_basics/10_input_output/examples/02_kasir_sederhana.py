# 02_kasir_sederhana.py
# Simulasi Kasir: Latihan menerjemahkan input (Casting)

print("=== KASIR TOKO BUAH ===")

toko = "BUAH SEGAR"
print(f"Selamat datang di Toko {toko}")
print("-" * 25)

# Input selalu string, jadi harus diterjemahkan (casting)
raw_harga = input("Harga Buah (per kg): ")
raw_jumlah = input("Jumlah Beli (kg): ")

# Proses Casting (Parsing)
try:
    harga = float(raw_harga)
    jumlah = float(raw_jumlah)
    
    total = harga * jumlah
    
    print("-" * 25)
    print(f"TOTAL YANG HARUS DIBAYAR: Rp {total:,.2f}")
    
except ValueError:
    print("\n[ALARM]: Maaf, Resepsionis bingung. Harap masukkan angka yang benar!")

print("\nTerima kasih sudah berkunjung!")
