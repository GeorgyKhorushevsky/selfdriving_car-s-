from tkinter import *
from functions import functions
from tkinter import messagebox as mb, ttk

root = Tk()
root.title("Login page")
# root.geometry("850x500")
xm, ym = 850, 500
func = functions()
canv = Canvas(root, width=xm, heigh=ym)
canv.pack()
label_welcome = Label(root, text="Welcome!", background="white", font="Times 48")
label_login = Label(root, text="Login:", background="white", font="60")
label_password = Label(root, text="Password:", background="white", font="60")
entry_login = Entry(root, foreground="black", background="white", font="60")
entry_password = Entry(root, show="*", foreground="black", background="white", font="60")

day = [str(i) for i in range(1, 32)]
month = [str(i) for i in range(1, 13)]
year = [str(i) for i in range(1999, 2019)]
def clean(i):
    for y in range(-1000, 500):
        canv.create_line(0, y, xm, y, fill="white", arrow=LAST, width=0.1)
    if i:
        label_welcome.destroy()
        label_login.destroy()
        label_password.destroy()
        entry_password.destroy()
        entry_login.destroy()
        login_but.destroy()


clean(0)
canv.create_text(xm - 130, 20, text="For TA:")
canv.create_text(xm - 130, 35, text="login: admin")
canv.create_text(xm - 130, 50, text="password: admin")


def one():
    arra= func.funct[0]()
    root1 = Tk()
    root1.title("Case 1")
    scrollbar = Scrollbar(root1, orient=VERTICAL)
    scrollbar.pack(fill=Y, side=RIGHT)
    listbox = Listbox(root1)
    listbox.pack(fill=BOTH, expand=1)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    for i in arra:
        listbox.insert(END,i)
    root1.mainloop()


def two():
    root2 = Tk()
    root2.title("Date")
    countryVar = StringVar()
    countryCombo = ttk.Combobox( root2,textvariable=countryVar)
    countryCombo['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                              '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    countryCombo.current(1)
    countryCombo.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)
    countryVar1 = StringVar()
    countryCombo1 = ttk.Combobox(root2, textvariable=countryVar1)
    countryCombo1['values'] = (
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
    countryCombo1.current(1)
    countryCombo1.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)
    countryVar2 = StringVar()
    countryCombo2 = ttk.Combobox(root2, textvariable=countryVar2)
    countryCombo2['values'] = (
    '99', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
    '17', '18', '19', '20')
    countryCombo2.current(1)
    countryCombo2.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)
    entry_month = Entry(root2, foreground="black", background="white", font="60")
    def apply():
        arra = func.funct[1]([int(countryCombo1.get()), int(countryCombo.get()), int(countryCombo2.get())])
        root2.destroy()
        root1 = Tk()
        root1.title("Case 2")
        scrollbar = Scrollbar(root1, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root1)
        listbox.pack(fill=BOTH, expand=1)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        for i in arra:
            listbox.insert(END, i)
        root1.mainloop()

    apply_but = Button(root2,text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root2.mainloop()


def three():
    busy = func.funct[2]
    root1 = Tk()
    root1.title("Case 3")
    listbox = Listbox(root1)
    listbox.pack(fill=BOTH, expand=1)

    listbox.insert("Morning     Afternoon     Evening")
    kek = str(busy[0])+"           "+str(busy[1])+"            "+str(busy[2])
    listbox.insert(END, kek)
    root1.mainloop()


def four():
    # some shit we don't know what to do
    print("kek4")


def five():
    root2 = Tk()
    root2.title("Date")
    countryVar = StringVar()
    countryCombo = ttk.Combobox(root2, textvariable=countryVar)
    countryCombo['values'] = (
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    countryCombo.current(1)
    countryCombo.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)
    countryVar1 = StringVar()
    countryCombo1 = ttk.Combobox(root2, textvariable=countryVar1)
    countryCombo1['values'] = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
    countryCombo1.current(1)
    countryCombo1.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)
    countryVar2 = StringVar()
    countryCombo2 = ttk.Combobox(root2, textvariable=countryVar2)
    countryCombo2['values'] = (
        '99', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
        '17', '18', '19', '20')
    countryCombo2.current(1)
    countryCombo2.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)
    entry_month = Entry(root2, foreground="black", background="white", font="60")

    def apply():
        arra = func.funct[4]([int(countryCombo1.get()), int(countryCombo.get()), int(countryCombo2.get())])
        root2.destroy()
        root1 = Tk()
        root1.title("Case 5")
        listbox = Listbox(root1)
        listbox.pack(fill=BOTH, expand=1)
        listbox.insert("Distance     Duration")
        kek = str(arra[0]) + "           " + str(arra[1])
        listbox.insert(END, kek)
        root1.mainloop()

    apply_but = Button(root2, text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root2.mainloop()


def six():
    arra = func.funct[5]()
    root1 = Tk()
    root1.title("Case 6")
    listbox = Listbox(root1)
    listbox.pack(fill=BOTH, expand=1)
    listbox.insert("Morning     Afternoon     Evening")
    kek = str(arra[0][0]) + "           " + str(arra[0][1]) + "            " + str(arra[0][2])
    listbox.insert(END, kek)
    kek = str(arra[1][0]) + " " + str(arra[1][1]) + " " + str(arra[1][2])
    listbox.insert(END, kek)
    root1.mainloop()


def seven():
    arra = func.funct[6]()
    root1 = Tk()
    root1.title("Case 7, list of 10% worst cars")
    scrollbar = Scrollbar(root1, orient=VERTICAL)
    scrollbar.pack(fill=Y, side=RIGHT)
    listbox = Listbox(root1)
    listbox.pack(fill=BOTH, expand=1)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    for i in arra:
        listbox.insert(END, i)
    root1.mainloop()
    print("kek7")


def eight():
    root2 = Tk()
    root2.title("Date")
    countryVar = StringVar()
    countryCombo = ttk.Combobox(root2, textvariable=countryVar)
    countryCombo['values'] = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    countryCombo.current(1)
    countryCombo.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)
    countryVar1 = StringVar()
    countryCombo1 = ttk.Combobox(root2, textvariable=countryVar1)
    countryCombo1['values'] = (
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
    countryCombo1.current(1)
    countryCombo1.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)
    countryVar2 = StringVar()
    countryCombo2 = ttk.Combobox(root2, textvariable=countryVar2)
    countryCombo2['values'] = (
        '99', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
        '17', '18', '19', '20')
    countryCombo2.current(1)
    countryCombo2.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)
    entry_month = Entry(root2, foreground="black", background="white", font="60")

    def apply():
        arra = func.funct[7]([int(countryCombo1.get()), int(countryCombo.get()), int(countryCombo2.get())])
        root2.destroy()
        root1 = Tk()
        root1.title("Case 8")
        listbox = Listbox(root1)
        listbox.pack(fill=BOTH, expand=1)
        listbox.insert("UserId     Amount")
        for i in range(len(arra)):
            kek = str(arra[i][0]) + "        " + str(arra[i][1])
            listbox.insert(END, kek)
        root1.mainloop()

    apply_but = Button(root2, text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root2.mainloop()

def nine():
    print("kek9")


def ten():
    arra = func.funct[9]()
    root1 = Tk()
    root1.title("Case 10")
    listbox = Listbox(root1)
    listbox.pack(fill=BOTH, expand=1)
    listbox.insert(END, arra)
    root1.mainloop()
    print("kek10")
funct = [one, two, three, four,five, six, seven, eight, nine, ten]

def login():

    keker = func.user(str(entry_login), str(entry_password))
    if (keker):
        root.title("Cases:")
        clean(1)
        canv.destroy()
        buttons = [Button(text="3." + (str(i) if i == 10 else ("0" + str(i))), background="#148", foreground="#ccc", padx="14",
                   pady="7", font="13", command=funct[i-1]) for i in range(1,11)]

        for i in range(len(buttons)):
            buttons[i].grid(column=i % 5, row=0 if i < 5 else 1)

    else:
        mb.showerror("Mistake", "login or password is incorrect")
        mb.showinfo("for TA:", "if you are our TA, your login is \"admin\". Password is also \"admin\"")


label_welcome.place(x=200, y=150)
label_login.place(x=200, y=250)
entry_login.place(x=300, y=250)
label_password.place(x=200, y=290)
entry_password.place(x=300, y=290)
login_but = Button(text="Log in", background="#148", foreground="#ccc", padx="14", pady="7", font="13", command=login)
login_but.place(x=250, y=350)
root.mainloop()
