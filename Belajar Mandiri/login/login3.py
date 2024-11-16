pengguna_terdaftar = {}

def registrasi():
    print("--- Registrasi Akun ---")
    nama = input("Masukkan nama Anda: ")
    
    if nama in pengguna_terdaftar:
        print("Nama sudah terdaftar. Silakan login.")
        return
    
    password = input("Masukkan password Anda: ")
    
    pengguna_terdaftar[nama] = password
    print(f"Akun dengan nama '{nama}' berhasil terdaftar.")

def login():
    print("--- Login ---")
    nama = input("Masukkan nama Anda: ")
    
    if nama not in pengguna_terdaftar:
        print("Nama belum terdaftar. Silakan registrasi terlebih dahulu.")
        return
    
    password = input("Masukkan password Anda: ")
    
    if pengguna_terdaftar[nama] == password:
        print(f"Selamat datang, {nama}! Anda berhasil masuk.")
    else:
        print("Password salah. Akses ditolak.")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Registrasi")
        print("2. Login")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == '1':
            registrasi()
        elif pilihan == '2':
            login()
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
