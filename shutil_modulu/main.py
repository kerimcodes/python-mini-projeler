import shutil
import os
from datetime import datetime
calısma_dosyam = r"C:\Users\lenovo\OneDrive\Masaüstü\çalışma klasörü"

if not os.path.exists("yedekler"):
    os.mkdir("yedekler")
if not os.path.exists("yedek_arsiv"):
    os.mkdir("yedek_arsiv")

with open("log.txt","a",encoding="utf-8") as loglanacak:
    for dosya in os.listdir(calısma_dosyam):
        if dosya.endswith("txt"):
            tam_yol = os.path.join(calısma_dosyam,dosya)
            hedef_yol = os.path.join("yedekler/",dosya)
            if os.path.isfile(tam_yol):
                shutil.copy(tam_yol,hedef_yol)
                loglanacak.write(f'{dosya} dosyası {datetime.now().strftime("%Y-%m-%d %H:%M")} tarihinde yedeklendi.\n')
    shutil.make_archive("yedek_arsiv","zip","yedekler")
    loglanacak.write(f'yedekler klasörü {datetime.now().strftime('%Y-%m-%d %H:%M')} tarihinde arşivlendi.\n')
                