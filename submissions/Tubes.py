kursus_list = []

#Fungsi Membuat Kursus
def create():
    try:
        print("\n=== TAMBAHKAN KURSUS  ===")
        id = int(input("ID Kursus: "))        
        for kursus in kursus_list:
            if kursus[0] == id:
                print("ID sudah digunakan!")
                return
        nama = input("Nama Kursus yang dibuat: ")
        harga = int(input("Harga: "))
        durasi = int(input("Durasi (jam): "))
        kursus_list.append([id, nama, harga, durasi])
        print("--- Kursus berhasil ditambahkan! ---")
    except ValueError:
        print("Mohon maaf, harap gunakan angka.")

#Fungsi Menampilkan Kursus
def read():
    print("\n=== LIST KURSUS ===")
    if not kursus_list:
        print("Belum ada kursus, harap tambahkan kursus dulu.")
        return
    for kursus in kursus_list:
        print(f"ID: {kursus[0]} | {kursus[1]} | Rp {kursus[2]:,} | {kursus[3]} jam")

#Fungsi Update Kursus
def update():
    try:
        print("\n=== UPDATE KURSUS ===")
        id_update = int(input("ID Kursus yang akan diupdate: "))
        for kursus in kursus_list:
            if kursus[0] == id_update:
                kursus[1] = input("Nama Baru: ")
                kursus[2] = int(input("Harga Baru: "))
                kursus[3] = int(input("Durasi Baru (jam): "))
                print("Kursus berhasil diupdate!")
                return
        print("ID tidak ditemukan!")
    except ValueError:
        print("Mohon maaf, harap gunakan angka.")

#Fungsi Memhapus Kursus
def delete():
    try:
        print("\n=== HAPUS KURSUS ===")
        id_hapus = int(input("ID Kursus yang akan dihapus: "))
        for i, kursus in enumerate(kursus_list):
            if kursus[0] == id_hapus:
                kursus_list.pop(i)
                print("Kursus berhasil dihapus!")
                return
        print("ID tidak ditemukan!")
    except ValueError:
        print("Mohon maaf, harap gunakan angka.")

#Fungsi Mencari Kursus
def search():
    print("\n=== CARI KURSUS ===")
    print("1. Cari berdasarkan ID")
    print("2. Cari berdasarkan Nama")
    try:
        pilihan = int(input("\nPilih metode pencarian: "))
        if pilihan == 1:
            id_cari = int(input("Masukkan ID yang dicari: "))
            found = False
            for kursus in kursus_list:
                if kursus[0] == id_cari:
                    print("\nHasil Pencarian:")
                    print(f"ID: {kursus[0]} | {kursus[1]} | Rp {kursus[2]:,} | {kursus[3]} jam")
                    found = True
                    break
            if not found:
                print("Kursus dengan ID tersebut tidak ditemukan!")
        elif pilihan == 2:
            nama_cari = input("Masukkan nama kursus yang dicari: ").lower()
            results = []
            for kursus in kursus_list:
                if nama_cari in kursus[1].lower():
                    results.append(kursus)
            if results:
                print(f"\nDitemukan {len(results)} hasil pencarian:")
                for kursus in results:
                    print(f"ID: {kursus[0]} | {kursus[1]} | Rp {kursus[2]:,} | {kursus[3]} jam")
            else:
                print("Tidak ada kursus dengan nama tersebut!")
    except ValueError:
        print("Mohon maaf, harap gunakan angka.")

#Fungsi Mengurutkan Kursus
def sort_kursus():
    print("\n=== SORTIR KURSUS ===")
    if not kursus_list:
        print("Belum ada kursus, harap tambahkan kursus dulu.")
        return
    print("Pilih kriteria pengurutan:")
    print("1. Berdasarkan ID")
    print("2. Berdasarkan Nama")
    print("3. Berdasarkan Harga")
    print("4. Berdasarkan Durasi")
    try:
        kriteria = int(input("Pilihan (1-4): "))
        if kriteria not in [1, 2, 3, 4]:
            print("Pilihan tidak valid!")
            return
        print("\nPilih urutan:")
        if kriteria == 2:
            print("1. A-Z (Ascending)")
            print("2. Z-A (Descending)")
        else:  
            print("1. Terkecil ke Terbesar (Ascending)")
            print("2. Terbesar ke Terkecil (Descending)")
        urutan = int(input("Pilihan (1-2): "))
        if urutan not in [1, 2]:
            print("Pilihan tidak valid!")
            return        
        sorted_list = kursus_list.copy()        
        n = len(sorted_list)
        for i in range(n-1):
            for j in range(0, n-i-1):
                swap = False                
                if kriteria == 1: 
                    if urutan == 1:  
                        if sorted_list[j][0] > sorted_list[j+1][0]:
                            swap = True
                    else:  
                        if sorted_list[j][0] < sorted_list[j+1][0]:
                            swap = True
                elif kriteria == 2:  
                    if urutan == 1:  
                        if sorted_list[j][1].lower() > sorted_list[j+1][1].lower():
                            swap = True
                    else: 
                        if sorted_list[j][1].lower() < sorted_list[j+1][1].lower():
                            swap = True
                elif kriteria == 3: 
                    if urutan == 1:  
                        if sorted_list[j][2] > sorted_list[j+1][2]:
                            swap = True
                    else:  
                        if sorted_list[j][2] < sorted_list[j+1][2]:
                            swap = True
                elif kriteria == 4:  
                    if urutan == 1:  
                        if sorted_list[j][3] > sorted_list[j+1][3]:
                            swap = True
                    else:  
                        if sorted_list[j][3] < sorted_list[j+1][3]:
                            swap = True
                if swap:
                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
        print(f"\n=== HASIL SORTIR ===")
        print(f"Kriteria: {'ID' if kriteria == 1 else 'Nama' if kriteria == 2 else 'Harga' if kriteria == 3 else 'Durasi'}")
        print(f"Urutan: {'Ascending' if urutan == 1 else 'Descending'}")
        print("-" * 50)
        for kursus in sorted_list:
            print(f"ID: {kursus[0]} | {kursus[1]} | Rp {kursus[2]:,} | {kursus[3]} jam")
        konfirmasi = input("\nApakah Anda ingin mengubah urutan data asli? (ya/tidak): ").lower()
        if konfirmasi == 'ya':
            for i in range(len(kursus_list)):
                kursus_list[i] = sorted_list[i]
            print("Data berhasil diperbarui!")
    except ValueError:
        print("Pilihan hanya boleh angka!")

#Fungsi Menu Utama
def main():
    while True:
        print("\n=== Aplikasi Raja Akademik ===")
        print("1. Tambahkan Kursus")
        print("2. List Kursus")
        print("3. Update Kursus")
        print("4. Hapus Kursus")
        print("5. Cari Kursus")
        print("6. Pengurutan Kursus") 
        print("7. Keluar")
        try:
            pilihan = int(input("\nPilih menu: "))
            if pilihan == 1:
                create()
            elif pilihan == 2:
                read()
            elif pilihan == 3:
                update()
            elif pilihan == 4:
                delete()
            elif pilihan == 5:
                search()
            elif pilihan == 6:
                sort_kursus()
            elif pilihan == 7:
                print("\n======================================================")
                print("=== Terimakasih sudah mengunjungi aplikasi kami :) ===")
                print("======================================================\n")
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Masukkan angka!")

main()