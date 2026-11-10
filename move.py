import tkinter as tk
import turtle

def maju():
    t.forward(50)
def mundur():
    t.backward(30)
def kiri():
    t.left(45)
def kanan():
    t.right(45)

def ikuti_mouse(event):

    x = canvas.canvasx(event.x)
    y = -canvas.canvasy(event.y)
    t.setheading(t.towards(x, y))
    t.goto(x, y)

root = tk.Tk()
root.title("kontrol dengan button")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=350)
canvas.pack(pady=10)

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.shape("turtle")
t.color("teal")
t.speed(0)
t.pendown() 


canvas.bind("<Motion>", ikuti_mouse)
canvas.bind("<B1-Motion>", ikuti_mouse)

frame_tombol = tk.Frame(root)
frame_tombol.pack(pady=10)

btn_kiri = tk.Button(frame_tombol, text="belok Kiri", command=kiri, width=10, bg="lightgrey")
btn_kiri.grid(row=0, column=0, padx=5)

btn_kanan = tk.Button(frame_tombol, text="belok Kanan", command=kanan, width=10, bg="lightgrey")
btn_kanan.grid(row=0, column=1, padx=5)

btn_maju = tk.Button(frame_tombol, text="maju", command=maju, width=10, bg="lightgrey")
btn_maju.grid(row=1, column=0, padx=5, pady=5)  

btn_mundur = tk.Button(frame_tombol, text="mundur", command=mundur, width=10, bg="lightgrey")
btn_mundur.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()