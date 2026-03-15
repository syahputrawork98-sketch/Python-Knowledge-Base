# 01_simulasi_atm.py
# Bab 07: Encapsulation
# Contoh simulasi Brankas dan Teller Bank

class AkunBank:
    def __init__(self, nama_pemilik, saldo_awal):
        # Public attribute (Semua orang boleh tahu namanya)
        self.nama = nama_pemilik
        
        # Protected attribute (Saran sopan: jangan sentuh!)
        self._nomor_rekening = "123-456-789"
        
        # Private attribute (Sangat keras: jangan ubah tanpa izin!)
        # Disembunyikan agar saldo tidak bisa diset manual menjadi minus
        self.__saldo = saldo_awal
        
        # Private attribute lain
        self.__pin = "1234" 

    # --- GETTER ---
    # Cara resmi untuk sekadar melihat saldo
    def cek_saldo(self, pin_input):
        if pin_input == self.__pin:
            return f"Saldo Anda: Rp. {self.__saldo}"
        else:
            return "Akses Ditolak: PIN Salah!"

    # --- SETTER ---
    # Cara resmi untuk menambahkan saldo
    def tabung(self, nominal):
        if nominal > 0:
            self.__saldo += nominal
            print(f"Berhasil menabung Rp. {nominal}.")
        else:
            print("Gagal: Harus menabung dengan jumlah positif.")

    # Cara resmi untuk mengambil saldo
    def tarik_tunai(self, nominal, pin_input):
        if pin_input != self.__pin:
            print("Akses Ditolak: PIN Salah!")
            return
            
        if nominal <= 0:
            print("Gagal: Penarikan harus lebih dari 0.")
            return
            
        if nominal > self.__saldo:
            print("Gagal: Saldo tidak mencukupi.")
            return
            
        self.__saldo -= nominal
        print(f"Berhasil menarik Rp. {nominal}.")


# --- Uji Coba Program ---
print("--- Simulasi Mesin ATM Python ---")
akun_budi = AkunBank("Budi Santoso", 500000)

print(f"Pemilik Akun: {akun_budi.nama}")
# Mengambil atribut protected masih bisa (walau tidak disarankan secara konvensi)
print(f"Nomor Rek: {akun_budi._nomor_rekening}")

print("\n(1) Usaha Maling Saldo (Mengakses __saldo secara langsung)")
try:
    # Akan ERROR merah karena Nama __saldo telah diubah (Name Mangling)
    akun_budi.__saldo = 999999999
except AttributeError as e:
    print(f"Sistem ATM Menolak: {e}")

print("\n(2) Budi Menggunakan Jalur Resmi (Setter/Getter)")
# Menabung harus lewat metode (teller)
akun_budi.tabung(100000)

# Teller menolak logika bank yang aneh
akun_budi.tabung(-5000) 

# Cek saldo harus pakai PIN dan fungsi Getter resmi
print(akun_budi.cek_saldo("0000")) # Ditolak
print(akun_budi.cek_saldo("1234")) # Diterima, saldo: 600000

print("\n(3) Penarikan Uang")
akun_budi.tarik_tunai(1000000, "1234") # Ditolak karena miskin
akun_budi.tarik_tunai(50000, "1234")   # Berhasil ditarik
print(akun_budi.cek_saldo("1234"))     # Saldo terakhir: 550000
