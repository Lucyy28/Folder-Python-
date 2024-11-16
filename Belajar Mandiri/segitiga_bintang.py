def cetak_segitiga(baris):
    for i in range(1, baris + 1):
        print('*' * i)

def main():
    baris = int(input("Masukkan jumlah baris segitiga: "))
    
    cetak_segitiga(baris)

main()
