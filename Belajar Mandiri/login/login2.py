def cek_nama_password():
    nama = input("Masukkan nama Anda: ")
    password = input("Masukkan password Anda: ")

    if nama == "foxter" and password == "123":
        print("Selamat datang, Foxter! Anda berhasil masuk.")
    else:
        print("Nama atau password salah. Akses ditolak.")

def main():
    print("Selamat datang!")
    
    cek_nama_password()

main()
