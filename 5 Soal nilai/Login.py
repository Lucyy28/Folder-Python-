usr_pw = {'Admin123': 'Nimda123'}

print("SELAMAT DATANG SILAHKAN LOGIN TERLEBIH DAHULU!")

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in usr_pw and usr_pw[username] == password:
    print("Login Succes!")
else:
    print("Login Failed! Forgot The Password?")
