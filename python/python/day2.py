print("Merhaba")

faiz=1.59
vade="36"
krediAdi="İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#string i int e dönüştürdü
print(int(vade)+12)

#string e dönüştürdü
faiz=str(faiz)
print(type(faiz))


vade=39 #int(input("Lütfen istediğiniz vade sayısını giriniz."))
print(type(vade))
vade=vade+12




# string interpolation
#seçtiğiniz vade sonucu ortaya cıkan vade:

print("Seçtiğiniz vade sonucu ortaya çıkan vade:"+ str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade :{vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sayısı:{vade}")

isim= input("isminizi giriniz")
#isim= "ali" #input("isminizi giriniz")
#metin="Merhaba {name}".format(name=isim)
metin=f"merhaba {isim}"
print(metin)


#f-string
metin=f"Hoşgeldiniz {isim}"
print(metin)

metin=f"Hoşgeldiniz {1+1}"
print(metin)

#listeler 
#döngüler
#fonksiyonlar

dizi=["ihtiyaç Kredisi",10,5.2,True]
print(dizi)


krediler=["İhtiyaç kredisi","Taşıt Kredisi","Konut Kredisi"]
print(type(krediler))
print(krediler)
print(krediler[0])
print(krediler[1])
print(len(krediler))

krediler.append("Özel kredi")
print(krediler)
krediler.append("Evlilik Kredisi")
print(krediler)

krediler.pop()
#son indexi siler.
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi","Z Kredisi"])
print(krediler)

# For
#i=0 i<10 i++
x=10
for i in range(x):
    print("aa")
    print(i)

print("***************")
for i in range(5,11):
    print(i)

print("**************")
for i in range(3,51,10):
    print(i)
print("**************")
for i in  range (0,50,2):
    print(i)
# for i in range(0.1,0.5):
#     print(i) hataaaaa int istiyor

krediler=["İhtiyaç kredisi","Taşıt Kredisi","Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("****************")

for i in range(len(krediler)):
    print(krediler[i])
print("********aa*******")

#sonsuz döngü

i=0
while i<10:
    print("x")
    i+=1
print("y")

print("**********")

while True:
    print("XX")
    break
print("*****************")

i=0
while i<len(krediler):
    print(krediler[i])
    i+=1
print("*******son********")

i=0
while i<len(krediler):
    if krediler[i]=="Konut Kredisi":
        break
    print(krediler[i])
    i+=1

# fonksiyonlar
fiyat=100
indirim=20
yeniFiyat=fiyat-indirim

#definition define
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,2)
calculateWithParams(100,30)
sayHello("ali")
sayHello("veli")


def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat=calculateAndReturn(200,50)
print(yeniFiyat)
print(yeniFiyat+10)

#void
def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

print("-----------------------")
fonk1=calculatePrice(100,50)
fonk2=calculatePriceAndReturn(300,100)

print(f"165.satırım: {fonk1}")
print(f"166.satır: {fonk2}")
print("************************")