#Python Veri Tipleri-Python Data Types

# Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

# Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

# Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.

# Ödev linkinizi buraya yorum olarak ekleyiniz.

#String: Metinsel ifadeler için kullanılır.
name="Python-Selenium Camp"
print(name)

#int:Tam sayılar için kulanılır.
intDataType=20
print(intDataType)

#float:ondalıklı değerler için kullanıllır.
value=100
floatDataType=80.5
print(floatDataType)
print(value/floatDataType)


#bool=true-false 
isTrue=True
print(isTrue,type(isTrue))

#list
listDataType=[1,2,3,True,"ASS"]
print(listDataType,type(listDataType))

#tuple,değiştirilemez öğeler koleksıyonudur.
tupleData=(1,2,3,4,5,True,"ss")
print(tupleData)

# Sözlükler ,Dictionaries: Sözlükler, anahtar-değer çiftleri olarak depolanan bir koleksiyondur.
dictData={
    "first":1,
    "second":2
}
print(dictData)

#Küme (set): Elemanları benzersiz olan veri yapılarıdır. Süslü parantezler { } veya set() fonksiyonu ile tanımlanabilirler. 
kumeData={1, 2, 3, 'a', 'b'}
print(kumeData,type(kumeData))



userName="Sebahaaaat"
userPassword="1202971"

loginName="Sebahat"
loginPassword="1202971"
if userName==loginName and userPassword==loginPassword:
    print("Hoşgeldiniz.Başarılı bir giriş yaptınız.")
else:
    print("Eşleşmeyen veriler var . Bilgilerinizi kontrol ediniz.")