print("operatorler")
sayi = 15
print(sayi + 10)
print(sayi - 10)
print(sayi * 10)
print(sayi / 10)
print("****")
sayi = sayi + 10
print(sayi + 10)
print(sayi - 10)
print(sayi * 10)
print(sayi / 10)

print(sayi % 2)  #!! MOD OPERATÖRÜ

ondalikSayi = 10.5 

print(ondalikSayi + 10)
print(ondalikSayi - 10)
print(ondalikSayi * 10)
print(ondalikSayi / 10)

sayi = 100
print(sayi ** 2) ##!! ÜS ALMA İŞLEMİ
print(sayi // 15) ##!! TAM BÖLME İŞLEMİ

baslik = "merhaba"
print(baslik + "Etiya")
print(baslik + "Kodlamaio" + "Engin Demiroğ")
print(baslik*10)

print(baslik.lower())
print(baslik.upper())
print(len(baslik))

print(16%2)

#TİP DEĞİŞTİRME
### input => kullanıcıdan veri alma ###

vade = input()
print(f"Vadenin tipi ilk başta: {type(vade)}")
vade = int(vade)
vade = vade + 10
print(f"Vadenin tipi dönüşümden sonra: {type(vade)}")
print(f"Girdiğiniz vade: {vade}")

#pair.py oluşturup kullanıcıdan veri alalım
#1. input vize notu % 40
#2. input final notu % 60
# Geçme notunun 50'den büyük olma durumunu 

vize = int(input('Vize Notu:'))
final = int( input('Final Notu:'))

gecerNotu = ((vize)*0.4 + (final)*0.6)
basarili = (gecerNotu>50)
basarisiz = (gecerNotu<50)

print(f"{gecerNotu} : Geçme durumu başarılı : {basarili}")
print(f"{gecerNotu} : Geçme durumu başarısız : {basarisiz}")

