def create(data):
    print("\n=== TAMBAH PESANAN JERSEY ===")
    print("Pilihan Klub:")
    print("1. Manchester United (MU)")
    print("2. Real Madrid (RM)") 
    print("3. FC Barcelona (FCB)")
    print("4. Inter Milan (INT)")
    print("5. Juventus (JUV)")
    
    try:
        klub_pilihan = int(input("Pilih klub [1-5]: "))
        if klub_pilihan < 1 or klub_pilihan > 5:
            print("Pilihan klub tidak valid!")
            return data
            
        klub_dict = {1: "MU", 2: "RM", 3: "FCB", 4: "INT", 5: "JUV"}
        klub = klub_dict[klub_pilihan]
        
        print("\nPilihan Ukuran:")
        print("1. XL")
        print("2. L") 
        print("3. M")
        print("4. S")
        
        ukuran_pilihan = int(input("Pilih ukuran [1-4]: "))
        if ukuran_pilihan < 1 or ukuran_pilihan > 4:
            print("Pilihan ukuran tidak valid!")
            return data
            
        ukuran_dict = {1: "XL", 2: "L", 3: "M", 4: "S"}
        ukuran = ukuran_dict[ukuran_pilihan]
        
        harga_dict = {"MU": 250000, "RM": 240000, "FCB": 230000, "INT": 220000, "JUV": 210000}
        harga = harga_dict[klub]
        
        jumlah = int(input("Jumlah pesanan: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0")
            return data
            
        total_harga = harga * jumlah
        
        id_pesanan = f"JER{len(data)+1:03d}"
        
        pesanan = {
            "id": id_pesanan,
            "klub": klub,
            "ukuran": ukuran,
            "harga_satuan": harga,
            "jumlah": jumlah,
            "total_harga": total_harga
        }
        
        data.append(pesanan)
    
        print("\n" + "="*50)
        print("        PESANAN BERHASIL DITAMBAHKAN!")
        print("="*50)
        print("ID Pesanan | Klub | Ukuran | Harga Satuan | Jumlah | Total Harga")
        print("-"*70)
        print(f"{pesanan['id']:10} | {pesanan['klub']:4} | {pesanan['ukuran']:6} | "
              f"Rp {pesanan['harga_satuan']:>9,} | {pesanan['jumlah']:6} | Rp {pesanan['total_harga']:>9,}")
        
    except ValueError:
        print("Input harus berupa angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
    return data

def selection_sort_descending(data):
    n = len(data)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if data[j]['total_harga'] > data[max_idx]['total_harga']:
                max_idx = j
        data[i], data[max_idx] = data[max_idx], data[i]
    return data

def read(data):
    print("\n" + "="*50)
    print("             DAFTAR PESANAN JERSEY")
    print("="*50)
    
    if not data:
        print("Belum ada pesanan...")
        return
    
    data_terurut = selection_sort_descending(data.copy())
    
    print("ID Pesanan | Klub | Ukuran | Harga Satuan | Jumlah | Total Harga")
    print("-"*70)
    
    total_semua = 0
    for pesanan in data_terurut:
        print(f"{pesanan['id']:10} | {pesanan['klub']:4} | {pesanan['ukuran']:6} | "
              f"Rp {pesanan['harga_satuan']:>9,} | {pesanan['jumlah']:6} | Rp {pesanan['total_harga']:>9,}")
        total_semua += pesanan['total_harga']
    
    print("-"*70)
    print(f"TOTAL SEMUA PESANAN: Rp {total_semua:>9,}")
    
    print("\n1. Tampilkan semua (terurut)")
    print("2. Cari berdasarkan klub")
    print("3. Urutkan dari total harga terkecil")
    
    try:
        pilihan_cari = int(input("Pilihan [1-3]: "))
        if pilihan_cari == 2:
            klub_cari = input("Masukkan klub (MU/RM/FCB/INT/JUV): ").upper()
            if klub_cari in ["MU", "RM", "FCB", "INT", "JUV"]:
                hasil_cari = [p for p in data if p['klub'] == klub_cari]
                if hasil_cari:
                    hasil_cari_terurut = selection_sort_descending(hasil_cari)
                    print(f"\nHasil pencarian untuk klub {klub_cari} (terurut):")
                    print("-"*50)
                    for p in hasil_cari_terurut:
                        print(f"  {p['id']} - {p['ukuran']} - {p['jumlah']} pcs - Rp {p['total_harga']:,}")
                else:
                    print(f"Tidak ditemukan pesanan untuk klub {klub_cari}")
            else:
                print("Klub tidak valid!")
        elif pilihan_cari == 3:
            data_terurut_kecil = sorted(data, key=lambda x: x['total_harga'])
            print("\nDaftar Pesanan (Total Harga Terkecil ke Terbesar):")
            print("ID Pesanan | Klub | Ukuran | Harga Satuan | Jumlah | Total Harga")
            print("-"*70)
            for pesanan in data_terurut_kecil:
                print(f"{pesanan['id']:10} | {pesanan['klub']:4} | {pesanan['ukuran']:6} | "
                      f"Rp {pesanan['harga_satuan']:>9,} | {pesanan['jumlah']:6} | Rp {pesanan['total_harga']:>9,}")
                
    except ValueError:
        print("Input harus berupa angka!")

def update(data):
    if not data:
        print("Belum ada pesanan untuk diupdate...")
        return data
        
    read(data)
    
    try:
        id_cari = input("\nMasukkan ID pesanan yang akan diupdate: ").upper()
        
        pesanan_ditemukan = None
        index = -1
        for i, pesanan in enumerate(data): 
            if pesanan['id'] == id_cari:
                pesanan_ditemukan = pesanan
                index = i
                break
        
        if not pesanan_ditemukan:
            print("ID pesanan tidak ditemukan!")
            return data
        
        print(f"\nData pesanan {id_cari}:")
        print(f"Klub: {pesanan_ditemukan['klub']}")
        print(f"Ukuran: {pesanan_ditemukan['ukuran']}")
        print(f"Jumlah: {pesanan_ditemukan['jumlah']}")
        print(f"Total: Rp {pesanan_ditemukan['total_harga']:,}")
        
        print("\nPilihan update:")
        print("1. Ubah jumlah")
        print("2. Ubah ukuran")
        print("3. Batalkan update")
        
        pilihan_update = int(input("Pilihan [1-3]: "))
        
        if pilihan_update == 1:
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            if jumlah_baru > 0:
                data[index]['jumlah'] = jumlah_baru
                data[index]['total_harga'] = data[index]['harga_satuan'] * jumlah_baru
                print(f"\nJumlah pesanan berhasil diupdate menjadi {jumlah_baru}")
                print(f"Total harga baru: Rp {data[index]['total_harga']:,}")
            else:
                print("Jumlah harus lebih dari 0!")
                
        elif pilihan_update == 2:
            print("\nPilihan Ukuran:")
            print("1. XL | 2. L | 3. M | 4. S")
            ukuran_baru = int(input("Pilih ukuran baru [1-4]: "))
            if 1 <= ukuran_baru <= 4:
                ukuran_dict = {1: "XL", 2: "L", 3: "M", 4: "S"}
                data[index]['ukuran'] = ukuran_dict[ukuran_baru]
                print(f"Ukuran berhasil diupdate menjadi {ukuran_dict[ukuran_baru]}")
            else:
                print("Pilihan ukuran tidak valid!")
                
        elif pilihan_update == 3:
            print("Update dibatalkan")
        else:
            print("Pilihan tidak valid!")
            
    except ValueError:
        print("Input harus berupa angka!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
    return data

def delete(data):
    if not data:
        print("Belum ada pesanan untuk dihapus")
        return data
        
    read(data)
    
    try:
        id_hapus = input("\nMasukkan ID pesanan yang akan dihapus: ").upper()
        
        pesanan_ditemukan = None
        index = -1
        for i, pesanan in enumerate(data):
            if pesanan['id'] == id_hapus:
                pesanan_ditemukan = pesanan
                index = i
                break
        
        if not pesanan_ditemukan:
            print("ID pesanan tidak ditemukan!")
            return data
        
        print(f"\nData pesanan yang akan dihapus:")
        print(f"ID: {pesanan_ditemukan['id']}")
        print(f"Klub: {pesanan_ditemukan['klub']}")
        print(f"Ukuran: {pesanan_ditemukan['ukuran']}")
        print(f"Jumlah: {pesanan_ditemukan['jumlah']}")
        print(f"Total: Rp {pesanan_ditemukan['total_harga']:,}")
        
        konfirmasi = input("Yakin ingin menghapus? (iya/tidak): ").lower()
        if konfirmasi == 'iya':
            del data[index]
            print("Pesanan berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan")
            
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    
    return data

def menuUtama():
    print("\n" + "="*50)
    print("    APLIKASI PEMESANAN JERSEY BOLA")
    print("         by ABI STORE")
    print("="*50)
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan") 
    print("3. Edit Pesanan")
    print("4. Hapus Pesanan")
    print("5. Keluar")
    
    try:
        pilihan = int(input("\nMasukkan pilihan [1-5]: "))
        if pilihan < 1 or pilihan > 5:
            print("Pilihan hanya antara 1 sampai 5. Silakan coba lagi.")
            input("Tekan ENTER untuk melanjutkan...")
        else:
            return pilihan
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        input("Tekan ENTER untuk melanjutkan...")

pilihan = 0
data = []

while (pilihan != 5):
    pilihan = menuUtama()
    if (pilihan == 1):
        data = create(data)
        input("\nTekan ENTER untuk kembali ke menu...")
    elif (pilihan == 2):
        read(data)
        input("\nTekan ENTER untuk kembali ke menu...")
    elif (pilihan == 3):
        data = update(data)
        input("\nTekan ENTER untuk kembali ke menu...")
    elif (pilihan == 4):
        data = delete(data)
        input("\nTekan ENTER untuk kembali ke menu...")

print("\nTerima kasih telah menggunakan aplikasi pemesanan jersey!")