def toplam(sayi1,sayi2):
    return sayi1+sayi2 
def çıkarma(sayi1,sayi2):
    return sayi1-sayi2
def çarpma(sayi1,sayi2):
    return sayi1*sayi2
def bölme(sayi1,sayi2):
    return sayi1/sayi2
sayi1= int(input("1. sayıyı giriniz:"))
sayi2= int(input("2. sayıyı giriniz:"))
işlem_turu= input("(+,-,*,/)bunlardan birini seçiniz:")
if işlem_turu== "+":
    print("Sonuç:",toplam(sayi1,sayi2))
elif işlem_turu=="-":
    print("Sonuç:",çıkarma(sayi1,sayi2))
elif işlem_turu=="*":
    print("Sonuç:",çarpma(sayi1,sayi2))
elif işlem_turu=="/":
    if sayi2==0:
       print("Bir sayı 0'a bölünemez!")
    else:
        print("Sonuç:",bölme(sayi1,sayi2))
else:
  print("Geçersiz işlem girdiniz...")