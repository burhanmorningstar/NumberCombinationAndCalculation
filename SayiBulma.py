#Aybars Mete Keleş 222803012
#Burhan İsmail Demir 222802042

import random
import itertools
import time

def sayi_uret():
    sayilar = [random.randint(1, 9) for _ in range(5)]
    iki_basamakli_sayi = random.randint(1, 9) * 10
    uc_basamakli_sayi = random.randint(100, 999)
    sayilar.append(iki_basamakli_sayi)
    return sayilar, uc_basamakli_sayi

def islemi_gerceklestir(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return int(a / b)

def ifadeyi_degerlendir(sayilar, islemler):
    sonuc = sayilar[0]
    for i in range(len(islemler)):
        sonuc = islemi_gerceklestir(sonuc, sayilar[i + 1], islemler[i])
    return sonuc

def main():
    start_time = time.time()
    sayilar, uc_basamakli_sayi = sayi_uret()
    print("Sayilar:", sayilar)
    print("Hedef Sayi:", uc_basamakli_sayi)
    bulundu = False
    bulunan_islem = None
    en_yakin_sonuc = 0
    tum_kombinasyonlar = list(itertools.permutations(sayilar))
    for sayilar_permutasyonu in tum_kombinasyonlar:
        for islemler in itertools.product(['+', '-', '*', '/'], repeat=5):
            sonuc = ifadeyi_degerlendir(sayilar_permutasyonu, islemler)
            hedefe_olan_fark = abs(sonuc - uc_basamakli_sayi)

            if hedefe_olan_fark < abs(en_yakin_sonuc - uc_basamakli_sayi):
                en_yakin_sonuc = sonuc
                bulunan_islem = f"({sayilar_permutasyonu[0]} {islemler[0]} {sayilar_permutasyonu[1]} {islemler[1]} {sayilar_permutasyonu[2]} {islemler[2]} {sayilar_permutasyonu[3]} {islemler[3]} {sayilar_permutasyonu[4]} {islemler[4]} {sayilar_permutasyonu[5]})"
                bulundu = True
    if bulundu:
        print("Bulunan islem:", bulunan_islem)
    else:
        print("İstenilen kosullari saglayan bir islem bulunamadi.")
    print("En yakin sonuc:", en_yakin_sonuc)
    fark = abs(en_yakin_sonuc - uc_basamakli_sayi)
    if fark == 0:
        puan = 10
    elif fark <= 9:
        puan = 10 - fark
    else:
        puan = 0
    print("Puan:", puan)
    print("Calisma suresi:", time.time() - start_time)
if __name__ == "__main__":
    main()