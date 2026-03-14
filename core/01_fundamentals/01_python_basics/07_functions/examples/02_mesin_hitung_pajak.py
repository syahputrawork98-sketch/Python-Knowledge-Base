# 02_mesin_hitung_pajak.py
# Simulasi Nampan Output: Fungsi dengan Parameter dan Return

# Mesin ini menerima bahan mentah (harga) dan mengembalikan hasil matang (total)
def hitung_pajak_ppn(harga_barang):
    tarif = 0.11 # 11% PPN
    pajak = harga_barang * tarif
    total = harga_barang + pajak
    
    # Mengirimkan hasil keluar melalui nampan 'return'
    return total

# Mengambil hasil dari nampan dan menyimpannya ke variabel
laptop = 10000000
total_bayar = hitung_pajak_ppn(laptop)

print(f"Harga Dasar : Rp {laptop:,}")
print(f"Total Bayar : Rp {total_bayar:,.0f}")
