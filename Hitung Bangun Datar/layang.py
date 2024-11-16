diagonal_1 = float(input("Masukkan panjang diagonal pertama layang-layang: "))
diagonal_2 = float(input("Masukkan panjang diagonal kedua layang-layang: "))
sisi_1 = float(input("Masukkan panjang sisi pertama layang-layang: "))
sisi_2 = float(input("Masukkan panjang sisi kedua layang-layang: "))

luas = 0.5 * diagonal_1 * diagonal_2
keliling = 2 * (sisi_1 + sisi_2)

print(f"Luas layang-layang adalah: {luas}")
print(f"Keliling layang-layang adalah: {keliling}")
