
# Playing games with a steam account
 # CS GO -EURO TRUCK - GARRYS MOD THİS GAMES FOR FEES AND PACKAGES

 # CS GO : 1,2,3 version  , 1. version 30 $, 2.version = 65 $ , 3.version= 72 $ , all = 140 $
 # EURO TRUCK : 1,2 VERSİON , 1. version = 39 $ , 2. version= 52 $ ,  all = 84 $
 # GARYS MOD : ONE MODE HAVE, PRİCE= 27 $

 # >>>> customer_acount>130 all cart %15 discount

"""müşteri cs go 2. ve 3. versiyonlarını alsın,
   müşteri aynı zamanda garys mod oyununu alsın,
   müşteri euro truck 1,2 ve 3. versionlarının tamamını alsın,
   müşterinin hesabı 130 doları geçerse %15 indirim uygulanacak"""

# Get the customer name
customer_name=(input("Your Name? >>"))


def game_price(product,x):
 games_prices={
    "cs_go":{
     "cs_version1":30,
     "cs_version2":65,
     "cs_version3":72,
     "cs_all":140
    },
    "euro_truck":{
     "euro_truck1":39,
     "euro_truck2":52,
     "euro_all":84
    },
   "garys_mod":27}

 if product in game_price:
  if isinstance(game_price([product]),dict):
   if x in game_price([product]):
    price=games_prices[product][x]
    return f"{x.capitalize()} cs_go for price :{price} $"
   else:
    return "error"
  else:
   price=game_price([product])
   return f"{price} for  price: {price} $ "
 else:
  return " error"
select_product=input("please select product games : cs go, euro truck, garys mod")
select_x=""
if select_product == "cs_go":
 select_x=input("please select product version: 1,2,3 versions ")
print(game_price(select_product,select_x))

######################################################--------------------------->>>>

print(f" CS GO : 1,2,3 version  , 1. version 30 $, 2.version = 65 $ , 3.version= 72 $ , all = 140 $")
print(" EURO TRUCK : 1,2 VERSİON , 1. version = 39 $ , 2. version= 52 $ ,  all = 84 $")
print("GARYS MOD : ONE MODE HAVE, PRİCE= 27 dollars")


def hesap_bakiye_hesapla(toplam_fiyat):
 hesap_bakiye = 130
 if toplam_fiyat >= hesap_bakiye:
  indirim_tutari = toplam_fiyat * 0.15
  toplam_fiyat -= indirim_tutari
  print(f"Hesap bakiyeniz {hesap_bakiye} $ olduğu için %15 indirim uygulandı.")
 return toplam_fiyat


urunler = {
 "CS GO": {
  1: 30,
  2: 65,
  3: 72,
  "all": 140
 },
 "EURO TRUCK": {
  1: 39,
  2: 52,
  "all": 84
 },
 "GARYS MOD": {
  1: 27
 }
}

sepetteki_urunler = []

# CS GO oyununu alıp almayacağını soralım
cs_go_alacak_mi = input("CS GO oyununu almak istiyor musunuz? (Evet/Hayır): ")
if cs_go_alacak_mi.lower() == "evet":
 cs_go_versiyonlar = input("Hangi versiyonları almak istiyorsunuz? (1, 2, 3, all): ").split(", ")
 for versiyon in cs_go_versiyonlar:
  if versiyon.isdigit() and int(versiyon) in urunler["CS GO"]:
   sepetteki_urunler.append(urunler["CS GO"][int(versiyon)])
  else:
   print(f"{versiyon} versiyonu mevcut değil, geçerli bir versiyon seçiniz.")

# EURO TRUCK oyununu alıp almayacağını soralım
euro_truck_alacak_mi = input("EURO TRUCK oyununu almak istiyor musunuz? (Evet/Hayır): ")
if euro_truck_alacak_mi.lower() == "evet":
 euro_truck_versiyonlar = input("Hangi versiyonları almak istiyorsunuz? (1, 2, all): ").split(", ")
 for versiyon in euro_truck_versiyonlar:
  if versiyon.isdigit() and int(versiyon) in urunler["EURO TRUCK"]:
   sepetteki_urunler.append(urunler["EURO TRUCK"][int(versiyon)])
  else:
   print(f"{versiyon} versiyonu mevcut değil, geçerli bir versiyon seçiniz.")

# GARYS MOD oyununu alıp almayacağını soralım
garys_mod_alacak_mi = input("GARYS MOD oyununu almak istiyor musunuz? (Evet/Hayır): ")
if garys_mod_alacak_mi.lower() == "evet":
 sepetteki_urunler.append(urunler["GARYS MOD"][1],dict)


# Toplam fiyatı hesaplayalım
toplam_fiyat = sum(sepetteki_urunler)

# İndirim uygulayalım
indirimli_fiyat = hesap_bakiye_hesapla(toplam_fiyat)

# Sonuçları yazdıralım
print(f"Sepetinizdeki ürünlerin toplam fiyatı: {toplam_fiyat} $")
print(f"Ödemeniz gereken tutar (indirimli): {indirimli_fiyat} $")
print("toplam fiyatı ",sum(sepetteki_urunler))

