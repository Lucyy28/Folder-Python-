teks = input("Masukkan sebuah kalimat: ")

frekuensi_huruf = {}

for huruf in teks:
    if huruf != " ":

        if huruf in frekuensi_huruf:
            frekuensi_huruf[huruf] += 1

        else:
            frekuensi_huruf[huruf] = 1

for huruf, frekuensi in frekuensi_huruf.items():
    print(f"Huruf '{huruf}' muncul sebanyak {frekuensi} kali")
