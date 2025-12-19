# - Sistem Penilaian Permainan Karnaval -

def create(data):
    print("\n= Tambah Peserta Baru =")
    try:
        id = input("ID tiket: ")
        nama = input("Nama peserta: ")
        print("\nSkor setiap permainan (0–100):")
        skor1 = int(input("1. Darts          : "))
        skor2 = int(input("2. High Striker   : "))
        skor3 = int(input("3. Lempar Cincin  : "))
        skor4 = int(input("4. Lempar Kaleng  : "))
        skor5 = int(input("5. Whack-a-Mole   : "))
        if not all(0 <= s <= 100 for s in [skor1, skor2, skor3, skor4, skor5]):
            print("Harus di antara 0 dan 100!")
            return data
        total = skor1 + skor2 + skor3 + skor4 + skor5
        data.append([id, nama, skor1, skor2, skor3, skor4, skor5, total])
        print(f"Peserta {nama} berhasil ditambahkan.")
    except ValueError:
        print("Harus berupa angka!")
    return data

def read(data):
    print("\n= Lihat Data Peserta =")
    if len(data) == 0:
        print("Belum ada data peserta.")
        return
    print("1. Tampilkan semua peserta")
    print("2. Cari peserta berdasarkan ID tiket")
    print("3. Urutkan berdasarkan total skor dan tampilkan peringkat")
    try:
        pilihan = int(input("Pilih opsi (1-3): "))
        if pilihan == 1:
            tampil_data(data)
        elif pilihan == 2:
            cari = input("ID tiket: ")
            hasil = search(data, cari)
            if hasil != -1:
                print("\nData ditemukan:")
                tampil_data([data[hasil]])
            else:
                print("Peserta tidak ditemukan.")
        elif pilihan == 3:
            tampil_peringkat(data)
        else:
            print("Pilihan tidak valid. (1-3)")
    except ValueError:
        print("Harus berupa angka!")

def update(data):
    print("\n= Ubah Data Peserta =")
    if len(data) == 0:
        print("Belum ada data peserta.")
        return data
    id = input("ID tiket: ")
    index = search(data, id)
    if index == -1:
        print("Peserta tidak ditemukan.")
        return data
    print(f"Data lama: {data[index]}")
    try:
        nama = input("Nama baru (kosongkan jika tidak diubah): ")
        skor_baru = []
        for i, game in enumerate(["Darts", "High Striker", "Lempar Cincin", "Lempar Kaleng", "Whack-a-Mole"], start = 1):
            val = input(f"{i}. Skor {game} baru (kosongkan jika tidak diubah): ")
            skor_baru.append(val)
        if nama:
            data[index][1] = nama
        for i in range(5):
            if skor_baru[i]:
                data[index][2 + i] = int(skor_baru[i])
        data[index][7] = sum(data[index][2:7])
        print("Data peserta berhasil diubah.")
    except ValueError:
        print("Harus berupa angka!")
    return data

def delete(data):
    print("\n= Hapus Data Peserta =")
    if len(data) == 0:
        print("Belum ada data peserta.")
        return data
    id = input("ID tiket: ")
    index = search(data, id)
    if index == -1:
        print("Peserta tidak ditemukan.")
    else:
        konfirmasi = input(f"Apakah benar-benar ingin menghapus {data[index][1]}? (y/n): ")
        if konfirmasi == 'y':
            data.pop(index)
            print("Data peserta berhasil dihapus.")
        else:
            print("Penghapusan dibatalkan.")
    return data

def search(data, id):
    for i in range(len(data)):
        if data[i][0] == id:
            return i
    return -1

def sort(data, reverse = False):
    n = len(data)
    sorted_data = data.copy()
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (reverse and sorted_data[j][7] < sorted_data[j + 1][7]) or \
               (not reverse and sorted_data[j][7] > sorted_data[j + 1][7]):
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
    return sorted_data

def tampil_data(data):
    print("\n{:<8} {:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(
        "ID", "Nama", "Game1", "Game2", "Game3", "Game4", "Game5", "Total"))
    print("-" * 75)
    for d in data:
        print("{:<8} {:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(*d))
    print("-" * 75)

def tampil_peringkat(data):
    print("\n= Peringkat Peserta Berdasarkan Total Skor =")
    if len(data) == 0:
        print("Belum ada data peserta.")
        return
    sorted_data = sort(data, reverse = True)
    print("\n{:<5} {:<8} {:<15} {:<8}".format("Rank", "ID", "Nama", "Total"))
    print("-" * 40)
    for i, d in enumerate(sorted_data, start = 1):
        print("{:<5} {:<8} {:<15} {:<8}".format(i, d[0], d[1], d[7]))
    print("-" * 40)

def menuUtama():
    print("\n=====================================")
    print(" Sistem Penilaian Permainan Karnaval")
    print("=====================================")
    print("1. Tambah Peserta")
    print("2. Lihat Peserta")
    print("3. Ubah Peserta")
    print("4. Hapus Peserta")
    print("5. Keluar")
    try:
        pilihan = int(input("Pilih opsi (1-5): "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan tidak valid. (1-5)")
            return 0
        else:
            return pilihan
    except ValueError:
        print("Harus berupa angka!")
        return 0
data = []
pilihan = 0
while pilihan != 5:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
        input("\nTekan ENTER untuk kembali.")
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)
print("\nTerima kasih telah bermain di karnaval ini!")