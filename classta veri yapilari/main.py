class Ogrenci:

    def __init__(self,isim):
        self.isim = isim
        self.notlar = []

    def not_ekle(self,not_):
        if not_ >= 0 and not_ <= 100: 
            self.notlar.append(not_)
        else:
            print("Not 0 ile 100 arasında olmalıdır.")

    def not_sil(self,not_):
        if not not_ in self.notlar:
            print(f"Notlarınız arasında {not_} bulunmuyor")
        else:
            self.notlar.remove(not_)

    def notlari_temizle(self):
        self.notlar = []
        print("Bütün notlar temizlendi")               

    def  ortalama_hesapla(self):
        if len(self.notlar) == 0:
            print("Henüz not girişi olmamıştır.")
        else:
            ort = sum(self.notlar)/len(self.notlar)
            print(f"Ortalamanız: {ort}")
    def __str__(self):
        return f"Öğrenci: {self.isim} | Notlar: {self.notlar}"

    def en_yuksek_not(self):
        if len(self.notlar) == 0:
            print("Henüz not girişi olmamıştır.")
        else:    
            print(f"En yüksek notunuz: {max(self.notlar)}")

    def en_dusuk_not(self):
        if len(self.notlar) == 0:
            print("Henüz not girişi olmamıştır.")
        else:
            print(f"En düşük notunuz: {min(self.notlar)}")

ogrenci1 = Ogrenci("Kerim")
ogrenci1.not_ekle(100)
ogrenci1.not_ekle(98)
ogrenci1.not_ekle(90)
ogrenci1.not_sil(90)
ogrenci1.ortalama_hesapla()
ogrenci1.en_dusuk_not()
ogrenci1.en_yuksek_not()
print(ogrenci1)
ogrenci1.notlari_temizle()
print(ogrenci1)