# 01_komposisi_mobil.py
# Bab 10: Composition vs Inheritance
# Demonstrasi HAS-A Relationship (Mobil HAS-A Mesin, HAS-A Ban)

# Kita membuat bagian-bagian (Parts) secara terpisah
class Mesin:
    def nyalakan(self):
        return "Brumm! Mesin V8 Menyala!"

class Ban:
    def putar(self):
        return "Ban berputar maju..."

class Radio:
    def mainkan_musik(self):
        return "Memutar lagu favorit Padi - Begitu Indah..."

# Ini adalah kelas Komposisi
# Mobil BUKAN keturunan dari Mesin, Mobil BUKAN Ban!
# Tapi, Mobil MEMILIKI Mesin dan Ban.
class Mobil:
    def __init__(self):
        # Perakitan bagian-bagian mobil
        self.mesin_saya = Mesin()
        self.ban_saya = Ban()
        self.radio_mobil = Radio()
        
    def jalan(self):
        # Mobil memerintahkan bagian-bagiannya untuk bekerja
        suara_mesin = self.mesin_saya.nyalakan()
        suara_ban = self.ban_saya.putar()
        print(suara_mesin)
        print(suara_ban)
        print("Mobil melaju kencang!")

    def hiburan(self):
        print(self.radio_mobil.mainkan_musik())

# --- Uji Coba Program ---
print("--- Simulasi Pabrik Mobil ---")
mobil_sport = Mobil()
mobil_sport.jalan()
print("\n--- Nyalakan Hiburan ---")
mobil_sport.hiburan()
