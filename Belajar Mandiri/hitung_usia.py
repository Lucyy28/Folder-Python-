from datetime import datetime

def hitung_usia(tanggal_lahir):
    tanggal_sekarang = datetime.now()
    
    usia = tanggal_sekarang.year - tanggal_lahir.year
    
    if (tanggal_sekarang.month, tanggal_sekarang.day) < (tanggal_lahir.month, tanggal_lahir.day):
        usia -= 1
    
    print(f"Usia Anda adalah {usia} tahun.")

def penghitung_usia():
    print("Program Penghitung Usia Berdasarkan Tanggal Lahir")
    
    tanggal_lahir_str = input("Masukkan tanggal lahir (dd/mm/yyyy): ")
    
    tanggal_lahir = datetime.strptime(tanggal_lahir_str, "%d/%m/%Y")
    
    hitung_usia(tanggal_lahir)

penghitung_usia()
