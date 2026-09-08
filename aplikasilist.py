xrpl2 = []

while True: 
    print("\n--- Daftar Murid Kelas X RPL 2 ---")
    print("Pilih menu:")
    print("1. Tampilkan daftar murid")
    print("2. Tambah murid")
    print("3. Hapus murid")
    print("4. Keluar aplikasi")

    # Pastikan input dan logika if/elif berada di dalam while True
    pilihan = int(input("Masukkan pilihan anda = "))
    
    if pilihan == 1:
        if len(xrpl2) == 0:
            print("Daftar murid saat ini masih kosong.")
        else:
            print("Daftar murid:", xrpl2)
            
    elif pilihan == 2:
        # Tidak perlu menggunakan str(input(...)) karena input() otomatis menghasilkan string
        murbar = input("Masukkan nama murid baru = ")
        xrpl2.append(murbar)
        print(f"'{murbar}' berhasil ditambahkan ke daftar!")
        
    elif pilihan == 3:
        murhap = input("Masukkan nama murid yang ingin dihapus = ")
        # Cek dulu apakah nama tersebut ada di dalam list sebelum dihapus
        if murhap in xrpl2:
            xrpl2.remove(murhap)
            print(f"'{murhap}' berhasil dihapus dari daftar!")
        else:
            print(f"Maaf, '{murhap}' tidak ditemukan di daftar.")
            
    elif pilihan == 4:
        print("Keluar dari aplikasi. Sampai jumpa!")
        break
        
    else:
        print("Pilihan tidak tersedia, silakan masukkan angka 1-4.")
