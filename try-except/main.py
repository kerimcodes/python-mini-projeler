# Sayı tahmin
import random

rekor_sayisi = None
rekor_ismi = None
while True:
    oyuncu = input("Oyuncu adınızı girin (çıkmak için 'q'): ")
    if oyuncu.lower() == 'q':
        print("Oyun bitti.")
        if rekor_ismi:
            print(f"🏆 Tüm zamanların rekoru: {rekor_ismi} - {rekor_sayisi} tahminle")
        else:
            print("Henz bir rekor sahibi yok.")
        break
    gizli_sayi = random.randint(1, 100)
    tahmin_sayisi = 0
    print(f"{oyuncu}, 1 ile 100 arasında bir sayı tuttum. Tahmin et bakalım!")
    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        tahmin_sayisi += 1

        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı girin.")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı girin.")
        else:
            print(f"Tebrikler {oyuncu}! {tahmin_sayisi} denemede doğru bildiniz.")
            break

    # Rekor kontrolü
    if rekor_sayisi is None or tahmin_sayisi < rekor_sayisi:
        print("🎉 Yeni rekor! Bravo!")
        rekor_sayisi = tahmin_sayisi
        rekor_ismi = oyuncu
    else:
        print(f"Şu anki rekor: {rekor_ismi} - {rekor_sayisi} tahmin")