# 01_tulis_catatan.py
# Simulasi Menulis Buku: Membuat file teks baru

print("=== SISTEM PENULISAN CATATAN ===")

# Menyiapkan konten
isi_catatan = """Halo! Ini adalah file pertama yang dibuat oleh Python.
Belajar File I/O itu seru karena data kita tidak akan hilang
saat komputer dimatikan.
"""

# Membuka file dengan mode 'w' (Write)
# Hati-hati: mode 'w' akan menghapus isi file lama jika sudah ada!
with open("catatan_saya.txt", "w", encoding="utf-8") as file:
    file.write(isi_catatan)
    print("Berhasil menulis ke 'catatan_saya.txt'!")

print("\n(Cek folder Anda, sekarang ada file baru bernama catatan_saya.txt)")
