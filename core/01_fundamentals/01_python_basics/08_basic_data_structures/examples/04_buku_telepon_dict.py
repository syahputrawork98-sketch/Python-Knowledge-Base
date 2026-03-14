# 04_buku_telepon_dict.py
# Simulasi Loker Berlabel: Pencarian Key-Value

print("=== DATABASE KONTAK (DICTIONARY) ===")

# Struktur: { 'Kunci': 'Nilai' }
kontak = {
    "Polisi": "110",
    "Ambulans": "118",
    "Pemadam": "113"
}

# 1. Mencari berdasarkan Label (Key)
print(f"Nomor Polisi: {kontak['Polisi']}")

# 2. Menambah/Update data
kontak["Zaka"] = "0812-3456"
print(f"Setelah tambah Zaka: {kontak}")

# 3. Pengamanan (.get) - Menghindari Error jika kunci ga ada
cari = "Gojek"
hasil = kontak.get(cari, "Tidak Terdaftar")
print(f"Cari '{cari}': {hasil}")

# 4. Membongkar isi koper
print("\n--- Daftar Nama di Buku ---")
for nama in kontak.keys():
    print(f"- {nama}")

print("\n--- Detail Lengkap ---")
for nama, nomor in kontak.items():
    print(f"Hubungi {nama} di {nomor}")
