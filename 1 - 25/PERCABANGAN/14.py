def hitung_upah(nama, jam_kerja, tarif_per_jam):
    upah = jam_kerja * tarif_per_jam
    print(f"\nUpah {nama}: Rp {upah:,.2f}")

def main():
    print("Program Menghitung Upah Karyawan")

    karyawan = [
        {"nama": "Rizwan", "jam_kerja": 0, "tarif_per_jam": 0},
        {"nama": "Cahya", "jam_kerja": 0, "tarif_per_jam": 0},
        {"nama": "Firdan", "jam_kerja": 0, "tarif_per_jam": 0},
    ]
    
    for k in karyawan:
        k["jam_kerja"] = float(input(f"\nMasukkan jam kerja untuk {k['nama']}: "))
        k["tarif_per_jam"] = float(input(f"Masukkan tarif per jam untuk {k['nama']}: "))
    
    total_upah = 0
    for k in karyawan:
        upah = k["jam_kerja"] * k["tarif_per_jam"]
        total_upah += upah
        hitung_upah(k["nama"], k["jam_kerja"], k["tarif_per_jam"])
    
    print(f"\nTotal Upah Semua Karyawan: Rp {total_upah:,.2f}")

if __name__ == "main":
    main()
