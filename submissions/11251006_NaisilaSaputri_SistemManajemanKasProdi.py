from datetime import datetime

#----------------------------------------------------------------------------------------------------
#  SISTEM MANAJEMAN KAS PRODI BYE NAISILA 
#-----------------------------------------------------------------------------------------------------

admin_password = "adminnih11" # merupakan password default untuk yang login sebagai admin.
target = 30000 # target adalah batas untuk status "LUNAS"
data_mahasiswa = [] # data mahasiswa yang ada didalam prodi berdasarkan NIM & Nama
data_transaksi = [] # data transaksi kas yang ada didalam prodi

#-------------------------------------------------------------------------------------------------------
# CRUD untuk data mahasiswa (admin)
#-------------------------------------------------------------------------------------------------------
def create_mahasiswa(data):
    print("\n=== Tambah Mahasiswa ===")
    try:
        nim = int(input("Masukan NIM Mahasiswa: "))
    except ValueError:
        print("Nim Harus angka!!!")
        return data
    # nim = str(nim_input) #simpan nim sebagai string agar tetap aman

    nama = input("Masukan Nama Mahasiswa: ")
    if nama == "":
        print("Nama Tidak boleh kosong!")
        return
    nama = nama.title()

    # untuk mengecek crate yang dilakukan agar tdk terjadi duplikat nim dan nama
    for mahasiswa in data_mahasiswa:
        if mahasiswa[0] == nim:
            print("NIM sudah ada dalam data mahasiswa!!! Batal Menambahkan.")
            return
        if mahasiswa[1].lower() == nama.lower():
            print("Nama sudah ada dalam data mahasiswa! Batal menambahkan.")
            return data
    
    data_mahasiswa.append([nim, nama])
    print("Mahasiswa berhasil ditambahkan!\n")
    return data

def read_mahasiswa(data):
    print("\n=== Daftar Mahasiswa ===\n")
    print("--------------------------------------------------")

    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
        return

    print("No | NIM        | Nama")
    print("----------------------------------------------------")

    for i, mahasiswa in enumerate(data_mahasiswa, 1):
        print(f"{i:2d} | {mahasiswa[0]:10} | {mahasiswa[1]}")

    print()
    return data


    
def delete_mahasiswa(data):
    print("\n=== HAPUS DATA MAHASISWA ===")
    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa")
        return
    read_mahasiswa(data)

    try:
        nomer_urut_mahasiswa = int(input("Pilih nomer mahasiswa yang ingin dihapus: "))
    except ValueError:
        print("Input Harus Berupa Angka!. Batal.")
        return

    if nomer_urut_mahasiswa < 1 or nomer_urut_mahasiswa > len(data_mahasiswa):
        print("Nomer urut tidak valid! Batal.")
        return
    
    urutan_mahasiswa = nomer_urut_mahasiswa -1 

    del data_mahasiswa[urutan_mahasiswa]
    print("Data mahasiswa berhasil dihapus!")
    return data 
    

    

#--------------------------------------------------------------------------------------------------------------------
# CRUD untuk data Transaksi (admin)
#--------------------------------------------------------------------------------------------------------------------
def create_transaksi(data):
    print("\n=== Tambah Transaki Kas Prodi ===")

    tanggal_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    print(f"Tanggal transaksi otomatis: {tanggal_transaksi}")

    if len(data_mahasiswa) == 0:
        print("Belum ada data mahasiswa! Tidak dapat menambahkan transaksi.")
        return data

    # Menampilkan daftar mahasiswa 
    print("\n=== Daftar Mahasiswa ===\n")
    print("-----------------------------------------")
    print("No | NIM        | Nama")
    print("-----------------------------------------")

    for i, mahasiswa in enumerate(data_mahasiswa, 1):
        print(f"{i:2d} | {mahasiswa[0]:10} | {mahasiswa[1]}")
    print("-----------------------------------------")

    try:
        nomer_urut_mahasiswa = int(input("Pilih nomer urut mahassiwa: "))
    except ValueError:
        print("Harus angka!!! Batal.")
        return data

    if nomer_urut_mahasiswa < 1 or nomer_urut_mahasiswa > len (data_mahasiswa):
        print("Nomor tidak valid! Batal.")
        return data
    
    #fungsi untuk mengambil data mahasiswa otomatis [nim & nama] sesuai dengan inputan 
    urutan_mahasiswa = data_mahasiswa[nomer_urut_mahasiswa -1 ]
    nim = urutan_mahasiswa[0]
    nama = urutan_mahasiswa[1]

    

    #tampilkan data mahasiswa yang dipilih
    print("\nMahasiswa dipilih:")
    print(f"NIM   : {nim}")
    print(f"Nama  : {nama}")

    try:
        nominal = int(input("Nominal (<=30000): "))
    except ValueError:
        print("Harus angka!!!")
        return data

    periode = input("Periode kas yang ingin dibayarkan (contoh: November): ")

    if nominal < target:
        status = "BELUM LUNAS"
    else:
        status = "LUNAS"

    data.append([tanggal_transaksi, nim, nama, nominal, periode, status])
    print("Transaksi berhasil ditambahkan!\n")
    return data


def read_transaksi(data):
    print("\n=== Daftar Transaksi Kas Prodi ===\n")

    if len(data) == 0:
        print("Belum ada transaksi!\n")
        return

    print("No   | Tanggal              | NIM        | Nama               | Nominal      | Periode       | Status")
    print("-----------------------------------------------------------------------------------------------------------")
    
    for i, transaksi in enumerate(data):
        print(f"{i+1:<4} | {transaksi[0]:<20} | {transaksi[1]:<10} | {transaksi[2]:<18} | Rp{transaksi[3]:<10} | {transaksi[4]:<12} | {transaksi[5]}")


    print()
    return data



def update_transaksi(data):
    print("\n=== Edit Transaksi ===\n")
    read_transaksi(data)

    if len(data) == 0:
        return data

    try:
        nomer_transaksi = int(input("Pilih nomer Transaksi yang ingi diedit: "))
    except ValueError:
        print("Harus Angka!!!")
        return data


    posisi = nomer_transaksi -1 
    if posisi < 0 or posisi >= len(data):
        print("Nomer Transaksi yang anda pilih tidak valid")
        return data
    
    # Ambil data lama dari transaksi sebelumnya
    tanggal_lama, nim_lama, nama_lama, nominal_lama, periode_lama, status_lama = data[posisi]
    print("\n------Silahkan masukkan data baru (tekan ENTER jika tidak ingin mengubah data)-----\n")

    # Tanggal otomatis saat melakukan update 
    tanggal_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # melakukan update nim jika memasukan nim baru, jika tidak maka akan default ke nim lama
    nim_update = input(f"NIM [{nim_lama}]: ")
    if nim_update.strip() == "":
        nim_update = nim_lama

    # melakukan update nama jika memasukan nama baru, jika tidak maka akan default ke nama lama
    nama_update = input(f"Nama [{nama_lama}]: ")
    if nama_update.strip() == "":
        nama_update = nama_lama
    
    # melakukan update nominal jika memasukan nominal baru, jika tidak maka akan default ke nominal lama
    print("\n------Jika ingin menambah pembayaran, masukkan nominal tambahan.-----")
    print("---Jika tidak ingin mengubah nominal, tekan ENTER.---")
    nominal_input = input(f"Nominal Tambahan (<=30000) [0]: ")

    if nominal_input.strip() == "":
        nominal_tambahan = 0
    else:
        try:
            nominal_tambahan = int(nominal_input)
        except ValueError:
            print("Harus angka!!!")
            return data

    # akumulasi nominal jika memasukan nominal tambahan (jika sebelumnya nominal adalah 10000 dan memasukan lagi dgn jumlah 20000 maka akan menjadi 30000 dan status lunas)
    nominal_update = nominal_lama + nominal_tambahan

    # melakukan update periode jika memasukan periode baru, jika tidak maka akan default ke periode lama
    periode_update = input(f"Periode [{periode_lama}]: ")
    if periode_update.strip() == "":
        periode_update = periode_lama
    
    # status akan diupdate otomatis jika nominal sudah mencapai target
    status_update = "LUNAS" if nominal_update >= target else "BELUM LUNAS"

    data[posisi] = [tanggal_update, nim_update, nama_update, nominal_update, periode_update, status_update]

    print("Data Transaksi Berhasil Di Update.\n")
    return data
    

def delete_transaksi(data):
    print("\n=== Hapus Data Transaksi ===\n")
    read_transaksi(data)

    if not data:
        return data

    try:
        nomer_transaksi = int(input("Piliha Nomer Transaksi yang ingin dihapus: "))
    except ValueError:
            print("Harus Angka!!!")
            return data

    posisi = nomer_transaksi -1 

    for i in range(len(data)):
        del data[i]
        print("Data Transaksi Berhasil Di Hapus.\n")
        return data

    print("Data Transaksi tidak ditemukan.")
    return data 


# ---------------------------------------------------------------------------------------------------------------------
# Fungsi Menampilkan Semua Data Transaksi
# ---------------------------------------------------------------------------------------------------------------------

def tampilkan_semua_transaksi(data):
    print("\n=== Tampilkan Semua Data Transaksi ===\n")

    if len(data) == 0:
        print("Belum ada data transaksi!\n")
        return data

    print("No   | Tanggal              | NIM        | Nama               | Nominal      | Periode       | Status")
    print("-----------------------------------------------------------------------------------------------------------")

    for i, transaksi in enumerate(data, start=1):
        print(f"{i:<4} | {transaksi[0]:<20} | {transaksi[1]:<10} | {transaksi[2]:<18} | Rp{transaksi[3]:<10} | {transaksi[4]:<12} | {transaksi[5]}")

    print()
    return data



# ---------------------------------------------------------------------------------------------------------------------
# Fungsi Searching dgn menggunakan (Sequential Search)
# ---------------------------------------------------------------------------------------------------------------------

def search_transaksi(data):
    print("\n=== Pencarian Transaksi ===\n")
    # Menampilkan semua data transaksi yang ada.
    tampilkan_semua_transaksi(data)

    # Meminta input berdasarkan kolom dan kata kunci pencarian 
    kolom_dicari = input("Cari berdasarkan (NIM/NAMA/PERIODE/STATUS): ").lower()
    key = input("Masukkan kata yang dicari: ").lower()  

    posisi_kolom_dicari = {
        "nim": 1,
        "nama": 2,
        "periode": 4,
        "status": 5
    }

    if kolom_dicari not in posisi_kolom_dicari:
        print("Kolom tidak valid! Pilih NIM, NAMA, PERIODE, atau STATUS.\n")
        return data

    posisi_kolom = posisi_kolom_dicari[kolom_dicari]

    # Menyaring data sesuai kolom dan kata kunci 
    hasil_pencarian = []
    for transaksi in data:
        nilai_kolom = str(transaksi[posisi_kolom]).lower()

        # Untuk STATUS, harus sama persis seperti kata kunci yang di ketikan pada saat pencarian
        if kolom_dicari == "status":
            if nilai_kolom == key:
                hasil_pencarian.append(transaksi)
        # Untuk kolom lain, harus mengandung kata kunci pencarian
        else:
            if key in nilai_kolom:
                hasil_pencarian.append(transaksi)

    # Jika tidak sesuai pencarian maka tampilkkan pesan sebagai berikut.
    if not hasil_pencarian:
        print("Data yang anda cari tidak ditemukan!!!!. Silahkan coba lagi pencarian lainnya.\n")
        return data

    # Menampilkan hasil hasil pencarian sesuai data yang dicari 
    print("\n=== Hasil Pencarian ===")
    print("No   | Tanggal              | NIM        | Nama               | Nominal      | Periode       | Status")
    print("-----------------------------------------------------------------------------------------------------------")
    for nomor, transaksi in enumerate(hasil_pencarian, start=1):
        print(f"{nomor:<4} | {transaksi[0]:<20} | {transaksi[1]:<10} | {transaksi[2]:<18} | Rp{transaksi[3]:<10} | {transaksi[4]:<12} | {transaksi[5]}")
    print()

    return data


# ---------------------------------------------------------------------------------------------------------------------
# Fungsi Sorting dgn menggunakan (BUBBLE SORT)
# ---------------------------------------------------------------------------------------------------------------------
def buble_sort_transaksi(data, key):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):

            # mengambil nilai berdasarka kata kunci (key) yang dimasukan
            # === sorting berdasarkan Nama (A-Z) ===
            if key == "nama":
                nama_1 = data[j][2].lower()
                nama_2 = data[j + 1][2].lower()

                if nama_1 > nama_2:
                    data[j], data[j + 1] = data[j + 1], data[j]

            # === SORTING BERDASARKAN NIM (kecil - besar), misal 1125 & 1124 maka 1124 akan diurutkan terlebih dahulu, begitupula dgn nim belakang nya 06 dan 46, maka 06 terlebih dahulu ===
            elif key == "nim":
                nim_1 = int(data[j][1])
                nim_2 = int(data[j + 1][1])

                if nim_1 > nim_2:
                    data[j], data[j + 1] = data[j + 1], data[j]
            
            # === SORTING BERDASARKAN NOMINAL (besar → kecil) ===
            elif key == "nominal":
                nominal_1 = data[j][3]
                nominal_2 = data[j + 1][3]

                if nominal_1 < nominal_2:   # besar → kecil
                    data[j], data[j + 1] = data[j + 1], data[j]
            
            # === SORTING BERDASARKAN STATUS ===
            # BELUM LUNAS - LUNAS
            elif key == "status":
                status_1 = data[j][5].lower()
                status_2 = data[j + 1][5].lower()

                if status_1 > status_2:   
                    data[j], data[j + 1] = data[j + 1], data[j]   
                    
    return data

            
# ---------------------------------------------------------------------------------------------------------------------
# Menu Utama
# ---------------------------------------------------------------------------------------------------------------------

def menu_admin():
    print("===================================")
    print("=== Sistem Manajemen Kas Prodi ===")
    print("===            ADMIN            ===")
    print("===================================")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Mahasiswa")
    print("3. Hapus Mahasiswa")
    print("4. Tambah Transaksi")
    print("5. Lihat Transaksi")
    print("6. Edit Transaksi")
    print("7. Hapus Transaksi")
    print("8. Sorting Transaksi")
    print("9. Searching Transaksi")
    print("10. Logout")


    try:
        pilihan = int(input("Masukkan pilihan [1 - 10]: "))
        return pilihan
    except ValueError:
        print("Input harus angka!")
        return 0

# ---------------------------------------------------------------------------------------------------------------------------------
# MENU USER (read-only)
# ---------------------------------------------------------------------------------------------------------------------------------

def menu_user():
    print("===================================")
    print("=== Sistem Manajemen Kas Prodi ===")
    print("===             USER             ===")
    print("===================================")
    print("1. Lihat Mahasiswa")
    print("2. Lihat Transaksi")
    print("3. Sorting Transaksi")
    print("4. Searching Transaksi")
    print("5. Logout")

    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        return pilihan
    except ValueError:
        print("Input harus angka!")
        return 0

# ---------------------------------------------------------------------------------------------------------------------------------------------
# PROGRAM UTAMA
# ----------------------------------------------------------------------------------------------------------------------------------------------

def menuUtama():
    print("=== SISTEM MANAJEMEN KAS PRODI ===")

    while True:
        print("\n=== LOGIN SISTEM ===")
        print("1. Admin")
        print("2. User")
        print("3. Keluar")

        try:
            pilihan_login = int(input("Masukan pilihan [1-3]: " ))
        except ValueError:
                print("Input Harus Angka!!! Silahkan coba lagi.")
                pilihan_login = 0

        # --------------------------------- KELUAR ------------------------------------------------
        if pilihan_login == 3:
            print("Terima kasih sudah login ke sistem manajeman kas prodi kami.")
            break
        
        # --------------------------------- ADMIN ------------------------------------------------
        elif pilihan_login == 1:
            pw = input("Masukkan password admin: ")

            if pw != admin_password:
                print("Password salah!!!, silahkan coba lagi.")
            
            else:
                pilihan = 0
                while pilihan != 10:
                    pilihan = menu_admin()

                    if pilihan == 1:
                        create_mahasiswa(data_mahasiswa)
                    elif pilihan == 2:
                        read_mahasiswa(data_mahasiswa)
                    elif pilihan == 3:
                        delete_mahasiswa(data_mahasiswa)
                    elif pilihan == 4:
                        create_transaksi(data_transaksi)
                    elif pilihan == 5:
                        read_transaksi(data_transaksi)
                    elif pilihan == 6:
                        update_transaksi(data_transaksi)
                    elif pilihan == 7:
                        delete_transaksi(data_transaksi)
                    # fitur sorting dgn pilihan berdasarkan key yang di masukan.
                    elif pilihan == 8: 
                        print("\n=== Tampilkan Semua Data Transaksi ===\n")

                        if len(data_transaksi) == 0:
                            print("Belum ada data transaksi! Tidak bisa melakukan sorting.\n")
                            continue  # balik ke menu admin

                        tampilkan_semua_transaksi(data_transaksi)

                        print("\n=== Urutkan Transaksi ===")
                        print("1. Nama (A-Z)")
                        print("2. NIM (Ascending)")
                        print("3. Nominal (Besar ke Kecil)")
                        print("4. Status")

                        try:
                            pilih = int(input("Pilih jenis sorting: "))
                        except ValueError:
                            print("Input harus angka!")
                            continue

                        if pilih == 1:
                            buble_sort_transaksi(data_transaksi, "nama")
                        elif pilih == 2:
                            buble_sort_transaksi(data_transaksi, "nim")
                        elif pilih == 3:
                            buble_sort_transaksi(data_transaksi, "nominal")
                        elif pilih == 4:
                            buble_sort_transaksi(data_transaksi, "status")
                        else:
                            print("Pilihan tidak valid!")
                            continue
                        
                        print("\n=== Hasil Sorting ===\n")
                        tampilkan_semua_transaksi(data_transaksi)

                    elif pilihan == 9:
                        search_transaksi(data_transaksi)
                    elif pilihan == 10:
                        print("Terima Kasih sudah menggunakan sistem kami. Semoga hari anda menyenangkan.\n")
        
        # -------------------- USER ---------------------- 
        elif pilihan_login == 2:
            pilihan = 0
            while pilihan != 5:
                pilihan = menu_user()

                if pilihan == 1:
                    read_mahasiswa(data_mahasiswa)
                elif pilihan == 2:
                    read_transaksi(data_transaksi)
                # fitur sorting berdasarkan key yang di masukan
                elif pilihan == 3:
                    print("\n=== Tampilkan Semua Data Transaksi ===\n")

                    if len(data_transaksi) == 0:
                        print("Belum ada data transaksi! Tidak bisa melakukan sorting.\n")
                        continue

                    tampilkan_semua_transaksi(data_transaksi)

                    print("\n=== Urutkan Transaksi ===")
                    print("1. Nama (A-Z)")
                    print("2. NIM (Ascending)")
                    print("3. Nominal (Besar ke Kecil)")
                    print("4. Status")

                    try:
                        pilih = int(input("Pilih jenis sorting: "))
                    except ValueError:
                        print("Input harus angka!")
                        continue

                    if pilih == 1:
                        buble_sort_transaksi(data_transaksi, "nama")
                    elif pilih == 2:
                        buble_sort_transaksi(data_transaksi, "nim")
                    elif pilih == 3:
                        buble_sort_transaksi(data_transaksi, "nominal")
                    elif pilih == 4:
                        buble_sort_transaksi(data_transaksi, "status")
                    else:
                        print("Pilihan tidak valid!")
                        continue

                    print("\n=== Hasil Sorting ===\n")
                    tampilkan_semua_transaksi(data_transaksi)

                elif pilihan == 4:
                    search_transaksi(data_transaksi)
                elif pilihan == 5:
                    print("Terima Kasih sudah menggunakan sistem kami. Semoga hari anda menyenangkan.\n")

        else:
            print("Pilihan tidak valid. Silahkan coba lagi!")
menuUtama()