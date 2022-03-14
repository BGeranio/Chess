import tkinter
from PIL import Image, ImageTk

tk = tkinter.Tk()

canvas = tkinter.Canvas(tk, height=500, width=500)


img = Image.open("white_square.png")
what = ImageTk.PhotoImage(img)

canvas.create_image(10,10, image=what)
canvas.create_image(40,10, image=what)

canvas.pack()

tk.mainloop()