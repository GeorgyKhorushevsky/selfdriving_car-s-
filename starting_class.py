import calendar
import functools
from datetime import datetime
from tkinter import *
from tkinter.ttk import Combobox

from functions import functions
from tkinter import messagebox as mb, ttk
from db_handler import *
import db_initializer as db_init
import sampling as db_sampling

db = Database('db.sqlite')
db_init.init(db)
db_sampling.sampling(db)
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


def centralize():
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def on_select(event, panel):
    w = event.widget
    check = w.curselection()
    if check:
        for wid in panel.winfo_children():
            wid.destroy()
        index = int(w.curselection()[0])
        value = w.get(index)
        column_names = db.get_table_columns(value)
        column_labels = []
        i = 0
        for name in column_names:
            label = Label(panel, text=name, width=12, wraplength=55)
            label.grid(row=0, column=i)
            column_labels.append(label)
            i += 1
        data = db.get_data(value)
        items = list(data)
        for index, item in enumerate(items):
            for j in range(len(column_labels)):
                Label(panel, text=item[j]).grid(row=index+1, column=j)


def fill_tables():
    tables_names = db.get_table_names()
    tables_content = []
    for name in tables_names:
        tables_content.append(db.get_data(name))
    return tables_names, tables_content


def init():
    master = Frame(root)
    centralize()
    master.pack(expand=YES, fill=BOTH)

    panels = PanedWindow(master, orient=HORIZONTAL)
    panels.pack(expand=YES, fill=BOTH)

    left_panel = Frame(panels)
    left_panel.pack(expand=YES, fill=BOTH)

    tables_names, tables_content = fill_tables()

    list1 = Listbox(left_panel)
    list1.pack(expand=YES, fill=BOTH)

    for name in tables_names:
        list1.insert(END, name)

    right_panel = PanedWindow(panels, orient=VERTICAL)
    right_panel.pack(expand=YES, fill=BOTH)

    top_frame = Frame(right_panel)
    top_frame.pack(expand=YES, fill=BOTH)
    list1.bind('<<ListboxSelect>>', functools.partial(on_select, panel=top_frame))
    list1.selection_set(first=0)
    list1.event_generate('<<ListboxSelect>>')
    right_panel.add(top_frame, stretch="always")

    bottom_frame = Frame(right_panel)
    bottom_frame.pack_propagate(0)
    var = StringVar()
    tasks = list(range(1, 11))
    var.set('1')
    combo = Combobox(bottom_frame, textvariable=var)
    combo['values'] = tasks
    combo.bind('<<ComboboxSelected>>')
    Label(bottom_frame, text="Task Number").grid(row=1, column=1)
    combo.grid(row=2, column=1)

    # if selected value changed
    def change_dropdown(*args):
        selected_value = var.get()
        if selected_value == '1':
            one(bottom_frame)
        elif selected_value == '2':
            two(bottom_frame)
        elif selected_value == '3':
            three()
        elif selected_value == '4':
            four()
        elif selected_value == '5':
            five(bottom_frame)
        elif selected_value == '6':
            six()
        elif selected_value == '7':
            seven()
        elif selected_value == '8':
            eight()
        elif selected_value == '9':
            nine()
        elif selected_value == '10':
            ten()

    var.trace('w', change_dropdown)
    right_panel.add(bottom_frame)
    Label(master, text='tables\' names').pack(side=LEFT, fill=BOTH)
    Label(master, text='tables\' content').pack(fill=BOTH)
    Button(master, text='quit', command=master.quit).pack(side=RIGHT, fill=BOTH)
    Button(master, text='Assignment 3', background="#148", foreground="#ccc").pack(side=RIGHT, fill=BOTH)

    panels.add(left_panel)
    panels.add(right_panel, stretch="always")


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


def one(bottom_frame):
    # arra = func.funct[0]()
    root1 = Toplevel(root)
    root1.title("Case 1")
    # scrollbar = Scrollbar(root1, orient=VERTICAL)
    # scrollbar.pack(fill=Y, side=RIGHT)

    sample_user = StringVar()
    username = Entry(root1, textvariable=sample_user)
    username.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)
    sample_user.set("john_doe")

    sample_letters = StringVar()
    first_letters = Entry(root1, textvariable=sample_letters)
    first_letters.grid(row=0, column=2, padx=5, pady=2, sticky=W)
    sample_letters.set("AN")

    sample_color = StringVar()
    color = Entry(root1, textvariable=sample_color)
    color.grid(row=0, column=3, padx=5, pady=2, sticky=W)
    sample_color.set("red")

    def get_username():
        return sample_user.get()

    def get_letters():
        return sample_letters.get()

    def get_color():
        return sample_color.get()

    sample_user.trace('w', get_username)
    sample_letters.trace('w', get_letters)
    sample_color.trace('w', get_color)

    def case_1(username, color, first_letter):
        query = "SELECT car.* FROM car JOIN ride_order ON car.CID = ride_order.CID " \
                "                      JOIN customer ON customer.username = '{0}'" \
                "                      WHERE car.color = '{1}' AND car.license_plate LIKE '{2}%'".format(username, color, first_letter)
        result = db.get_result(query)
        root2 = Tk()
        root2.title("Case #1")
        scrollbar = Scrollbar(root2, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root2)
        listbox.pack(fill=BOTH, expand=1)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        listbox.insert(END, "Ti pidor")
        for row in result:
            listbox.insert(END, row)
        root2.mainloop()

    def apply():
        user = get_username()
        letters = get_letters()
        color = get_color()
        case_1(user, color, letters)
        root1.destroy()
        root2 = Tk()
        root2.title("Case #2")
        scrollbar = Scrollbar(root2, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root2)
        listbox.pack(fill=BOTH, expand=1)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        root2.mainloop()


    apply_but = Button(root1, text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root1.mainloop()
    listbox = Listbox(root1)
    # listbox.pack(fill=BOTH, expand=1)

    # listbox.config(yscrollcommand=scrollbar.set)
    # scrollbar.config(command=listbox.yview)
    #
    # for i in arra:
    #     listbox.insert(END,i)
    root1.mainloop()
    column_names = db.get_table_columns('car')
    column_labels = []
    i = 0
    for name in column_names:
        label = Label(bottom_frame, text=name, width=12, wraplength=55)
        label.grid(row=0, column=i)
        column_labels.append(label)
        i += 1
    result = db.get_result(query)
    items = list(result)
    for index, item in enumerate(items):
        for j in range(len(column_labels)):
            Label(bottom_frame, text=item[j]).grid(row=index + 1, column=j)


def two(bottom_frame):
    root2 = Toplevel(root)
    root2.title("Case #2")

    day = StringVar()
    day_list = list(range(1, 32))
    days = ttk.Combobox(root2, textvariable=day)
    days['values'] = day_list
    days.current(1)
    days.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)

    month = StringVar()
    months = ttk.Combobox(root2, textvariable=month)
    month_list = list(range(1, 13))
    months['values'] = month_list
    months.current(1)
    months.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)

    year = StringVar()
    years = ttk.Combobox(root2, textvariable=year)
    year_list = list(range(2015, 2020))
    years['values'] = year_list
    years.current(1)
    years.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)

    # entry_month = Entry(root2, foreground="black", background="white", font="60")

    def get_day(*args):
        selected_day = int(day.get())
        return selected_day

    def get_month(*args):
        selected_month = int(month.get())
        return selected_month

    def get_year(*args):
        selected_year = int(year.get())
        return selected_year

    day.trace('w', get_day)
    month.trace('w', get_month)
    year.trace('w', get_year)

    def case_2(year, month, day):
        column_names = db.get_table_columns('car')
        column_labels = []
        i = 0
        for name in column_names:
            label = Label(bottom_frame, text=name, width=12, wraplength=55)
            label.grid(row=0, column=i)
            column_labels.append(label)
            i += 1
        form_date = datetime(year, month, day).date()
        for hour_interval in range(0, 24):
            hour_interval = datetime(year, month, day, hour_interval).strftime('%H')
            start = "%s:00" % str(hour_interval)
            end = "%s:00" % str(int(hour_interval) + 1)
            query = "SELECT COUNT(*) FROM charging_order WHERE date(start_time) = '{0}'" \
                    "AND strftime('%H', start_time) = '{1}'".format(form_date, hour_interval)
            result = db.get_result(query)
            if result:
                for row in result:
                    print(start + "-" + end + " : " + str(row))

    def apply():
        sel_day = get_day()
        sel_month = get_month()
        sel_year = get_year()
        case_2(sel_year, sel_month, sel_day)
        root2.destroy()
        root1 = Tk()
        root1.title("Case #2")
        scrollbar = Scrollbar(root1, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root1)
        listbox.pack(fill=BOTH, expand=1)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        root1.mainloop()

    apply_but = Button(root2,text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root2.mainloop()
    # =================================================================
    # Company management wants to get a statistics on the efficiency
    # of charging stations utilization. Given a date, compute how many
    # sockets were occupied each hour.
    # =================================================================



def three():
    busy = func.funct[2]
    root1 = Toplevel(root)
    root1.title("Case #3")
    day = StringVar()
    day_list = list(range(1, 32))
    days = ttk.Combobox(root1, textvariable=day)
    days['values'] = day_list
    days.current(1)
    days.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)

    month = StringVar()
    months = ttk.Combobox(root1, textvariable=month)
    month_list = list(range(1, 13))
    months['values'] = month_list
    months.current(1)
    months.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)

    year = StringVar()
    years = ttk.Combobox(root1, textvariable=year)
    year_list = list(range(2015, 2020))
    years['values'] = year_list
    years.current(1)
    years.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)

    def get_day(*args):
        selected_day = int(day.get())
        return selected_day

    def get_month(*args):
        selected_month = int(month.get())
        return selected_month

    def get_year(*args):
        selected_year = int(year.get())
        return selected_year

    day.trace('w', get_day)
    month.trace('w', get_month)
    year.trace('w', get_year)

    def case_3(year, month, day):
        # for morning (7 AM - 10 AM)
        morning_start = datetime(year, month, day, 7, 00).strftime('%H')
        print(morning_start)
        morning_end = datetime(year, month, day, 10, 00).strftime('%H')
        # for afternoon (12 AM - 2 PM)
        afternoon_start = datetime(year, month, day, 12, 00).strftime('%H')
        afternoon_end = datetime(year, month, day, 14, 00).strftime('%H')
        # for evening (5 PM - 7 PM)
        evening_start = datetime(year, month, day, 17, 00).strftime('%H')
        evening_end = datetime(year, month, day, 19, 00).strftime('%H')

        form_date = datetime(year, month, day).date()

        query_morning = "SELECT COUNT(DISTINCT CID) FROM ride_order WHERE date(start_time) = '{0}' AND " \
                    "strftime('%H', start_time) >= '{1}' AND strftime('%H', start_time) < '{2}'".format(
                    form_date, morning_start, morning_end)
        result = str(db.get_result(query_morning)[0])
        query_afternoon = "SELECT COUNT(DISTINCT CID) FROM ride_order WHERE date(start_time) = '{0}' AND " \
                    "strftime('%H', start_time) >= '{1}' AND strftime('%H', start_time) < '{2}'".format(
                    form_date, afternoon_start, afternoon_end)
        result += " " + str(db.get_result(query_afternoon)[0])
        query_evening = "SELECT COUNT(DISTINCT CID) FROM ride_order WHERE date(start_time) = '{0}' AND " \
                          "strftime('%H', start_time) >= '{1}' AND strftime('%H', start_time) < '{2}'".format(
            form_date, evening_start, evening_end)
        result += " " + str(db.get_result(query_evening)[0])
        print(result)


    def apply():
        sel_day = get_day()
        sel_month = get_month()
        sel_year = get_year()
        case_3(sel_year, sel_month, sel_day)
        root1.destroy()
        root2 = Toplevel(root)
        root2.title("Case #3")
        scrollbar = Scrollbar(root2, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root2)
        listbox.pack(fill=BOTH, expand=2)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        root2.mainloop()

    apply_but = Button(root1,text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root1.mainloop()


def four():
    # some shit we don't know what to do
    print("kek4")


def five(bottom_frame):
    root2 = Toplevel(root)
    root2.title("Date")

    day = StringVar()
    day_list = list(range(1, 32))
    days = ttk.Combobox(root2, textvariable=day)
    days['values'] = day_list
    days.current(1)
    days.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)

    month = StringVar()
    months = ttk.Combobox(root2, textvariable=month)
    month_list = list(range(1, 13))
    months['values'] = month_list
    months.current(1)
    months.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)

    year = StringVar()
    years = ttk.Combobox(root2, textvariable=year)
    year_list = list(range(2015, 2020))
    years['values'] = year_list
    years.current(1)
    years.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)

    # entry_month = Entry(root2, foreground="black", background="white", font="60")

    def get_day(*args):
        selected_day = int(day.get())
        return selected_day

    def get_month(*args):
        selected_month = int(month.get())
        return selected_month

    def get_year(*args):
        selected_year = int(year.get())
        return selected_year

    day.trace('w', get_day)
    month.trace('w', get_month)
    year.trace('w', get_year)

    def case_5(year, month, day):
        column_names = db.get_table_columns('car')
        column_labels = []
        i = 0
        for name in column_names:
            label = Label(bottom_frame, text=name, width=12, wraplength=55)
            label.grid(row=0, column=i)
            column_labels.append(label)
            i += 1
        form_date = datetime(year, month, day).date()
        query = "SELECT AVG(start_pick_up_dest), AVG(CAST((julianday(end_time) -  julianday(start_time)) * 24 * 60 AS INTEGER)) FROM ride_order WHERE date(start_time) = '{0}'".format(form_date)
        result = db.get_result(query)
        if result:
            for row in result:
                print(str(row))

    def apply():
        sel_day = get_day()
        sel_month = get_month()
        sel_year = get_year()
        case_5(sel_year, sel_month, sel_day)
        root2.destroy()
        root1 = Tk()
        root1.title("Case #2")
        scrollbar = Scrollbar(root1, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root1)
        listbox.pack(fill=BOTH, expand=1)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        root1.mainloop()

    apply_but = Button(root2, text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root2.mainloop()


def six():
    root2 = Toplevel(root)
    root2.title("Date")

    day = StringVar()
    day_list = list(range(1, 32))
    days = ttk.Combobox(root2, textvariable=day)
    days['values'] = day_list
    days.current(1)
    days.grid(row=0, column=1, padx=5, pady=5, ipady=2, sticky=W)

    month = StringVar()
    months = ttk.Combobox(root2, textvariable=month)
    month_list = list(range(1, 13))
    months['values'] = month_list
    months.current(1)
    months.grid(row=0, column=0, padx=5, pady=5, ipady=2, sticky=W)

    year = StringVar()
    years = ttk.Combobox(root2, textvariable=year)
    year_list = list(range(2015, 2020))
    years['values'] = year_list
    years.current(1)
    years.grid(row=0, column=2, padx=5, pady=5, ipady=2, sticky=W)

    day2 = StringVar()
    day_list2 = list(range(1, 32))
    days2 = ttk.Combobox(root2, textvariable=day)
    days2['values'] = day_list
    days2.current(1)
    days2.grid(row=1, column=1, padx=5, pady=5, ipady=2, sticky=W)

    month2 = StringVar()
    months2 = ttk.Combobox(root2, textvariable=month)
    month_list2 = list(range(1, 13))
    months2['values'] = month_list
    months2.current(1)
    months2.grid(row=1, column=0, padx=5, pady=5, ipady=2, sticky=W)

    year2 = StringVar()
    years2 = ttk.Combobox(root2, textvariable=year)
    year_list2 = list(range(2015, 2020))
    years2['values'] = year_list
    years2.current(1)
    years2.grid(row=1, column=2, padx=5, pady=5, ipady=2, sticky=W)

    # entry_month = Entry(root2, foreground="black", background="white", font="60")

    def get_day(*args):
        selected_day = int(day.get())
        return selected_day

    def get_month(*args):
        selected_month = int(month.get())
        return selected_month

    def get_year(*args):
        selected_year = int(year.get())
        return selected_year

    def get_day2(*args):
        selected_day = int(day2.get())
        return selected_day

    def get_month2(*args):
        selected_month = int(month2.get())
        return selected_month

    def get_year2(*args):
        selected_year = int(year2.get())
        return selected_year

    day.trace('w', get_day)
    month.trace('w', get_month)
    year.trace('w', get_year)
    day2.trace('w', get_day2)
    month2.trace('w', get_month2)
    year2.trace('w', get_year2)

    def case_5(year, month, day):
        # for morning (7 AM - 10 AM)
        morning_start = datetime(year, month, day, 7, 00).strftime('%H')
        morning_end = datetime(year, month, day, 10, 00).strftime('%H')
        # for afternoon (12 AM - 2 PM)
        afternoon_start = datetime(year, month, day, 12, 00).strftime('%H')
        afternoon_end = datetime(year, month, day, 14, 00).strftime('%H')
        # for evening (5 PM - 7 PM)
        evening_start = datetime(year, month, day, 17, 00).strftime('%H')
        evening_end = datetime(year, month, day, 19, 00).strftime('%H')

        form_date = datetime(year, month, day).date()

        morning_pickup = "SELECT pick_up_location, COUNT(pick_up_location) AS count " \
                "FROM ride_order WHERE strftime('%H', start_time) >= '{0}' " \
                "AND strftime('%H', start_time) < '{1}' GROUP BY pick_up_location " \
                "ORDER BY count DESC LIMIT 3".format(morning_start, morning_end)
        morning_dest = "SELECT end_location, COUNT(end_location) AS count " \
                "FROM ride_order WHERE strftime('%H', start_time) >= '{0}' " \
                "AND strftime('%H', start_time) < '{1}' GROUP BY end_location " \
                "ORDER BY count DESC LIMIT 3".format(morning_start, morning_end)

        afternoon_pickup = "SELECT pick_up_location, COUNT(pick_up_location) AS count " \
                           "FROM ride_order WHERE strftime('%H', start_time) >= '{0}' " \
                           "AND strftime('%H', start_time) < '{1}'GROUP BY pick_up_location " \
                           "ORDER BY count DESC LIMIT 3".format(morning_start, morning_end)
        afternoon_dest = "SELECT pick_up_location, COUNT(pick_up_location) AS count " \
                         "FROM ride_order WHERE strftime('%H', start_time) >= '{0}' " \
                         "AND strftime('%H', start_time) < '{1}'GROUP BY pick_up_location " \
                         "ORDER BY count DESC LIMIT 3".format(morning_start, morning_end)

        evening_pickup = "SELECT pick_up_location, COUNT(pick_up_location) AS count " \
                         "FROM ride_order WHERE strftime('%H', start_time) >= '{0}' " \
                         "AND strftime('%H', start_time) < '{1}'GROUP BY pick_up_location " \
                         "ORDER BY count DESC LIMIT 3".format(morning_start, morning_end)
        evening_dest = "SELECT pick_up_location, COUNT(pick_up_location) AS count " \
                       "FROM ride_order WHERE strftime('%H', start_time) >= '{0}' " \
                       "AND strftime('%H', start_time) < '{1}'GROUP BY pick_up_location " \
                       "ORDER BY count DESC LIMIT 3".format(morning_start, morning_end)

        # result = db.get_result(query)
        # if result:
            # for row in result:
                # print(str(row))

    def apply():
        sel_day = get_day()
        sel_month = get_month()
        sel_year = get_year()
        case_5(sel_year, sel_month, sel_day)
        root2.destroy()
        root1 = Tk()
        root1.title("Case #2")
        scrollbar = Scrollbar(root1, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT)
        listbox = Listbox(root1)
        listbox.pack(fill=BOTH, expand=1)

        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        root1.mainloop()

    apply_but = Button(root2, text="APPLY", background="#148", foreground="#ccc", padx="14", pady="7", font="13",
                       command=apply)
    apply_but.grid(column=1, row=1)
    root2.mainloop()


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
    keker = func.user(str(entry_login.get()), str(entry_password.get()))
    if (keker):
        root.title("Cases:")
        clean(1)
        canv.destroy()
        buttons = [Button(text="3." + (str(i) if i == 10 else ("0" + str(i))), background="#148", foreground="#ccc", padx="14",
                   pady="7", font="13", command=funct[i-1]) for i in range(1,11)]
        init()

        # for i in range(len(buttons)):
        #     buttons[i].grid(column=i % 5, row=0 if i < 5 else 1)

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
centralize()
root.mainloop()