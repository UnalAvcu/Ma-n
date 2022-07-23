##koşul yapıları if, elif ( else if ), else
#indent

# ortalamaNot = 69

# if ortalamaNot < 50:
#     print("Kaldınız")
# elif ortalamaNot >= 50 and ortalamaNot <= 70:
#     print("Normal Geçtiniz")
# else:
#     print("Başarıyla Geçtiniz")


# vade = 24
# kredi = 25000

# if vade > 24 and kredi < 30000:
#     print("30000 TL ve altına 24 aydan fazla kredi çekemezsiniz")
# elif vade < 24 and kredi < 20000:
#     print("20000 TL ve altına 24 aydan küçük vadeli kredi çekemezsiniz")
# else:
#     print("krediniz kullanıma hazırdır")

sayi = input("Sayıyı Giriniz: ")
sayi = float(sayi)
if sayi % 2 == 0:
    print("Sayı çifttir")
elif sayi % 2 == 1:
    print("Sayı tektir")
else:
    print("Sayı hesaplamadı")
