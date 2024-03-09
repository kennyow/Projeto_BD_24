from utils import *
import io
import os
from os.path import join, splitext
import PIL.Image
import PIL.ImageTk

from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    window = Tk()

    window.title("Farmacia")
    w = 800
    h = 600
    x = 150
    y = 100

    window.geometry("%dx%d+%d+%d" % (w, h, x, y))

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.parenttree = ttk.Treeview(window)
    window.parenttree.heading("#0", text="Medicamentos")

    med_list = get_medicine_list()
    for item in med_list:
        window.parenttree.insert('', END, text=item['product'], iid=item['id'], open=False)

    window.parenttree.grid(row=0, column=0, sticky='nsew')

    window.mainloop()

   #menu()
