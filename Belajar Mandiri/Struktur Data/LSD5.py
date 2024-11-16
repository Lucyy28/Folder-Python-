

print("Selamat datang di Kalkulator Sederhana!")

print("\nPilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")
elif pilihan == "2":
    hasil = angka1 - angka2
    print(f"Hasil pengurangan: {hasil}")
elif pilihan == "3":
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {hasil}")
elif pilihan == "4":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Pilihan tidak valid. Silakan pilih operasi yang benar.")
