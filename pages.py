from tkinter import Frame, Button, LabelFrame
from tkinter import TOP,BOTTOM, LEFT,RIGHT, X, Y, YES, BOTH, HORIZONTAL, VERTICAL
import tkinter as tk
from tkinter import GROOVE
from tkinter.ttk import Scrollbar, Style, Treeview
from tkinter.messagebox import askokcancel
from dbhandler import DataHandler
from guimixin import NORMAL_MMFONT,BG_COLOR
from tkinter.ttk import Notebook,Combobox

# here we are going to define font and colors

FG_COLOR = "#dedad1"
BUTTON_FONT = ("Myanmar Pixel Smooth", 14, "bold italic")
NORMAL_BURMESE = ("Myanmar Pixel Smooth", 12, "normal italic")
TABLE_BURMESE = ("Myanmar Pixel Smooth", 12, "normal")


def width_limiter(col):
    selector = {"စဉ်": 40, "အမျိုးအမည်": 150, "အရေအတွက်": 90, "မှတ်ချက်": 150
                , "လိပ်စာ": 200}
    result = selector.get(col, 100)
    return result


class MenuFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(side=LEFT, fill=Y, padx=30, pady=5)
        self.config(bg=BG_COLOR, pady=10, padx=10)

        menu_items = {
            'ပစ္စည်းစာရင်း': lambda: parent.controller.show_frame(InStock),
            'ဘောင်ချာ': lambda: parent.controller.show_frame(Voucher),
            'ဝယ်သူစာရင်း': lambda: parent.controller.show_frame(Customers),
            'အရောင်းစာရင်း': lambda: parent.controller.show_frame(Sales),
            'Feature1': lambda: parent.controller.show_frame(Feature1)
        }
        for (key, value) in menu_items.items():
            Button(self, text=key, command=value, font=BUTTON_FONT,
                   activebackground='#F0ECE3', bg=BG_COLOR, pady=10, relief=GROOVE
                   ).pack(side=TOP, fill=tk.BOTH, pady=30)
        Quitter(self).pack(side=TOP, fill=tk.BOTH, pady=20)


class Voucher(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        MenuFrame(self)
        label_frame = LabelFrame(self)
        label_frame.pack(side=LEFT, expand=YES, fill=BOTH, padx=10, pady=10)
        label_frame.config(bg=BG_COLOR)


# "ပစ္စည်းစာရင်း" in Burmese
class InStock(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        MenuFrame(self)
        main_frame = LabelFrame(self)
        main_frame.pack(side=LEFT, expand=YES, fill=BOTH, padx=10, pady=10)
        main_frame.config(bg=BG_COLOR)
        food_frame = LabelFrame(main_frame, text="     အစာ     ", font=NORMAL_BURMESE,
                                fg="black")
        food_frame.config(bg=BG_COLOR)
        food_frame.pack(side=LEFT, padx=20, pady=20, expand=YES, fill=Y)
        scrollbar_y = Scrollbar(food_frame, orient=VERTICAL)
        scrollbar_x = Scrollbar(food_frame, orient=HORIZONTAL)
        food_col = ("စဉ်", "အမျိုးအမည်","ဈေးနှုန်း", "အရေအတွက်", "မှတ်ချက်")
        food_table= Treeview(food_frame, columns=food_col, show='headings')
        for col in food_col:
            food_table.heading(col, text=col)
            width = width_limiter(col)
            food_table.column(col, minwidth=0, width=width)
        scrollbar_y.config(command=food_table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.config(command=food_table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        food_table.pack(padx=10)

        med_frame = LabelFrame(main_frame, text="     ဆေး     ", font=NORMAL_BURMESE,
                             fg="black")
        med_frame.config(bg=BG_COLOR)
        med_frame.pack(side=LEFT, padx=20, pady=20, expand=YES, fill=Y)
        scroll_bar_y = Scrollbar(med_frame, orient=VERTICAL)
        scroll_bar_x = Scrollbar(med_frame, orient=HORIZONTAL)
        med_col = ("စဉ်", "အမျိုးအမည်", "ဈေးနှုန်း", "အရေအတွက်", "မှတ်ချက်")
        med_table = Treeview(med_frame, columns=med_col, show='headings')
        for col in med_col:
            med_table.heading(col, text=col)
            width = width_limiter(col)
            med_table.column(col, minwidth=0, width=width)
        scroll_bar_y.config(command=med_table.yview)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        scroll_bar_x.config(command=med_table.xview)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        med_table.pack(padx=10)


# "ဝယ်သူစာရင်း" in Burmese
class Customers(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        MenuFrame(self)
        main_frame = LabelFrame(self)
        main_frame.pack(side=LEFT, expand=YES, fill=BOTH, padx=10, pady=10)
        main_frame.config(bg=BG_COLOR)
        style: Style = Style()
        style.theme_use("clam")
        style.configure("Treeview", background=FG_COLOR, fieldbackground=FG_COLOR)
        table_frame = LabelFrame(main_frame, text="     ဝယ်ယူသူစာရင်း     ", font=NORMAL_BURMESE,
                                 fg="black")
        table_frame.config(bg=BG_COLOR)
        table_frame.pack(side=LEFT, padx=20, pady=20, expand=YES, fill=BOTH)
        scrollbar_y = Scrollbar(table_frame, orient=VERTICAL)
        scrollbar_x = Scrollbar(table_frame, orient=HORIZONTAL)
        table_col = ("စဉ်", "အမည်", "လိပ်စာ", "ဖုန်းနံပါတ်", "ရရန်ကျန်", "မှတ်ချက်")
        table = Treeview(table_frame, columns=table_col, show='headings')
        for col in table_col:
            table.heading(col, text=col)
            width = width_limiter(col)
            table.column(col, minwidth=0, width=width)
        scrollbar_y.config(command=table.yview)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.config(command=table.xview)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        # Inserting data from database
        db = DataHandler()
        data = db.query("customer")
        counter = 1
        for row in data:
            chk = counter % 2
            if chk > 0:
                odd = 'odd'
            else:
                odd = 'even'
            table.insert('', 'end', values=(counter, row[1], row[3], row[2]),
                         tags=(odd,))
            counter += 1
        table.tag_configure('odd', background='#E8E8E8')
        table.tag_configure('even', background='#DFDFDF')
        table.pack(padx=10)


class Sales(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        MenuFrame(self)
        label_frame = LabelFrame(self)
        label_frame.pack(side=LEFT, expand=YES, fill=BOTH, padx=10, pady=10)
        label_frame.config(bg=BG_COLOR)


class Feature1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        MenuFrame(self)
        label_frame = LabelFrame(self)
        label_frame.pack(side=LEFT, expand=YES, fill=BOTH, padx=10, pady=10)
        label_frame.config(bg=BG_COLOR)


class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        self.pack()

        widget = Button(parent, text='ထွက်မည်', command=self.quit, font=NORMAL_MMFONT,
                        bg=BG_COLOR, borderwidth=0)

        widget.pack(side=TOP, expand=True, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")

        if ans:
            Frame.quit(self)
