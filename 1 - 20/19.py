jumlah_nilai = int(input("Masukkan jumlah nilai: "))

nilai = []

for i in range(jumlah_nilai):
    nilai_input = float(input(f"Masukkan nilai ke-{i + 1}: "))
    nilai.append(nilai_input)

total_nilai = sum(nilai)

if jumlah_nilai > 0:
    rata_rata = total_nilai / jumlah_nilai
else:
    rata_rata = 0

print(f"Jumlah Total Nilai: {total_nilai}")
print(f"Rata-rata Nilai: {rata_rata}")
