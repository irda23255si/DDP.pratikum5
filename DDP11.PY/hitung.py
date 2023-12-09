import math

#Tambah
def tambah(bil1, bil2):
    hasil = bil1 + bil2
    print('penjumlahan ', bil1, "+", bil2, '=', hasil)
#kurang
def kurang(bil1, bil2):
    hasil = (bil2 - bil2)
#pangkat, math.pow
def pangkat(bilangan1, pangkat):
    print('pangkat',bilangan1, '^', pangkat , 'adalah',math.pow(2,3))
#kali
def perkalian(bil1, bil2):
    hasil = (bil1 * bil2)
    print('perkalian', bil1, '*', bil2, '=', hasil)
#bagi
def pembagian (bil1, bil2):
    hasil =bil1 / bil2
    print('pembagian', bil1, '/', bil2, '=', hasil)
#log, math.log
def log (bil):
    print('log dari', bil, 'adalah', math.log(bil))
#akar, math.sqrt
def akar (bil):
    print('akar dari', bil, 'adalah', math.log(bil)) 
#sin,
def sin(bil):
    print('sin dari', bil, 'adalah', math.sin(bil))
#cos,
def cos(bil):
    print('cos dari', bil, 'adalah', math.cos(bil))
#Tan,
def tan (bil):
    print('tan dari', bil, 'adalah', math.tan(bil))








#bangun_datar.py

import math

def persegi(sisi):
    luas = sisi**2
    keliling_persegi= 4 * sisi
    print("luas persegi:", luas)
    print("keliling persegi:keliling", keliling_persegi)

def persegipanjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2*(panjang + lebar)
    print("luas persegi panjang:", luas)
    print("keliling persegi panjang:", keliling)

def lingkaran(jari_jari):
    luas = math.pi * jari_jari**2
    keliling = 2* math.pi * jari_jari
    print("luas lingkaran:",luas)
    print("keliling lingkaran:",keliling)

def segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = alas + alas + alas
    print("luas segitiga:", luas)
    print("keliling segitiga:", keliling)

def trapesiun(alas_atas, alas_bawah, tinggi):
    luas = 0.5 *(alas_atas+alas_bawah)*tinggi
    keliling = alas_atas + alas_bawah + alas_atas + alas_bawah
    print("luas trapesiun:", luas)
    print("keliling trapesiun:", keliling)

def jajargenjang(alas,tinggi):
    luas = alas*tinggi
    keliling = 2*(alas+ alas)
    print("luas jajargenjang:", luas)
    print("keliling jajargenjang:", keliling)

def belahketupat(d1,d2):
    luas = 0.5 * d1 * d2
    keliling = 4*d1
    print("luas belahketupat:", luas)
    print("keliling belahketupat:",)