# 01_solid_dan_mro.py
# Bab 12: OOP Best Practices
# Contoh mematuhi Single Responsibility Principle dan observasi MRO.

# --- BAD CODE (Melanggar SRP) ---
# Kelas ini melakukan terlalu banyak hal: Menyimpan data, dan Mencetak ke Layar!
class LaporanBuruk:
    def __init__(self, teks):
        self.konten = teks
        
    def format_teks(self):
        self.konten = f"--- LAPORAN ---\n{self.konten}"
        
    def simpan_ke_file_dan_cetak(self):
        print("Menyimpan ke file...")
        print(self.konten)

# --- GOOD CODE (Sesuai SRP) ---
# Pemisahan tugas: 1 Kelas = 1 Tanggung Jawab
class Laporan:
    def __init__(self, teks):
        self.konten = teks
        
    def dapatkan_teks(self):
        return f"--- LAPORAN RAHTAH ---\n{self.konten}"

class MesinCetak:
    # Mesin cetak tidak peduli darimana teksnya berasal, ia hanya bertugas mencetak
    def cetak(self, teks_apapun):
        print("[Mencetak ke Kertas...]")
        print(teks_apapun)


# --- CONTOH MRO (Method Resolution Order) ---
# Pewarisan ganda (Multiple Inheritance) yang rumit
class Kakek:
    def bicara(self): return "Kakek bicara"

class Ayah(Kakek):
    def bicara(self): return "Ayah bicara"

class Paman(Kakek):
    def bicara(self): return "Paman bicara"

class Anak(Ayah, Paman):
    pass

# --- Uji Coba Program ---
print("--- Menguji SRP ---")
data_laporan = Laporan("Pendapatan Q3 meningkat 20%")
printer_hp = MesinCetak()

# Kerjasama dua objek (Bukan satu objek Dewa)
printer_hp.cetak(data_laporan.dapatkan_teks())

print("\n--- Misteri MRO (Siapa yang bicara?) ---")
budi = Anak()
# Jika Anak tidak punya metode bicara, ke siapakah ia mencari? Ayah atau Paman?
# Jawabannya: Yang disebut lebih dulu di dalam kurung class Anak(Ayah, Paman) -> Yaitu Ayah!
print(budi.bicara())

# Ingin melihat urutan pencariannya? Gunakan `__mro__`!
print("\nJalur Pencarian Metode (MRO Python):")
for jalur in Anak.__mro__:
    print("->", jalur.__name__)
