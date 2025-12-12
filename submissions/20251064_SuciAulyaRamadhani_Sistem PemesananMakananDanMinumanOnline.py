# SISTEM PEMESANAN MAKANAN & MINUMAN ONLINE 


menu = [
    [1, "Makanan", "Nasi goreng", 18000],
    [2, "Makanan", "Mie goreng", 15000],
    [3, "Minuman", "Es coklat", 10000],
    [4, "Minuman", "Es teh", 5000]
    ]

#Read
def read_menu():
    print("=== DAFTAR MENU ===\n")
    
    print("Kategori: Makanan")
    for item in menu:
        if item[1].lower() == "makanan":
            print(f"ID {item[0]} | {item[2]} - Rp{item[3]}")
    
    print("\nKategori: Minuman")
    for item in menu:
        if item[1].lower() == "minuman":
            print(f"ID {item[0]} | {item[2]} - Rp{item[3]}")



#Create
def create_menu(): 
    print("\n=== Tambah Menu Baru ===")

    kategori = input("Masukan kategori makanan/minuman:").lower()
    if kategori not in ["makanan" , "minuman"] :
        print("Kategori tidak valid")
        
    nama = input("Masukkan nama menu:")
    try:
        harga = int(input("Masukkan harga:"))
    except ValueError : 
            print("Harga harus angka:")
            return 
        
    new_id = menu [-1][0] + 1

    menu.append ( [new_id, kategori, nama, harga]) 
    print("Menu berhasil ditambahkan")
    print(f"ID {new_id}, {nama}, - Rp {harga}")


#Update
def update_menu():
    print("\n=== Update Menu ===")

    try:
        id_update = int(input("Masukkan ID menu yang ingin diperbarui: "))
    except ValueError:
        print("ID harus angka!")
        return

    for item in menu:
        if item[0] == id_update:
            print(f"Menu ditemukan: {item[2]} - Rp{item[3]}")

            kategori_baru = input("Kategori baru (makanan/minuman): ").lower()
            if kategori_baru not in ["makanan", "minuman"]:
                print("Kategori tidak valid!")
                return
            
            nama_baru = input("Nama menu baru: ")

            try:
                harga_baru = int(input("Harga baru: "))
            except ValueError:
                print("Harga harus angka!")
                return

            item[1] = kategori_baru.capitalize()
            item[2] = nama_baru
            item[3] = harga_baru

            print("\nMenu berhasil diperbarui!")
            print(f"ID {item[0]} | {item[1]} | {item[2]} - Rp{item[3]}")
            return

    print("ID tidak ditemukan!")


#Delete
def delete_menu():
    print("\n=== Hapus menu===")

    id_delete = int(input("Masukkan ID menu yang ingin dihapus: "))

    for item in menu:
        if item[0] == id_delete:
            print(f"Menu ditemukan: {item[2]} - Rp{item[3]}")
            konfirmasi = input("Yakin ingin menghapus menu? (Y/N): ").strip().lower()
            if konfirmasi == "y":
                menu.remove(item)
                print("Menu berhasil dihapus")
            else:
                print("Penghapusan dibatalkan")
            return

#Searching
def search_menu():
    print("\n=== Pencarian Menu ===")
    keyword = input("Masukkan kata kunci (nama menu):").lower()
    hasil = []

    for item in menu:
        if keyword in item[2].lower():
            hasil.append(item)
    if hasil:
        print("\nMenu ditemukan:")
        for item in hasil:
            print(f"ID {item[0]} {item[1]} {item[2]} - Rp{item[3]}")
    else:
        print("Menu tidak ditemukan")

#Sorting
def sort_menu():
    print("\n=== Urutkan menu ===")
    print("1. Berdasar kan nama (A-Z)")
    print("2. Berdasarkan harga (termahal-termurah)")
    print("3. Berdasarkan harga (termurah-termahal)")

    pilihan = input("Pilih opsi (1-3):").strip()

    if pilihan == "1":
        sorted_menu = sorted(menu, key=lambda x: x[2].lower())
    elif pilihan == "2": 
        sorted_menu = sorted(menu, key=lambda x: x[3], reverse=True)
    elif pilihan == "3":
        sorted_menu= sorted (menu, key=lambda x:x [3])
    else:
        print("Opsi tidak valid")
        return

    print("\n=== Hasil menu setelah sorting ===")
    for item in sorted_menu:
        print(f"ID {item[0]} {item[1]} {item[2]} - Rp{item[3]}")

#Keranjang belanja
cart = []
#Tambah item ke keranjang
def add_to_cart():
    print("\n=== Tambahkan menu ke keranjang ===")
    read_menu()
    
    try:
        id_pesanan = int(input("Masukkan ID menu yang ingin dipesan: ").strip())
        qty = int(input("Jumlah pesanan: ").strip())
    except ValueError:
        print("ID dan jumlah harus angka!")
        return

    # cari item di menu berdasarkan ID
    for item in menu:
        if item[0] == id_pesanan:
            if qty <= 0:
                print("Jumlah harus lebih dari 0")
                return
            nama = item[2]
            harga = item[3]
            # tambahkan ke keranjang: (nama, harga, qty)
            cart.append([nama, harga, qty])
            print(f"Berhasil menambahkan {qty} x {nama} ke keranjang.")
            return

    # kalau tidak ditemukan
    print("ID menu tidak ditemukan!")
#lihat keranjang
def view_cart(): 
    if not cart:
        print("\nKeranjang kosong.")
        return
    print("\n===Keranjang Anda ===")
    total = 0
    for i, item in enumerate(cart, 1):
        nama , harga, qty = item 
        subtotal = harga * qty 
        total += subtotal
        print(f"{i}.{nama} Rp{harga} * {qty} = Rp{subtotal}")
    print(f"Total: Rp{total}")

#Checkout
def checkout():
    if not cart:
        print("\nKeranjang kosong. Tambahkan menu terlebih dahulu.")
        return
    
    view_cart()
    konfirmasi = input("Apakah Anda ingin melanjutkan pembayaran? (Y/N):")
    if konfirmasi == "y":
        total= sum(item[1]*item[2] for item in cart)
        print(f"\nTotal pembayaran: Rp{total}")
        print("Terima kasih! Pesanan Anda sedang diproses")
        cart.clear()
    else:
        print("Checkout dibatalkan")
        
def main():
    while True:
        
        print("\n=== Aplikasi menu ===")
        print("1. Lihat menu")
        print("2. Tambah menu")
        print("3. Update menu")
        print("4. Hapus menu")
        print("5. Cari menu")
        print("6. Sortir menu")
        print("7. Tambah pesanan ke keranjang")
        print("8. Lihat keranjang")
        print("9. Checkout")
        print("10. Keluar")
        pilihan = input("Pilih (1-10):").strip()
        
        if pilihan == "1":
            read_menu()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "2":
            create_menu()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "3":
            update_menu()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "4":
            delete_menu()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "5":
            search_menu()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "6":
            sort_menu()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "7":
            add_to_cart()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "8":
            view_cart()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "9":
            checkout()
            input("\nTekan enter untuk kembali...")
        elif pilihan == "10":
            print("Keluar, Sampai Jumpa dan Terima Kasih")
            break
        else:
            print("Pilihan tidak valid")
            input("Tekan Enter untuk lanjut...")
main()
