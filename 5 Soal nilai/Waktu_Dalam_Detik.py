total_detik = int(input("Masukkan waktu dalam detik: "))

hari = total_detik // (24 * 3600)
sisa_detik = total_detik % (24 * 3600)
jam = sisa_detik // 3600
sisa_detik %= 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{hari} hari, {jam} jam, {menit} menit, {detik} detik")
