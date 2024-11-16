def hitung_vokal(kalimat):
    vokal = "aeiouAEIOU"
    jumlah_vokal = 0

    for char in kalimat:
        if char in vokal:
            jumlah_vokal += 1

    print(f"Jumlah vokal dalam kalimat: {jumlah_vokal}")

def main():
    kalimat = input("Masukkan kalimat: ")
    
    hitung_vokal(kalimat)

main()
