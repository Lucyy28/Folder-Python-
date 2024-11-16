import random

angka_tertentu = random.randint(1, 100)  # Angka acak antara 1 dan 100

print("Tebak angka yang telah saya pilih antara 1 dan 100!")

percobaan = 0

while True:
    tebakan = int(input("Masukkan tebakan Anda: "))
    percobaan += 1

    if tebakan < angka_tertentu:
        print("Tebakan Anda terlalu rendah. Coba lagi!")
    elif tebakan > angka_tertentu:
        print("Tebakan Anda terlalu tinggi. Coba lagi!")
    else:
        print(f"Selamat! Anda berhasil menebak angka {angka_tertentu} dalam {percobaan} percobaan.")
        break
