import math

print("1. Hitung keliling lingkaran")
print("2. Hitung luas lingkaran")

pilihan = int(input("Masukkan pilihan : "))
r = float(input("Masukkan jari-jari lingkaran : "))

if pilihan == 1:
    keliling_lingkaran = 2 * math.pi * r
    print("Keliling lingkaran = ", keliling_lingkaran)
elif pilihan == 2:
    luas_lingkaran = math.pi * r * r
    print("Luas lingkaran = ", luas_lingkaran)
else:
    print("Pilihan tidak valid, pilih angka 1/2")