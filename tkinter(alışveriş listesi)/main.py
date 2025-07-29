import tkinter as tk 

def ekle():
    urun = urun_gir.get()
    urun_tur = urun_turu.get()
    miktar = urun_miktar.get()
    if not urun or not miktar or not urun_tur:
        return 
    eklencek = f"{urun.strip()}-{urun_tur.strip()}-{miktar.strip()}"
    liste.insert(tk.END,eklencek)
    urun_gir.delete(0,tk.END)
    urun_miktar.set(None)
    urun_turu.set(None)

def guncelle():
    secim = liste.curselection()
    if not secim:
        return
    urun = urun_gir.get()
    urun_tur = urun_turu.get()
    miktar = urun_miktar.get()
    yeni_veri = f"{urun} - {urun_tur} - {miktar}"
    liste.delete(secim[0])
    liste.insert(secim[0], yeni_veri)
    urun_gir.delete(0, tk.END)
    urun_miktar.set(None)
    urun_turu.set(None)

def secimi_goster(event):
    secilen = liste.curselection()
    if not secilen:
        return
    secilen_veri = liste.get(secilen[0])
    urun,urun_tur,miktar = secilen_veri.split("-")
    urun_gir.delete(0,tk.END)
    urun_gir.insert(0,urun)
    urun_turu.set(urun_tur)
    urun_miktar.set(miktar)

def temizle():
    liste.delete(0,tk.END)

pencere = tk.Tk()
pencere.title("Alışveriş Listesi")
pencere.resizable(width =False,height=False)

urun_gir = tk.Entry(pencere)
urun_gir.pack()

urun_miktar = tk.StringVar()
urun_miktar.set(None)

az_urun = tk.Radiobutton(pencere,text="Az",value="Az",variable=urun_miktar)
orta_urun = tk.Radiobutton(pencere,text="Orta",value="Orta",variable=urun_miktar)
cok_urun = tk.Radiobutton(pencere,text="Çok",value="Çok",variable=urun_miktar)
az_urun.pack()
orta_urun.pack()
cok_urun.pack()

urun_turu = tk.StringVar()
urun_turu.set(None)

meyve = tk.Radiobutton(text="Meyve",variable=urun_turu,value="Meyve")
sebze = tk.Radiobutton(text="Sebze",variable=urun_turu,value="Sebze")
diger = tk.Radiobutton(text="Diğer",variable=urun_turu,value="Diğer")
meyve.pack()
sebze.pack()
diger.pack()

frame_btn = tk.Frame(pencere)
frame_btn.pack()

btn_ekle = tk.Button(frame_btn,text="Ekle",command=ekle)
btn_ekle.pack(side=tk.LEFT,padx=4)

btn_temizle = tk.Button(frame_btn,text="Temizle",command=temizle)
btn_temizle.pack(side=tk.LEFT,padx=4)

btn_guncelle = tk.Button(frame_btn,text="Güncelle",command=guncelle)
btn_guncelle.pack(side=tk.LEFT,padx=4)

frame = tk.Frame(pencere)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

liste = tk.Listbox(frame,yscrollcommand=scrollbar.set,width=35)
liste.pack(side=tk.LEFT,fill=tk.BOTH)

liste.bind("<<ListboxSelect>>", secimi_goster)

scrollbar.config(command=liste.yview)

pencere.mainloop()