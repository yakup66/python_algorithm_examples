############
#######>>>>>> 3 ve 5'in katı olan 10'dan küçük tüm doğal sayıları listelersek 3,5,6 ve 9'u elde ederiz. bu katların toplamı 23 eder.
# 3'ün ve 5'in 1000'den küçük tüm katlarının toplamını bulunuz.
toplam=0
for sayi in range(1000):                # sayı 1000 e kadar sayar
    if sayi % 3== 0 or sayi % 5 == 0:   # sayı 3 ya da 5'e bölünüyor ise
        print(sayi)        # ekrana basar
        toplam = toplam + sayi          # ve toplam=0  toplam=toplam + sayi şeklinde gelen her sayıyı işleme alır ve toplam değeri kalır.

print( " Toplam değeri : ", toplam)
