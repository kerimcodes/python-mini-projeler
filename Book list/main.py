import tkinter as tk 
from tkinter import ttk,messagebox 
import json

dosya = "book.json"

def listing():
    for item in tree.get_children():
        tree.delete(item)

    try:
        with open(dosya,"r",encoding="utf-8") as tobe_read:
            book_ = json.load(tobe_read)
            for book in book_:
                tree.insert("","end",values=(book["Title"],book["Author"],book["Year"]))
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        book_ = []


def add_book(new_book):
    try:
        with open(dosya,"r",encoding="utf-8") as tobe_written:
            book_ = json.load(tobe_written)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        book_ = []

    book_.append(new_book)

    with open(dosya,"w",encoding="utf-8") as tobe_read:
        json.dump(book_,tobe_read,ensure_ascii=False,indent=2)

    listing()

def save_book():
        title = title_entry.get().title()
        author = author_entry.get().title()
        year = year_entry.get()
        if title and author and year:
            new_book_ = {"Title":title,"Author":author,"Year":int(year)}
            add_book(new_book_)
            title_entry.delete(0,tk.END)
            author_entry.delete(0,tk.END)
            year_entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Warning","text boxes cannot be left empty")

def delete_book():
    try: 
        with open(dosya,"r",encoding="utf-8") as tobe_read:
            book_ = json.load(tobe_read)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messagebox.showerror("Error","File is empty")
        book_ = []
    
    title = title_entry.get().title()
    author = author_entry.get().title()
    year = year_entry.get()
    if title and author and year:
        removed_book = {"Title":title,"Author":author,"Year":int(year)}
        found = False
        for book in book_:
            if book == removed_book:
                sure = messagebox.askyesno("",f"Are you sure you want to delete the book named {book['Title']}")
                if sure:
                    book_.remove(book)
                    found = True
                    break

        if found:
            with open(dosya,"w",encoding="utf-8") as f:
                json.dump(book_,f,ensure_ascii=False,indent=2)
            listing()
            title_entry.delete(0,tk.END)
            author_entry.delete(0,tk.END)
            year_entry.delete(0,tk.END)
        else:
            messagebox.showerror("Error","No book found")
       
    else:
        messagebox.showwarning("Warning","text boxes cannot be left empty")

def double_selection(event):
    selected = tree.selection()
    if selected:
        year_entry.delete(0,tk.END)
        author_entry.delete(0,tk.END)
        title_entry.delete(0,tk.END)
        data = tree.item(selected[0])["values"]
        title_entry.insert(0,data[0])
        author_entry.insert(0,data[1])
        year_entry.insert(0,data[2])

def update_book():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning","No book selected")
        return

    try:
        with open(dosya,"r",encoding="utf-8") as f:
            book_ = json.load(f)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messagebox.showerror("Error","File is empty")
        book_ = []
        return

    title = title_entry.get().title()
    author = author_entry.get().title()
    year = year_entry.get()

    if not title or not author or not year:
        messagebox.showwarning("Warning","Text boxes cannot be left empty")
        return

    old_data = tree.item(selected[0])["values"]

    for book in book_:
        if book["Title"] == old_data[0] and book["Author"] == old_data[1] and str(book["Year"]) == str(old_data[2]):
            book_.remove(book)
            break

    book_.append({"Title":title,"Author":author,"Year":int(year)})

    with open(dosya,"w",encoding="utf-8") as f:
        json.dump(book_,f,ensure_ascii=False,indent=2)

    listing()
    title_entry.delete(0,tk.END)
    author_entry.delete(0,tk.END)
    year_entry.delete(0,tk.END)


def validate_year(P):
    return P.isdigit() or P == ""

window = tk.Tk()
window.title("Book List")

mainframe = ttk.Frame(window)
mainframe.pack()

title_label = ttk.Label(mainframe,text="Title:")
title_label.grid(row=0,column=0,ipadx=3)
author_label = ttk.Label(mainframe,text="Author:")
author_label.grid(row=0,column=2,ipadx=3)
year_label = ttk.Label(mainframe,text="Year:")
year_label.grid(row=0,column=4,ipadx=3)

title_entry = ttk.Entry(mainframe)
title_entry.grid(row=0,column=1,ipadx=3)
author_entry = ttk.Entry(mainframe)
author_entry.grid(row=0,column=3,ipadx=3)
year_entry = ttk.Entry(mainframe)
year_entry.grid(row=0,column=6,ipadx=3)

year_entry.config(validate="key", validatecommand=(window.register(validate_year), '%P'))

save_btn = ttk.Button(mainframe,text="Save",command=save_book)
save_btn.grid(row=1,column=2)
delete_btn = ttk.Button(mainframe,text="Delete",command=delete_book)
delete_btn.grid(row=1,column=3)
update_btn = ttk.Button(mainframe,text="Update",command=update_book)
update_btn.grid(row=1,column=4)

alt_frame = ttk.Frame(window)
alt_frame.pack()

columns = ("Title","Author","Year")
tree = ttk.Treeview(alt_frame,columns=columns,show="headings")
tree.pack(side="left",fill="both")

scroll = ttk.Scrollbar(alt_frame,command=tree.yview)
scroll.pack(side="right",fill="y")

tree.configure(yscrollcommand=scroll.set)

for column in columns:
    tree.heading(column,text=column,anchor="center")
    tree.column(column,anchor="center",width=100)

listing()

window.bind("<Double-Button-1>",double_selection)
window.mainloop()