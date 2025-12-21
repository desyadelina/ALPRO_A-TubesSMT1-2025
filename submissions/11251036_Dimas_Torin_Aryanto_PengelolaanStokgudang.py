import os

# fungsi untuk membersihkan layar
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# DATA 
stok_data = []

# DATA RIWAYAT BARANG KELUAR
riwayat_keluar = []

#### CREATE ####
def create(stok_data):
    clean_screen()
    print("===========================")
    print("=== MEMASUKKAN BARANG ===")
    print("===========================")

    nama_barang = input("Nama Barang: ")
    id_barang = input("ID Barang: ")
    tanggal_masuk = input("Tanggal Masuk (dd/mm/yyyy): ")

    try:
        jumlah_masuk = int(input("Jumlah Masuk: "))
    except ValueError:
        input("Jumlah harus angka! Tekan ENTER...")
        return stok_data

    # CEK apakah ID sudah ada
    for barang in stok_data:
        if barang["id"] == id_barang:
            barang["jumlah"] += jumlah_masuk
            input("Barang berhasil dimasukkan. Tekan ENTER...")
            return stok_data

    # Jika ID belum ada, tambahkan data baru
    stok_data.append({
        "id": id_barang,
        "nama": nama_barang,
        "jumlah": jumlah_masuk,
        "tanggal": tanggal_masuk
    })

    input("Barang berhasil dimasukkan. Tekan ENTER...")
    return stok_data


#### READ ####
def read(stok_data):
    clean_screen()
    print("============================")
    print("=== STOK BARANG ===")
    print("============================\n")

    if not stok_data:
        print("Belum ada data barang.")
        return

    # untuk tabel
    print(f"{'ID':<10} {'Nama Barang':<20} {'Jumlah':<10} {'Tanggal Masuk':<15}")
    print("-" * 55)

    for barang in stok_data:
        print(f"{barang['id']:<10} {barang['nama']:<20} {barang['jumlah']:<10} {barang['tanggal']:<15}")


#### UPDATE ####
def update(stok_data):
    clean_screen()
    print("==============================")
    print("=== MENGELOLA BARANG KELUAR===")
    print("==============================")

    id_barang = input("ID Barang: ")

    # Cari berdasarkan ID
    for barang in stok_data:
        if barang["id"] == id_barang:
            print("Nama Barang     :", barang["nama"])
            print("Jumlah Saat Ini :", barang["jumlah"])

            tanggal_keluar = input("Tanggal Keluar (dd/mm/yyyy): ")

            try:
                jumlah_keluar = int(input("Jumlah Keluar: "))
            except ValueError:
                input("Jumlah harus angka! Tekan ENTER...")
                return stok_data

            if jumlah_keluar <= barang["jumlah"]:
                barang["jumlah"] -= jumlah_keluar
                input("Barang berhasil dikeluarkan. Tekan ENTER...")

                # Catat riwayat
                riwayat_keluar.append({
                    "id": barang["id"],
                    "nama": barang["nama"],
                    "jumlah": jumlah_keluar,
                    "tanggal": tanggal_keluar
                })

            else:
                input("Jumlah barang keluar melebihi stok! Tekan ENTER...")

            return stok_data

    input("Barang tidak ditemukan. Tekan ENTER...")
    return stok_data


#### DELETE ####
def delete(stok_data):
    clean_screen()
    print("==========================")
    print("=== HAPUS DATA BARANG ===")
    print("==========================")

    id_barang = input("Masukkan ID barang yang ingin dihapus: ")

    for barang in stok_data:
        if barang["id"] == id_barang:
            konfirmasi = input(
                f"Yakin hapus barang '{barang['nama']}'? (y/n): "
            ).lower()

            if konfirmasi == "y":
                stok_data.remove(barang)
                input("Data berhasil dihapus! Tekan ENTER...")
            else:
                input("Penghapusan dibatalkan. Tekan ENTER...")

            return stok_data

    input("Barang tidak ditemukan! Tekan ENTER...")
    return stok_data


#################### BATAS CRUD ####################

#### SEARCH ####
def search_item(stok_data):
    clean_screen()
    print("==========================")
    print("=== CARI DATA BARANG ===")
    print("==========================")

    print("1. Cari berdasarkan ID")
    print("2. Cari berdasarkan Nama")
    pilihan = input("Pilih metode pencarian: ")

    if pilihan == "1":
        id_barang = input("Masukkan ID Barang: ")
        for barang in stok_data:
            if barang["id"] == id_barang:
                print("\nData ditemukan:\n")
                print(f"{'ID':<10}: {barang['id']}")
                print(f"{'Nama':<10}: {barang['nama']}")
                print(f"{'Jumlah':<10}: {barang['jumlah']}")
                print(f"{'Tanggal':<10}: {barang['tanggal']}")
                input("\nTekan ENTER untuk kembali...")
                return
        print("Barang tidak ditemukan.")

    elif pilihan == "2":
        nama_cari = input("Masukkan Nama Barang: ").lower()
        ditemukan = False

        print("\nHasil pencarian:\n")
        print(f"{'ID':<10} {'Nama Barang':<20} {'Jumlah':<10} {'Tanggal Masuk':<15}")
        print("-" * 55)

        for barang in stok_data:
            if nama_cari in barang["nama"].lower():
                print(f"{barang['id']:<10} {barang['nama']:<20} {barang['jumlah']:<10} {barang['tanggal']:<15}")
                ditemukan = True

        if not ditemukan:
            print("Nama barang tidak ditemukan.")

    else:
        print("Pilihan tidak valid.")

    input("\nTekan ENTER untuk kembali...")


#### SORT ####
def sort_stok(stok_data):
    clean_screen()
    print("==========================")
    print("=== URUTKAN DATA BARANG ===")
    print("==========================")
    print("Sorting berdasarkan jumlah barang (kecil → besar)\n")

    if not stok_data:
        input("Tidak ada data untuk diurutkan. ENTER...")
        return

    # Bubble sort
    n = len(stok_data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if stok_data[j]["jumlah"] > stok_data[j + 1]["jumlah"]:
                stok_data[j], stok_data[j + 1] = stok_data[j + 1], stok_data[j]

    clean_screen()
    print("=== HASIL SORTING (Jumlah Barang) ===\n")

    print(f"{'ID':<10} {'Nama Barang':<20} {'Jumlah':<10} {'Tanggal Masuk':<15}")
    print("-" * 55)

    for barang in stok_data:
        print(f"{barang['id']:<10} {barang['nama']:<20} {barang['jumlah']:<10} {barang['tanggal']:<15}")

    input("\nTekan ENTER untuk kembali...")


#### RIWAYAT BARANG KELUAR ####
def riwayat_barang_keluar():
    clean_screen()
    print("================================")
    print("=== RIWAYAT BARANG KELUAR ===")
    print("================================\n")

    if not riwayat_keluar:
        print("Belum ada barang keluar.")
        input("ENTER...")
        return

    print(f"{'ID':<10} {'Nama Barang':<20} {'Jumlah Keluar':<15} {'Tanggal Keluar':<15}")
    print("-" * 65)

    for r in riwayat_keluar:
        print(f"{r['id']:<10} {r['nama']:<20} {r['jumlah']:<15} {r['tanggal']:<15}")

    input("\nTekan ENTER untuk kembali...")


#### MENU ####
def menu_utama():
    clean_screen()
    print("============================")
    print("===   MENU UTAMA GUDANG  ===")
    print("============================")
    print("1. Barang Masuk")
    print("2. Barang Keluar")
    print("3. Lihat Stok")
    print("4. Hapus Data Barang")
    print("5. Cari Barang")
    print("6. Urutkan Barang")
    print("7. Riwayat Barang Keluar")
    print("8. Keluar")

    try:
        pilihan_menu = int(input("Masukkan pilihan [1-8]: "))
        return pilihan_menu
    except ValueError:
        input("Input harus angka! Tekan ENTER...")
        return 0


#### PROGRAM UTAMA ####

data = stok_data
pilihan_menu = 0

while pilihan_menu != 8:
    pilihan_menu = menu_utama()

    if pilihan_menu == 1:
        data = create(data)
    elif pilihan_menu == 2:
        data = update(data)
    elif pilihan_menu == 3:
        read(data)
        input("Tekan ENTER untuk kembali...")
    elif pilihan_menu == 4:
        data = delete(data)
    elif pilihan_menu == 5:
        search_item(data)
    elif pilihan_menu == 6:
        sort_stok(data)
    elif pilihan_menu == 7:
        riwayat_barang_keluar()
    elif pilihan_menu == 8:
        break
    else:
        input("Pilihan tidak valid. ENTER...")

print("Terima kasih! Program selesai.")

