def cetak_ganjil(batas):
    angka = 1  # Mulai dari angka ganjil pertama
    while angka <= batas:
        print(angka)
        angka += 2  # Melompat ke angka ganjil berikutnya

# Contoh penggunaan
batas_input = int(input("Masukkan batas maksimal: "))
cetak_ganjil(batas_input)