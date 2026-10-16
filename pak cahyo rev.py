
# ==========================================
# SISTEM PENGELOLAAN APOTEK
# ==========================================

obat = {
    "A001": {"nama": "Paracetamol", "harga": 5000, "stok": 20},
    "A002": {"nama": "Vitamin C", "harga": 10000, "stok": 15},
    "A003": {"nama": "Obat Batuk", "harga": 8000, "stok": 10},
    "A004": {"nama": "Antasida", "harga": 7000, "stok": 12}
}


def tampilkan_obat():
    print("\n========== DAFTAR OBAT ==========")
    print("Kode\tNama Obat\tHarga\tStok")
    print("------------------------------------------")

    for kode, data in obat.items():
        print(
            f"{kode}\t{data['nama']:<15}\t"
            f"Rp{data['harga']}\t{data['stok']}"
        )


def tambah_obat():
    print("\n========== TAMBAH OBAT ==========")

    kode = input("Masukkan kode obat: ")

    if kode in obat:
        print("Kode obat sudah digunakan!")
        return

    nama = input("Masukkan nama obat: ")
    harga = int(input("Masukkan harga obat: "))
    stok = int(input("Masukkan stok obat: "))

    obat[kode] = {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

    print("Obat berhasil ditambahkan!")


def cari_obat():
    print("\n========== CARI OBAT ==========")

    nama_cari = input("Masukkan nama obat: ").lower()
    ditemukan = False

    for kode, data in obat.items():
        if nama_cari in data["nama"].lower():
            print("\nObat ditemukan!")
            print("Kode  :", kode)
            print("Nama  :", data["nama"])
            print("Harga : Rp", data["harga"])
            print("Stok  :", data["stok"])
            ditemukan = True 

    if not ditemukan:
        print("Obat tidak ditemukan.")


def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Masukkan angka yang valid!")


def transaksi():
    print("\n========== TRANSAKSI ==========")

    keranjang = []   # list untuk menyimpan semua barang yang dibeli

    # --- Tahap 1: isi keranjang (perulangan) ---
    while True:
        kode = input("\nKode obat (ketik 'selesai' untuk bayar): ").upper()

        if kode == "SELESAI":
            break

        if kode not in obat:
            print("Kode obat tidak ditemukan!")
            continue

        data = obat[kode]

        # hitung stok yang masih tersedia (dikurangi yang sudah masuk keranjang)
        sudah_di_keranjang = sum(
            item["jumlah"] for item in keranjang if item["kode"] == kode
        )
        tersedia = data["stok"] - sudah_di_keranjang

        print("Nama obat :", data["nama"])
        print("Harga     : Rp", data["harga"])
        print("Stok      :", tersedia)

        jumlah = input_angka("Jumlah yang dibeli: ")

        if jumlah <= 0:
            print("Jumlah pembelian tidak valid!")
            continue

        if jumlah > tersedia:
            print("Stok obat tidak mencukupi!")
            continue

        keranjang.append({
            "kode": kode,
            "nama": data["nama"],
            "harga": data["harga"],
            "jumlah": jumlah
        })
        print("Ditambahkan ke keranjang!")

    # --- Tahap 2: cek keranjang ---
    if len(keranjang) == 0:
        print("Keranjang kosong, transaksi dibatalkan.")
        return

    # --- Tahap 3: cetak struk ---
    print("\n========== STRUK PEMBELIAN ==========")
    total = 0
    for item in keranjang:
        subtotal = item["harga"] * item["jumlah"]
        total += subtotal
        print(f"{item['nama']:<15} {item['jumlah']} x Rp{item['harga']} = Rp{subtotal}")

    print("-------------------------------------")
    print("Total : Rp", total)

    # --- Tahap 4: pembayaran ---
    while True:
        bayar = input_angka("Uang pembayaran (0 untuk batal): Rp")

        if bayar == 0:
            print("Transaksi dibatalkan.")
            return

        if bayar < total:
            print("Uang pembayaran tidak mencukupi!")
        else:
            break

    kembalian = bayar - total

    # --- Tahap 5: kurangi stok setelah pembayaran berhasil ---
    for item in keranjang:
        obat[item["kode"]]["stok"] -= item["jumlah"]

    print("Kembalian : Rp", kembalian)
    print("Transaksi berhasil!")


def main():
    while True:
        print("\n================================")
        print("       SISTEM APOTEK")
        print("================================")
        print("1. Tampilkan Daftar Obat")
        print("2. Tambah Obat")
        print("3. Cari Obat")
        print("4. Transaksi")
        print("5. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_obat()

        elif pilihan == "2":
            tambah_obat()

        elif pilihan == "3":
            cari_obat()

        elif pilihan == "4":
            transaksi()

        elif pilihan == "5":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak tersedia!")


# Menjalankan program
main()