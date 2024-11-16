def hitung_diskon(harga_asli, diskon_persen):
    diskon = harga_asli * (diskon_persen / 100) 
    harga_setelah_diskon = harga_asli - diskon 
    return harga_setelah_diskon, diskon

def kalkulator_diskon():
    print("Program Perhitungan Nilai Diskon")
    
    harga_asli = float(input("Masukkan harga asli: Rp "))
    diskon_persen = float(input("Masukkan persentase diskon: "))
    
    harga_setelah_diskon, diskon = hitung_diskon(harga_asli, diskon_persen)
    
    print(f"\nHarga asli: Rp {harga_asli}")
    print(f"Diskon: Rp {diskon}")
    print(f"Harga setelah diskon: Rp {harga_setelah_diskon}")

kalkulator_diskon()
