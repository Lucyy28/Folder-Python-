def input_nama_password():
    nama = input("Masukkan nama Anda: ")
    password = input("Masukkan password Anda: ")
    
    print("\nData yang dimasukkan:")
    print(f"Nama: {nama}")
    print(f"Password: {password}")

def main():
    print("Selamat datang!")
    
    input_nama_password()

main()
