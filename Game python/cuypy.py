import random
lokasi_list = ["hutan", "gunung", "pantai", "danau", "gurun"]

lokasi_rahasia = random.choice(lokasi_list)


print("Selamat datang di game CuyPy!")
print("CuyPy telah memilih satu lokasi rahasia dari=> hutan, gunung, pantai, danau, atau gurun.")
print("Tebak di mana lokasinya! (Ketik 'keluar' untuk berhenti)")

while True:
    tebakan = input("Masukkan tebakan lokasi: ").lower()
    
    if tebakan == "keluar":
        print("Terima kasih telah bermain! Sampai jumpa!")
        break
    elif tebakan == lokasi_rahasia:
        print("Selamat! Tebakan kamu benar. Lokasi rahasianya adalah:", lokasi_rahasia)
        break
    else:
        print("Tebakan salah! Coba lagi.")
