# 02_pencarian_berkas.py
# Simulasi Mencari Berkas: Menangani file yang hilang

print("=== INSPEKTUR BERKAS DARURAT ===")

nama_file = input("Masukkan nama file yang ingin dicari (misal: rahasia.txt): ")

try:
    with open(nama_file, "r") as f:
        print(f"\n[SUKSES]: Berkas '{nama_file}' ditemukan. Membuka isi...")
        print(f"Konten: {f.read()}")

except FileNotFoundError:
    print(f"\n[ALARM]: Berkas '{nama_file}' TIDAK ADA di gudang.")
    print("Saran: Gunakan File I/O (Bab 10) untuk membuatnya terlebih dahulu.")

except PermissionError:
    print(f"\n[ALARM]: Anda tidak punya akses ke berkas '{nama_file}'!")

print("\nProgram berakhir dengan tenang (tidak crash).")
