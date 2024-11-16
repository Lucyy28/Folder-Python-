angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

if angka1 % angka2 == 0:
    print(f"{angka1} adalah kelipatan dari {angka2}")
else:
    print(f"{angka1} bukan kelipatan dari {angka2}")
