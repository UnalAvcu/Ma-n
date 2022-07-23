girilecekNotSayisi = int(input("Kaç adet not gireceksiniz:"))
girilenNotlar = []
for note in range(girilecekNotSayisi):
    vize = int(input("Vize Notu:"))
    final = int(input("Final Notu:"))
    ortalama = vize*0.4 + final*0.6
    girilenNotlar.append(ortalama)
    
    if ortalama > 50:
        print(f"{note+1}. Dersin Vizesi: {vize}, Dersin Finali: {final}  Dersin Ortalaması: {ortalama} Tebrikler Geçtiniz !")
        print("..........")

    else:
        print(f"{note+1}. Dersin Vizesi: {vize}, Dersin Finali: {final}  Dersin Ortalaması: {ortalama} Üzgünüz Kaldınız.")
        print("...........")

for sayac in range(len(girilenNotlar)-(len(girilenNotlar)-1)):
    for note2 in girilenNotlar:
        print(f"{sayac+1}. Dersin Ortalaması: {note2}")
        sayac += 1