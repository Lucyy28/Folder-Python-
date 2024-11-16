def konversi_mata_uang():
    print("Selamat datang Bossku di Konversi Mata Uang!")

    dari_mata_uang = input("Masukkan mata uang yang ingin dikonversi (misal: USD, IDR, EUR): ").upper()
    ke_mata_uang = input("Masukkan mata uang tujuan (misal: USD, IDR, EUR): ").upper()

    nilai_tukar = float(input(f"Masukkan nilai tukar dari {dari_mata_uang} ke {ke_mata_uang}: "))

    jumlah = float(input(f"Masukkan jumlah {dari_mata_uang} yang ingin dikonversi: "))

    hasil = jumlah * nilai_tukar

    print(f"{jumlah} {dari_mata_uang} setara dengan {hasil} {ke_mata_uang}.")

konversi_mata_uang()
