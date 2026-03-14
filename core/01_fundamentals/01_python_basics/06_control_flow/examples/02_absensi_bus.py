# 02_absensi_bus.py
# Simulasi Bus Wisata: Mengunjungi Daftar Halte

print("=== BUS WISATA PYTHON - JALUR KOTA ===")

# Daftar Iterasi (Peta Halte)
daftar_halte = ["Monas", "Kota Tua", "Senayan", "Blok M"]

# Menjalankan mesin 'for' (Iterasi terukur)
for halte in daftar_halte:
    print(f"Bus berhenti di halte: {halte}")
    print(">> Menurunkan & menaikkan penumpang...")
    print("-----------------------------------")

print("Tour Selesai. Seluruh halte telah dikunjungi.")

print("\nBonus: Menghitung mundur keberangkatan bus...")
for detik in range(5, 0, -1):
    print(f"Bus berangkat dalam {detik}...")
print("BIP BIP! Berangkat!")
