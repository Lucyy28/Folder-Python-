def cari_kata(kalimat, kata):
    if kata.lower() in kalimat.lower():
        print(f"Kata '{kata}' ditemukan dalam kalimat.")
    else:
        print(f"Kata '{kata}' tidak ditemukan dalam kalimat.")

def main():
    kalimat = input("Masukkan kalimat: ")
    kata = input("Masukkan kata yang ingin dicari: ")
    
    cari_kata(kalimat, kata)

main()
