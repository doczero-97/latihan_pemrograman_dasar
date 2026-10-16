# ==========================================
# SISTEM PEMINJAMAN BUKU PERPUSTAKAAN
# ==========================================
from datetime import date, datetime, timedelta

# --- Pengaturan ---
LAMA_PINJAM = 7          # hari
DENDA_PER_HARI = 1000    # rupiah
MAKS_PINJAM = 3          # maksimal buku yang dipinjam satu orang

# --- STRUKTUR DATA ---
# dictionary untuk data buku, list berisi dictionary untuk riwayat peminjaman
buku = {
    "B001": {"judul": "Dasar Pemrograman Python", "penulis": "Andi Wijaya", "stok": 3},
    "B002": {"judul": "Algoritma dan Struktur Data", "penulis": "Rina Sari", "stok": 2},
    "B003": {"judul": "Basis Data untuk Pemula", "penulis": "Budi Santoso", "stok": 4},
    "B004": {"judul": "Jaringan Komputer", "penulis": "Dewi Lestari", "stok": 1},
}

peminjaman = []


# ------------------------------------------
# FUNGSI BANTU
# ------------------------------------------
def input_angka(pesan):
    """Meminta angka dari pengguna sampai input valid."""
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Masukkan angka yang valid!")


def input_tanggal(pesan):
    """Meminta tanggal format DD-MM-YYYY. Kosong = hari ini."""
    while True:
        teks = input(pesan).strip()
        if teks == "":
            return date.today()
        try:
            return datetime.strptime(teks, "%d-%m-%Y").date()
        except ValueError:
            print("Format tanggal salah! Contoh: 07-10-2026")


def hitung_denda(jatuh_tempo, tgl_kembali):
    """Denda = hari terlambat x tarif per hari (0 jika tidak terlambat)."""
    terlambat = (tgl_kembali - jatuh_tempo).days
    if terlambat > 0:
        return terlambat, terlambat * DENDA_PER_HARI
    return 0, 0


def pinjaman_aktif(nama):
    """Mengembalikan list peminjaman yang belum dikembalikan oleh seseorang."""
    hasil = []
    for p in peminjaman:
        if p["nama"].lower() == nama.lower() and p["status"] == "Dipinjam":
            hasil.append(p)
    return hasil


def format_tanggal(tgl):
    """Mengubah tanggal menjadi string format DD-MM-YYYY."""
    return tgl.strftime("%d-%m-%Y")


# ------------------------------------------
# FUNGSI MENU
# ------------------------------------------
def tampilkan_buku():
    print("\n========== DAFTAR BUKU ==========")
    print(f"{'Kode':<7}{'Judul':<30}{'Penulis':<15}{'Stok'}")
    print("-" * 60)
    for kode, data in buku.items():
        print(f"{kode:<7}{data['judul']:<30}{data['penulis']:<15}{data['stok']}")


def tambah_buku():
    print("\n========== TAMBAH BUKU ==========")
    kode = input("Kode buku: ").strip().upper()

    if kode == "":
        print("Kode tidak boleh kosong!")
        return
    if kode in buku:
        print("Kode buku sudah digunakan!")
        return

    judul = input("Judul buku: ").strip()
    penulis = input("Penulis: ").strip()
    stok = input_angka("Jumlah stok: ")

    if judul == "" or stok <= 0:
        print("Data tidak valid!")
        return

    buku[kode] = {"judul": judul, "penulis": penulis, "stok": stok}
    print("Buku berhasil ditambahkan!")


def cari_buku():
    print("\n========== CARI BUKU ==========")
    kata = input("Masukkan judul/penulis: ").strip().lower()
    ditemukan = False

    for kode, data in buku.items():
        if kata in data["judul"].lower() or kata in data["penulis"].lower():
            print(f"[{kode}] {data['judul']} - {data['penulis']} (stok: {data['stok']})")
            ditemukan = True

    if not ditemukan:
        print("Buku tidak ditemukan.")


def pinjam_buku():
    print("\n========== PEMINJAMAN BUKU ==========")
    nama = input("Nama peminjam: ").strip()
    if nama == "":
        print("Nama tidak boleh kosong!")
        return

    sedang_pinjam = len(pinjaman_aktif(nama))
    sisa_kuota = MAKS_PINJAM - sedang_pinjam
    if sisa_kuota <= 0:
        print(f"Batas peminjaman ({MAKS_PINJAM} buku) sudah tercapai!")
        return

    tgl_pinjam = input_tanggal("Tanggal pinjam (DD-MM-YYYY, kosong = hari ini): ")
    jatuh_tempo = tgl_pinjam + timedelta(days=LAMA_PINJAM)
    dipinjam_sekarang = []

    while sisa_kuota > 0:
        kode = input("\nKode buku (ketik 'selesai' untuk berhenti): ").strip().upper()

        if kode == "SELESAI":
            break
        if kode not in buku:
            print("Kode buku tidak ditemukan!")
            continue
        if buku[kode]["stok"] <= 0:
            print("Stok buku habis!")
            continue

        sudah = False
        for p in pinjaman_aktif(nama):
            if p["kode"] == kode:
                sudah = True
        if sudah:
            print("Buku ini sedang Anda pinjam!")
            continue

        buku[kode]["stok"] -= 1
        peminjaman.append({
            "nama": nama,
            "kode": kode,
            "tgl_pinjam": tgl_pinjam,
            "jatuh_tempo": jatuh_tempo,
            "status": "Dipinjam",
        })
        dipinjam_sekarang.append(kode)
        sisa_kuota -= 1
        print("Berhasil dipinjam:", buku[kode]["judul"])

    if len(dipinjam_sekarang) == 0:
        print("Tidak ada buku yang dipinjam.")
        return

    print("\n========== BUKTI PEMINJAMAN ==========")
    print("Peminjam    :", nama)
    print("Tgl pinjam  :", format_tanggal(tgl_pinjam))
    print("Jatuh tempo :", format_tanggal(jatuh_tempo), f"({LAMA_PINJAM} hari)")
    for i, kode in enumerate(dipinjam_sekarang, start=1):
        print(f"{i}. {buku[kode]['judul']}")
    print(f"Denda keterlambatan: Rp{DENDA_PER_HARI}/hari")


def kembalikan_buku():
    print("\n========== PENGEMBALIAN BUKU ==========")
    nama = input("Nama peminjam: ").strip()
    aktif = pinjaman_aktif(nama)

    if len(aktif) == 0:
        print("Tidak ada pinjaman aktif atas nama tersebut.")
        return

    print("Buku yang sedang dipinjam:")
    for p in aktif:
        print(f"- [{p['kode']}] {buku[p['kode']]['judul']} (jatuh tempo {format_tanggal(p['jatuh_tempo'])})")

    total_denda = 0
    while len(aktif) > 0:
        kode = input("\nKode buku yang dikembalikan (ketik 'selesai' untuk berhenti): ").strip().upper()
        if kode == "SELESAI":
            break

        data_pinjam = None
        for p in aktif:
            if p["kode"] == kode:
                data_pinjam = p
        if data_pinjam is None:
            print("Kode tersebut tidak ada di daftar pinjaman Anda!")
            continue

        tgl_kembali = input_tanggal("Tanggal kembali (DD-MM-YYYY, kosong = hari ini): ")
        if tgl_kembali < data_pinjam["tgl_pinjam"]:
            print("Tanggal kembali tidak boleh sebelum tanggal pinjam!")
            continue

        hari_telat, denda = hitung_denda(data_pinjam["jatuh_tempo"], tgl_kembali)

        data_pinjam["status"] = "Dikembalikan"
        data_pinjam["tgl_kembali"] = tgl_kembali
        data_pinjam["denda"] = denda
        buku[kode]["stok"] += 1
        aktif.remove(data_pinjam)
        total_denda += denda

        print("Buku dikembalikan:", buku[kode]["judul"])
        if hari_telat > 0:
            print(f"Terlambat {hari_telat} hari, denda Rp{denda}")
        else:
            print("Tepat waktu, tidak ada denda.")

    print("\nTotal denda yang harus dibayar: Rp", total_denda)


def tampilkan_peminjaman():
    print("\n========== DAFTAR PEMINJAMAN ==========")
    if len(peminjaman) == 0:
        print("Belum ada data peminjaman.")
        return

    for p in peminjaman:
        judul = buku[p["kode"]]["judul"]
        print(f"{p['nama']:<12} {judul:<30} {p['status']:<13} jatuh tempo: {format_tanggal(p['jatuh_tempo'])}")


def main():
    while True:
        print("\n================================")
        print("   SISTEM PERPUSTAKAAN")
        print("================================")
        print("1. Tampilkan Daftar Buku")
        print("2. Tambah Buku")
        print("3. Cari Buku")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Daftar Peminjaman")
        print("7. Keluar")
        print("================================")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tambah_buku()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            pinjam_buku()
        elif pilihan == "5":
            kembalikan_buku()
        elif pilihan == "6":
            tampilkan_peminjaman()
        elif pilihan == "7":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak tersedia!")


main()