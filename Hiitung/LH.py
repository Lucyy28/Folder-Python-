def hitung_kata(teks):
    kata_list = teks.split()
    jumlah_kata = len(kata_list)
    print(f"Jumlah kata: {jumlah_kata}")

teks = input("Masukkan kalimat: ")
hitung_kata(teks)
