from tkinter import *
from tkinter import ttk

from tkinter.filedialog import asksaveasfile

class StoreUI(Tk):
    def __init__(self, title, w, h, x, y):
        super().__init__()

        self.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.title(title)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.sidebar_entries_size = 0
        self.dialog_entries_size = 0
        self.curr_prod = -1

        self.username = ""
        self.password = ""

        self.db = None
    
    def connect(self, db):
        self.db = db

    def main(self):
        self.mainloop()

    def export_log(self):
        data = asksaveasfile(mode='w', initialfile="relatorio.txt")
        data.write(self.log)
        data.close()

    def log_dialog(self):
        self.l_dialog = Toplevel(self)
        self.l_dialog.title("Relatorio de produtos")

        w = 600
        h = 500
        x = 300
        y = 200

        self.l_dialog.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.l_dialog.rowconfigure(0, weight=1)
        self.l_dialog.columnconfigure(0, weight=1)

        self.l_dialog = Frame(self.l_dialog)
        self.l_dialog.rowconfigure(0, weight=1)
        self.l_dialog.columnconfigure(0, weight=1)
        self.l_dialog.grid(row=0, column=0, sticky='new', pady=(20, 20))

        textbox = Text(self.l_dialog)
        textbox.grid(row=0, column=0, padx=(10, 10), sticky='nsew')

        self.log = self.db.log()
        textbox.insert(END, self.log)

        newbtn = Button(self.l_dialog, text="Salvar", width=8, command=lambda: self.export_log())
        newbtn.grid(row=self.dialog_entries_size+2, column=0, pady=(10, 10))

        self.l_dialog.bind("<Return>", lambda x: self.create())

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

        self.db.create(name, category, limit_date, t_class, status, active, price)

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

        self.dialog_entries_size = 0

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

    def do_login(self, uname, pwd):
        if self.db.login(uname.get(), pwd.get()):
            self.dialog.destroy()
            self.dialog.update()
            self.username = uname.get()
            self.password = pwd.get()
        else:
            self.incorrect_login_data = Label(self.dialog, text="Usuario ou senha incorretos", width=22)
            self.incorrect_login_data.grid(row=self.dialog_entries_size+3, column=0, sticky='n', pady=(12, 12))

    def login_dialog(self):
        self.dialog = Toplevel(self)
        self.dialog.title("Login")

        w = 400
        h = 200
        x = 300
        y = 200

        self.dialog.geometry("%dx%d+%d+%d" % (w, h, x, y))

        self.dialog.rowconfigure(0, weight=1)
        self.dialog.columnconfigure(0, weight=1)

        self.dialog_div = Frame(self.dialog)
        self.dialog_div.rowconfigure(0, weight=1)
        self.dialog_div.columnconfigure(0, weight=1)
        self.dialog_div.grid(row=0, column=0, sticky='new', pady=(20, 20))

        self.dialog_entries_size = 0

        uname = StringVar()
        pwd =   StringVar()

        username =   self.add_dialog_entry("Usuario", uname)
        password =       self.add_dialog_entry("Senha", pwd)

        newbtn = Button(self.dialog, text="Entrar", width=8, command=lambda: self.do_login(uname, pwd))
        newbtn.grid(row=self.dialog_entries_size+2, column=0, pady=(10, 10))




    def update(self):
        if self.curr_prod != -1:
            name =             self.prod_name_v.get()
            category =     self.prod_category_v.get()
            limit_date = self.prod_limit_date_v.get()
            t_class =         self.prod_class_v.get()
            status =         self.prod_status_v.get()
            active =         self.prod_active_v.get()
            price =           self.prod_price_v.get()

            self.db.update(self.curr_prod, name, category, limit_date, t_class, status, active, price)
            self.reset_list()

    def delete(self):
        if self.curr_prod != -1:
            self.db.delete(self.curr_prod)
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

        separator = ttk.Separator(self.sidebar, orient='horizontal')
        separator.grid(row=self.sidebar_entries_size+3, column=0, sticky='ew', pady=(10, 10))

        buttons_div2 = Frame(self.sidebar)
        buttons_div2.rowconfigure(0, weight=1)
        buttons_div2.columnconfigure(1, weight=1)
        buttons_div2.grid(row=self.sidebar_entries_size+4, column=0, sticky='n', pady=(10, 10))

        logbtn = Button(buttons_div2, text="Relatorio", width=8, command=lambda: self.log_dialog())
        logbtn.grid(row=0, column=0, padx=(10, 5))

        storebtn = Button(buttons_div2, text="Abrir loja", width=8, command=lambda: self.login_dialog())
        storebtn.grid(row=0, column=1, padx=(5, 10))

    def set_entry_value(self, component, value):
        component.delete(0, END)
        component.insert(0, value) 

    def select_product(self):
        selection = self.parenttree.selection()

        if len(selection) == 0:
            return
        
        selection = int(self.parenttree.focus())

        self.set_entry_value(self.product_name,                  self.med_list[selection]['product']) 
        self.set_entry_value(self.product_category,             self.med_list[selection]['category']) 
        self.set_entry_value(self.product_class,       self.med_list[selection]['therapeutic_class']) 
        self.set_entry_value(self.product_limit_date,         self.med_list[selection]['limit_date']) 
        self.set_entry_value(self.product_status,                 self.med_list[selection]['status']) 
        self.set_entry_value(self.product_active,                 self.med_list[selection]['active']) 
        self.set_entry_value(self.product_price,                   self.med_list[selection]['price']) 

        self.curr_prod = selection

    def search_list(self):
        query = self.search_text.get()

        for item in self.parenttree.get_children():
            self.parenttree.delete(item)

        initial_list = self.db.list()
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

        initial_list = self.db.list()
        keys = [item['id'] for item in initial_list]
        self.med_list = dict(zip(keys, initial_list)) 

        for item in self.med_list.values():
            self.parenttree.insert('', END, text=item['product'], iid=item['id'], open=False)

        self.curr_prod = -1

    def run(self):
        box_div = Frame(self)
        box_div.rowconfigure(0, weight=1)
        box_div.columnconfigure(0, weight=1)
        box_div.grid(row=0, column=0, sticky='new')

        div = Frame(box_div)
        div.rowconfigure(0, weight=1)
        div.columnconfigure(0, weight=1)
        div.grid(row=0, column=0, sticky='n', pady=(10, 10))

        newbtn = Button(div, text="Novo", width=8, command=lambda: self.create_dialog())
        newbtn.grid(row=0, column=0, padx=(10, 5))

        separator = ttk.Separator(div, orient='vertical')
        separator.grid(row=0, column=1, sticky='ns', padx=(5, 10))

        self.search_text = StringVar()
        self.searchbox = Entry(div, width=35, textvariable=self.search_text)
        self.searchbox.grid(row=0, column=2)

        self.searchbox.bind('<Return>', lambda x: self.search_list())

        searchbtn = Button(div, text="Pesquisar", width=8, command=lambda: self.search_list())
        searchbtn.grid(row=0, column=3, padx=(10, 5))

        clearbtn = Button(div, text="Limpar", width=8, command=lambda: self.reset_list())
        clearbtn.grid(row=0, column=4, padx=(5, 10))

        tree_div = Frame(box_div)
        tree_div.rowconfigure(0, weight=1)
        tree_div.columnconfigure(0, weight=1)
        tree_div.grid(row=1, column=0, sticky='nsew')

        self.parenttree = ttk.Treeview(tree_div, height=26)
        self.parenttree.heading("#0", text="Medicamentos")

        initial_list = self.db.list()
        keys = [item['id'] for item in initial_list]
        self.med_list = dict(zip(keys, initial_list)) 

        for item in self.med_list.values():
            self.parenttree.insert('', END, text=item['product'], iid=item['id'], open=False)

        self.parenttree.grid(row=0, column=0, sticky='nsew')
        self.parenttree.bind("<Double-Button-1>", lambda x: self.select_product())
        self.parenttree.bind("<Return>",          lambda x: self.select_product())

        self.setup_sidebar()

        self.main()
