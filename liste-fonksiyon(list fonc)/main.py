alisveris_listesi = []
def urun_ekle():
    urun=input("Ürün ismini yazınız:").strip()
    alisveris_listesi.append(urun)
    print("İstediğiniz ürün eklendi.")
def urun_sil():
    silinecek_urun=input("Lütfen silmek istediğiniz ürünü giriniz:")
    for urun in alisveris_listesi:
        if silinecek_urun.lower()==urun.lower():
            alisveris_listesi.remove(urun)
            print("İstediğiniz ürün silindi.")
            break
    else:
        print("Silmek istediğiniz ürün zaten listede bulunmuyor.")
def liste_göruntule():
    if len(alisveris_listesi)==0:
        print("Listenizde hiç ürün yok!")
    else:
        for urun in alisveris_listesi:
            print(urun)
def liste_temizle():
    alisveris_listesi.clear()
    print("Liste Temizlendi.")

while True:
 print("\n Ana Menü")
 print("1.Ürün Ekle")
 print("2.Ürün Sil")
 print("3.Listeyi Görüntüle")
 print("4.Listeyi Temizle")
 print("5. Çıkış")
 seçim=int(input("Seçiminizi Yapınız:"))
 if seçim==1:
     urun_ekle()
 elif seçim==2:
     urun_sil()
 elif seçim==3:
     liste_göruntule()
 elif seçim==4:
     liste_temizle()
 elif seçim==5:
     break
 else:
     print("Hatalı seçim yaptınız...")