from utils import *
import PIL.Image
import PIL.ImageTk

from tkinter import *
from tkinter import ttk

class StoreUI(Tk):
    def __init__(self, title, w, h, x, y):
        super().__init__()

        self.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.title(title)

        self.sidebar_entries_size = 0

    def main(self):
        self.mainloop()

    def add_sidebar_entry(self, name):
        div = Frame(self.sidebar)
        div.rowconfigure(0, weight=1)
        div.columnconfigure(0, weight=1)
        div.grid(row=self.sidebar_entries_size+2, column=0, sticky='n')

        label = Label(div, text=f"{name}:", width=15, anchor='w')
        label.grid(row=0, column=0)

        entry = Entry(div, width=35)
        entry.grid(row=0, column=1)

        self.sidebar_entries_size += 1

        return entry
	
    def setup_sidebar(self):
        self.sidebar = Frame(self)
        self.sidebar.rowconfigure(0, weight=1)
        self.sidebar.columnconfigure(1, weight=1)
        self.sidebar.grid(row=0, column=1, sticky='n', padx=(10, 10))
        label = Label(self.sidebar, text="Descricao", width=22, relief=GROOVE).grid(row=0, column=0, sticky='n')
        padding = Label(self.sidebar, text="", width=40).grid(sticky='s')

        self.product_name =                      self.add_sidebar_entry("Nome")
        self.product_category =             self.add_sidebar_entry("Categoria")
        self.product_class =       self.add_sidebar_entry("Classe terapeutica")
        self.product_limit_date =          self.add_sidebar_entry("Vencimento")
        self.product_status =                self.add_sidebar_entry("Situacao")
        self.product_active =         self.add_sidebar_entry("Principio ativo")
        self.product_price =                    self.add_sidebar_entry("Valor")

    def set_entry_value(self, component, value):
        component.delete(0, END)
        component.insert(0, value) 

    def select_product(self):
        selection = self.parenttree.selection()

        if len(selection) == 0:
            return
        
        selection = int(self.parenttree.focus())

        self.set_entry_value(self.product_name,                  ui.med_list[selection]['product']) 
        self.set_entry_value(self.product_category,             ui.med_list[selection]['category']) 
        self.set_entry_value(self.product_class,       ui.med_list[selection]['therapeutic_class']) 
        self.set_entry_value(self.product_limit_date,         ui.med_list[selection]['limit_date']) 
        self.set_entry_value(self.product_status,                 ui.med_list[selection]['status']) 
        self.set_entry_value(self.product_active,                 ui.med_list[selection]['active']) 
        self.set_entry_value(self.product_price,                   ui.med_list[selection]['price']) 

    def search_list(self):
        query = self.search_text.get()

        for item in self.parenttree.get_children():
            self.parenttree.delete(item)

        initial_list = get_medicine_list()
        keys = [item['id'] for item in initial_list]
        self.med_list = dict(zip(keys, initial_list)) 

        for item in self.med_list.values():
            if query in item['product'].lower():
                self.parenttree.insert('', END, text=item['product'], iid=item['id'], open=False)

    def reset_list(self):
        self.search_text.set("")

        self.set_entry_value(self.product_name,        "") 
        self.set_entry_value(self.product_category,    "") 
        self.set_entry_value(self.product_class,       "") 
        self.set_entry_value(self.product_limit_date,  "") 
        self.set_entry_value(self.product_status,      "") 
        self.set_entry_value(self.product_active,      "") 
        self.set_entry_value(self.product_price,       "") 

        for item in self.parenttree.get_children():
            self.parenttree.delete(item)

        initial_list = get_medicine_list()
        keys = [item['id'] for item in initial_list]
        self.med_list = dict(zip(keys, initial_list)) 

        for item in self.med_list.values():
            self.parenttree.insert('', END, text=item['product'], iid=item['id'], open=False)


if __name__ == '__main__':
    ui = StoreUI("Farmacia", 800, 600, 150, 150)

    ui.rowconfigure(0, weight=1)
    ui.columnconfigure(0, weight=1)

    box_div = Frame(ui)
    box_div.rowconfigure(0, weight=1)
    box_div.columnconfigure(0, weight=1)
    box_div.grid(row=0, column=0, sticky='new')

    div = Frame(box_div)
    div.rowconfigure(0, weight=1)
    div.columnconfigure(0, weight=1)
    div.grid(row=0, column=0, sticky='n', pady=(10, 10))

    ui.search_text = StringVar()
    ui.searchbox = Entry(div, width=35, textvariable=ui.search_text)
    ui.searchbox.grid(row=0, column=0)

    ui.searchbox.bind('<Return>', lambda x: ui.search_list())

    searchbtn = Button(div, text="Pesquisar", width=8, command=lambda: ui.search_list())
    searchbtn.grid(row=0, column=1, padx=(10, 5))

    searchbtn = Button(div, text="Limpar", width=8, command=lambda: ui.reset_list())
    searchbtn.grid(row=0, column=2, padx=(5, 10))

    tree_div = Frame(box_div)
    tree_div.rowconfigure(0, weight=1)
    tree_div.columnconfigure(0, weight=1)
    tree_div.grid(row=1, column=0, sticky='nsew')

    ui.parenttree = ttk.Treeview(tree_div, height=26)
    ui.parenttree.heading("#0", text="Medicamentos")

    initial_list = get_medicine_list()
    keys = [item['id'] for item in initial_list]
    ui.med_list = dict(zip(keys, initial_list)) 

    for item in ui.med_list.values():
        ui.parenttree.insert('', END, text=item['product'], iid=item['id'], open=False)

    ui.parenttree.grid(row=0, column=0, sticky='nsew')
    ui.parenttree.bind("<Button-1>", lambda x: ui.select_product())

    ui.setup_sidebar()

    ui.main()

   #menu()
