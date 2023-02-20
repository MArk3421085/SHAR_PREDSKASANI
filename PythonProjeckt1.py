from tkinter import *
from tkinter import messagebox
import random



root=Tk()
root.geometry('600x400')

def shar():
    otv=random.randint(0,2)
    if otv == 0:
        messagebox.showinfo('Шар говорит', 'НЕТ')
    elif otv==1:
        messagebox.showinfo('Шар говорит', 'ДА')
    else:
        messagebox.showinfo('Шар говорит', 'ВОЗМОЖНО')

a=Button(width=25, height=10, bg="#F01103",text="встряхнуть",command=shar).pack()




root.mainloop()