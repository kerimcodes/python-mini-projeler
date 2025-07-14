import json
from datetime import datetime
 
def kayıt_olma():   
    try: 
        with open("kullanici_bilgileri.json","r",encoding="utf-8") as okunacak:    
            kisi_bilgileri = json.load(okunacak)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
            kisi_bilgileri = []    
    while True:
        kullanici_adi = input("Kullanıcı adı seçiniz:")
        if any(kisi["kullanici_adi"]==kullanici_adi for kisi in kisi_bilgileri):
            print("Kullanıcı adı daha önceden seçilmiş.Lütfen başka bir ad seçiniz.")
            continue                   
        sifre = input("şifre belirleyiniz (Sadece rakamlardan oluşmalı):")
        if not sifre.isdigit():
            print("Şifreniz sadece rakamlardan oluşmalıdır.")
            continue
        with open("kullanici_bilgileri.json","w",encoding="utf-8") as yazilacak:
            kisi_bilgileri.append({"kullanici_adi":kullanici_adi,"sifre":sifre})
            json.dump(kisi_bilgileri,yazilacak,indent=4,ensure_ascii=False)
        print("Kayıt başarılı.")
        break
    

def giris():
    with open("kullanici_bilgileri.json","r",encoding="utf-8") as dosya:
        kisi_bilgileri = json.load(dosya)
        while True:
            kullanici_adi = input("Kullanıcı adınızı giriniz:")
            sifre = input("Şifrenizi giriniz:")
            for kullanici in kisi_bilgileri:
                if kullanici["kullanici_adi"] == kullanici_adi and kullanici["sifre"] == sifre:
                    print(f"Sisteme Hoş geldiniz {kullanici_adi}")
                    return kullanici_adi
            else:               
                print("Kullanıcı adı veya şifre hatalı,Lütfen tekrar deneyiniz:")
def harcama_yukle(kullanici_adi):
    try:
        with open("harcamalar.json","r",encoding="utf-8") as okunacak:
            harcalamalar = json.load(okunacak)
            harcamalar = harcalamalar.get(kullanici_adi,[])
            if not harcamalar:
                print("Herhangi bir harcamanız bulunmuyor.")
            else:
                for i,harcama in enumerate(harcamalar,start=1):
                    print(f'{i}-Miktar: {harcama["miktar"]} , Kategori: {harcama["kategori"]} , Tarih: {harcama["tarih"]}')              
    except FileNotFoundError:
        print("Herhangi bir harcama bulunmuyor.")
        
def harcama_ekle(kullanici_adi):
    try:
        with open("harcamalar.json","r",encoding="utf-8") as f:
            harcamalar = json.load(f)
    except (FileNotFoundError,json.decoder.JSONDecodeError):        
        harcamalar = {}
    while True:
        try:
            miktar = float(input("Harcama miktarınızı giriniz:"))
        except ValueError:
            print("Lütfen miktarınızı girerken sadece sayı kullanınız:")
            continue
        kategori = input("Harcamanızın kategorisini yazınız:")
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
        break
    yeni_kayit = {"miktar":miktar,"kategori":kategori,"tarih":tarih}
    if kullanici_adi not in harcamalar:
        harcamalar[kullanici_adi] = []
    harcamalar[kullanici_adi].append(yeni_kayit)
    with open("harcamalar.json","w",encoding="utf-8") as yazilacak:
        json.dump(harcamalar,yazilacak,indent=4,ensure_ascii=False)
    print("Harcamanız başarıyla kaydedildi.")
def kullanici_sayfasi(kullanici_adi):
    while True:
        print("""
    1- Harcama Ekle
    2- Harcamaları göster          
    3- Çıkış
    """)
        secim = input("Seçiminizi yapınız:")
        if secim == "1":
                harcama_ekle(kullanici_adi)
        elif secim == "2":
            harcama_yukle(kullanici_adi)
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break   
        else:
            print("Yanlış seçim")
def main():
    while True:
        print("""
    1- Kayıt Ol
    2- Giriş Yap          
    3- Çıkış
    """)
        secim = input("Seçiminizi yapınız:")
        if secim == "1":
            kayıt_olma()
        elif secim == "2":
            kullanici_adi = giris()
            if kullanici_adi:
                kullanici_sayfasi(kullanici_adi)
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Yanlış seçim")

if __name__=="__main__":
    main()