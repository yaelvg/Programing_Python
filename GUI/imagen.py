import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

ven=tk.Tk()
ven.wm_title('holis')
img=ImageTk.PhotoImage(Image.open('git.jpeg'))
git=ttk.Label(master=ven, image=img)
git.pack()

ven.mainloop()