jam = int(input("Masukkan jam (0-23): "))
menit = int(input("Masukkan menit (0-59): "))

jam_berikutnya = (jam + 1) % 24

print(f"Jam berikutnya: {jam_berikutnya:02}:{menit:02}")
