# 03_pembersihan_paksa.py
# Simulasi Protokol Pembersihan: Kekuatan 'finally'

def jalankan_prosedur_risiko():
    print("Membuka Pintu Brankas...")
    try:
        pilihan = input("Ingin memicu error? (y/n): ")
        if pilihan.lower() == 'y':
            1 / 0 # Memicu Crash
        print("Prosedur berjalan normal.")
        return "SUKSES"
        
    except ZeroDivisionError:
        print("Menangani insiden di dalam prosedur...")
        return "GAGAL"
        
    finally:
        # Bagian ini tetap jalan biarpun ada 'return' atau 'crash' di atas!
        print(">>> [PENTING]: Mengunci kembali pintu brankas dengan aman.")

print("Memulai simulasi...")
status = jalankan_prosedur_risiko()
print(f"Status Akhir: {status}")
