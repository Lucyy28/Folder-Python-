def kata_terpanjang(kalimat):
    kata_list = kalimat.split()
    
    kata_panjang = max(kata_list, key=len)
    
    print(f"Kata terpanjang dalam kalimat adalah: '{kata_panjang}'")

def main():
    kalimat = input("Masukkan kalimat: ")
    
    kata_terpanjang(kalimat)

main()
