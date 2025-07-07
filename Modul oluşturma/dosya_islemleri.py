import os

def dosya_varmi(dosya):
    if not  isinstance(dosya,str):
        raise TypeError("dosya_varmi fonksiyonunda string şeklinde yol kullanılmalıdır.")
    return os.path.exists(dosya)

def dosyaya_yazma(dosya,metin):
    if not  isinstance(dosya,str):
        raise TypeError("dosyaya_yazma fonksiyonunda dosya string şeklinde yol kullanılmalıdır.")
    if not  isinstance(metin,str):
        raise TypeError("dosyaya_yazma fonksiyonunda metin string şeklinde olmalıdır.")
    if not metin.endswith("\n"):
        metin += "\n"
    with open(dosya,"a",encoding="utf-8") as yazilacak:
        return yazilacak.write(metin)
    
def dosyadan_oku(dosya):
    if not  isinstance(dosya,str):
        raise TypeError("dosyadan_oku fonksiyonunda string şeklinde yol kullanılmalıdır.")
    if not os.path.exists(dosya):
        raise FileNotFoundError("dosyadan_oku fonksiyonunda yazdığınız dosya yolu bulunmamaktadır.")
    with open(dosya,"r",encoding="utf-8") as okunacak:
        return okunacak.read()  
    
    
if __name__=="__main__":
    print(dosya_varmi(r"C:\Users\lenovo\OneDrive\Masaüstü\Python-Projeler\Mini_projeler\Modul oluşturma\text.txt"))
    dosyaya_yazma(r"C:\Users\lenovo\OneDrive\Masaüstü\Python-Projeler\Mini_projeler\Modul oluşturma\text.txt","Şampiyon Galatasaray")
    print(dosyadan_oku(r"C:\Users\lenovo\OneDrive\Masaüstü\Python-Projeler\Mini_projeler\Modul oluşturma\text.txt"))