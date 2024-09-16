nilai_akhir = float(input("Masukkan nilai akhir mahasiswa: "))
kehadiran = float(input("Masukkan persentase kehadiran mahasiswa: "))

if kehadiran < 75:
    print("Tidak Lulus karena kehadiran kurang dari 75%.")
elif nilai_akhir >= 85:
    print("Lulus dengan Predikat A.")
elif nilai_akhir >= 70:
    print("Lulus dengan Predikat B.")
elif nilai_akhir >= 60:
    print("Lulus dengan Predikat C.")
elif nilai_akhir < 60:
     print("Tidak Lulus.")
