def tampilkan_menu():
    print("\nTo-Do List")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def tambah_tugas(tugas_list):
    tugas = input("Masukkan tugas yang ingin ditambahkan: ")
    tugas_list.append(tugas)
    print(f"Tugas '{tugas}' telah ditambahkan.")

def lihat_tugas(tugas_list):
    if len(tugas_list) == 0:
        print("Tidak ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for idx, tugas in enumerate(tugas_list, start=1):
            print(f"{idx}. {tugas}")

def hapus_tugas(tugas_list):
    lihat_tugas(tugas_list)
    if len(tugas_list) > 0:
        try:
            index = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
            if 1 <= index <= len(tugas_list):
                tugas = tugas_list.pop(index - 1)
                print(f"Tugas '{tugas}' telah dihapus.")
            else:
                print("Nomor tugas tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

def main():
    tugas_list = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            tambah_tugas(tugas_list)
        elif pilihan == '2':
            lihat_tugas(tugas_list)
        elif pilihan == '3':
            hapus_tugas(tugas_list)
        elif pilihan == '4':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
