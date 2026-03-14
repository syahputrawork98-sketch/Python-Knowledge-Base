# toko_alat.py
# Simulasi Kotak Paket: Modul penyedia alat-alat (Fungsi & Variabel)

NAMA_TOKO = "Python Tool Shop"

def hitung_harga_obeng(jumlah):
    harga_satuan = 5000
    return jumlah * harga_satuan

def hitung_harga_palu(jumlah):
    harga_satuan = 15000
    return jumlah * harga_satuan

# Rahasia: Bagian tes mandiri yang tidak akan jalan saat di-import
if __name__ == "__main__":
    print("--- TESTING MANDIRI DI TOKO ---")
    print(f"Tes harga 2 obeng: {hitung_harga_obeng(2)}")
