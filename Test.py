def tampilkan_menu():
    print("1. Tambah barang")
    print("2. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih: ")
    if pilihan == "2":
        break
    elif pilihan == "1":
        print("Barang ditambahkan")
    else:
        print("Pilihan tidak valid")