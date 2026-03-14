# 02_scanner_identitas.py
# Simulasi Pemindai Material: Mengetahui Tipe dan Dokumentasi Alat

print("=== PEMINDAI MATERIAL DIGITAL ===")

benda_misterius = [1, 2, 3]

# 1. type() - Menscan jenis material
print(f"Jenis Material: {type(benda_misterius)}")

# 2. id() - Mengintip alamat gudang penyimpanan
print(f"Lokasi Rak Gudang (Memory Address): {id(benda_misterius)}")

# 3. dir() - Mengintip 'fitur' yang ada di benda tersebut
fitur = dir(benda_misterius)
print(f"\nJumlah fitur yang dimiliki benda ini: {len(fitur)}")
print(f"Contoh fitur (5 pertama): {fitur[:5]}")

# 4. help() - Membaca buku manual
print("\n--- MENAMPILKAN RINGKASAN BUKU MANUAL UNTUK FUNGSI 'len' ---")
# help(len) # Baris ini akan mencetak banyak teks, di-comment agar output bersih
print("(Cabut komentar pada 'help(len)' di kode jika ingin baca manual utuh)")
