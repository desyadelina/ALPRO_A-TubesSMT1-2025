import os
import time

#Membersihkan terminal
def clear_screen():
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

#List dari daftar tol
tarif_tol = [
    [1, "Tol Balikpapan-Samarinda", "Mobil K", 10000],
    [2, "Tol Samarinda-Samboja", "Mobil B", 15000],
    [3, "Tol Samboja-Penajam", "Truk", 25000],
]

#Create
    #Menerima input dari user dan menyimpan / menambahkan ke list data
    #Membaut nomor otomatis
    #Menambahkan data baru ke list

def create_tarif():
    clear_screen()
    print("=== Tambah Tarif Tol Baru ===")
   
    nomor = max([d[0] for d in tarif_tol]) + 1 if tarif_tol else 1
    
    nama_tol = input("Nama Tol: ")
    jenis_kendaraan = input("Jenis Kendaraan: ")
    
    try:
        tarif = int(input("Tarif (Rp): "))
        
        tarif_tol.append([nomor, nama_tol, jenis_kendaraan, tarif])
        
        print("Data berhasil ditambahkan!")
    except ValueError:
        print("Tarif harus berupa angka!")
    
    input("Tekan Enter untuk kembali...")


#Read

    #Menampilkan data yang tersimpan secara rapi dan terstruktur
    #Dapat memberikan pilihan user apakah ingin ditampilkan semua (sorted)
    #atau mencari dengan pilihan dari user

def tampilkan(data):
    print(f"{'Nomor':<6} {'Nama Tol':<25} {'Jenis':<10} {'Tarif'}")
    for d in data:
        print(f"{d[0]:<6} {d[1]:<25} {d[2]:<10} Rp{d[3]}")

def read_tarif():
    clear_screen()
    print("=== Lihat Data Tarif Tol ===")
    print("1. Tampilkan Semua (sorted)")
    print("2. Cari Data")
    pilih = input("Pilih (1/2): ")

    if pilih == "1":
        clear_screen()
        print("=== Semua Data (Sorted) ===")
        data_sorted = bubble_sort(tarif_tol.copy())
        tampilkan(data_sorted)
        input("Tekan Enter untuk kembali...")

    elif pilih == "2":
        clear_screen()
        print("=== Cari Berdasarkan ===")
        print("1. Nomor Tol")
        print("2. Nama Tol")
        print("3. Jenis Kendaraan")

        kategori = input("Pilih (1/2/3): ")
        hasil = [] 

        if kategori == "1":
            nomor = input("Masukkan nomor: ")
            hasil = [d for d in tarif_tol if str(d[0]) == nomor]

        elif kategori == "2":
            nama = input("Masukkan nama: ").lower()
            hasil = [d for d in tarif_tol if nama in d[1].lower()]

        elif kategori == "3":
            jenis = input("Masukkan jenis kendaraan: ").lower()
            hasil = [d for d in tarif_tol if jenis in d[2].lower()]

        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter...")
            return

        clear_screen()
        print("=== Hasil Pencarian ===")
        if hasil:
            tampilkan(hasil)
        else:
            print("Data tidak ditemukan!")

        input("Tekan Enter untuk kembali...")

#sorting

def bubble_sort(data):
    n = len(data)
    for i in range(n-1):                    
        for j in range(0, n-i-1):           
            if (data[j][0] > data[j+1][0]): 
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                
    return data

#Update

def update_tarif():
    #Mengupdate data di list data sesuai data baru dari input user

    clear_screen()
    print("=== Update Tarif Tol ===")
    
    try:
        nomor_update = int(input("Masukkan Nomor yang ingin diupdate: "))

        for t in tarif_tol:
            if t[0] == nomor_update:
                t[1] = input(f"Nama Tol ({t[1]}): ") or t[1]
                t[2] = input(f"Jenis Kendaraan ({t[2]}): ") or t[2]

                tarif_baru = input(f"Tarif ({t[3]}): ")
                if tarif_baru:
                    t[3] = int(tarif_baru)

                print("Data berhasil diupdate!")
                input("Tekan Enter untuk kembali...")
                return
        
        print("Nomor tidak ditemukan!")

    except ValueError:
        print("Nomor harus berupa angka!")

    input("Tekan Enter untuk kembali...")


#Delete

def delete_tarif(data):
    #Menghapus data pilihan user dari list data
   
    clear_screen()
    print("=== Hapus Tarif Tol ===")

    try:
        nomor_hapus = int(input("Masukkan Nomor Tol yang ingin dihapus: "))

        for t in tarif_tol:
            if t[0] == nomor_hapus:
                tarif_tol.remove(t)
                print("Data berhasil dihapus!")
                input("Tekan Enter...")
                return

        print("Nomor tidak ditemukan!")

    except ValueError:
        print("Input harus berupa angka!")

    input("Tekan Enter...")

    return data

def menuUtama(): #contoh fungsi menuUtama
    print("==========================")
    print("=== Aplikasi Tarif Tol ===")
    print("===     by Tol long    ===")
    print("==========================")
    print("1. Tambah Tarif")
    print("2. Lihat Tarif")
    print("3. Edit Tarif")
    print("4. Hapus tarif")
    print("5. Keluar")
    try:
        pilihan = int(input("Masukkan pilihan [1 - 5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya antara 1 sampai 5. Silakan coba lagi.")
            input()
        else:
            return pilihan
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")


##### PROGRAM UTAMA #####

pilihan = 0
data = []

while (pilihan != 5):
    pilihan = menuUtama()
    if (pilihan == 1):
        data = create_tarif()
    elif (pilihan == 2):
        data = read_tarif()
        input("Kembali tekan ENTER..")
    elif (pilihan == 3):
        data = update_tarif()
    elif (pilihan == 4):
        data = delete_tarif(data)
print("Terima kasih..!")
