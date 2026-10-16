def pinjam_buku():
    nama = input("Nama Peminjam: ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return


def main():
    while True:
        print("\n========SISTEM PERPUSTAKAAN========")
        print("1. Pinjam Buku")

        pilihan = input("Pilih menu :").strip()

        if pilihan == "1":
            pinjam_buku()
        else:
            print("Pilihan tidak tersedia")


main()