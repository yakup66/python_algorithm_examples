####### KULLANICININ GİRDİĞİ CÜMLENİN KELİME SAYISINI BULMA

cumle = input("Lütfen bir cümle gir ")

bosluk=0

for veri in input():
    if veri == " ":
        bosluk = bosluk + 1

print(" Kelime sayısı : " , bosluk + 1)