class Araba:
    def __init__(self,marka,model,hiz = 0,yakit = 50):
        self.marka = marka
        self.model = model
        self.hız = hiz
        self.yakıt = yakit
    
    def bilgi_göster(self):
        print(f"Arabanızın markası: {self.marka}, modeli: {self.model}, anlık sürati: {self.hız}, yakıt seviyesi: {self.yakıt} Litre")

    def hizlan(self,miktar):
        if self.hız + miktar>200:
            print("Araba en fazla 200 hıza ulaşabilir")
            self.hız =200
        else:
            self.hız += miktar
    
    def fren_yap(self,miktar):
        if self.hız - miktar<0:
            print("Hız minimum 0 olabilir")
            self.hız = 0
        else:
            self.hız -= miktar

    def yakit_durumu(self):
        print(f"Aracınızın yakıtı: {self.yakıt}")
        if self.yakıt<10:
            print("Yakıtınız 10 Litrenin altında.Lütfen yakıt ekleyiniz:")

    def yakit_ekle(self,miktar):
        if self.yakıt + miktar >100:
            print("Depo en fazla 100 litre yakıt alabilir.")
            self.yakıt = 100
        else:
            self.yakıt += miktar

araba1 = Araba("Ford", "Focus")
araba1.bilgi_göster()
araba1.hizlan(50)
araba1.fren_yap(20)
araba1.bilgi_göster()
araba1.yakit_ekle(40)
araba1.yakit_durumu()
  
