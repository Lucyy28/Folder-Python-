import inflect

p = inflect.engine()

angka = int(input("Masukkan angka: "))

kata = p.number_to_words(angka)

print(f"Angka {angka} dalam kata adalah: {kata}")
