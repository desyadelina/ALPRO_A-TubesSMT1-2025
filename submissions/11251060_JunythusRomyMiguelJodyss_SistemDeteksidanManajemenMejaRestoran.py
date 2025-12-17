# ====================================================================
# Program Sistem Deteksi dan Manajemen Meja Restoran (TUBES)
# ====================================================================

daftar_meja = [] 

def baca_data():
    global daftar_meja
    daftar_meja = []
    
    try:
        with open("database_meja.txt", "r") as f:
            for baris in f:
                data = baris.strip().split(',')
                if len(data) == 3:
                    try:
                        nomor_meja_int = int(data[0])
                        kapasitas_int = int(data[1])
                        daftar_meja.append([nomor_meja_int, kapasitas_int, data[2]])
                    except ValueError:
                        print(f"[ERROR] Baris data ({data[0]}, {data[1]}) tidak valid (Nomor/Kapasitas bukan angka) dan diabaikan.")
                        
        print("-> Data meja berhasil dimuat.")
    except FileNotFoundError:
        print("-> File database belum ada. Memulai dengan data kosong.")
        

def simpan_data():
    try:
        with open("database_meja.txt", "w") as f:
            for meja in daftar_meja:
                f.write(f"{meja[0]},{meja[1]},{meja[2]}\n")
        print("-> Data berhasil disimpan.")
    except Exception as e:
        print(f"-> Gagal menyimpan data: {e}")

# --- FUNGSI ALGORITMA DASAR ---

def bubble_sort():
    n = len(daftar_meja)
    
    for i in range(n-1):
        for j in range(n-1):
            if daftar_meja[j][1] > daftar_meja[j+1][1]:
                daftar_meja[j], daftar_meja[j+1] = daftar_meja[j+1], daftar_meja[j]
    return

def sequential_search(kunci_str):
    try:
        kunci_int = int(kunci_str)
    except ValueError:
        return [] 

    hasil_pencarian = []
    for meja in daftar_meja:
        if meja[0] == kunci_int: 
            hasil_pencarian.append(meja)
    return hasil_pencarian

# --- FUNGSI CRUD ---

def create_meja():
    print("\n=== Tambah Data Meja ===")
    
    while True:
        try:
            nomor_meja_str = input("Masukkan nomor meja (harus angka): ")
            nomor = int(nomor_meja_str)
            break
        except ValueError:
            print("[ERROR] Nomor meja harus berupa angka!")
            continue

    if sequential_search(str(nomor)):
        print("[ERROR] Nomor meja sudah terdaftar.")
        return
    
    while True:
        try:
            kapasitas = int(input("Masukkan kapasitas meja (angka): "))
            if kapasitas <= 0: 
                print("Kapasitas harus positif.")
                continue
            break
        except ValueError:
            print("[ERROR] Input kapasitas harus berupa angka!")
    
    status = "kosong"
    daftar_meja.append([nomor, kapasitas, status])
    print(f"\n[INFO] Meja {nomor} berhasil ditambahkan.")

def read_meja(list_data):
    print("\n--- DAFTAR MEJA ---")
    if not list_data:
        print("Data meja masih kosong.")
        return
        
    print(f"{'Nomor':<10}{'Kapasitas':<15}{'Status':<10}")
    print("-" * 35)
    
    for meja in list_data:
        kapasitas_display = f"{meja[1]} orang"
        
        print(f"{meja[0]:<10}{kapasitas_display:<15}{meja[2].capitalize():<10}")
    print("-" * 35)

def menu_read():
    if not daftar_meja:
        read_meja(daftar_meja)
        return
        
    print("\n=== TAMPILAN DATA ===")
    print("1. Tampilkan semua data")
    print("2. Urutkan data")
    print("3. Cari data meja")
    opsi = input("Pilih opsi [1-3]: ") 

    if opsi == "1":
        read_meja(daftar_meja)
    elif opsi == "2":
        bubble_sort()
        read_meja(daftar_meja)
    elif opsi == "3":
        kunci = input("Masukkan Nomor Meja yang dicari: ")
        hasil = sequential_search(kunci)
        if hasil:
            read_meja(hasil)
        else:
            print(f"[INFO] Meja dengan nomor '{kunci}' tidak ditemukan atau input tidak valid.") 
    else:
        print("[WARNING] Pilihan tidak valid.")

def update_status():
    print("\n=== Ubah Status Meja ===")
    nomor_input_str = input("Masukkan nomor meja yang ingin diubah: ")
    
    try:
        nomor_input = int(nomor_input_str)
    except ValueError:
        print("[ERROR] Nomor meja harus berupa angka!")
        return

    ditemukan = False
    for meja in daftar_meja:
        if meja[0] == nomor_input:
            if meja[2] == "kosong":
                meja[2] = "terisi"
            else:
                meja[2] = "kosong"
                
            print(f"\n[SUCCESS] Status meja {nomor_input} berhasil diubah menjadi {meja[2].upper()}.")
            ditemukan = True
            break
    
    if not ditemukan:
        print(f"\n[ERROR] Nomor meja '{nomor_input}' tidak ditemukan.")


def delete_meja():
    print("\n=== Hapus Data Meja ===")
    nomor_input_str = input("Masukkan nomor meja yang ingin dihapus: ")
    
    try:
        nomor_input = int(nomor_input_str)
    except ValueError:
        print("[ERROR] Nomor meja harus berupa angka!")
        return
    
    for i in range(len(daftar_meja)):
        if daftar_meja[i][0] == nomor_input:
            del daftar_meja[i] 
            print(f"\n[SUCCESS] Data meja {nomor_input} berhasil dihapus.")
            return
            
    print(f"\n[ERROR] Nomor meja '{nomor_input}' tidak ditemukan.")

# --- FUNGSI MENU UTAMA ---

def menu_utama():
    print("\n" + "#" * 34)
    print("### SISTEM MANAJEMEN MEJA CAFE ###")
    print("#" * 34)
    print("1. Tambah Meja")
    print("2. Lihat / Cari / Urutkan Meja")
    print("3. Ubah Status Meja")
    print("4. Hapus Meja")
    print("5. Keluar dan Simpan Data")

    while True:
        pilihan = input("\nMasukkan pilihan [1 - 5]: ")
        
        if pilihan in ("1", "2", "3", "4", "5"):
            return pilihan
        else:
            print("[ALERT] Pilihan harus 1 sampai 5. Coba lagi!")


def main():
    baca_data()
    
    pilihan = "0"
    while pilihan != "5":
        pilihan = menu_utama()

        if pilihan == "1":
            create_meja()
        elif pilihan == "2":
            menu_read()
            input("Tekan ENTER untuk kembali...")
        elif pilihan == "3":
            update_status()
        elif pilihan == "4":
            delete_meja()
        elif pilihan == "5":
            simpan_data()
            print("\n[INFO] Terima kasih! Sampai jumpa.\n")
            break
            
            
main()