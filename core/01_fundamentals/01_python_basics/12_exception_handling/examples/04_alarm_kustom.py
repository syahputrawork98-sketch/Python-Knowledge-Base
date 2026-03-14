# 04_alarm_kustom.py
# Simulasi Tombol Alarm Manual: Menggunakan 'raise'

def validasi_input_umur(umur):
    if umur < 0:
        # Menolak input secara sengaja dengan alarm alarm manual
        raise ValueError(f"Umur tidak masuk akal: {umur}. Harap masukkan angka positif!")
    if umur > 150:
        raise ValueError("Selamat, Anda adalah manusia tertua, tapi sistem tidak percaya!")
    
    return f"Umur anda {umur} tahun berhasil diverifikasi."

print("=== SISTEM VERIFIKASI UMUR ===")

try:
    input_user = int(input("Masukkan umur Anda: "))
    pesan = validasi_input_umur(input_user)
    print(pesan)
except ValueError as e:
    print(f"\n[ALARM MANUAL DIPICU]: {e}")

print("\nVerifikasi Selesai.")
