#matematiksel operatorler
vade=36
ekvade=6
# +
print(5 + 10)
print(vade + 12)
print(vade+ekvade)

# -
print(5-5)
print(vade-ekvade)

# *
print(5*10)
print(vade*2)
print(vade*ekvade)


# /
print(10/3)
print(vade/ekvade)
print(10/2)


yeniVade=vade/2
fiyat=100
indirimliFiyat=fiyat-20
print(yeniVade)
print(indirimliFiyat)

# %  mod alma (kalan demek)
print(10%2)
print(vade%5)
print(vade%ekvade)


# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1>2)
print(3>1)

print(1>=1)
print(1>1)

# ctrl+k+c    seçerek yorum satırı yaparım...

print(1!=1)
print(1!=2)

#or ,and
print(1>2 or 5>2)
print(1>2 and 5>2)

print(1>2 and 5>2 and 3>2)
print(1>2 or 5>2 and 3>2)
print(2>1 or 1>2 and 3>2)


# karar yapıları
#if else 
sayi1=15
sayi2=15
#sayi1 sayi2den buyukse ekrana sayı1 den buyuktur yazdır
#condition

#indent
if sayi1<sayi2:
    print("sayi1 say2 den küçüktür")
    print("Hala if bloğunun içerisindeyim.")#başındaki boşluklar içeride oldugunu gösteriyor
print("Burası if bloğunun dışıdır.")

if sayi1<sayi2:
    print("sayi1 say2 den küçüktür")
    print("Hala if bloğunun içerisindeyim.")#başındaki boşluklar içeride oldugunu gösteriyor
#eğer if bloğuna girmez ise
elif sayi1==sayi2:
    print("iki sayı eşittir.")
else:
    print("Sayı1 sayı2 den buyuktur.")
print("Burası if bloğunun dışıdır.")



