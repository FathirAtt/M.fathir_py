#Program Gabungan Aritmatika, Logika dan Ekspresi
#Menentukan status kelulusan mahasiswa

#Input
tugas = float(input("Nilai Tugas : "))
uts = float(input("Nilai UTS   : "))
uas = float(input("Nilai UAS   : "))
kehadiran = float(input("Kehadiran   : "))

# Operator aritmatika: hitung nilai akhir
nilai_akhir = (0.2 * tugas) + (0.3 * uts) + (0.5 * uas)
nilai_akhir = round(nilai_akhir, 2)  # hindari error pembulatan float (mis. 84.99999)

# Operator perbandingan + logika: syarat kelulusan
lulus = nilai_akhir >= 75 and kehadiran >= 80

# Operator perbandingan + logika + modulus: syarat predikat
predikat = nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0

# Tentukan status
if lulus and predikat:
    status = "LULUS DENGAN PREDIKAT"
elif lulus:
    status = "LULUS"
else:
    status = "BELUM LULUS"

#Output
print()
print("Nilai Akhir :", nilai_akhir)
print("Status      :", status)