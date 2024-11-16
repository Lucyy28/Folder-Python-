print('\t\t\t\t\t\t\t\t=================================')
print('\t\t\t\t\t\t\t\tSELAMAT DATANG DI TABEL PERKALIAN')
print('\t\t\t\t\t\t\t\t=================================')

for i in range(1, 11):
    for j in range(1, 11):
        hasil = i * j
        print(f"{i} x {j} = {hasil}", end="\t")
    print()
