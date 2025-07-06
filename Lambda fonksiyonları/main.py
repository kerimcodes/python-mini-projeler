from functools import reduce
def sayi_isteme_kontrol():
    while True:
        sayilar = input("Lütfen en az 2 sayı yazınız ve her sayıyı ',' ile ayırınız:")
        if not "," in sayilar:
            print("Lütfen sayıları virgül(,) ile ayırınız.")
            continue
        sayi_list = sayilar.split(",")
        
        if len(sayi_list) <2:
            print("Lütfen en az 2 sayı giriniz.")
            sayi_list.clear()
            continue
        try:
            sayi_list = [int(x.strip()) for x in sayi_list]
            return sayi_list
        except ValueError:
            print("Lütfen sadece sayı giriniz.")
            continue
        
    
def sayi_kare_toplam(sayi_list):
    
    kare_toplam = reduce(lambda x,y:x+y,map(lambda x : x**2,filter(lambda x:x>0,sayi_list)))

    print(f"Yazdığınız sayılar içerisinden pozitif olanlar ayırt edilip kareleri alınmıştır.Karelerinin toplamı : {kare_toplam}")
    
sayi_listem = sayi_isteme_kontrol()
sayi_kare_toplam(sayi_listem)