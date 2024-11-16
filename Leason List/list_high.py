def cari_tertinggi_terendah():
    angka_list = input("Masukkan angka-angka (pisahkan dengan koma): ")
    
    angka_list = [int(angka) for angka in angka_list.split(",")]

    tertinggi = max(angka_list)
    terendah = min(angka_list)

    print(f"Angka tertinggi: {tertinggi}")
    print(f"Angka terendah: {terendah}")

cari_tertinggi_terendah()
