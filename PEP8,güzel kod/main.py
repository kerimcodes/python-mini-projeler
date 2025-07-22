import json
import os

DOSYA_ADI = "rehber.json"

def rehberi_yukle():
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Hatalı dosya yapısı, boş rehber başlatılıyor.")
        return {}

def rehberi_kaydet():
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(rehber, dosya, indent=4, ensure_ascii=False)

def kisi_ekle():
    kisi = input("Eklemek istediğiniz kişinin ismini giriniz: ").strip().capitalize()
    if kisi in rehber:
        print(f"{kisi} zaten rehberde kayıtlı.")
        return

    numara = input("11 haneli telefon numarasını giriniz: ").strip()
    if not numara.isdigit() or len(numara) != 11:
        print("Hatalı numara. Sadece 11 haneli rakam giriniz.")
        return

    rehber[kisi] = numara
    rehberi_kaydet()
    print(f"{kisi} rehbere eklendi.")

def kisi_sil():
    kisi = input("Silmek istediğiniz kişinin ismini giriniz: ").strip().capitalize()
    if kisi in rehber:
        del rehber[kisi]
        rehberi_kaydet()
        print(f"{kisi} silindi.")
    else:
        print(f"{kisi} bulunamadı.")

def kisi_tara():
    kisi = input("Aramak istediğiniz kişinin ismini giriniz: ").strip().capitalize()
    if kisi in rehber:
        print(f"{kisi} --> {rehber[kisi]}")
    else:
        print(f"{kisi} rehberde bulunamadı.")

def rehber_listele():
    if not rehber:
        print("Rehber boş.")
    else:
        for kisi, numara in sorted(rehber.items(), key=lambda x: x[0]):
            print(f"{kisi} --> {numara}")

def ana_menu():
    while True:
        print("""
📞  Telefon Rehberi Uygulaması
1 - Kişi Ekle
2 - Kişi Sil
3 - Kişi Ara
4 - Rehberi Listele
5 - Çıkış
""")
        secim = input("Seçiminiz: ").strip()
        if secim == "1":
            kisi_ekle()
        elif secim == "2":
            kisi_sil()
        elif secim == "3":
            kisi_tara()
        elif secim == "4":
            rehber_listele()
        elif secim == "5":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    rehber = rehberi_yukle()
    ana_menu()