from datetime import datetime

print("Selamat datang di Kalkulator Hari Ulang Tahun!\n")

ulang_input = input("Masukkan tanggal lahir Anda dengan angka (format: Hari-Bulan-Tahun): ")

birth_date = datetime.strptime(ulang_input, "%d-%m-%Y")

today = datetime.now()

next_birthday = datetime(today.year, birth_date.month, birth_date.day)

if next_birthday < today:
    next_birthday = datetime(today.year + 1, birth_date.month, birth_date.day)

days_left = (next_birthday - today).days
print(f"\nUlang tahun Anda berikutnya adalah pada {next_birthday.strftime('%d-%m-%Y')}.")
print(f"Sisa {days_left} hari lagi hingga ulang tahun Anda berikutnya!")
