def kalkulator():
    print("Pilih Operasinya mau apa coy!:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print(f"Hasil: {angka1 + angka2}")
    elif pilihan == '2':
        print(f"Hasil: {angka1 - angka2}")
    elif pilihan == '3':
        print(f"Hasil: {angka1 * angka2}")
    elif pilihan == '4':
        if angka2 != 0:
            print(f"Hasil: {angka1 / angka2}")
        else:
            print("Tidak dapat dibagi dengan nol ganteng.")
    else:
        print("Input enggak valid.")

kalkulator()
