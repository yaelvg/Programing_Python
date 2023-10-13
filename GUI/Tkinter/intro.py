import tkinter as tk
from tkinter import ttk



ventana= tk.Tk()

#ttk.Style.configure('E1.Tlabel', foreground='blue')
#Tlabel se pone por defeecto 

ventana.wm_title("Hola usuario")
etiqueta=tk.Label(ventana,text='Hola a todes', foreground="red")
ventana.wm_minsize(300,200)
etiqueta.pack()

boton=tk.Button(ventana,text='Presioname')
boton.pack()
# etiqueta2=ttk.Label(ventana,text='Otro texto pero con diferente color', style='E1.Tlabel')
# etiqueta2.pack()
ventana.mainloop()
