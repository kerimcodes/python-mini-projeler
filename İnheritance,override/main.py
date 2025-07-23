class Hayvan:
    def __init__(self,isim,tur):
        self.isim = isim 
        self.tur = tur 
    
    def bilgi_ver(self):
        return f"Hayvanın ismi: {self.isim}, Türü: {self.tur}"
    
    def hareket_et(self):
        print("Hayvan hareket ediyor.")

class Kus(Hayvan):   
    def __init__(self, isim, tur,kanat_uzunlugu):
        super().__init__(isim, tur)
        self.kanat_uzunlugu = kanat_uzunlugu
    
    def uc(self):
        print("Kuş uçuyor")

    def hareket_et(self):
        print("Kuş yürüyor ve bazen uçuyor")

class Penguen(Kus):
    def uc(self):
        print("Penguenler uçamaz")

    def hareket_et(self):
        print("Penguenler yüzerek hareket eder.")
    
h1 = Hayvan("Luna", "Memeli")
print(h1.bilgi_ver())
h1.hareket_et()

print("-----")

k1 = Kus("Serçe", "Kuş", 25)
print(k1.bilgi_ver())
k1.uc()
k1.hareket_et()

print("-----")

p1 = Penguen("Pingu", "Kuş", 50)
print(p1.bilgi_ver())
p1.uc()
p1.hareket_et()
