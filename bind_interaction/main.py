import tkinter as tk 

window = tk.Tk()
window.title("Mini project with bind interactions")

canvas = tk.Canvas(window,bg="white",width=600,height=600)
canvas.pack()

circle = canvas.create_oval(80,80,120,120,fill="blue")
square = canvas.create_rectangle(280,280,320,320,fill="yellow")

score = 0 
label = tk.Label(window,text=f"Your score: {score}")
label.pack()

collided = False
def check_collision():
    global score,collided

    x1, y1, x2, y2 = canvas.coords(square)
    ox1, oy1, ox2, oy2 = canvas.coords(circle)
    
    if x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1:
        if not collided:
            score += 1
            label.config(text=f"Your score: {score}")
            collided = True
    else:
        collided = False

def move_circle(event):
    x = event.x 
    y = event.y 
    canvas.coords(circle,x-20,y-20,x+20,y+20)
    check_collision()

def move_or_changecolour_square(event):
    if event.keysym == "Up":
        canvas.move(square,0,-5)
    elif event.keysym == "Down":
        canvas.move(square,0,5)
    elif event.keysym == "Right":
        canvas.move(square,5,0)
    elif event.keysym == "Left":
        canvas.move(square,-5,0)
    elif event.keysym == "space":
        canvas.itemconfig(square,fill="red")
    check_collision()

def reset(event):
    global score
    score = 0
    label.config(text=f"Your score: {score}")

canvas.bind("<Motion>",move_circle)
canvas.bind("<Key>",move_or_changecolour_square)
canvas.focus_set()

window.bind("<Escape>",lambda x: window.destroy())
window.bind("<Button-3>",reset)

window.mainloop()