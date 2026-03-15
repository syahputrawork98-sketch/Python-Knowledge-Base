# 01_konversi_suhu.py
# Bab 11: Property Decorators
# Contoh setter dan getter Pythonic untuk konversi otomatis

class PengukurSuhu:
    def __init__(self, celsius_awal):
        # Kita menggunakan atribut private untuk menyimpan data aslinya
        self._celsius = celsius_awal

    # --- THE GETTER ---
    # @property mengubah metode ini menjadi seolah-olah sebuah atribut.
    # Orang bisa memanggil `obj.suhu_celsius` tanpa tanda kurung ()
    @property
    def suhu_celsius(self):
        print("[Log] Mengambil data suhu derajat Celcius...")
        return self._celsius

    # --- THE SETTER ---
    # Jika orang mencoba mengubah `obj.suhu_celsius = 50`, fungsi ini yang akan menanganinya!
    @suhu_celsius.setter
    def suhu_celsius(self, nilai_baru):
        if nilai_baru < -273.15:
            raise ValueError("Suhu tidak mungkin di bawah Nol Mutlak (-273.15 C)!")
        
        print(f"[Log] Memperbarui suhu menjadi {nilai_baru} C...")
        self._celsius = nilai_baru

    # --- PROPERTY LAIN: FAHRENHEIT ---
    # Kita bisa membuat "Ilusi" atribut.
    # Pengguna mengira ada variabel 'suhu_fahrenheit', padahal ini dihitung on-the-fly!
    @property
    def suhu_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @suhu_fahrenheit.setter
    def suhu_fahrenheit(self, fahrenheit_baru):
        print(f"[Log] Anda menyetel Fahrenheit ke {fahrenheit_baru}")
        # Mengubah Fahrenheit akan OTOMATIS mengubah Celsius internal!
        self.suhu_celsius = (fahrenheit_baru - 32) * 5/9


# --- Uji Coba Program ---
print("--- Termometer Pintar ---")

termometer = PengukurSuhu(25)

print("\n--- Mengecek Suhu Awal ---")
# Perhatikan! Tidak ada tanda (), ini diperlakukan seperti variabel biasa
print(f"Celsius: {termometer.suhu_celsius}") 
print(f"Fahrenheit: {termometer.suhu_fahrenheit}")

print("\n--- Mengubah Suhu (Menyerang lewat Setter) ---")
# Saat kita menggunakan '=' (assignment), @setter yang bekerja
termometer.suhu_celsius = 30
print(f"Berubah! Sekarang Fahrenheit-nya: {termometer.suhu_fahrenheit}")

print("\n--- Mengubah Fahrenheit ---")
termometer.suhu_fahrenheit = 100
print(f"Celsius internal ikut berubah menjadi: {termometer.suhu_celsius}")

print("\n--- Menguji Validasi ---")
try:
    termometer.suhu_celsius = -300
except ValueError as error_mutlak:
    print(f"Ditolak: {error_mutlak}")
