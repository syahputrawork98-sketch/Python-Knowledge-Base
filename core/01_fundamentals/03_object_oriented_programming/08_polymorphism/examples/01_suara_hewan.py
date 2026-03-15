# 01_suara_hewan.py
# Bab 08: Polymorphism
# Simulasi polimorfisme melalui metode yang dioverride

class Hewan:
    def bersuara(self):
        # Ini adalah metode abstrak (hanya kerangka)
        # Seharusnya diisi oleh kelas anaknya
        pass

class Kucing(Hewan):
    # Meng-override (menimpa) metode bersuara dari induknya
    def bersuara(self):
        return "Meow!"

class Anjing(Hewan):
    # Meng-override metode bersuara dari induknya
    def bersuara(self):
        return "Guk! Guk!"

class Bebek(Hewan):
    def bersuara(self):
        return "Kwek kwek!"

# --- Fungsi Polimorfik ---
# Fungsi ini tidak peduli apa tipe hewannya (Kucing, Anjing, atau Bebek).
# Selama objek tersebut punya metode 'bersuara', fungsi ini bisa menjalankannya.
# Inilah yang disebut "Duck Typing" di Python.

def konser_hewan(daftar_hewan):
    print("--- Konser Hewan Dimulai ---")
    for hewan in daftar_hewan:
        print(f"Seekor {type(hewan).__name__} menyanyi: {hewan.bersuara()}")

# --- Uji Coba Program ---
kucing_oren = Kucing()
anjing_bulldog = Anjing()
bebek_karet = Bebek()

# Kita kumpulkan semua objek yang BENAR-BENAR BERBEDA ini ke dalam satu list
peserta_konser = [kucing_oren, anjing_bulldog, bebek_karet]

# Dan satu fungsi bisa menangani mereka semua tanpa if/else yang panjang!
konser_hewan(peserta_konser)

print("\n--- Contoh Duck Typing Ekstrim ---")
class RobotPeniru:
    # Robot ini BUKAN keturunan dari kelas Hewan
    def bersuara(self):
        return "Bip bop! Bip bop!"

robot = RobotPeniru()
peserta_konser.append(robot)

# Walau bukan hewan, fungsi konser tetap bisa menjalankannya
# "If it walks like a duck, and quacks like a duck, it must be a duck."
konser_hewan(peserta_konser)
