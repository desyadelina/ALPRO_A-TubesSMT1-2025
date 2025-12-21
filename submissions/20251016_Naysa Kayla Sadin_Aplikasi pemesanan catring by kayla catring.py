# ===============================================
#       Aplikasi Pemesanan Catering - Kayla 
# ===============================================

def create(data):
    print("\n=== Tambah Pesanan ===")
    nama = input("Nama Pemesan : ")
    menu = input("Menu Pesanan : ")
    jumlah = input("Jumlah Porsi : ")

    pesanan = {
        "nama": nama,
        "menu": menu,
        "jumlah": jumlah
    }

    data.append(pesanan)
    print("Pesanan berhasil ditambahkan!")
    input("Tekan ENTER untuk kembali...")
    return data


def read(data):
    print("\n=== Daftar Pesanan ===")

    if len(data) == 0:
        print("Belum ada pesanan.")
        input("Tekan ENTER untuk kembali...")
        return

    print("1. Tampilkan semua (sorted by nama)")
    print("2. Cari pesanan")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        sorted_data = sorted(data, key=lambda x: x["nama"])
        for i, d in enumerate(sorted_data):
            print(f"{i+1}. Nama   : {d['nama']}")
            print(f"   Menu   : {d['menu']}")
            print(f"   Jumlah : {d['jumlah']}\n")

    elif pilihan == "2":
        key = input("Masukkan nama/keyword pencarian: ").lower()
        hasil = [d for d in data if key in d["nama"].lower()]
        if len(hasil) == 0:
            print("Data tidak ditemukan.")
        else:
            for i, d in enumerate(hasil):
                print(f"{i+1}. Nama   : {d['nama']}")
                print(f"   Menu   : {d['menu']}")
                print(f"   Jumlah : {d['jumlah']}\n")
    else:
        print("Pilihan tidak valid.")

    input("Tekan ENTER untuk kembali...")


def update(data):
    print("\n=== Edit Pesanan ===")

    if len(data) == 0:
        print("Belum ada pesanan.")
        input("Tekan ENTER untuk kembali...")
        return data

    for i, d in enumerate(data):
        print(f"{i+1}. Nama   : {d['nama']}")
        print(f"   Menu   : {d['menu']}")
        print(f"   Jumlah : {d['jumlah']}")
        print()

    idx = int(input("Pilih nomor pesanan yang mau diedit: ")) - 1

    if idx < 0 or idx >= len(data):
        print("Index tidak valid.")
        return data

    print("Masukkan data baru (biarkan kosong jika tidak ingin mengubah):")
    nama = input("Nama Pemesan baru: ")
    menu = input("Menu baru: ")
    jumlah = input("Jumlah baru: ")

    if nama != "":
        data[idx]["nama"] = nama
    if menu != "":
        data[idx]["menu"] = menu
    if jumlah != "":
        data[idx]["jumlah"] = jumlah

    print("Pesanan berhasil diperbarui!")
    input("Tekan ENTER untuk kembali...")
    return data


def delete(data):
    print("\n=== Hapus Pesanan ===")

    if len(data) == 0:
        print("Belum ada pesanan.")
        input("Tekan ENTER untuk kembali...")
        return data

    for i, d in enumerate(data):
        print(f"{i+1}. {d['nama']} - {d['menu']} - {d['jumlah']} porsi")

    idx = int(input("Pilih nomor yang mau dihapus: ")) - 1

    if idx < 0 or idx >= len(data):
        print("Index tidak valid.")
        return data

    data.pop(idx)

    print("Pesanan berhasil dihapus!")
    input("Tekan ENTER untuk kembali...")
    return data


def menuUtama():
    print("========================================")
    print("===   Aplikasi Pemesanan Catering    ===")
    print("===        by Kayla Catering         ===")
    print("========================================")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Keluar")

    try:
        pilihan = int(input("Masukkan pilihan [1-5]: "))
        if 1 <= pilihan <= 5:
            return pilihan
        else:
            print("Pilihan harus 1 - 5.")
            input("Tekan ENTER...")
    except ValueError:
        print("Input harus angka.")
        input("Tekan ENTER...")

    return 0


# ===============================================
# PROGRAM UTAMA
# ===============================================
pilihan = 0
data = []

while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)

print("Terima kasih telah menggunakan aplikasi!")