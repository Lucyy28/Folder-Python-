stok_barang = {}

while True:
    print("\nMenu:")
    print("1. Tambah barang")
    print("2. Perbarui stok barang")
    print("3. Tampilkan stok barang")
    print("4. Keluar")
    
    pilihan = input("Pilih opsi (1/2/3/4): ")
    
    if pilihan == "1":
        # nambah barang
        nama_barang = input("Masukkan nama barang: ")
        jumlah_stok = int(input("Masukkan jumlah stok: "))
        
        # Cek barang ada atau engga
        if nama_barang in stok_barang:
            print("Barang sudah ada. Gunakan opsi 2 untuk memperbarui stok.")
        else:
            stok_barang[nama_barang] = jumlah_stok
            print(f"Barang '{nama_barang}' berhasil ditambahkan dengan stok {jumlah_stok}")
    
    elif pilihan == "2":
        # Perbarui stock
        nama_barang = input("Masukkan nama barang yang akan diperbarui: ")
        
        # Ngecek
        if nama_barang in stok_barang:
            jumlah_stok_baru = int(input("Masukkan jumlah stok baru: "))
            stok_barang[nama_barang] = jumlah_stok_baru
            print(f"Stok barang '{nama_barang}' diperbarui menjadi {jumlah_stok_baru}")
        else:
            print("Barang tidak ditemukan. Gunakan opsi 1 untuk menambah barang.")
    
    elif pilihan == "3":
        #Tampil
        if stok_barang:
            print("\nDaftar Stok Barang:")
            for barang, stok in stok_barang.items():
                print(f"{barang}: {stok} unit")
        else:
            print("Belum ada barang yang ditambahkan.")
    
    elif pilihan == "4":
        print("Keluar dari program.")
        break
    else:
        print("Opsi tidak valid. Silakan pilih lagi.")
