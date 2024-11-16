def angka_ke_kata(angka):
    satuan = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"]
    belasan = ["Sepuluh", "Sebelas", "Dua belas", "Tiga belas", "Empat belas", "Lima belas", "Enam belas", "Tujuh belas", "Delapan belas", "Sembilan belas"]
    puluhan = ["", "Sepuluh", "Dua puluh", "Tiga puluh", "Empat puluh", "Lima puluh", "Enam puluh", "Tujuh puluh", "Delapan puluh", "Sembilan puluh"]

    if angka == 0:
        return "Nol"
    elif angka < 10:
        return satuan[angka]
    elif angka < 20:
        return belasan[angka - 10]
    elif angka < 100:
        puluhan_digit = angka // 10
        satuan_digit = angka % 10
        return puluhan[puluhan_digit] + (" " + satuan[satuan_digit] if satuan_digit != 0 else "")
    else:
        return "Angka lebih dari 99 tidak didukung oleh program ini"

angka = int(input("Masukkan angka: "))

kata = angka_ke_kata(angka)

print(f"Angka {angka} dalam kata adalah: {kata}")
