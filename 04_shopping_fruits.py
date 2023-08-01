### Your fruits shopping project

"""
ING-Jack's going to the grocery store. There are only bananas, apples and grapes in the greengrocer. The greengrocer asks Jack which fruit he wants.
If Jack wants bananas; the greengrocer asks how many kilos he wants and calculates the fee he will pay as 5tl per kilo and tells Jack.
If Jack wants an apple, the greengrocer asks what color apple he wants, and Jack says he wants a red, yellow or green apple. The greengrocer asks how many kilos he wants and calculates the fee he will pay as 2tl per kilo and tells Jack.
If Jack wants grapes, he chooses the purple or green grape and pays a fee of 3tl per kilo for the purple grape. If he chooses green grapes, he will pay 3.5tl per kilo. The greengrocer asks for the grape he wants and calculates how many pounds he wants and tells the fee.
What should be the codes for Jack's grocery shopping?



TR-jack manava gidince alışveriş kodları nasıl olmalıdır?
"""

grocery={"banana":20,"apple":15,"grape":35}    # meyvelerin isimlerini ve fiyatlarını dictionary içerisinde key,value olarak tuttuk

kg=0  # >> global alanda kg tanımlandı
for x,y in grocery.items():

  print(f"{x}:{y}")

want_fruit=input("please write a fruit name") # alınmak istenilen meyvenin ismini input ile aldık
y=grocery.get(want_fruit)  ## girilen meyve ismini grocery dictionary içerisinde bulunan
                            # key anahtarını aldı ve y değişkenine aktardı .get(girilen meyve ismi)
                            ### > BURADA BULUNAN get.(want_fruit) fonks for döngüsünde key ve valuelere aktarılan değişkenleri girilen değişken want_fruit içerisinde aldık.
 # kaç kg meyve alacaksın

if want_fruit == ("banana"):
    kg=int(input("please write kg for fruit"))
    print(kg*y, " $ price")

elif want_fruit == "apple":
    color=input("what color apple do you want ")
    if color == "red":
        kg=int(input("please write kg for apple"))
    elif color == "green":
        kg = int(input("please write kg for apple"))
    print(color,"Apple",kg*y, " $ price")


elif want_fruit == "grape":
    color=input("what color grape do you want ")
    if color == "purple":
        kg = int(input("please write kg for grape"))
    elif color== "green":
        kg = int(input("please write kg for grape"))
    print(color ," Grape " , kg*y , " $ price")
else:
    print("please enter the correct information")


## Yukarıdaki projede:
"""
Bir kişinin almak istediği ve kullanıcın gireceği meyve ismine ve renk'ine göre hazırda bulunan ve dictionary ile oluşturulan,
meyve ve fiyatları sözcüklerimizde 
Kullanıcının girdiği meyvenin isim,renk ve kg değişkenlerine göre ekrana fiyatını veren projedir.
Bu projede meyve isim ve fiyatları dictionary içerisinde tutulmuş olup,
for döngüsü ile dictionary içerisindeki key ve value değerleri x ve y değişkenlerine aktarılmış olup,
daha sonra girilen meyve ismine göre ,for döngüsü sayesinde dictionary içerisindeki value değerini 
aktarılan değişken y'yi get fonksiyonu ile tanımladık.
döngülerimiz ve işlem kısmı olan if else ile kg*y değerini, kullanıcının girdiği meyve isim,renk,kg değişkenlerine göre 
hesaplama yapılır ve ekrana çıktısı verilir.
"""







