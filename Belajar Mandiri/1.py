def hitung_kecepatan():
    print("Hitung Kecepatan Ready!")
    jarak = int(input("Masukan Jarak > "))
    waktu = int(input("Masukan Waktu > "))
    kecepatan = jarak * waktu
    print("kecepatan: ", kecepatan)

def hitung_segitiga():
    print("Hitung Luas Segitiga")
    alas = int(input("Masukan Alas > "))
    tinggi = int(input("Masukan Tinggi > "))
    luas = 0.5 * (alas * tinggi)
    print("Hasilnya Adalah > ", luas)

while True :
    userinput = int(input("Pilih rumus yang akan di pakai > \n\n1. HItung Kecepatan\n2. Luas Segitiga\n3. Luas Balok\n4. Luas Bola\n\n Pilih Nomor Berapa > "))
    if(userinput == 1):
        hitung_kecepatan()
    elif(userinput == 2):
        hitung_segitiga()
    else:
        break