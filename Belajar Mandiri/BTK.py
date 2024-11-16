import random

print("Selamat datang di Game Batu-Kertas-Gunting!")
print("Cara bermain: Pilih Batu, Kertas, atau Gunting.\n")

options = ["Batu", "Kertas", "Gunting"]

while True:
    user = input("Pilihan Anda (Batu/Kertas/Gunting): ").capitalize()
    if user not in options:
        print("Pilihan tidak valid, coba lagi.\n")
        continue

    bot = random.choice(options)
    print(f"Komputer memilih: {bot}")

    if user == bot:
        print("Hasil: Seri!\n")
    elif (user == "Batu" and bot == "Gunting") or \
         (user == "Kertas" and bot == "Batu") or \
         (user == "Gunting" and bot == "Kertas"):
        print("Hasil: Anda Menang!\n")
    else:
        print("Hasil: Anda Kalah!\n")

    play_again = input("Ingin bermain lagi? (ya/tidak): ").lower()
    if play_again != "ya":
        print("Terima kasih telah bermain!")
        break
