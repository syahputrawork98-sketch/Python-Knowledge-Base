# 04_asisten_otomatis.py
# Simulasi Membaca Baris demi Baris: Efisiensi Memori

print("=== SISTEM SCANNER BARIS ===")

# Membuat file dummy untuk dibaca
with open("data_list.txt", "w") as f:
    f.write("Baris Satu\nBaris Dua\nBaris Tiga\n")

print("Membaca file 'data_list.txt' per baris:")
print("-" * 20)

# Cara paling efisien membaca file besar: Loop langsung pada objek file
with open("data_list.txt", "r") as file:
    for indeks, baris in enumerate(file, start=1):
        # strip() membuang karakter '\n' di ujung agar tidak ada baris kosong ganda
        print(f"Baris {indeks}: {baris.strip()}")

print("-" * 20)
print("Selesai. File otomatis ditutup oleh Asisten 'with'.")
