# 02_uji_identitas.py
# Simulasi Kartu Identitas: Memahami __name__ == "__main__"

import toko_alat 
# Saat Baris di atas jalan, toko_alat.py TIDAK akan mencetak bagian "TESTING MANDIRI" 
# karena __name__ di sana bukan "__main__" melainkan "toko_alat".

print("--- EKSEKUSI FILE UTAMA (02_uji_identitas.py) ---")
print(f"Identitas file ini sekarang adalah: {__name__}")

if __name__ == "__main__":
    print("Saya adalah file yang Anda klik/panggil langsung!")
