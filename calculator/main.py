from tkinter import ttk 
import tkinter as tk

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{result}")
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: division by 0")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Basic Calculator")
window.state("zoomed")  

main_frame = ttk.Frame(height=200,width=200)
main_frame.pack(expand=True,fill="both")

entry = ttk.Entry(main_frame,width=30,font=("Arial",30))
entry.pack(padx=10,pady=10,ipadx=3,ipady=3,fill="both",expand=True)

innerframe = ttk.Frame(main_frame,width=30,height=30)
innerframe.pack(fill="both",expand=True)

for i in range(5):
    innerframe.rowconfigure(i, weight=1)
for j in range(4):
    innerframe.columnconfigure(j, weight=1)

def on_enter(e):
    e.widget['style'] = "Hover.TButton"
def on_leave(e):
    e.widget['style'] = "TButton"

style = ttk.Style()
style.configure("TButton", font=("Arial",15), background="#f0f0f0")  # normal
style.configure("Hover.TButton", font=("Arial",15), background="#d9d9d9") # hover

ac_btn = ttk.Button(innerframe,text="AC",command=lambda x=entry:x.delete(0,tk.END),style="TButton")
ac_btn.grid(row=0,column=0,ipady=3,sticky="nsew")
del_btn = ttk.Button(innerframe,text="DEL",command=lambda x=entry:x.delete(len(x.get())-1,tk.END),style="TButton")
del_btn.grid(row=0,column=1,ipady=3,sticky="nsew")
equal_btn = ttk.Button(innerframe,text="=",command=equal,style="TButton")
equal_btn.grid(row=0,column=2,ipady=3,sticky="nsew")

numbers = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("4",2,0), 
    ("5",2,1), ("6",2,2),("1",3,0),("2",3,1), 
    ("3",3,2), ("0",4,0), ("00",4,1),(".",4,2), 
    ("+",0,3), ("-",1,3), ("*",2,3), ("/",3,3),("%",4,3)
]

for text,r,c in numbers:
    btn = ttk.Button(innerframe,text=text,command=lambda x=text:entry.insert(tk.END,x),style="TButton")
    btn.grid(row=r,column=c,ipady=3,sticky="nsew")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

for b in [ac_btn, del_btn, equal_btn]:
    b.bind("<Enter>", on_enter)
    b.bind("<Leave>", on_leave)

window.mainloop()