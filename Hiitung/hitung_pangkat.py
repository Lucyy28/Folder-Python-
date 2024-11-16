def hitung_pangkat(bilangan, pangkat):
    hasil = bilangan ** pangkat
    print(f"{bilangan} pangkat {pangkat} = {hasil}")

def main():
    bilangan = float(input("Masukkan angka dasar: "))
    pangkat = int(input("Masukkan angka pangkat: "))
    
    hitung_pangkat(bilangan, pangkat)

main()
