kamus = {
    "python": "Bahasa pemrograman tingkat tinggi yang populer digunakan untuk pengembangan perangkat lunak, analisis data, dan kecerdasan buatan.",
    "algoritma": "Langkah-langkah atau prosedur yang sistematis untuk menyelesaikan masalah.",
    "komputer": "Perangkat elektronik yang dapat menerima, memproses, dan menyimpan data.",
    "jaringan": "Sekumpulan perangkat yang saling terhubung untuk berbagi data dan sumber daya.",
    "database": "Sistem yang digunakan untuk menyimpan dan mengelola data secara terstruktur.",
    "programming": "Proses menulis, menguji, dan memelihara kode yang menjalankan perangkat lunak."
}

def cari_kata(kata):
    return kamus.get(kata.lower(), "Kata tidak ditemukan dalam kamus.")

def kamus_sederhana():
    print("Selamat datang di Kamus Sederhana!")
    while True:
        kata = input("\nMasukkan kata untuk mencari definisinya (atau ketik 'exit' untuk keluar): ").strip().lower()
        
        if kata == 'exit':
            print("Terima kasih telah menggunakan Kamus Sederhana!")
            break
        
        definisi = cari_kata(kata)
        print(f"Definisi '{kata}': {definisi}")

kamus_sederhana()
