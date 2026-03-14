# 03_koki_default.py
# Simulasi Pengaturan Standar: Fungsi dengan Default Arguments

def buat_pesanan_kopi(jenis, gula="Tanpa Gula", susu=False):
    print(f"\n[ORDEER MASUK]: Kopi {jenis}")
    print(f"- Pilihan Gula: {gula}")
    print(f"- Tambahan Susu: {'Ya' if susu else 'Tidak'}")

# 1. Memanggil dengan semua data
buat_pesanan_kopi("Latte", "Gula Aren", True)

# 2. Memanggil dengan minimal data (mengandalkan default)
buat_pesanan_kopi("Espresso")

# 3. Memanggil dengan argumen spesifik (Keyword Argument)
buat_pesanan_kopi("Americano", susu=True)
