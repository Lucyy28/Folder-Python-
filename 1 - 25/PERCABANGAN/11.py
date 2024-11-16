huruf = input("Masukkan sebuah huruf: ").lower()

if huruf in 'aeiou':
    print("Huruf vokal")
elif huruf.isalpha():
    print("Huruf konsonan")
else:
    print("Input bukan huruf")
