def gunluk_görme():
    with open("gunluk2.txt","r") as okunacak:
        icerik=okunacak.read()
        print(icerik)
def yeni_kayit_ekleme():
    with open("gunluk2.txt","a") as eklenecek:
        tarih=input("Tarihi giriniz:")            
        icerik=input("İçeriği giriniz:")
        eklenecek.write(f"{tarih}:{icerik}\n")
        print(f"Girdi eklendi: {tarih}:{icerik}")
while True:
    print("--- GÜNLÜK UYGULAMASI ---\n")
    print("1. Günlüğü Gör")
    print("2. Yeni Kayıt Ekle")
    print("3. Çıkış")
    secim=int(input("Seçiminizi yapınız:"))
    if secim==1:
        gunluk_görme()
    elif secim==2:
        yeni_kayit_ekleme()
    elif secim==3:
        print("Çıkış yapılıyor...")
        break
    else:
        print("Hatalı seçim yapıldı!")