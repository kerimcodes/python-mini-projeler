import json

class Kitap:
    def __init__(self,isim:str,yazar:str,sayfa_sayisi,basim_yılı):
        self.isim = isim.title()
        self.yazar = yazar.title()
        self.sayfa_sayisi = sayfa_sayisi
        self.basim_yili = basim_yılı
    
    def bilgi_dict(self):
        return {"isim":self.isim,"yazar":self.yazar,"sayfa sayısı":self.sayfa_sayisi,"basım yılı":self.basim_yili}
    
    def dosyaya_kaydet(self,dosya_adi):
        try:
            with open(dosya_adi,"r",encoding="utf-8") as okunacak:
                kitaplar = json.load(okunacak)
        except FileNotFoundError:
            kitaplar = []
        
        for kitap in kitaplar:
            if self.isim == kitap["isim"] and self.yazar == kitap["yazar"]:
                print(f"Yazarı {self.yazar} olan {self.isim} isimli kitap zaten dosyada mevcuttur.")
                break
        else:
            kitaplar.append(self.bilgi_dict())
        
        with open(dosya_adi,"w",encoding="utf-8") as yazilacak:
            json.dump(kitaplar,yazilacak,ensure_ascii=False,indent=2)

    @staticmethod
    def dosyayi_oku(dosya_adi):
        try:
            with open(dosya_adi,"r",encoding="utf-8") as okunacak:
                dosyalar = json.load(okunacak)
                for i,dosya in enumerate(dosyalar,start=1):
                    print(f"{i}- Kitabın ismi: {dosya["isim"]}-Yazarı:{dosya["yazar"]}-Sayfa sayısı:{dosya["sayfa sayısı"]}-Basım yılı:{dosya["basım yılı"]}")
        except FileNotFoundError:
            print("Dosyada herhangi bir kitap bulunmamaktadır.")
    
    @staticmethod
    def kitap_sil(dosya_adi,kitap_adi:str):
        try:    
            with open(dosya_adi,"r",encoding="utf-8") as okunacak:
                kitaplar = json.load(okunacak)
                for kitap in kitaplar:
                    if kitap["isim"] == kitap_adi.title():
                        kitaplar.remove(kitap)
                        print(f"{kitap_adi.title()} kitabı silindi.")
                        break
                else:
                    print(f"{kitap_adi.title()} isminde kitap bulunamadı.")
            with open(dosya_adi,"w",encoding="utf-8") as yazilacak:
                json.dump(kitaplar,yazilacak,ensure_ascii=False,indent=2)
        except FileNotFoundError:
            print("Dosyada henüz bir kitap bulunmamaktadır.")

k1 = Kitap("Sefiller","Victor Hugo",200,1975).dosyaya_kaydet("kitaplar.json")
k2 = Kitap("Suç ve Ceza","Dostoyevski",500,1970).dosyaya_kaydet("kitaplar.json")
k3 = Kitap("Atatürk","İlber Ortaylı",440,2020).dosyaya_kaydet("kitaplar.json")
Kitap.dosyayi_oku("kitaplar.json")
Kitap.kitap_sil("kitaplar.json","Sefiller")
Kitap.dosyayi_oku("kitaplar.json")