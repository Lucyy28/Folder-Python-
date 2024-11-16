def hitung_segitiga():
    print("Menghitung Segitiga")
    
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    
    luas = 0.5 * alas * tinggi
    
    sisi_miring = (alas**2 + tinggi**2) ** 0.5  
    keliling = alas + tinggi + sisi_miring
    
    print(f"Luas segitiga: {luas}")
    print(f"Keliling segitiga: {keliling}")

hitung_segitiga()
