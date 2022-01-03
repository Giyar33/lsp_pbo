while True:
    name_siswa = input("Masukan Nama Anda : ")
    nilai_harian = int(input("Masukan Nama Harian : "))
    nilai_uts = int(input("Masukan Nama UTS : "))
    nilai_uas = int(input("Masukan Nama UAS : "))
    # deklarasi rata rata (harian+uts+uas)/3
    #nilai_akhir = int(nilai_harian+nilai_uts+nilai_uas)/3
    # deklarasi rata rata (harian 40% + uts 30% + uas 30%)/3
    nilai_akhir = int((nilai_harian*40)+(nilai_uts*30)+(nilai_uas*30)/300)

    if nilai_akhir >= 85:
        predikat_nilai = 'Amat Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    elif nilai_akhir >= 75:
        predikat_nilai = 'Baik'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    elif nilai_akhir >= 65:
        predikat_nilai = 'Cukup'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    elif nilai_akhir >= 55:
        predikat_nilai = 'Kurang'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    elif nilai_akhir <= 55:
        predikat_nilai = 'Kurang Sekali'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
    else:
        predikat_nilai = 'Kurang Sekali'
        print("Nama Lengkap Anda = ", name_siswa)
        print("Nilai Akhir Anda = ", nilai_akhir)
        print("Predikat Anda = ", predikat_nilai)
