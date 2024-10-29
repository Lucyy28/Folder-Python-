jumlah_angka = 0
string_output = ""

for i in range(1, 6):
    jumlah_angka += i
    string_output += str(i)
    if i < 5:
        string_output += " + "

string_output += " = " + str(jumlah_angka)

print(string_output)