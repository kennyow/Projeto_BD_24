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
        self.dialog_entries_size = 0
        self.curr_prod = -1

    def main(self):
        self.mainloop()

    def add_dialog_entry(self, name, strvar):
        div = Frame(self.dialog_div)
        div.rowconfigure(0, weight=1)
        div.columnconfigure(0, weight=1)
        div.grid(row=self.dialog_entries_size+2, column=0, sticky='n')

        label = Label(div, text=f"{name}:", width=15, anchor='w')
        label.grid(row=0, column=0)

        entry = Entry(div, width=35, textvariable=strvar)
        entry.grid(row=0, column=1)

        self.dialog_entries_size += 1

        return entry
    
    def create(self):
        self.dialog.destroy()
        self.dialog.update()

        name =             self.new_prod_name.get()
        category =     self.new_prod_category.get()
        limit_date = self.new_prod_limit_date.get()
        t_class =         self.new_prod_class.get()
        status =         self.new_prod_status.get()
        active =         self.new_prod_active.get()
        price =           self.new_prod_price.get()

        insert_product(name, category, limit_date, t_class, status, active, price)

        self.reset_list()

    def create_dialog(self):
        self.dialog = Toplevel(self)
        self.dialog.title("Cadastrar produto")

        w = 400
        h = 300
        x = 300
        y = 200

        self.dialog.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.dialog.rowconfigure(0, weight=1)
        self.dialog.columnconfigure(0, weight=1)

        self.dialog_div = Frame(self.dialog)
        self.dialog_div.rowconfigure(0, weight=1)
        self.dialog_div.columnconfigure(0, weight=1)
        self.dialog_div.grid(row=0, column=0, sticky='new', pady=(20, 20))

        self.new_prod_name =       StringVar()
        self.new_prod_category =   StringVar()
        self.new_prod_class =      StringVar()
        self.new_prod_limit_date = StringVar()
        self.new_prod_status =     StringVar()
        self.new_prod_active =     StringVar()
        self.new_prod_price =      StringVar()

        product_name =                      self.add_dialog_entry("Nome", self.new_prod_name)
        product_category =         self.add_dialog_entry("Categoria", self.new_prod_category)
        product_class =      self.add_dialog_entry("Classe terapeutica", self.new_prod_class)
        product_limit_date =    self.add_dialog_entry("Vencimento", self.new_prod_limit_date)
        product_status =              self.add_dialog_entry("Situacao", self.new_prod_status)
        product_active =       self.add_dialog_entry("Principio ativo", self.new_prod_active)
        product_price =                   self.add_dialog_entry("Valor", self.new_prod_price)

        newbtn = Button(self.dialog, text="Salvar", width=8, command=lambda: self.create())
        newbtn.grid(row=self.dialog_entries_size+2, column=0, pady=(10, 10))

        self.dialog.bind("<Return>", lambda x: self.create())

    def update(self):
        if self.curr_prod != -1:
            name =             self.prod_name_v.get()
            category =     self.prod_category_v.get()
            limit_date = self.prod_limit_date_v.get()
            t_class =         self.prod_class_v.get()
            status =         self.prod_status_v.get()
            active =         self.prod_active_v.get()
            price =           self.prod_price_v.get()

            update_product(self.curr_prod, name, category, limit_date, t_class, status, active, price)
            self.reset_list()

    def delete(self):
        if self.curr_prod != -1:
            delete_product(self.curr_prod)
            self.reset_list()

    def add_sidebar_entry(self, name, strvar):
        div = Frame(self.sidebar)
        div.rowconfigure(0, weight=1)
        div.columnconfigure(0, weight=1)
        div.grid(row=self.sidebar_entries_size+2, column=0, sticky='n')

        label = Label(div, text=f"{name}:", width=15, anchor='w')
        label.grid(row=0, column=0)

        entry = Entry(div, width=35, textvariable=strvar)
        entry.grid(row=0, column=1)

        self.sidebar_entries_size += 1

        return entry
	
    def setup_sidebar(self):
        self.sidebar = Frame(self)
        self.sidebar.rowconfigure(0, weight=1)
        self.sidebar.columnconfigure(1, weight=1)
        self.sidebar.grid(row=0, column=1, sticky='n', padx=(10, 10))
        label = Label(self.sidebar, text="Dados do produto", width=22, relief=GROOVE)
        label.grid(row=0, column=0, sticky='n', pady=(12, 12))

        self.prod_name_v =       StringVar()
        self.prod_category_v =   StringVar()
        self.prod_class_v =      StringVar()
        self.prod_limit_date_v = StringVar()
        self.prod_status_v =     StringVar()
        self.prod_active_v =     StringVar()
        self.prod_price_v =      StringVar()

        self.product_name =                      self.add_sidebar_entry("Nome", self.prod_name_v)
        self.product_category =         self.add_sidebar_entry("Categoria", self.prod_category_v)
        self.product_class =      self.add_sidebar_entry("Classe terapeutica", self.prod_class_v)
        self.product_limit_date =    self.add_sidebar_entry("Vencimento", self.prod_limit_date_v)
        self.product_status =              self.add_sidebar_entry("Situacao", self.prod_status_v)
        self.product_active =       self.add_sidebar_entry("Principio ativo", self.prod_active_v)
        self.product_price =                   self.add_sidebar_entry("Valor", self.prod_price_v)

        buttons_div = Frame(self.sidebar)
        buttons_div.rowconfigure(0, weight=1)
        buttons_div.columnconfigure(1, weight=1)
        buttons_div.grid(row=self.sidebar_entries_size+2, column=0, sticky='n', pady=(10, 10))

        savebtn = Button(buttons_div, text="Salvar", width=8, command=lambda: self.update())
        savebtn.grid(row=0, column=0, padx=(10, 5))

        deletebtn = Button(buttons_div, text="Excluir", width=8, command=lambda: self.delete())
        deletebtn.grid(row=0, column=1, padx=(5, 10))

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

        self.curr_prod = selection

    def search_list(self):
        query = self.search_text.get()

        for item in self.parenttree.get_children():
            self.parenttree.delete(item)

        initial_list = get_medicine_list()
        keys = [item['id'] for item in initial_list]
        self.med_list = dict(zip(keys, initial_list)) 

        for item in self.med_list.values():
            if query.lower() in item['product'].lower():
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

        self.curr_prod = -1


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

    newbtn = Button(div, text="Novo", width=8, command=lambda: ui.create_dialog())
    newbtn.grid(row=0, column=0, padx=(10, 5))

    separator = ttk.Separator(div, orient='vertical')
    separator.grid(row=0, column=1, sticky='ns', padx=(5, 10))

    ui.search_text = StringVar()
    ui.searchbox = Entry(div, width=35, textvariable=ui.search_text)
    ui.searchbox.grid(row=0, column=2)

    ui.searchbox.bind('<Return>', lambda x: ui.search_list())

    searchbtn = Button(div, text="Pesquisar", width=8, command=lambda: ui.search_list())
    searchbtn.grid(row=0, column=3, padx=(10, 5))

    searchbtn = Button(div, text="Limpar", width=8, command=lambda: ui.reset_list())
    searchbtn.grid(row=0, column=4, padx=(5, 10))

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
    ui.parenttree.bind("<Double-Button-1>", lambda x: ui.select_product())
    ui.parenttree.bind("<Return>",          lambda x: ui.select_product())

    ui.setup_sidebar()

    ui.main()

