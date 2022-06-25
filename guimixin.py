from tkinter import Frame,Button, Label, Toplevel, LabelFrame
from tkinter import HORIZONTAL, VERTICAL, X, Y,TOP, BOTTOM, LEFT, RIGHT, BOTH, YES, EW,E,NSEW
import tkinter as tk
from tkinter import StringVar, BooleanVar
from tkinter.ttk import Combobox, Notebook, Entry, Scrollbar, Treeview
from tkinter.messagebox import askokcancel
from tkcalendar import DateEntry
from dbhandler import DataHandler


HEADER_FONT = ("Times New Roman", 36, 'bold italic')
BUTTON_FONT = ("times", 14, "bold italic")
NORMAL_MMFONT= ("Myanmar Pixel Smooth", 14)
HEADER_MMFONT= ("Myanmar Pixel Smooth", 35, "bold")
BG_COLOR = "#335759"
FG_COLOR = "#ffe382"
TEXT_FONT_BOLD = ("Times New Roman", 16, 'bold')
TEXT_FONT_NORM = ("Times New Roman", 14)



def width_limiter(col):
    selector = {"စဉ်": 40, "အမျိုးအမည်": 150, "အရေအတွက်": 90, "မှတ်ချက်": 150
                , "လိပ်စာ": 200}
    result = selector.get(col, 100)
    return result


class Quitter(Frame):
    def __init__(self, parent=None):

        Frame.__init__(self, parent)

        self.pack()

        widget = Button(self, text='Exit', command=self.quit,font=BUTTON_FONT,
                        activebackground='light blue', bg=BG_COLOR,pady=10, relief=tk.GROOVE)

        widget.pack(expand=tk.YES, fill=tk.BOTH)

    def quit(self):

        ans = askokcancel('Verify exit', "Really quit?")

        if ans:
            Frame.quit(self)


class HeaderFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=tk.X)
        self.config(bg=BG_COLOR)
        mLabel = Label(self,text="စံပြ", font=HEADER_MMFONT, fg='#A68DAD')
        mLabel.config(bg=BG_COLOR,padx=30)
        mLabel.pack(side=tk.TOP, anchor="center")
        dLabel = Label(self,text="မွေးမြူရေးအစားအစာနှင့် ဆေးဆိုင်", font=('Myanmar Pixel Smooth', 24,'bold italic')
                       , fg="#A68DAD")
        dLabel.config(bg=BG_COLOR,padx=30, pady=10)
        dLabel.pack(side=tk.TOP,anchor="center")
        lineframe1 = Frame(self, height=5, width=50, bg="#8c2c2c")
        lineframe1.pack(fill=tk.X)



class ItemPrices(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.table = "items"
        self.sub = StringVar()
        self.db = DataHandler()
        name = StringVar()
        code = StringVar()
        i_type = StringVar()
        price = StringVar()
        package = StringVar()
        feedback = StringVar()
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        width = 1000
        height = 600
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.overrideredirect(0)
        self.grab_set()
        self.title("ပစ္စည်း/ဈေးနှုန်း")
        items = {"အစာ": 0, "ဆေး": 1}
        # Make 3 frame from TOP to Bottom
        top = Frame(self,bg= BG_COLOR)
        mid = LabelFrame(self,bg=BG_COLOR)
        bot = Frame(self,bg=BG_COLOR)
        top.pack(side=TOP, expand=False, fill=X)
        mid.pack(side=TOP, expand=YES, fill=BOTH)
        bot.pack(side=BOTTOM, expand=False, fill=X)

        def make_ent(event):
            if type_entry.get() == "အစာ":
                feed_frame.pack(side=LEFT)
                med_frame.pack_forget()
            if type_entry.get() == "ဆေး":
                med_frame.pack(side=LEFT)
                feed_frame.pack_forget()

        win_title = Label(top, text="ပစ္စည်းစာရင်းထည့်သွင်းခြင်းနှင့် ဈေးနှုန်းသတ်မှတ်ခြင်း",
                          font=("Myanmar Pixel Smooth", 14, "normal"), bg=BG_COLOR, pady=10)
        win_title.pack()
        fb_lbl = Label(top, text=feedback.get(), bg=BG_COLOR)
        fb_lbl.pack(side=BOTTOM)
        item_type = Label(top,text='type    :',bg=BG_COLOR)
        item_type.pack(side=LEFT,padx=10, pady=10)

        type_entry = Combobox(top, values=list(items.keys()),width=10, state='readonly')
        type_entry.bind('<<ComboboxSelected>>', lambda event: i_type.set(items[type_entry.get()]))
        type_entry.bind('<<ComboboxSelected>>', make_ent)
        type_entry.pack(side=LEFT,pady=10)

        item_name = Label(top,text="name    :", bg=BG_COLOR)
        item_name.pack(side=LEFT, padx=10)

        name_entry = Entry(top,textvariable=name)
        name_entry.pack(side=LEFT)

        feed_frame = Frame(top, bg=BG_COLOR)
        feed_frame.pack_forget()
        med_frame = Frame(top,bg=BG_COLOR)
        med_frame.pack_forget()

        # packing in feed_frame
        code_lbl = Label(feed_frame, text="code  :", bg=BG_COLOR)
        code_lbl.pack(side=LEFT, padx=10)
        code_entry = Entry(feed_frame, textvariable=code)
        code_entry.pack(side=LEFT)
        pack_lbl = Label(feed_frame, text="package:", bg=BG_COLOR)
        pack_lbl.pack(side=LEFT, padx=10)
        pack_entry = Entry(feed_frame, textvariable=package)
        pack_entry.pack(side=LEFT)
        price_lbl = Label(feed_frame, text='Price', bg=BG_COLOR)
        price_lbl.pack(side=LEFT, padx=10)
        price_entry = Entry(feed_frame, textvariable=price)
        price_entry.pack(side=LEFT)
        but2 = Button(feed_frame,text="Insert", width=10,command=lambda: try_insert(0))
        but2.pack(side=LEFT,padx=10)

        # packing in medicine frame
        pack_lbl = Label(med_frame, text="package:", bg=BG_COLOR)
        pack_lbl.pack(side=LEFT, padx=10)
        pack_entry = Entry(med_frame, textvariable=package)
        pack_entry.pack(side=LEFT)
        price_lbl = Label(med_frame, text='Price', bg=BG_COLOR)
        price_lbl.pack(side=LEFT, padx=10)
        price_entry = Entry(med_frame, textvariable=price)
        price_entry.pack(side=LEFT)
        med_but = Button(med_frame,text="Insert", width=10, command=lambda: try_insert(1))
        med_but.pack(side=LEFT, padx=10)






        # Making Tabs for "ဆေး" and "အစာ"
        tabControl = Notebook(mid)
        tab1 = Frame(tabControl, bg=BG_COLOR)
        tab2 = Frame(tabControl, bg=BG_COLOR)
        tabControl.add(tab1, text="     အစာ      ")
        tabControl.add(tab2, text="     ဆေး      ")
        tabControl.pack(expand=YES, fill=BOTH)

        # Adding items in "အစာ" tab
        scrollbar_y = Scrollbar(tab1, orient=VERTICAL)
        scrollbar_x = Scrollbar(tab1, orient=HORIZONTAL)
        table_col = ("စဉ်", "Item Name", "Code", "Bag", "Price", "မှတ်ချက်")
        table = Treeview(tab1, columns=table_col, show='headings')
        for col in table_col:
            table.heading(col, text=col)
            width = width_limiter(col)
            table.column(col, minwidth=0, width=width)
        scrollbar_y.config(command=table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.config(command=table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.db.cursor.execute('SELECT  i.item_name, f.code, f.price, f.package '
                               'FROM items AS i '
                               'JOIN feed AS f ON i.item_id = f.item_id;')
        databag = self.db.cursor.fetchall()
        self.db.connection.commit()
        iterator = 1
        for row in databag:
            chk = iterator % 2
            if chk > 0:
                odd = 'odd'
            else:
                odd = 'even'
            table.insert('', 'end', values=(iterator, row[0], row[1], row[3], row[2]),
                             tags=(odd,))
            iterator += 1
        table.tag_configure('odd', background='#E8E8E8')
        table.tag_configure('even', background='#DFDFDF')
        table.pack(padx=10)

        # Adding items in "medicine" tab
        scrollbar_y = Scrollbar(tab2, orient=VERTICAL)
        scrollbar_x = Scrollbar(tab2, orient=HORIZONTAL)
        med_table_col = ("စဉ်", "Item Name", "Package", "Price", "မှတ်ချက်")
        med_table = Treeview(tab2, columns=med_table_col, show='headings')
        for col in med_table_col:
            med_table.heading(col, text=col)
            width = width_limiter(col)
            med_table.column(col, minwidth=0, width=width)
        scrollbar_y.config(command=table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.config(command=table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        med_itrator = 1
        self.db.cursor.execute('SELECT  i.item_name, m.package, m.price '
                               'FROM items AS i '
                               'JOIN med AS m ON i.item_id = m.item_id;')
        data = self.db.cursor.fetchall()
        print(data)
        self.db.connection.commit()
        for row in data:
            chk = med_itrator % 2
            if chk > 0:
                odd = 'odd'
            else:
                odd = 'even'
            med_table.insert('', 'end', values=(med_itrator, row[0], row[1], row[2]),
                             tags=(odd,))
            med_itrator += 1
        med_table.tag_configure('odd', background='#E8E8E8')
        med_table.tag_configure('even', background='#DFDFDF')
        med_table.pack(padx=10)

        b3 = Button(bot, text=' Close Child', command=self.destroy)
        b3.pack(side=RIGHT, padx=20)

        def try_insert(chk):
            empty = 1
            if chk == 0:
                entry_list = [child for child in feed_frame.winfo_children()
                          if isinstance(child, Entry)]
            else:
                entry_list = [child for child in med_frame.winfo_children()
                              if isinstance(child, Entry)]
            for entry in entry_list:
                if not entry.get():
                    empty = 0
                    feedback.set("")
            if empty == 1:
                if chk == 0:
                    query = (name.get(),chk)
                    f_id = self.insert(query)
                    query2 = (f_id, code.get(), price.get(), package.get())
                    self.table = "feed"
                    self.insert(query2)

                    name.set(""), code.set(""), package.set(""), price.set(""), type_entry.set("")
                    self.table = "items"
                    feedback.set("Successfully added the item to Database.")
                    fb_lbl.config(text=feedback.get(), fg="black")
                if chk == 1:
                    query = (name.get(), chk)
                    m_id = self.insert(query)
                    query2 = (m_id, package.get(),price.get())
                    self.table = "med"
                    self.insert(query2)
                    name.set(""), package.set(""), price.set(""), type_entry.set("")
                    self.table = "items"
                    feedback.set("Successfully added the item to Database.")
                    fb_lbl.config(text=feedback.get(), fg="black")
            else:
                print("Provide all requires")
                feedback.set("အချက်အလက်များ ပြည့်စုံအောင် ဖြည့်သွင်းပါ။")
                fb_lbl.config(text=feedback.get(),fg="#ed6d6d")

    def insert(self, values):
        self.db.insert(self.table, values)
        ident = self.db.cursor.lastrowid
        return ident

    def select_all(self, entity):
        data = self.db.query(entity)
        return data

    def test(self):
        print("working")


class Customer(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.config(bg=BG_COLOR)
        self.table = "customer"
        self.db = DataHandler()
        name = StringVar()
        address = StringVar()
        phone = StringVar()
        feedback = StringVar()
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        width = 1000
        height = 600
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.overrideredirect(0)
        self.grab_set()
        self.title("ဖောက်သည်များ")
        # Make 3 frame from TOP to Bottom
        top = Frame(self,bg= BG_COLOR)
        mid = LabelFrame(self,bg=BG_COLOR)
        bot = Frame(self,bg=BG_COLOR)
        top.pack(side=TOP, expand=False, fill=X)
        mid.pack(side=TOP, expand=YES, fill=BOTH,padx=5)
        bot.pack(side=BOTTOM, expand=False, fill=X)
        win_title = Label(top, text="ဖောက်သည်များစာရင်း",
                          font=("Myanmar Pixel Smooth", 14, "normal"), bg=BG_COLOR)
        win_title.pack(expand=YES,fill=X,pady=20)
        b3 = Button(bot, text=' Close Child', command=self.destroy)
        b3.pack(side=RIGHT, padx=50, pady=20)
        stable_frame = Frame(mid, bg=BG_COLOR)
        stable_frame.pack(fill=X,pady=10)
        fb_lbl = Label(stable_frame, text=feedback.get(), bg=BG_COLOR)
        fb_lbl.pack(side=BOTTOM)
        self.add_butt = Button(stable_frame,text="Add New Customer", command=lambda: self.show_hide(1))
        self.add_butt.pack(padx=20, pady=5, anchor='e')

        self.toggle = Frame(stable_frame,bg=BG_COLOR)
        self.toggle.pack_forget()

        c_name = Label(self.toggle, text="အမည်    :", bg=BG_COLOR)
        c_name.pack(side=LEFT,pady=5)

        name_entry = Entry(self.toggle, textvariable=name)
        name_entry.pack(side=LEFT,pady=5)

        c_address = Label(self.toggle, text='လိပ်စာ    :', bg=BG_COLOR)
        c_address.pack(side=LEFT,pady=5)

        adr_entry = Entry(self.toggle, textvariable=phone)
        adr_entry.pack(side=LEFT,pady=5)

        c_phone = Label(self.toggle, text='ဖုန်းနံပါတ်     :', bg=BG_COLOR)
        c_phone.pack(side=LEFT,pady=5)

        ph_entry = Entry(self.toggle, textvariable=address)
        ph_entry.pack(side=LEFT, pady=5)
        b1 = Button(self.toggle,text="Insert",command=lambda: try_insert(),width=20)
        b1.pack(side=RIGHT, padx=30, pady=5, anchor='e')

        # Adding items in "medicine" tab
        scrollbar_y = Scrollbar(mid, orient=VERTICAL)
        cus_table_col = ("စဉ်", "အမည်", "နေရပ်လိပ်စာ", "ဖုန်းနံပါတ်", "မှတ်ချက်")
        cus_table = Treeview(mid, columns=cus_table_col, show='headings')
        for col in cus_table_col:
            cus_table.heading(col, text=col)
            width = width_limiter(col)
            cus_table.column(col, minwidth=0, width=width)
        scrollbar_y.config(command=cus_table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        iterator = 1
        databag = self.select_all()
        for row in databag:
            chk = iterator % 2
            if chk > 0:
                odd = 'odd'
            else:
                odd = 'even'
            cus_table.insert('', 'end', values=(iterator, row[1], row[2], row[3]),
                             tags=(odd,))
            iterator += 1
        cus_table.tag_configure('odd', background='#E8E8E8')
        cus_table.tag_configure('even', background='#DFDFDF')
        cus_table.pack(padx=10)

        def try_insert():
            empty = 1
            entry_list = [child for child in self.toggle.winfo_children()
                          if isinstance(child, Entry)]
            for entry in entry_list:
                if not entry.get():
                    empty = 0
            if empty == 1:
                self.show_hide(0)
                query = (name.get(), address.get(), phone.get())
                self.insert(query)
                print(query)
                name.set(""), address.set(""), phone.set("")
                feedback.set("Successfully added the item to Database.")
                fb_lbl.config(text=feedback.get(), fg="black", bg=BG_COLOR)
            else:
                feedback.set("အချက်အလက်များ ပြည့်စုံအောင် ဖြည့်သွင်းပါ။")
                fb_lbl.config(text=feedback.get(),fg="#ed6d6d",bg=BG_COLOR)

    def show_hide(self, stat):
        if stat == 0:
            self.toggle.pack_forget()
            self.add_butt.pack(padx=20, pady=10, anchor='e')
        else:
            self.toggle.pack()
            self.add_butt.pack_forget()

    def select_all(self):
        data = self.db.query(self.table)
        return data

    def insert(self, values):
        self.db.insert(self.table, values)


class Imports(Toplevel):

    def __init__(self, parent):
        super().__init__()
        self.config(bg=BG_COLOR)
        self.table = "imports"
        self.db = DataHandler()
        name = StringVar()
        self.selection = StringVar()
        phone = StringVar()
        i_type = StringVar()
        feedback = StringVar()
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        width = 1000
        height = 600
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.overrideredirect(0)
        self.grab_set()
        self.title("အဝယ်စာရင်း")
        self.entries = []
        self.mylist = []


        item_names = self.db.specific_select("items","item_name")
        combo_names = [result[0] for result in item_names]

        top = Frame(self, bg=BG_COLOR)
        mid = LabelFrame(self, bg=BG_COLOR)
        bot = Frame(self,bg=BG_COLOR)
        top.pack(side=TOP, expand=False, fill=X)
        mid.pack(side=TOP, expand=YES, fill=BOTH,padx=5)
        bot.pack(side=BOTTOM, expand=False, fill=X)

        win_title = Label(top, text="အဝယ်စာရင်းသွင်းခြင်း",
                          font=("Myanmar Pixel Smooth", 14, "normal"), bg=BG_COLOR)
        win_title.pack(expand=YES,fill=X,pady=20)
        b3 = Button(bot, text=' Close Child', command=self.destroy)
        b3.pack(side=RIGHT, padx=50, pady=20)
        date_frame = Frame(mid,bg=BG_COLOR)
        date_frame.pack(side=TOP)
        date_lbl = Label(date_frame,text=" ဝယ်ယူသည့်နေ့စွဲ    :",bg=BG_COLOR)
        date_lbl.pack(side=LEFT, anchor='e')
        date_entry = DateEntry(date_frame, bg=BG_COLOR, date_pattern="dd/MM/yyyy")
        date_entry.pack(side=LEFT,padx=20, pady=20, anchor='e')

        grid_frame = Frame(mid, bg=BG_COLOR)
        grid_frame.pack(side=TOP)

        name_lbl = Label(grid_frame, text="ပစ္စည်းအမည်", bg=BG_COLOR)
        name_lbl.grid(row=0, column=0,pady=10)
        package_lbl = Label(grid_frame, text="ထုတ်ပိုးပုံ", bg=BG_COLOR)
        package_lbl.grid(row=0, column=1)
        tc_lbl = Label(grid_frame, text="သယ်ယူစရိတ်", bg=BG_COLOR)
        tc_lbl.grid(row=0, column=2)
        rate_lbl = Label(grid_frame, text="တစ်ယူနစ်ဈေး", bg=BG_COLOR)
        rate_lbl.grid(row=0, column=3)
        q_lbl = Label(grid_frame, text="အရေအတွက်", bg=BG_COLOR)
        q_lbl.grid(row=0, column=4)
        price_lbl = Label(grid_frame, text="သင့်ငွေ", bg=BG_COLOR)
        price_lbl.grid(row=0, column=5)
        self.make_entries(grid_frame, 1, combo_names)
        insert_butt = Button(mid,text="Save",width=20, command=lambda :self.fetch(self.entries, date_entry.get()))
        insert_butt.pack(side=BOTTOM,anchor='e')

        def try_insert():
            empty = 1
            entry_list = [child for child in self.toggle.winfo_children()
                          if isinstance(child, Entry)]
            for entry in entry_list:
                if not entry.get():
                    empty = 0
            if empty == 1:
                self.show_hide(0)
                query = (name.get(), address.get(), phone.get())
                self.insert(query)
                print(query)
                name.set(""), address.set(""), phone.set("")
                feedback.set("Successfully added the item to Database.")
            else:
                feedback.set("အချက်အလက်များ ပြည့်စုံအောင် ဖြည့်သွင်းပါ။")

    def make_entries(self, mas, r, names):
        ent1 = Combobox(mas, values=names)
        ent1.bind('<<ComboboxSelected>>',lambda event: self.get_2ndBox(ent1.get(),ent2))
        ent1.grid(row=r, column=0, padx=5)
        ent2 = Combobox(mas, values=self.mylist)
        ent2.grid(row=r, column=1, padx=5)
        ent3 = Entry(mas)
        ent3.grid(row=r, column=2, padx=5)
        ent4 = Entry(mas)
        ent4.grid(row=r, column=3, padx=5)
        ent5 = Entry(mas)
        ent5.grid(row=r, column=4, padx=5)
        ent6 = Entry(mas)
        ent6.grid(row=r, column=5, padx=5)
        add_butt = Button(mas, text="Add More", bg=BG_COLOR,
                          command=lambda: self.make_entries(mas, r+1, names))
        add_butt.grid(row=r, column=6, padx=5)
        self.entries.append((ent1, ent2, ent3, ent4, ent5, ent6))

    def show_hide(self, stat):
        if stat == 0:
            self.toggle.pack_forget()
            self.add_butt.pack(padx=20, pady=10, anchor='e')
        else:
            self.toggle.pack()
            self.add_butt.pack_forget()

    def select_all(self):
        data = self.db.query(self.table)
        return data

    def insert(self, values,*args):
        if args is not None:
            self.db.insert(args,values)
        else:
            self.db.insert(self.table, values)

    def fetch(self, entries,date):
        row_count = 0
        query1 = (date)
        self.insert(query1,"imp_voucher")
        # for entry in entries:
        #     text = entry[0].get(), entry[1].get(), entry[2].get(), entry[3].get(), entry[4].get()
        #     row_count +=1
        #     print(row_count,text)

    def get_2ndBox(self, val, ent2):
        ent2['values'] = ""
        self.db.cursor.execute('SELECT DISTINCT item_type FROM items WHERE item_name = "'+str(val)+'";')
        data = self.db.cursor.fetchall()
        checker = [r for r in data]
        if checker[0] == (0,):
            query = 'SELECT f.package FROM feed f JOIN items i ON f.item_id=i.item_id AND i.item_name = "'+ str(val)+'";'
        else:
            query = 'SELECT m.package FROM med m JOIN items i ON m.item_id=i.item_id AND i.item_name ="'+ str(val)+ '";'
        self.db.cursor.execute(query)
        egg = self.db.cursor.fetchall()
        self.db.connection.commit()
        self.mylist = [r for r in egg]
        ent2['values'] = self.mylist
