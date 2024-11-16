import random

def main():
    print("Selamat datang di Program Pengacak Nama!")
    
    names = input("Masukkan daftar nama, pisahkan dengan koma (,): ").split(",")
    
    names = [name.strip() for name in names]
    
    random.shuffle(names)
   
    print("\nHasil pengacakan nama:")
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

if __name__ == "__main__":
    main()
