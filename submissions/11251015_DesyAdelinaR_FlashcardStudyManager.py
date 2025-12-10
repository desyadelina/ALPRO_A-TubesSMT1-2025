# filepath: submissions/11251015_DesyAdelinaR_FlashcardStudyManager.py
# Nama     : Desy Adelina R
# NIM      : 11251015
# Judul    : Flashcard Study Manager

# dummy data flashcard dgn kategorinya
def dummy_data():
    return {
        "Algoritma dan Pemrograman": [
            {"q": "Apa itu crud?", "a": "Create, Read, Update, Delete"},
            {"q": "Apa itu algoritma?", "a": "Langkah-langkah penyelesaian masalah"},
            # {"q": "Apa itu flowchart?", "a": "Diagram alur proses algoritma"}, (sample ntar buat input)
        ],
        "Sistem Digital": [
            {"q": "Apa itu bit?", "a": "Unit terkecil data digital"},
            {"q": "Apa itu bilangan biner?", "a": "Bilangan berbasis 2 (0 dan 1)"},
        ],
        "Matematika Diskrit": [
            {"q": "Apa itu himpunan?", "a": "Kumpulan objek yang terdefinisi"},
            {"q": "Apa itu relasi?", "a": "Hubungan antar anggota himpunan"},
        ]
    }
# ada menu utama, menu manajemen kategori, menu manajemen flashcard, dan submenu lihat flashcard
def menu_utama():
    print("="*35)
    print("=     FlashCard Study Manager     =")
    print("="*35)
    print("1. Manajemen Flashcard")
    print("2. Manajemen Kategori")
    print("3. Mode Flashcard")
    print("4. Keluar")
    return input("Pilih menu [1-4]: ")
def menu_kat():
    print("\n--- Manajemen Kategori ---")
    print("1. Lihat Kategori")
    print("2. Tambah Kategori")
    print("3. Edit Kategori")
    print("4. Hapus Kategori")
    print("5. Kembali")
    return input("Pilih menu [1-5]: ")
def menu_fc():
    print("\n--- Manajemen Flashcard ---")
    print("1. Lihat Flashcard")
    print("2. Tambah Flashcard")
    print("3. Edit Flashcard")
    print("4. Hapus Flashcard")
    print("5. Kembali")
    return input("Pilih menu [1-5]: ")
def menu_lihat_fc():
    print("\nLihat Flashcard:")
    print("1. Tampilkan semua")
    print("2. Tampilkan terurut")
    print("3. Cari pertanyaan")
    print("4. Kembali")
    return input("Pilih menu [1-4]: ")
# func untuk manajemen kategori
def show_kat(kat):
    if not kat:
        print("Belum ada kategori.")
        return
    print("Kategori:")
    for i, k in enumerate(kat):
        print(f"{i+1}. {k}")
def tambah_kat(kat, fc):
    nama = input("Nama kategori baru: ").strip()
    if not nama:
        print("Kategori tidak boleh kosong!")
        return
    if nama in kat:
        print("Kategori sudah ada!")
        return
    kat.append(nama)
    fc[nama] = []
    print("Kategori berhasil ditambah.")
def edit_kat(kat, fc):
    show_kat(kat)
    if not kat: return
    try:
        idx = int(input("Pilih nomor kategori yang mau diubah: ")) - 1
        if idx < 0 or idx >= len(kat):
            print("Pilihan tidak valid."); return
        baru = input("Nama kategori baru: ").strip()
        if not baru:
            print("Nama kategori tidak boleh kosong!"); return
        if baru in kat:
            print("Kategori sudah ada!"); return
        fc[baru] = fc.pop(kat[idx])
        kat[idx] = baru
        print("Kategori berhasil diubah.")
    except ValueError:
        print("Input harus angka.")
def hapus_kat(kat, fc):
    show_kat(kat)
    if not kat: return
    try:
        idx = int(input("Pilih nomor kategori yang mau dihapus: ")) - 1
        if idx < 0 or idx >= len(kat):
            print("Pilihan tidak valid."); return
        konfirmasi = input(f"Yakin hapus kategori '{kat[idx]}'? (y/n): ").lower()
        if konfirmasi == "y":
            fc.pop(kat[idx])
            kat.pop(idx)
            print("Kategori berhasil dihapus.")
    except ValueError:
        print("Input harus angka.")
def pilih_kat(kat):
    show_kat(kat)
    if not kat: return None
    try:
        idx = int(input("Pilih nomor kategori: ")) - 1
        if idx < 0 or idx >= len(kat):
            print("Pilihan tidak valid."); return None
        return kat[idx]
    except ValueError:
        print("Input harus angka."); return None
# func untuk manajemen flashcard
def show_fc(fc, kat):
    k = pilih_kat(kat)
    if not k: return
    if not fc[k]:
        print("Belum ada flashcard di kategori ini."); return
    while True:
        pil = menu_lihat_fc()
        if pil == "1":
            tampilkan_flashcard(fc[k])
        elif pil == "2":
            sorted_cards = sort_fc(fc[k].copy())
            print("Flashcard terurut (pertanyaan):")
            tampilkan_flashcard(sorted_cards)
        elif pil == "3":
            keyword = input("Masukkan kata kunci pertanyaan: ").strip()
            hasil = search_fc(fc[k], keyword)
            if hasil:
                print(f"Flashcard ditemukan ({len(hasil)}):")
                tampilkan_flashcard(hasil)
            else:
                print("Tidak ditemukan pertanyaan dengan kata kunci tersebut.")
        elif pil == "4":
            break
        else:
            print("Menu tidak valid.")
        input("Tekan ENTER untuk lanjut...")
# func bantu nampilin flashcard dalam tabel
def tampilkan_flashcard(cards):
    max_q = max([len(card['q']) for card in cards]+[10])
    max_a = max([len(card['a']) for card in cards]+[7])
    line = "+" + "-"*5 + "+" + "-"*(max_q+2) + "+" + "-"*(max_a+2) + "+"
    print(line)
    print("| {:^3} | {:^{wq}} | {:^{wa}} |".format("No", "Pertanyaan", "Jawaban", wq=max_q, wa=max_a))
    print(line)
    for i, card in enumerate(cards):
        print("| {:>2}  | {:<{wq}} | {:<{wa}} |".format(i+1, card['q'], card['a'], wq=max_q, wa=max_a))
    print(line)
# func untuk manajemen flashcard jg
def tambah_fc(fc, kat):
    k = pilih_kat(kat)
    if not k: return
    q = input("Pertanyaan: ").strip()
    a = input("Jawaban: ").strip()
    if not q or not a:
        print("Pertanyaan dan jawaban tidak boleh kosong!"); return
    fc[k].append({"q": q, "a": a})
    print("Flashcard berhasil ditambah.")
def edit_fc(fc, kat):
    k = pilih_kat(kat)
    if not k: return
    if not fc[k]:
        print("Belum ada flashcard di kategori ini."); return
    tampilkan_flashcard(fc[k])
    try:
        idx = int(input("Pilih nomor flashcard yang mau diubah: ")) - 1
        if idx < 0 or idx >= len(fc[k]):
            print("Pilihan tidak valid."); return
        q = input("Pertanyaan baru (tekan ENTER jika tidak ingin mengubah): ").strip()
        a = input("Jawaban baru (tekan ENTER jika tidak ingin mengubah): ").strip()
        if q:
            fc[k][idx]['q'] = q
        if a:
            fc[k][idx]['a'] = a
        print("Flashcard berhasil diubah.")
    except ValueError:
        print("Input harus angka.")
def hapus_fc(fc, kat):
    k = pilih_kat(kat)
    if not k: return
    if not fc[k]:
        print("Belum ada flashcard di kategori ini."); return
    tampilkan_flashcard(fc[k])
    try:
        idx = int(input("Pilih nomor flashcard yang mau dihapus: ")) - 1
        if idx < 0 or idx >= len(fc[k]):
            print("Pilihan tidak valid."); return
        konfirmasi = input(f"Yakin hapus flashcard ini? (y/n): ").lower()
        if konfirmasi == "y":
            fc[k].pop(idx)
            print("Flashcard berhasil dihapus.")
    except ValueError:
        print("Input harus angka.")
def mode_fc(fc, kat):
    k = pilih_kat(kat)
    if not k: return
    if not fc[k]:
        print("Belum ada flashcard di kategori ini."); return
    print(f"\n--- Mode Flashcard: {k} ---")
    benar = 0
    for i, card in enumerate(fc[k]):
        print(f"\nPertanyaan {i+1}: {card['q']}")
        jawaban = input("Jawaban kamu: ").strip()
        if jawaban.lower() == card['a'].lower():
            print("Benar!"); benar += 1
        else:
            print(f"Salah! Jawaban: {card['a']}")
    print(f"\nSkor kamu: {benar}/{len(fc[k])}")
# func bantu untuk sorting dan searching flashcard
def sort_fc(cards):
    n = len(cards)
    for i in range(n):
        for j in range(0, n-i-1):
            if cards[j]['q'].lower() > cards[j+1]['q'].lower():
                cards[j], cards[j+1] = cards[j+1], cards[j]
    return cards
def search_fc(cards, keyword):
    return [card for card in cards if keyword.lower() in card['q'].lower()]
# main loop program dan pemanggilan fungsi2 di atas
def main():
    fc = dummy_data()
    kat = list(fc.keys())
    while True:
        pil = menu_utama()
        if pil == "1":
            while True:
                pil_fc = menu_fc()
                if pil_fc == "1": show_fc(fc, kat)
                elif pil_fc == "2": tambah_fc(fc, kat)
                elif pil_fc == "3": edit_fc(fc, kat)
                elif pil_fc == "4": hapus_fc(fc, kat)
                elif pil_fc == "5":
                    break
                else:
                    print("Menu tidak valid.")
                input("Tekan ENTER untuk lanjut...")
        elif pil == "2":
            while True:
                pil_kat = menu_kat()
                if pil_kat == "1": show_kat(kat)
                elif pil_kat == "2": tambah_kat(kat, fc)
                elif pil_kat == "3": edit_kat(kat, fc)
                elif pil_kat == "4": hapus_kat(kat, fc)
                elif pil_kat == "5":
                    break
                else:
                    print("Menu tidak valid.")
                input("Tekan ENTER untuk lanjut...")
        elif pil == "3":
            mode_fc(fc, kat)
            input("Tekan ENTER untuk lanjut...")
        elif pil == "4":
            print("Yippie! Sampai jumpa lagi!")
            break
        else:
            print("Menu tidak valid.")
            input("Tekan ENTER untuk lanjut...")
# jalankan prohram 
main()