import tkinter as tk
from pages import Quitter
from guimixin import HeaderFrame, BG_COLOR,NORMAL_MMFONT
from tkinter import LabelFrame, BOTH, YES, Label, TOP, Button, LEFT
from tkinter import Tk
from PIL import Image, ImageTk
from tkcalendar import Calendar
from time import strftime
from guimixin import ItemPrices, Customer, Imports

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.config(bg="#a7c3f2")
        self.overrideredirect(1)
        self.geometry("%dx%d+0+0" % (w, h))
        HeaderFrame(self)
        container = tk.Frame(self,bg=BG_COLOR)
        container.pack(side=LEFT, fill="both", expand=YES)
        admin_panel = LabelFrame(container)
        admin_panel.pack(side=LEFT, fill=BOTH, padx=20, pady=20)
        admin_panel.config(bg=BG_COLOR)

        sale_panel = LabelFrame(container)
        sale_panel.pack(fill=BOTH, expand=YES, padx=20, pady=20)
        sale_panel.config(bg=BG_COLOR)

        # items&price
        frame1 = LabelFrame(admin_panel)
        frame1.grid(column=0,row=0,padx=20, pady=15)
        frame1.config(bg=BG_COLOR)
        img1 = Image.open(".\photos\clipboard.png")
        img1 = img1.resize( [int(0.3 * s) for s in img1.size])
        img = ImageTk.PhotoImage(img1)
        panel = Label(frame1, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b1 = Button(frame1, text="ပစ္စည်း/ဈေးနှုန်း", font=NORMAL_MMFONT, bg=BG_COLOR
                    , borderwidth=0, command=lambda:ItemPrices(self))
        b1.pack(side=TOP,expand= True, fill= BOTH)

        frame2 = LabelFrame(admin_panel)
        frame2.grid(column=1, row=0, padx=20, pady=5)
        frame2.config(bg=BG_COLOR)
        img2 = Image.open(".\photos\\people.png")
        img2 = img2.resize([int(0.3 * s) for s in img2.size])
        img = ImageTk.PhotoImage(img2)
        panel = Label(frame2, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b2 = Button(frame2, text="ဖောက်သည်များ", font=NORMAL_MMFONT, bg=BG_COLOR
                    , borderwidth=0, command= lambda:Customer(self))
        b2.pack(side=TOP,expand= True, fill= BOTH)

        frame3 = LabelFrame(admin_panel)
        frame3.grid(column=2, row=0, padx=20, pady=5)
        frame3.config(bg=BG_COLOR)
        img3 = Image.open(".\photos\\data-warehouse.png")
        img3 = img3.resize([int(0.3 * s) for s in img3.size])
        img = ImageTk.PhotoImage(img3)
        panel = Label(frame3, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b3 = Button(frame3, text="အဝယ်စာရင်း", font=NORMAL_MMFONT, bg=BG_COLOR
                        ,borderwidth=0, command=lambda:Imports(self))
        b3.pack(side=TOP,expand= True, fill= BOTH)

        frame4 = LabelFrame(admin_panel)
        frame4.grid(column=0, row=1, padx=20, pady=15)
        frame4.config(bg=BG_COLOR)
        img4 = Image.open(".\photos\\settings.png")
        img4 = img4.resize([int(0.3 * s) for s in img4.size])
        img = ImageTk.PhotoImage(img4)
        panel = Label(frame4, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b4 = Button(frame4, text="အရောင်းစာရင်း", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        b4.pack(side=TOP,expand= True, fill= BOTH)

        frame5 = LabelFrame(admin_panel)
        frame5.grid(column=1, row=1, padx=20, pady=10)
        frame5.config(bg=BG_COLOR)
        img5 = Image.open(".\photos\\chicken.png")
        img5 = img5.resize([int(0.3 * s) for s in img5.size])
        img = ImageTk.PhotoImage(img5)
        panel = Label(frame5, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b5 = Button(frame5, text="Batches", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        b5.pack(side=TOP,expand= True, fill= BOTH)

        frame6 = LabelFrame(admin_panel)
        frame6.grid(column=2, row=1, padx=5, pady=5)
        frame6.config(bg=BG_COLOR)
        img6 = Image.open(".\photos\\profit.png")
        img6 = img6.resize([int(0.3 * s) for s in img6.size])
        img = ImageTk.PhotoImage(img6)
        panel = Label(frame6, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b6 = Button(frame6, text="စာရင်းချုပ်", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        b6.pack(side=TOP,expand= True, fill= BOTH)

        frame7 = LabelFrame(admin_panel)
        frame7.grid(column=0, row=2, padx=5, pady=5)
        frame7.config(bg=BG_COLOR)
        img7 = Image.open(".\photos\\profit_1.png")
        img7 = img7.resize([int(0.3 * s) for s in img7.size])
        img = ImageTk.PhotoImage(img7)
        panel = Label(frame7, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b7 = Button(frame7, text="ရရန်ကျန်", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        b7.pack(side=TOP,expand= True, fill= BOTH)

        frame8 = LabelFrame(admin_panel)
        frame8.grid(column=1, row=2, padx=5, pady=5)
        frame8.config(bg=BG_COLOR)
        img8 = Image.open(".\photos\\income.png")
        img8 = img8.resize([int(0.3 * s) for s in img8.size])
        img = ImageTk.PhotoImage(img8)
        panel = Label(frame8, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        b8 = Button(frame8, text="Feature 1", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        b8.pack(side=TOP, expand=True, fill=BOTH)

        global lbl
        lbl = Label(sale_panel, bg=BG_COLOR, fg='white',
                    font=('Times New Roman', 20, 'bold'))
        lbl.grid(column=0,row=0,columnspan=2, pady =20)
        sale_2 = Calendar(sale_panel)
        sale_2.grid(column=2, row=0, columnspan=3, padx=20, pady=20)

        sale1 = LabelFrame(sale_panel)
        sale1.grid(column=0, row=1, padx=20, pady=20)
        sale1.config(bg=BG_COLOR)
        s_img1 = Image.open(".\photos\\income.png")
        s_img1 = s_img1.resize([int(0.3 * s) for s in s_img1.size])
        img = ImageTk.PhotoImage(s_img1)
        panel = Label(sale1, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        button = Button(sale1, text="အဝယ်စာရင်း", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        button.pack(side=TOP, expand=True, fill=BOTH)

        sale2 = LabelFrame(sale_panel)
        sale2.grid(column=1, row=1, padx=5, pady=5)
        sale2.config(bg=BG_COLOR)
        s_img2 = Image.open(".\photos\\income.png")
        s_img2 = s_img2.resize([int(0.3 * s) for s in s_img2.size])
        img = ImageTk.PhotoImage(s_img2)
        panel = Label(sale2, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        button = Button(sale2, text="Sale", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        button.pack(side=TOP, expand=True, fill=BOTH)

        sale3 = LabelFrame(sale_panel)
        sale3.grid(column=4, row=1, padx=5, pady=5)
        sale3.config(bg=BG_COLOR)
        s_img3 = Image.open(".\photos\\income.png")
        s_img3 = s_img3.resize([int(0.3 * s) for s in s_img3.size])
        img = ImageTk.PhotoImage(s_img3)
        panel = Label(sale3, image=img, bg=BG_COLOR)
        panel.image = img
        panel.pack(side=TOP, expand=YES, fill=BOTH)
        button = Button(sale3, text="အဝယ်စာရင်း", font=NORMAL_MMFONT, bg=BG_COLOR
                        , borderwidth=0)
        button.pack(side=TOP, expand=True, fill=BOTH)

        quit_button = LabelFrame(sale_panel)
        quit_button.grid(column=4, row=2, padx=5, pady=5)
        quit_button.config(bg=BG_COLOR)
        exit_img = Image.open(".\photos\\income.png")
        exit_img = exit_img.resize([int(0.3*s) for s in exit_img.size])
        img = ImageTk.PhotoImage(exit_img)
        panel = Label(quit_button,image=img, bg=BG_COLOR)
        panel.img= img
        panel.pack(side=TOP, expand= YES, fill= BOTH)
        Quitter(quit_button)


def display():
    time_get = strftime("%d/%m/%Y\n%I:%M:%S %p")
    lbl.config(text=time_get)
    lbl.after(100,display)


app = App()
display()
app.mainloop()
