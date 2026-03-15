# 01_payment_gateway.py
# Bab 09: Abstract Base Classes
# Membuat Blueprint wajib untuk sistem pembayaran.

from abc import ABC, abstractmethod

# 1. Mendefinisikan Aturan Wajib (The Blueprint)
# Kelas ini tidak mungkin bisa digunakan langsung. Ia hanya berupa hukum.
class GerbangPembayaran(ABC):
    
    @abstractmethod
    def proses_bayar(self, jumlah):
        # Metode ini kosong. Ini adalah 'janji' yang wajib dipenuhi oleh anak-anaknya.
        pass
        
    @abstractmethod
    def cek_status(self, id_transaksi):
        # Janji kedua yang wajib dipenuhi.
        pass
        
    # Metode normal (bukan abstrak) di dalam kelas abstrak? BISA!
    # Ini adalah "fasilitas ekstra" yang diturunkan utuh ke anak-anaknya.
    def cetak_struk(self, jumlah):
        print(f"=== STRUK BUKTI: Berhasil bayar Rp. {jumlah} ===")

# 2. Membuat "Anak" yang Patuh Hukum
class GoPay(GerbangPembayaran):
    def proses_bayar(self, jumlah):
        print(f"[GoPay] Memotong saldo dompet digital sebesar Rp. {jumlah}.")
        
    def cek_status(self, id_transaksi):
        return "Berhasil"

# 3. Membuat "Anak" Pembangkang / Lupa Aturan
class KartuKredit(GerbangPembayaran):
    # Programmer-nya kelupaan membuat metode `cek_status`!
    def proses_bayar(self, jumlah):
        print(f"[CC] Menghubungi Visa Inc. untuk menarik Rp. {jumlah}.")


# --- Uji Coba Program ---
print("--- Sistem Kasir Toko ---")

bayar_gopay = GoPay()
bayar_gopay.proses_bayar(50000)
bayar_gopay.cetak_struk(50000) # Memakai metode bawaan induk

print("\n--- Sistem Kasir Toko CC ---")
try:
    # Ini akan CRASH bahkan SEBELUM Anda sempat memanggil metode apapun!
    bayar_cc = KartuKredit()
except TypeError as t_error:
    print(f"ALARM SISTEM: {t_error}")
    print("Programmer CC belum membuat fungsi 'cek_status'. Objek tidak bisa diciptakan!")
