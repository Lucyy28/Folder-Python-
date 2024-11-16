def konversi_celsius_ke_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

def main():
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    
    konversi_celsius_ke_fahrenheit(celsius)

main()
