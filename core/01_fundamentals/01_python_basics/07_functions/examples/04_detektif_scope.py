# 04_detektif_scope.py
# Simulasi Dinding Kaca: Eksperimen Lingkup (Scope)

bahan_global = "Tepung Terigu (Ada di luar)"

def stasiun_masak_spesifik():
    # Variabel ini hanya hidup di dalam dinding kaca stasiun ini (Local)
    bahan_lokal = "Bumbu Rahasia (Hanya ada di dalam)"
    
    print("--- DI DALAM STASIUN ---")
    print(f"Melihat ke luar: {bahan_global}")
    print(f"Melihat ke meja sendiri: {bahan_lokal}")

# Menjalankan fungsi
stasiun_masak_spesifik()

print("\n--- DI LUAR STASIUN ---")
print(f"Melihat bahan di gudang: {bahan_global}")

# BARIS DI BAWAH INI AKAN MENYEBABKAN ERROR:
# print(f"Mencoba intip bumbu rahasia: {bahan_lokal}")
# Pesan Error: NameError: name 'bahan_lokal' is not defined
