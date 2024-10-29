jumlah_angka = 0
string_output = ""

for i in range(2, 11, 2):
    jumlah_angka += i
    string_output += str(i)
    if i < 10:
        string_output += " + "

string_output += " = " + str(jumlah_angka)

print(string_output)