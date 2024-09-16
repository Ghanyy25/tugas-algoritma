nilai_akhir = float(input("Masukkan nilai akhir mahasiswa: "))
kehadiran = float(input("Masukkan persentase kehadiran mahasiswa: "))
tugas_tambahan = float(input("Masukkan nilai tugas tambahan (0 jika tidak ada): "))

if kehadiran < 75:
    print("Tidak Lulus karena kehadiran kurang dari 75%.")
elif nilai_akhir >= 85:
    print("Lulus dengan Predikat A.")
elif nilai_akhir >= 70:
    print("Lulus dengan Predikat B.")
elif nilai_akhir >= 60:
    print("Lulus dengan Predikat C.")
elif nilai_akhir < 60:
    if tugas_tambahan >= 70 and kehadiran >= 75:
        print("Lulus dengan Predikat C karena tugas tambahan diselesaikan dengan baik.")
    else:
        print("Tidak Lulus.")
