kutuphane=[]
def kitap_ekle():
    isim=input("Kitabın ismini yazınız:")
    yazar=input("kitabın yazarını yazınız:")
    yıl= int(input("Kitabın yazım yılını yazınız:"))
    kitap= {
   "isim":isim,
   "yazar":yazar,
   "yıl":yıl  }   
    kutuphane.append(kitap)
def kitap_ara():
    hangi_kitap= input("Kitabın ismini giriniz:")
    for kitap in kutuphane:
     if hangi_kitap.lower()==kitap["isim"].lower():
      print("Kitap bulundu", kitap)
      break
    else:
      print("Aradığınız kitap bulunamadı.")
def kitaplari_listele():
    if not kutuphane:
     print("Kitap bulunamadı.")
    else:
     for kitap in kutuphane:
      print(f'{kitap["isim"]}-{kitap["yazar"]}-{kitap["yıl"]}')

while True:
 print("ANA MENÜ")
 print("1. Kitap ekle")
 print("2. Kitap ara") 
 print("3.Kitapları listele")
 print("4.Çıkış")
 seçim=int(input("Seçiminizi yapınız:"))
 if seçim==1:
   kitap_ekle()
 elif seçim==2:
   kitap_ara()
 elif seçim==3:
   kitaplari_listele()
 elif seçim==4:
   print("Çıkış yapılıyor...")
   break
 else:
   print("Hatalı seçim")