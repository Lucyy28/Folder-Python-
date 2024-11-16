def cari_faktor(angka):
    faktor = []  
    for i in range(1, angka + 1):
        if angka % i == 0:  
            faktor.append(i)
    
    return faktor  
def penghitung_faktor():
    print("Program Pencari Faktor dari Angka")
    
    angka = int(input("Masukkan angka: "))
    
    faktor = cari_faktor(angka)
    
    print(f"Faktor-faktor dari {angka} adalah: {faktor}")

penghitung_faktor()
