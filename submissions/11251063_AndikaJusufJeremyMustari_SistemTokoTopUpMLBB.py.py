def create(pilihan):
	global item_dibeli
	nominal_diamond_ML = None

	if pilihan == 1:
		list_price = list_harga_diamond()
		price_list_diamond_ML = list_price[0]
		harga_list_diamond_ML = list_price[1]
		print("List Diamond Mobile Legends :")
		print("1. 0 Diamond\n2. 5 Diamond\n3. 12 Diamond\n4. 25 Diamond\n5. 50 Diamond\n6. 70 Diamond\n7. 150 Diamond\n8. 250 Diamond\n9. 500 Diamond\n10. 1000 Diamond\n11. 2500 Diamond")

		try:
			nominal_diamond_ML = int(input("Masukkan Pilihan Jumlah Diamond yang akan dibeli (1-11) :"))
			if 0 <= nominal_diamond_ML <= 11:
				harga_diamond_ML = harga_list_diamond_ML[nominal_diamond_ML - 1]
				jumlah_diamond = price_list_diamond_ML[nominal_diamond_ML - 1]
				pajak = harga_diamond_ML * 0.1
				total = harga_diamond_ML + pajak
				item_dibeli.append({"jenis": "diamond", "jumlah": jumlah_diamond, "harga": harga_diamond_ML, "pajak": pajak, "total": total})
				print(f"Pembelian sejumlah {jumlah_diamond} diamond seharga Rp{harga_diamond_ML} + pajak Rp{pajak:.0f} => Total Rp{total:.0f}")
				print(" ")
				tampilan()
			else:
				print("Pilihan tidak ada, coba lagi.")
				print(" ")
				tampilan()
		except ValueError:
			print("Input tidak cocok, coba lagi.")
	else:
		print("Pilihan tidak ada, coba lagi.")
	return pilihan

def read(pilihan):
	print("=== Data Transaksi ===")
	if not item_dibeli:
		print("Tidak ada data transaksi.")
		print(" ")
		tampilan()
	while True:
		print("Tampilan Data:\n1. Tampilkan Semua Data \n2. Cari Data Tertentu")
		try:
			opsi = int(input("Masukkan pilihan [1-2]: "))
			if opsi == 1:
				print("Item dibeli:")
				for item in item_dibeli:
					if isinstance(item, dict):
						print(f"- {item['jenis'].title()} : {item['jumlah']} unit | Rp{item['total']:.0f}")
						print(" ")
						tampilan()
					else:
						print("-", item)
						print(" ")
						tampilan()
			elif opsi == 2:
				cari = input("Masukkan kata kunci : ")
				ditemukan = False
				for item in item_dibeli:
					if isinstance(item, dict):
						if cari.lower() in item['jenis'].lower():
							print(f"Item ditemukan: {item['jenis'].title()} : {item['jumlah']} unit | Rp{item['total']:.0f}")
							print(" ")
							tampilan()
							ditemukan = True
					else:
						if cari.lower() in str(item).lower():
							print("Item ditemukan:", item)
							print(" ")
							tampilan()
							ditemukan = True
				if not ditemukan:
					print("Tidak ada item yang sesuai.")
					print(" ")
					tampilan()
				break
			else:
				print("Pilihan tidak ada.")
		except ValueError:
			print("Input tidak cocok, coba lagi.")
		break

def perhitungan():
	total_diamond = sum([item['jumlah'] for item in item_dibeli if isinstance(item, dict) and item['jenis'] == 'diamond'])
	total_harga = sum([item['total'] for item in item_dibeli if isinstance(item, dict) and item['jenis'] == 'diamond'])
	return

def update(data):
	if not data:
		print("Data transaksi tidak tersedia. \nTidak dapat memperbarui data transaksi.")
		print(" ")
		tampilan()
		return data
	if data:
		print("Data transaksi:")
		for item in data:
			if isinstance(item, dict):
				print(f"- {item['jenis'].upper()}: {item['jumlah']} unit, Rp{item['total']:.0f}")
		try:
			update_data = int(input("Masukkan tambahan pembelian (1. Diamond atau 2. Tidak menambah pembelian):"))
			while True:
				if update_data == "":
					print("Input kosong. Masukkan 1 atau 2.")
					update_data = int(input("Masukkan tambahan pembelian (1. Diamond atau 2. Tidak menambah pembelian):"))
					continue
				if not str(update_data).isdigit():
					print("Harus memasukkan angka (1 atau 2)!")
					update_data = int(input("Masukkan tambahan pembelian (1. Diamond atau 2. Tidak menambah pembelian):"))
					continue
				if update_data not in (1, 2):
					print("Pilihan harus 1 (Diamond) atau 2 (Tidak menambah pembelian).")
					update_data = int(input("Masukkan tambahan pembelian (1. Diamond atau 2. Tidak menambah pembelian):"))
					continue
				break
			if update_data == 1:
				print("Menambah pembelian...")
				create(1)
				perhitungan()
			elif update_data == 2:
				print("Tidak menambahkan pembelian.")
				print("Terima kasih telah berbelanja di JeMLBBStore.id!")
				exit()
			else:
				print("Pilihan tidak ada.")
		except ValueError:
			print("Input tidak cocok.")
	return

def delete(data):
	if not data:
		print("Data transaksi tidak tersedia. \nTidak ada data transaksi yang bisa dihapus.")
		print(" ")
		tampilan()
		return data
	if data:
		print("Data transaksi:")
		for idx, item in enumerate(data):
			if isinstance(item, dict):
				print(f"{idx + 1}. {item['jenis'].title()}: {item['jumlah']} unit, Rp{item['total']:.0f}")
		try:
			hapus_data = int(input("Masukkan nomor yang ingin dihapus: "))
			if 1 <= hapus_data <= len(data):
				dihapus = data.pop(hapus_data - 1)
				print(f"Item {dihapus['jenis'].title()} berhasil dihapus.")
				while True:
					data_confirm = input("Apakah ingin menampilkan transaksi? (1=Ya, 0=Tidak): ").strip()
					if data_confirm == "":
						print("Input kosong. Masukkan 1 atau 0.")
						continue
					if not data_confirm.isdigit():
						print("Harus memasukkan angka (1 atau 0)!")
						continue
					if data_confirm not in ("1", "0"):
						print("Pilihan harus 1 (Ya) atau 0 (Tidak).")
						continue
					data_confirm_int = int(data_confirm)
					if data_confirm_int == 1:
						print("Data transaksi:")
						for idx, item in enumerate(data):
							if isinstance(item, dict):
								print(f"{idx + 1}. {item['jenis'].title()}: {item['jumlah']} unit, Rp{item['total']:.0f}")
								print("Terima kasih telah berbelanja di JeMLBBStore.id! \n")
								tampilan()
						break
					elif data_confirm_int == 0:
						print("Terima kasih telah berbelanja di JeMLBBStore.id!")
						break
					else:
						break
			else:
				print("Terima kasih telah berbelanja di JeMLBBStore.id!")
		except ValueError:
			print("Input tidak cocok.")
	return data

pilihan = 0
item_dibeli = []

def profile():
    while True:
        id_ML = input("Masukkan ID Mobile Legend (8 atau 9 digit): ")
        if not id_ML.isdigit():
            print("ID harus berupa angka!")
            continue

        if 8 <= len(id_ML) <= 9:
            print(f"ID Mobile Legend: {id_ML}")
            break
        else:
            print("ID Mobile Legend harus terdiri dari 8 atau 9 digit.")

    while True:
        server_ML = input("Masukkan Server Mobile Legend (4 atau 5 digit: ")
        if not server_ML.isdigit():
            print("Server harus berupa angka!")
            continue
        if 4 <= len(server_ML) <= 5:
            print(f"Server Mobile Legend: {server_ML}")
            break
        else:
            print("Server Mobile Legend harus terdiri dari 4 atau 5 digit.")

def list_harga_diamond():
	price_list_diamond_ML = [0, 5, 12, 25, 50, 70, 150, 250, 500, 1000, 2500]
	harga_list_diamond_ML = [0, 1200, 2900, 5800, 11600, 16200, 29000, 48000, 97000, 194000, 485000]
	return price_list_diamond_ML, harga_list_diamond_ML

def tampilan():
	print("====================================")
	print("===       Toko TopUp MLBB        ===")
	print("===      by JeMLBBStore.id       ===")
	print("====================================")
	print("= Selamat Datang di JeMLBBStore.id =")
	print("====================================")
	print("1. Diamond Mobile Legend \n2. Lihat Pesanan Diamond \n3. Tambah Pesanan Diamond \n4. Hapus Pesanan Diamond \n5. Keluar " )
	try:
		pilihan = int(input("Masukkan Pilihan : "))
		if pilihan == 1:
			profile()
			create(pilihan)
		elif pilihan == 2:
			read(pilihan)
		elif pilihan == 3:
			update(item_dibeli)
		elif pilihan == 4:
			delete(item_dibeli)
		elif pilihan == 5:
			print("Terima kasih telah mengunjungi JeMLBBStore.id!")
		else :
			print("Pilihan tidak ada, harap coba lagi.")
	except ValueError:
		print("Input tidak cocok, harap coba lagi.")
tampilan()