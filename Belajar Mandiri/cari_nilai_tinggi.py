angka_input = input("Masukkan angka-angka (pisahkan dengan spasi): ")

angka_list = [int(x) for x in angka_input.split()]

nilai_tertinggi = max(angka_list)

print(f"Nilai tertinggi dalam list adalah: {nilai_tertinggi}")
