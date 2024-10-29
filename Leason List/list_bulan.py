nb = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
nb[0] = ['January']
nb[7] = ['August']

print(nb[2])
print(nb[9])

nb.append("Muharram")
for x,y in enumerate(nb):
    print(f"Bulan Ke {x+1} adalah {y}")