# 04_pintu_darurat.py
# Simulasi Antrian VIP: Penggunaan Break & Continue

print("=== SISTEM ANTRIAN VIP (PINTU DARURAT) ===")

# Kita punya 10 nomor antrian
for nomor in range(1, 11):
    
    # Contoh 'continue': Lewati nomor sial 4 & 7
    if nomor == 4 or nomor == 7:
        print(f"(Nomor {nomor} sedang di-skip oleh sistem...)")
        continue

    # Contoh 'break': Jika antrian mencapai nomor 9, sistem tutup darurat
    if nomor == 9:
        print("!!! ALARM: Server panas, hentikan antrian di nomor 9 !!!")
        break

    print(f"Melayani Pelanggan Nomor: {nomor}")

print("\nEvaluasi: Antrian 4 & 7 dilewati (continue). Antrian 10 tidak diproses (break).")
