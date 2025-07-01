from datetime import datetime
import os
import shutil
import zipfile
bugun = datetime.now().strftime("%Y-%m-%d")
klasor = "yedekler-"+bugun
if not os.path.exists(klasor):
    os.mkdir(klasor)

while True:
    kullanilcak_klasor = input("Lütfen klasörünüzü yol olarak giriniz.").replace("\\","/")
    if not kullanilcak_klasor.strip():
        print("Boş giriş yaptınız.Lütfen bir klasör yolu giriniz.")
    elif not  os.path.isdir(kullanilcak_klasor):
        print("Lütfen bir klasör yolu giriniz!")
    else:
        print("KLasör başarıyla tanındı.")
        break

zaman_damgasi = datetime.now().strftime("%Y-%m-%d_%H-%M")
with open("log.txt","a",encoding="utf-8") as log:
    for dosya in os.listdir(kullanilcak_klasor):
        if dosya.endswith(".py") or dosya.endswith(".txt"):
            tam_yol = os.path.join(kullanilcak_klasor,dosya)
            if os.path.isfile(tam_yol):
                ad,uzanti = os.path.splitext(dosya)
                yeni_dosya = ad + "_"+ zaman_damgasi + uzanti
                yeni_yol = os.path.join(klasor,yeni_dosya)
                shutil.copy(tam_yol,yeni_yol)
                log.write(f"Yedekleme tamamlandı. {dosya}-->{yeni_yol}")
zip_klasor = klasor +".zip"
with zipfile.ZipFile(zip_klasor,"w") as zip:
    for ana_klasor,alt_klasor,dosyalar in os.walk(klasor):
        for dosya in dosyalar:
            zip_tamyol = os.path.join(ana_klasor,dosya)
            zip.write(zip_tamyol,arcname=os.path.basename(dosya))