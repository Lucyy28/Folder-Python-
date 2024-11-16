from datetime import datetime

print("Selamat datang di Program Menebak Hari dan Bulan!")

date_input = input("Masukkan tanggal (format: DD-MM): ")

date_input_with_year = date_input + "-2024"

date_object = datetime.strptime(date_input_with_year, "%d-%m-%Y")

day_of_week = date_object.weekday()

hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
day_name = hari[day_of_week]

month_name = date_object.strftime("%B")

print(f"Tanggal {date_input} adalah hari {day_name} di bulan {month_name}.")
