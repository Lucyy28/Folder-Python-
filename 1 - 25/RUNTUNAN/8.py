def konversi_ke_detik(jam, menit, detik):
    total_detik = jam * 3600 + menit * 60 + detik
    print(f"\nTotal waktu dalam detik: {total_detik} detik")

def main():
    print("Program Konversi Waktu ke Detik")
    jam = int(input("Masukkan jumlah jam: "))
    menit = int(input("Masukkan jumlah menit: "))
    detik = int(input("Masukkan jumlah detik: "))

    konversi_ke_detik(jam, menit, detik)

if __name__ == "__main__":
    main()