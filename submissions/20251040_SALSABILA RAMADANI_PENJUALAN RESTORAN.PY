menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama": "Mie Goreng", "harga": 12000},
    3: {"nama": "Ayam Goreng", "harga": 18000},
    4: {"nama": "Es Teh", "harga": 5000},
    5: {"nama": "Es Jeruk", "harga": 6000}
}

pesanan = []

def tampil_menu():
    print("\n=== MENU ===")
    print("Kode | Nama         | Harga")
    print("-" * 30)
    for kode, item in menu.items():
        print(f"{kode:4} | {item['nama']:<12} | Rp {item['harga']}")

# CREATE 
def tambah():
    tampil_menu()
    try:
        kode = int(input("\nKode: "))
        if kode not in menu:
            print("Kode salah")
            return
        
        jml = int(input("Jumlah: "))
        if jml < 1:
            print("Minimal 1")
            return
        
        item = menu[kode]
        subtotal = item['harga'] * jml
        pesanan.append({
            "nama": item['nama'],
            "harga": item['harga'],
            "jumlah": jml,
            "subtotal": subtotal
        })
        print(f"{item['nama']} ditambah")
    except:
        print("Input angka")

# READ
def lihat():
    if not pesanan:
        print("\nTidak ada pesanan")
        return
    
    print("\n=== PESANAN ===")
    print("No | Menu         | Harga  | Jml | Subtotal")
    print("-" * 45)
    total = 0
    for i, item in enumerate(pesanan, 1):
        print(f"{i:2} | {item['nama']:<12} | {item['harga']:6} | {item['jumlah']:3} | {item['subtotal']:8}")
        total += item['subtotal']
    print("-" * 45)
    print(f"TOTAL: Rp {total}")

    # BUBBLE SORT
def urutkan():
    if not pesanan:
        print("\nTidak ada pesanan")
        return
    
    n = len(pesanan)
    
    for i in range(n-1):
        for j in range(0, n-1-i):
            if pesanan[j]['nama'] > pesanan[j+1]['nama']:
                pesanan[j], pesanan[j+1] = pesanan[j+1], pesanan[j]
    
    print("Pesanan diurutkan")

    # LINEAR SEARCH
def cari():
    if not pesanan:
        print("\nTidak ada pesanan")
        return
    
    cari_nama = input("\nCari nama: ").lower()
    
    hasil = []
    for i in range(len(pesanan)):
        if cari_nama in pesanan[i]['nama'].lower():
            hasil.append(pesanan[i])
    
    if hasil:
        print(f"\nDitemukan {len(hasil)}:")
        for item in hasil:
            print(f"{item['nama']} | Rp {item['harga']} | {item['jumlah']}x | Rp {item['subtotal']}")
    else:
        print("Tidak ditemukan")

# UPDATE 
def edit():
    if not pesanan:
        print("\nTidak ada pesanan")
        return
    
    lihat()
    try:
        no = int(input("\nNomor: "))
        if no < 1 or no > len(pesanan):
            print("Nomor salah")
            return
        
        jml_baru = int(input("Jumlah baru: "))
        if jml_baru < 1:
            print("Minimal 1")
            return
        
        pesanan[no-1]['jumlah'] = jml_baru
        pesanan[no-1]['subtotal'] = pesanan[no-1]['harga'] * jml_baru
        print("Diupdate")
    except:
        print("Input angka")

# DELETE
def hapus():
    if not pesanan:
        print("\nTidak ada pesanan")
        return
    
    lihat()
    try:
        no = int(input("\nNomor: "))
        if no < 1 or no > len(pesanan):
            print("Nomor salah")
            return
        
        yakin = input(f"Hapus {pesanan[no-1]['nama']}? (y/t): ")
        if yakin.lower() == 'y':
            item = pesanan.pop(no-1)
            print(f"{item['nama']} dihapus")
    except:
        print("Input angka")

def bayar():
    if not pesanan:
        print("\nTidak ada pesanan")
        return
    
    lihat()
    total = 0
    for item in pesanan:
        total += item['subtotal']
    
    try:
        bayar = int(input(f"\nTotal: Rp {total}\nBayar: Rp "))
        if bayar < total:
            print("Uang kurang")
            return
        
        kembali = bayar - total
        print(f"Kembali: Rp {kembali}")
        print("Terima kasih")
        pesanan.clear()
    except:
        print("Input angka")

def main():
    while True:
        print("\n" + "="*25)
        print("   RESTORAN SALSA")
        print("="*25)
        print("1. Lihat Menu")
        print("2. Tambah pesanan")
        print("3. Lihat Pesanan")
        print("4. Urutkan pesannan")
        print("5. Cari pesanan")
        print("6. Edit pesanan")
        print("7. Hapus pesanan")
        print("8. Bayar")
        print("9. Keluar")
        
        pilih = input("Pilih [1-9]: ")
        
        if pilih == '1':
            tampil_menu()
        elif pilih == '2':
            tambah()
        elif pilih == '3':
            lihat()
        elif pilih == '4':
            urutkan()
        elif pilih == '5':
            cari()
        elif pilih == '6':
            edit()
        elif pilih == '7':
            hapus()
        elif pilih == '8':
            bayar()
        elif pilih == '9':
            print("Selesai")
            break
        else:
            print("Pilihan salah")
        
        input("\nEnter...")

if __name__ == "__main__":
    main()