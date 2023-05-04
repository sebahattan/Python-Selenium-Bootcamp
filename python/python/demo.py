# Bu öğrenci kayıt sistemine;

#1*************************************** Aldığı isim soy isim ile listeye öğrenci ekleyen
# 2 Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# 3 Listeye birden fazla öğrenci eklemeyi mümkün kılan
# 4 *************************************Listedeki tüm öğrencileri tek tek ekrana yazdıran
# 5 Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# 6 Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# 7 fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.

ogrListesi=["AA","BB","CC","DD","EE","FF"]

#4.MADDE

for ogrenci in ogrListesi:
  print(ogrenci)

#1.MADDE
def ogrEkleme(ad,soyad):
  ogrListesi.append(f"{ad} {soyad}")
  print(ogrListesi)


#3.MADDE******

def topluEkleme(sayi,ad,soyad):
  sayi=int(input("eklenecek ogrenci sayısını giriniz:" ))
  for i in range(sayi):
     ad = input("Ad: ")
     soyad=input("Soyad: ")
     ogrEkleme(ad,soyad)



def sil(ad,soyad):
  ad=input("Silinecek ad: ")
  soyad=input("Silinecek soyad:")
  ogrListesi.remove(f"{ad} {soyad}")
  print(ogrListesi)



ad = input("İsim Giriniz: ")
soyad = input("Soyad Giriniz: ")

ogrEkleme(ad,soyad)
sil(ad,soyad)