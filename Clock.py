from tkinter import *
from tkinter.ttk import *
from time import strftime

root=Tk()
root.title('time')

def time():
    string=strftime('%c')
    lbl.config(text=string)
    lbl.after(50,time)

lbl = Label(root, font=('Gloucester MT', 40, 'bold'),
            background='black',
            foreground='white')
lbl.pack(anchor='center')
time()
mainloop()

    
   
