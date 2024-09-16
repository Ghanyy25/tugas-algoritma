usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota? (ya/tidak): ").lower()

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

harga_final = harga * 0.8 if anggota == "ya" else harga
print(f"Harga tiket yang harus dibayar: Rp{harga_final:.0f}")
