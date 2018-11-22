from tkinter import *
from functions import functions
root = Tk()
root.title("Login page")
root.geometry("850x500")
xm, ym = 850, 500

canv = Canvas(root, width=xm, heigh=ym)
canv.pack()

def clean():
    for y in range(-1000, 500):
         canv.create_line(0, y, xm , y, fill="white", arrow=LAST, width=0.1)

label_welcome = Label(root, text="Welcome!", font="Times 48")
label_login = Label(root, text="Login:", font="60")
label_password = Label(root, text="Password:", font="60")
entry_login = Entry(root, foreground="black", font="60")
entry_password = Entry(root, show="*", foreground="black", font="60")
canv.create_text(xm - 130, 20, text="For TA:")
canv.create_text(xm - 130, 35, text="login: admin")
canv.create_text(xm - 130, 50, text="password: admin")

def login():
    func = functions()
    keker = func.user(str(entry_login), str(entry_password))

label_welcome.place(x=200, y=150)
label_login.place(x=200, y=250)
entry_login.place(x=300, y=250)
label_password.place(x=200, y=290)
entry_password.place(x=300, y=290)
apply_but = Button(text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13", command=login)
apply_but.place(x=250, y=350)
root.mainloop()