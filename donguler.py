#for --- iteration
ogrenciler = ["Fatih", "Aykut", "Eyyub", "Deniz"]
for ogrenci in ogrenciler:
    if(ogrenci.lower() == "fatih".lower()):
        print("Okey")
#öğrenci ismi Fatih ise ekrana "Okey" yazsın
ogrenciler = ["Fatih","Aykut","Eyyub","Deniz"]


#range(100)>>100'e kadar olan sayılara 0'dan 1'er 1'er git
#range(50,100)>>>100'e kadar olan sayılara 50'den 1'er 1'er git
#range(50,100,3)>>>100'e kadar olan sayılara 50'den 3'er 3'er git
#for sayi in range(0,100,2):
    #print(sayi)

#while -> olduğu sürece
# sayac = 0
# while sayac <50:
#     print(sayac)
#     sayac += 1 

# sayac = 0
# while True:
#     print(sayac)
#     sayac+=1

# kullanıcı x kadar not ortalaması girmek istiyor
#girdiği not ortalamalarında 50'den büyük ve eşit olanlar geçti
#Consoleda : "50 dersten 25'ini geçtiniz"
#girdiği tüm notları programın sonunda görmek istiyor

girilecekNotSayisi = int(input("kaç adet not gireceksiniz?"))
gecilenDersSayisi = 0
girilenNotlar=[]
for note in range(girilecekNotSayisi):
        girilenNot = float(input(f"{note+1}.notu giriniz"))
        if (girilenNot >= 50):
            gecilenDersSayisi +=1
print(f"{girilecekNotSayisi} dersten {gecilenDersSayisi} kadar dersi geçtiniz")
print(f"Girdiğiniz Notlar {girilenNotlar}")