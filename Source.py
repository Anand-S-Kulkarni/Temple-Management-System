import tkinter
from tkinter import *
from tkinter import messagebox as ms, IntVar
from PIL import ImageTk, Image
import cx_Oracle as cx
import datetime as dt
import time
import tkinter.font as tkFont
import tkinter.ttk as ttk

# =======================Main Window========================================#

root = Tk()
width = 830
height = 510
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.resizable(0, 0)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

# ===============================Background Image================================#
img = ImageTk.PhotoImage(Image.open("temple1.png"))
bg_image = Label(root, image=img)
bg_image.pack()

img1 = ImageTk.PhotoImage(Image.open("admin.png"))
bg_image1 = Label(root, image=img1, width=55, height=55)

bg_image1.place(x=560, y=150)
img2 = ImageTk.PhotoImage(Image.open("user.png"))
bg_image2 = Label(root, image=img2, width=54, height=52)

bg_image2.place(x=561, y=207)
Top = Frame(root, bd=4, relief=FLAT, bg='white', width=100)
Top.place(x=330, y=15)
Form = Frame(root, height=800, width=200)
Form.place(x=620, y=150)


# ================================================HomPage=============================================#
def main_form():
    lbl_title = Label(Top, text="WELCOME", font=("Helvetica", 20), width=15)
    lbl_title.grid(row=0, column=2)
    btn_admin = Button(Form, text="Admin", font=('arial', 19), pady=5, width=10, command=admin_form)
    btn_admin.grid(row=0)
    btn_user = Button(Form, text="User", font=('arial', 19), pady=5, width=10, command=user_form)
    btn_user.grid(row=2)


# ==================================End of HomePage====================================================#


# ====================================Admin Login=====================================================#
def admin_login():
    if emailid.get() == "admin" and password.get() == "admin":
        emailid.delete("0", END)
        password.delete("0", END)
        Admin_First_Page()
    else:
        ms.showerror("Invalid EmailId or password")
        emailid.delete("0", END)
        password.delete("0", END)


def backtoroot():
    Admin_pg.destroy()
    root.deiconify()


def admin_form():
    root.withdraw()
    global Admin_pg
    Admin_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(Admin_pg, image=img3)
    bg_image3.place(x=0, y=0)

    width = 830
    height = 511
    screen_width = Admin_pg.winfo_screenwidth()
    screen_height = Admin_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Admin_pg.resizable(0, 0)
    Admin_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Label(Admin_pg, text="Admin Login", justify=CENTER, font=("Showcard Gothic", 20)).place(x=320, y=60)

    global emailid
    Label(Admin_pg, text="UserName: ", font=('', 16)).place(x=200, y=150)
    emailid = Entry(Admin_pg, bd=3, font=('', 16))
    emailid.place(x=320, y=145)

    global password
    Label(Admin_pg, text="Password: ", font=('', 16)).place(x=200, y=210)
    password = Entry(Admin_pg, bd=3, font=('', 16), show='*')
    password.place(x=320, y=205)

    Button(Admin_pg, text="Login", font=('', 16), width=10, bg="purple1", fg='white', command=admin_login).place(x=250,
                                                                                                                 y=270)
    Button(Admin_pg, text="Back", font=('', 16), width=10, bg="purple1", fg='white', command=backtoroot).place(x=420,
                                                                                                               y=270)
    Admin_pg.mainloop()


# ==========================================Admin Login End============================================================#


# ================================Page After Admin Login===============================================================#
def Backto_adminlogin():
    admin_first_page.destroy()
    Admin_pg.deiconify()


def Admin_First_Page():
    Admin_pg.withdraw()
    global admin_first_page

    admin_first_page = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(admin_first_page, image=img3)
    bg_image3.place(x=0, y=0)

    width = 830
    height = 511
    screen_width = admin_first_page.winfo_screenwidth()
    screen_height = admin_first_page.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    admin_first_page.resizable(0, 0)
    admin_first_page.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Button(admin_first_page, text="Add User", bg='white', font=('Helvetica', '12', "bold italic"),
           command=adduser).place(x=320, y=60, width=220, height=50)
    Button(admin_first_page, text="View Devotees", bg='white', font=('Helvetica', '12', "bold italic"),
           command=displaydevotees).place(x=320, y=120, width=220, height=50)
    Button(admin_first_page, text="Accounts And Payroll", bg='white', font=('Helvetica', '12', "bold italic"),
           command=displayAccount).place(x=320, y=180, width=220, height=50)
    Button(admin_first_page, text="Inventory Status", bg='white', font=('Helvetica', '12', "bold italic"),
           command=displayinventory).place(x=320, y=240, width=220, height=50)
    Button(admin_first_page, text="View Booking Status", bg='white', font=('Helvetica', '12', "bold italic"),
           command=displayDonation).place(x=320, y=300, width=220, height=50)
    Button(admin_first_page, text="Seva Details", bg='white', font=('Helvetica', '12', "bold italic"),
           command=displaySeva).place(x=320, y=360, width=220, height=50)
    Button(admin_first_page, text="Back", bg='white', font=('Helvetica', '12', "bold italic"),
           command=Backto_adminlogin).place(x=320, y=420, width=220, height=50)
    admin_first_page.mainloop()


# ====================================End of Admin ====================================================================#


# ======================================User Login=====================================================================#
def user_login():
    userloginconn = cx.connect("system", "system", "XE")
    userlogincursor = userloginconn.cursor()
    UserLoginUsername = entry_userpg_username.get()
    UserLoginPassword = entry_userpg_password.get()
    userlogincursor.execute("select password from user_registration where username=:k", {'k': UserLoginUsername})
    Userpassword = userlogincursor.fetchone()
    if UserLoginPassword == Userpassword[0]:
        ms.showinfo("Login Success", "Login Successful" + "\nGood Day")
        entry_userpg_username.delete("0", END)
        entry_userpg_password.delete("0", END)
        User_First_Page()
    else:
        ms.showinfo("Login Failed", "Enter Valid Username and Password" + "\nTry Again...!")
        entry_userpg_username.delete("0", END)
        entry_userpg_password.delete("0", END)
        userloginconn.close()


def Backtoroot():
    User_pg.destroy()
    root.deiconify()


def user_form():
    root.withdraw()
    global User_pg
    User_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(User_pg, image=img3)
    bg_image3.place(x=0, y=0)

    width = 830
    height = 511
    screen_width = User_pg.winfo_screenwidth()
    screen_height = User_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    User_pg.resizable(0, 0)
    User_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Label(User_pg, text="User Login", justify=CENTER, font=("Showcard Gothic", 20)).place(x=320, y=60)

    global entry_userpg_username
    Label(User_pg, text="UserName: ", font=('', 16)).place(x=200, y=150)
    entry_userpg_username = Entry(User_pg, bd=3, font=('', 16))
    entry_userpg_username.place(x=320, y=145)

    global entry_userpg_password
    Label(User_pg, text="Password: ", font=('', 16)).place(x=200, y=210)
    entry_userpg_password = Entry(User_pg, bd=3, font=('', 16), show='*')
    entry_userpg_password.place(x=320, y=205)

    Button(User_pg, text="Login", font=('', 16), width=10, bg="purple1", fg='white', command=user_login).place(x=250,
                                                                                                               y=270)
    Button(User_pg, text="Back", font=('', 16), width=10, bg="purple1", fg='white', command=Backtoroot).place(x=420,
                                                                                                              y=270)
    User_pg.mainloop()


# ==============================================End User Login=========================================================#


# ===============================================User First Page=======================================================#
def backto_userlogin():
    user_first_page.destroy()
    User_pg.deiconify()


def User_First_Page():
    User_pg.withdraw()
    global user_first_page
    user_first_page = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(user_first_page, image=img3)
    bg_image3.place(x=0, y=0)

    width = 830
    height = 511
    screen_width = user_first_page.winfo_screenwidth()
    screen_height = user_first_page.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    user_first_page.resizable(0, 0)
    user_first_page.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Button(user_first_page, text="Add Devotees", bg='white', font=('Helvetica', '12', "bold italic"),
           command=addDevotees).place(x=320, y=60, width=220, height=50)
    Button(user_first_page, text="Enter Accounts And Payroll", bg='white', font=('Helvetica', '12', "bold italic"),
           command=account_and_payroll).place(x=320, y=120, width=220, height=50)
    Button(user_first_page, text="Enter Inventory Details", bg='white', font=('Helvetica', '12', "bold italic"),
           command=inventory).place(x=320, y=180, width=220, height=50)
    Button(user_first_page, text="Fill Booking Details", bg='white', font=('Helvetica', '12', "bold italic"),
           command=donation).place(x=320, y=240, width=220, height=50)
    Button(user_first_page, text="Enter Seva Details", bg='white', font=('Helvetica', '12', "bold italic"),
           command=seva).place(x=320, y=300, width=220, height=50)
    Button(user_first_page, text="Back", bg='white', font=('Helvetica', '12', "bold italic"),
           command=backto_userlogin).place(x=320, y=360, width=220, height=50)
    user_first_page.mainloop()


# ================================================Endo of User First Page==============================================#


# ===========================================Add Devotees Page=========================================================#
def submitAddDevotee():
    devoteeconn = cx.connect("system", "system", "XE")
    devoteecursor = devoteeconn.cursor()
    devotee_name = entry_devotee_name.get()
    devotee_age = entry_devotee_age.get()
    devotee_gender = entry_devotee_gender.get()
    devotee_idproof = entry_devotee_idproof.get()
    devoteecursor.execute("insert into devotee values(:ed,:dn,:da,:dg,:di)", {'ed': dt.datetime.today(),
                                                                              'dn': devotee_name, 'da': devotee_age,
                                                                              'dg': devotee_gender,
                                                                              'di': devotee_idproof})
    devoteeconn.commit()
    devoteeconn.close()


def devoteesto_userfirstpage():
    devotee_pg.destroy()
    user_first_page.deiconify()


def resetDevotees():
    entry_devotee_name.delete("0", END)
    entry_devotee_age.delete("0", END)
    entry_devotee_gender.delete("0", END)
    entry_devotee_idproof.delete("0", END)


def addDevotees():
    user_first_page.withdraw()
    global devotee_pg
    devotee_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(devotee_pg, image=img3)
    bg_image3.place(x=0, y=0)

    width = 830
    height = 511
    screen_width = devotee_pg.winfo_screenwidth()
    screen_height = devotee_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    devotee_pg.resizable(0, 0)
    devotee_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Label(devotee_pg, text="DEVOTEES MODULE", font=("Showcard Gothic", 20)).place(x=320, y=70)

    global entry_devotee_name
    Label(devotee_pg, text='DEVOTEE NAME :', font=('', 13)).place(x=230, y=140)
    entry_devotee_name = Entry(devotee_pg, font=('', 14))
    entry_devotee_name.place(x=400, y=140)

    global entry_devotee_age
    Label(devotee_pg, text='AGE :', font=('', 13)).place(x=230, y=170)
    entry_devotee_age = Entry(devotee_pg, font=('', 14))
    entry_devotee_age.place(x=400, y=170)

    global entry_devotee_gender
    Label(devotee_pg, text='GENDER :', font=('', 13)).place(x=230, y=200)
    entry_devotee_gender = Entry(devotee_pg, font=('', 14))
    entry_devotee_gender.place(x=400, y=200)

    global entry_devotee_idproof
    Label(devotee_pg, text='ID PROOF :', font=('', 13)).place(x=230, y=230)
    entry_devotee_idproof = Entry(devotee_pg, font=('', 14))
    entry_devotee_idproof.place(x=400, y=230)

    Button(devotee_pg, text='SUBMIT', width=10, font=('', 13), command=submitAddDevotee).place(x=370, y=290)
    Button(devotee_pg, text='CANCEL', width=10, font=('', 13), command=devoteesto_userfirstpage).place(x=270, y=290)
    Button(devotee_pg, text='RESET', width=10, font=('', 13), command=resetDevotees).place(x=470, y=290)
    devotee_pg.mainloop()


# =======================================End of Add Devotees Page======================================================#


# ======================================Display Devotees List==========================================================#
def dispdevoteeto_adminfirstpage():
    dispdovotee_pg.destroy()
    admin_first_page.deiconify()


def displaydevotees():
    admin_first_page.withdraw()
    global dispdovotee_pg
    dispdovotee_pg = Toplevel(root)

    width = 830
    height = 511
    screen_width = dispdovotee_pg.winfo_screenwidth()
    screen_height = dispdovotee_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    dispdovotee_pg.resizable(0, 0)
    dispdovotee_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    devotee_header = ['Visit Date', 'Devotee Name', 'Age', 'Gender', 'Id Proof']

    tree = None
    s = "\Click on header to sort by that column to change width of column drag boundary"

    msg = ttk.Label(dispdovotee_pg, justify="left", anchor="n", padding=(10, 2, 10, 6), text=s)
    msg.pack(fill='x')

    container = ttk.Frame(dispdovotee_pg, width=180)
    container.pack(fill='both', expand=True)

    # create a treeview with dual scrollbars
    tree = ttk.Treeview(dispdovotee_pg, columns=devotee_header, show="headings", height=20)
    vsb = ttk.Scrollbar(dispdovotee_pg, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(dispdovotee_pg, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    for col in devotee_header:
        tree.heading(col, text=col.title(), command=lambda c=col: sortby(tree, c, 0))
        # adjust the column's width to the header string
        tree.column(col, width=tkFont.Font().measure(col.title()))

    conn = cx.connect("system", "system", "XE")
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("select * from devotee")
    car_list = cursor.fetchall()
    for item in car_list:
        tree.insert('', 'end', values=item)
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(str(val).rstrip())
            if tree.column(devotee_header[ix], width=None) < col_w:
                tree.column(devotee_header[ix], width=col_w)

    Button(dispdovotee_pg, text="Back", bg='purple1', fg='white', font=(" ", 15),
           command=dispdevoteeto_adminfirstpage).pack(fill='x')
    dispdovotee_pg.mainloop()


# ====================================End of Display Devotees List=====================================================#


# ============================================Enter Accounts And Payroll Page===========================================#
def reset_account_and_payroll():
    entry_acc_name.delete("0", END)
    entry_contactno.delete("0", END)
    entry_email_id.delete("0", END)


def account_and_payroll_to_userfirstpage():
    AccPayroll_pg.destroy()
    user_first_page.deiconify()


def account_and_payroll():
    user_first_page.withdraw()
    global AccPayroll_pg
    AccPayroll_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(AccPayroll_pg, image=img3)
    bg_image3.place(x=0, y=0)

    screen_width = AccPayroll_pg.winfo_screenwidth()
    screen_height = AccPayroll_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    AccPayroll_pg.resizable(0, 0)
    AccPayroll_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    def accountsandpayroll():
        accountsandpayrollconn = cx.connect("system", "system", "XE")
        accountsandpayrollcursor = accountsandpayrollconn.cursor()
        acc_name = entry_acc_name.get()
        contactno = entry_contactno.get()
        mailid = entry_email_id.get()
        date = dt.datetime.today()
        if v.get() == 1 and v1.get() == 1:
            accountsandpayrollcursor.execute("insert into accountandpayroll values(:apd,:acn,:cno,:mid,:pam,:stat)",
                                             {'apd': date, 'acn': acc_name, 'cno': contactno, 'mid': mailid,
                                              'pam': "CASH", 'stat': "PAYED"})
            accountsandpayrollconn.commit()
            accountsandpayrollconn.close()
        elif v.get() == 1 and v1.get() == 2:
            accountsandpayrollcursor.execute("insert into accountandpayroll values(:apd,:acn,:cno,:mid,:pam,:stat)",
                                             {'apd': date, 'acn': acc_name, 'cno': contactno, 'mid': mailid,
                                              'pam': "CASH", 'stat': "UNPAYED"})
            accountsandpayrollconn.commit()
            accountsandpayrollconn.close()
        elif v.get() == 2 and v1.get() == 1:
            accountsandpayrollcursor.execute("insert into accountandpayroll values(:apd,:acn,:cno,:mid,:pam,:stat)",
                                             {'apd': date,
                                              'acn': acc_name, 'cno': contactno, 'mid': mailid, 'pam': "CHEQUE",
                                              'stat': "PAYED"})
            accountsandpayrollconn.commit()
            accountsandpayrollconn.close()
        else:
            accountsandpayrollcursor.execute("insert into accountandpayroll values(:apd,:acn,:cno,:mid,:pam,:stat)",
                                             {'apd': date, 'acn': acc_name, 'cno': contactno, 'mid': mailid,
                                              'pam': "CHEQUE", 'stat': "UNPAYED"})
            accountsandpayrollconn.commit()
            accountsandpayrollconn.close()

    Label(AccPayroll_pg, text="ACCOUNTS AND PAYROLL\nMODULE", font=("Showcard Gothic", 20)).place(x=250, y=20)

    global entry_acc_name
    Label(AccPayroll_pg, text='NAME ', font=('', 13)).place(x=220, y=115)
    entry_acc_name = Entry(AccPayroll_pg, font=('', 13), width=25)
    entry_acc_name.place(x=350, y=115)

    global entry_contactno
    Label(AccPayroll_pg, text='CONTACT NO ', font=('', 13)).place(x=220, y=150)
    entry_contactno = Entry(AccPayroll_pg, font=('', 13), width=25)
    entry_contactno.place(x=350, y=150)

    global entry_email_id
    Label(AccPayroll_pg, text='EMAIL ID ', font=('', 13)).place(x=220, y=185)
    entry_email_id = Entry(AccPayroll_pg, font=('', 13), width=25)
    entry_email_id.place(x=350, y=185)

    v = IntVar()
    Label(AccPayroll_pg, text="MODE OF \nPAYMENT", font=('', 13)).place(x=220, y=220)
    Radiobutton(AccPayroll_pg, text='CASH', variable=v, value=1, font=('', 13)).place(x=350, y=230)
    Radiobutton(AccPayroll_pg, text='CHEQUE', variable=v, value=2, font=('', 13)).place(x=450, y=230)

    v1 = IntVar()
    Label(AccPayroll_pg, text='STATUS', font=('', 13)).place(x=220, y=275)
    Radiobutton(AccPayroll_pg, text='PAYED', variable=v1, value=1, font=('', 13)).place(x=350, y=275)
    Radiobutton(AccPayroll_pg, text='UNPAYED', variable=v1, value=2, font=('', 13)).place(x=450, y=275)
    Button(AccPayroll_pg, text='SUBMIT', width=12, font=('', 13), command=accountsandpayroll).place(x=340, y=320)
    Button(AccPayroll_pg, text='BACK', font=('', 13), width=12, command=account_and_payroll_to_userfirstpage).place(
        x=230, y=320)
    Button(AccPayroll_pg, text='RESET', width=12, font=('', 13), command=reset_account_and_payroll).place(x=450, y=320)
    AccPayroll_pg.mainloop()


# =====================================End of Accounts And Payroll Page================================================#


# ======================================Inventory Page=================================================================#
def submit_stock():
    stockconn = cx.connect("system", "system", "XE")
    stockcursor = stockconn.cursor()
    stockdate = entry_stockdate.get()
    quantity = entry_qty.get()
    units = entry_unit.get()
    expincome = entry_expincome.get()
    time_string = time.strftime('%H:%M:%S')
    stockcursor.execute("insert into stock values(:stk,:tm,:qty,:uts,:exi)",
                        {'stk': stockdate, 'tm': time_string, 'qty': quantity, 'uts': units, 'exi': expincome})
    stockconn.commit()
    stockconn.close()
    ms.showinfo("Success", "Entry Done")


def inventory_to_userfirstpage():
    inventory_pg.destroy()
    user_first_page.deiconify()


def reset_inventory():
    entry_stockdate.delete("0", END)
    entry_qty.delete("0", END)
    entry_unit.delete("0", END)
    entry_expincome.delete("0", END)


def inventory():
    user_first_page.withdraw()
    global inventory_pg
    inventory_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(inventory_pg, image=img3)
    bg_image3.place(x=0, y=0)

    screen_width = inventory_pg.winfo_screenwidth()
    screen_height = inventory_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    inventory_pg.resizable(0, 0)
    inventory_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Label(inventory_pg, text='INVENTORY MODULE', font=("Showcard Gothic", 20)).place(x=280, y=40)

    global entry_stockdate
    Label(inventory_pg, text='STOCK DATE', font=('', 13)).place(x=180, y=115)
    entry_stockdate = Entry(inventory_pg, font=('', 15))
    entry_stockdate.place(x=360, y=115)

    global entry_qty
    Label(inventory_pg, text='QUANTITY', font=('', 13)).place(x=180, y=150)
    entry_qty = Entry(inventory_pg, font=('', 15))
    entry_qty.place(x=360, y=150)

    global entry_unit
    Label(inventory_pg, text='UNIT', font=('', 13)).place(x=180, y=185)
    entry_unit = Entry(inventory_pg, font=('', 15))
    entry_unit.place(x=360, y=185)

    global entry_expincome
    Label(inventory_pg, text='EXPECTED INCOME', font=('', 13)).place(x=180, y=220)
    entry_expincome = Entry(inventory_pg, font=('', 15))
    entry_expincome.place(x=360, y=220)

    Button(inventory_pg, text='SUBMIT', font=('', 13), width=10, command=submit_stock).place(x=350, y=280)
    Button(inventory_pg, text='BACK', font=('', 13), width=10, command=inventory_to_userfirstpage).place(x=250, y=280)
    Button(inventory_pg, text='RESET', font=('', 13), width=10, command=reset_inventory).place(x=450, y=280)
    inventory_pg.mainloop()


# ==============================End of Inventory Page==================================================================#


# =====================================Display Inventory Page===========================================================#
def dispinvent_to_adminfirstpage():
    dispinvent_pg.destroy()
    admin_first_page.deiconify()


def sortby(tree, col, descending):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))


def displayinventory():
    admin_first_page.withdraw()
    global dispinvent_pg
    dispinvent_pg = Tk()
    width = 830
    height = 510
    screen_width = dispinvent_pg.winfo_screenwidth()
    screen_height = dispinvent_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    dispinvent_pg.resizable(0, 0)
    dispinvent_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    seva_header = ['Stock Date', 'Time Of Entry', 'Quantity', 'Units', 'Expected Income']

    tree = None
    s = "\Click on header to sort by that column to change width of column drag boundary"

    msg = ttk.Label(dispinvent_pg, justify="left", anchor="n", padding=(10, 2, 10, 6), text=s)
    msg.pack(fill='x')

    container = ttk.Frame(dispinvent_pg, width=180)
    container.pack(fill='both', expand=True)

    # create a treeview with dual scrollbars
    tree = ttk.Treeview(dispinvent_pg, columns=seva_header, show="headings", height=20)
    vsb = ttk.Scrollbar(dispinvent_pg, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(dispinvent_pg, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    for col in seva_header:
        tree.heading(col, text=col.title(), command=lambda c=col: sortby(tree, c, 0))
        tree.column(col, width=tkFont.Font().measure(col.title()))

    dispinvent_pgconn = cx.connect("system", "system", "XE")
    dispinvent_pgcursor = dispinvent_pgconn.cursor()
    dispinvent_pgcursor.execute("select * from stock")
    car_list = dispinvent_pgcursor.fetchall()
    dispinvent_pgconn.commit()
    dispinvent_pgconn.close()
    for item in car_list:
        tree.insert('', 'end', values=item)
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(str(val).rstrip())
            if tree.column(seva_header[ix], width=None) < col_w:
                tree.column(seva_header[ix], width=col_w)

    Button(dispinvent_pg, text="Back", bg='purple1', fg='white', font=(" ", 15),
           command=dispinvent_to_adminfirstpage).pack(fill='x')


# ==============================End Of Display of Inventory Page=======================================================#

# =====================================Display Donation Page===========================================================#

def dispdonation_to_adminfirstpage():
    dispdonation_pg.destroy()
    admin_first_page.deiconify()


def displayDonation():
    admin_first_page.withdraw()
    global dispdonation_pg
    dispdonation_pg = Tk()
    width = 830
    height = 510
    screen_width = dispdonation_pg.winfo_screenwidth()
    screen_height = dispdonation_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    dispdonation_pg.resizable(0, 0)
    dispdonation_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))
    donation_header = ['Name', 'Contact no', 'Email Id', 'Payment Mode', 'Status', 'Preferences', 'DateOfRegistration']

    tree = None
    s = "\Click on header to sort by that column to change width of column drag boundary"

    msg = ttk.Label(dispdonation_pg, justify="left", anchor="n", padding=(10, 2, 10, 6), text=s)
    msg.pack(fill='x')

    container = ttk.Frame(dispdonation_pg, width=180)
    container.pack(fill='both', expand=True)

    # create a treeview with dual scrollbars
    tree = ttk.Treeview(dispdonation_pg, columns=donation_header, show="headings", height=20)
    vsb = ttk.Scrollbar(dispdonation_pg, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(dispdonation_pg, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    for col in donation_header:
        tree.heading(col, text=col.title(), command=lambda c=col: sortby(tree, c, 0))
        # adjust the column's width to the header string
        tree.column(col, width=tkFont.Font().measure(col.title()))

    conn = cx.connect("system", "system", "XE")
    cursor = conn.cursor()
    cursor.execute("select * from donation")
    car_list = cursor.fetchall()
    for item in car_list:
        tree.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(str(val).rstrip())
            if tree.column(donation_header[ix], width=None) < col_w:
                tree.column(donation_header[ix], width=col_w)

    Button(dispdonation_pg, text="Back", bg='purple1', fg='white', font=(" ", 15),
           command=dispdonation_to_adminfirstpage).pack(fill='x')


# ==============================End Of Display of Donation Page=======================================================#


# =====================================Display Account And Payroll Page===========================================================#

def dispAccount_to_adminfirstpage():
    dispaccount_pg.destroy()
    admin_first_page.deiconify()


def displayAccount():
    admin_first_page.withdraw()
    global dispaccount_pg
    dispaccount_pg = Tk()
    width = 830
    height = 510
    screen_width = dispaccount_pg.winfo_screenwidth()
    screen_height = dispaccount_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    dispaccount_pg.resizable(0, 0)
    dispaccount_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    account_header = ['Payment Date', 'Account Holder Name', 'Account Number', 'Email Id', 'Pay Mode', 'Status']

    tree = None
    s = "\Click on header to sort by that column to change width of column drag boundary"

    msg = ttk.Label(dispaccount_pg, justify="left", anchor="n", padding=(10, 2, 10, 6), text=s)
    msg.pack(fill='x')

    container = ttk.Frame(dispaccount_pg, width=180)
    container.pack(fill='both', expand=True)

    # create a treeview with dual scrollbars
    tree = ttk.Treeview(dispaccount_pg, columns=account_header, show="headings", height=20)
    vsb = ttk.Scrollbar(dispaccount_pg, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(dispaccount_pg, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    for col in account_header:
        tree.heading(col, text=col.title(), command=lambda c=col: sortby(tree, c, 0))
        # adjust the column's width to the header string
        tree.column(col, width=tkFont.Font().measure(col.title()))

    conn = cx.connect("system", "system", "XE")
    conn.commit()
    cursor = conn.cursor()
    cursor.execute("select * from accountandpayroll")
    car_list = cursor.fetchall()
    for item in car_list:
        tree.insert('', 'end', values=item)
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(str(val).rstrip())
            if tree.column(account_header[ix], width=None) < col_w:
                tree.column(account_header[ix], width=col_w)

    Button(dispaccount_pg, text="Back", bg='purple1', fg='white', font=(" ", 15),
           command=dispAccount_to_adminfirstpage).pack(fill='x')


# ==============================End Of Display of Account And Payroll Page=======================================================#


# =====================================Display Seva Page===========================================================#
def dispSeva_to_adminfirstpage():
    dispseva_pg.destroy()
    admin_first_page.deiconify()


def displaySeva():
    admin_first_page.withdraw()
    global dispseva_pg
    dispseva_pg = Tk()
    width = 830
    height = 510
    screen_width = dispseva_pg.winfo_screenwidth()
    screen_height = dispseva_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    dispseva_pg.resizable(0, 0)
    dispseva_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    seva_header = ['Seva Name', 'Seva Description', 'Duration', 'From Date', 'To Date']

    tree = None
    s = "\Click on header to sort by that column to change width of column drag boundary"

    msg = ttk.Label(dispseva_pg, justify="left", anchor="n", padding=(10, 2, 10, 6), text=s)
    msg.pack(fill='x')

    container = ttk.Frame(dispseva_pg, width=180)
    container.pack(fill='both', expand=True)

    # create a treeview with dual scrollbars
    tree = ttk.Treeview(dispseva_pg, columns=seva_header, show="headings", height=20)
    vsb = ttk.Scrollbar(dispseva_pg, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(dispseva_pg, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew', in_=container)
    vsb.grid(column=1, row=0, sticky='ns', in_=container)
    hsb.grid(column=0, row=1, sticky='ew', in_=container)
    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    for col in seva_header:
        tree.heading(col, text=col.title(), command=lambda c=col: sortby(tree, c, 0))
        # adjust the column's width to the header string
        tree.column(col, width=tkFont.Font().measure(col.title()))

    conn = cx.connect("system", "system", "XE")
    cursor = conn.cursor()
    cursor.execute("select * from seva")
    car_list = cursor.fetchall()
    for item in car_list:
        tree.insert('', 'end', values=item)
        # adjust column's width if necessary to fit each value
        for ix, val in enumerate(item):
            col_w = tkFont.Font().measure(val)
            if tree.column(seva_header[ix], width=None) < col_w:
                tree.column(seva_header[ix], width=col_w)

    Button(dispseva_pg, text="Back", bg='purple1', fg='white', font=(" ", 15), command=dispSeva_to_adminfirstpage).pack(
        fill='x')


# =====================================Donation Page===================================================================#
def paydonation():
    payconn = cx.connect("system", "system", "XE")
    paycursor = payconn.cursor()
    name = entry_name.get()
    cno = entry_amount.get()
    eml = eentry_email_id.get()
    date = dt.datetime.today()
    online = "Online"
    cash = "Cash"
    payed = "Payed"
    unpaied = "Unpaied"
    mrn = "9am to 10am"
    aft = "10am to 11am"
    evn = "11am to 12pm"

    if (v.get() == 1) and (v1.get() == 1) and (v2.get() == 1):
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p,:d)",
                          {'n': name, 'c': cno, 'e': eml, 'm': cash, 's': payed, 'p': mrn, 'd': date})
        payconn.commit()

    if v.get() == 1 and v1.get() == 1 and v2.get() == 2:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': cash, 's': payed, 'p': aft, 'd': date})
        payconn.commit()

    if v.get() == 1 and v1.get() == 1 and v2.get() == 3:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': cash, 's': payed, 'p': evn, 'd': date})
        payconn.commit()

    if v.get() == 1 and v1.get() == 2 and v2.get() == 1:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': cash, 's': unpaied, 'p': mrn, 'd': date})
        payconn.commit()

    if v.get() == 1 and v1.get() == 2 and v2.get() == 2:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': cash, 's': unpaied, 'p': aft, 'd': date})
        payconn.commit()

    if v.get() == 1 and v1.get() == 2 and v2.get() == 3:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': cash, 's': unpaied, 'p': evn, 'd': date})
        payconn.commit()

    if v.get() == 2 and v1.get() == 1 and v2.get() == 1:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': online, 's': payed, 'p': mrn, 'd': date})
        payconn.commit()

    if v.get() == 2 and v1.get() == 1 and v2.get() == 2:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': online, 's': payed, 'p': aft, 'd': date})
        payconn.commit()

    if v.get() == 2 and v1.get() == 1 and v2.get() == 3:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': online, 's': payed, 'p': evn, 'd': date})
        payconn.commit()

    if v.get() == 2 and v1.get() == 2 and v2.get() == 1:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': online, 's': unpaied, 'p': mrn, 'd': date})
        payconn.commit()

    if v.get == 2 and v1.get() == 2 and v2.get() == 2:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': online, 's': unpaied, 'p': aft, 'd': date})
        payconn.commit()
    if v.get() == 2 and v1.get() == 2 and v2.get() == 3:
        paycursor.execute("insert into donation values(:n,:c,:e,:m,:s,:p)",
                          {'n': name, 'c': cno, 'e': eml, 'm': online, 's': unpaied, 'p': evn, 'd': date})
        payconn.commit()

    if (vari1.get() != 1):
        ms.showinfo(" ", "Please agree terms and conditions!!!");


def donationcancellation():
    payconn = cx.connect("system", "system", "XE")
    paycursor = payconn.cursor()
    name = entry_name.get()

    paycursor.execute("delete from donation where devoteename=:k", {'k': name})

    payconn.commit()


def reset_donation():
    entry_name.delete("0", END)
    entry_amount.delete("0", END)
    eentry_email_id.delete("0", tkinter.END)
    vari1 = 0




def donation_to_userfirstpage():
    donation_pg.destroy()
    user_first_page.deiconify()


def donation():
    user_first_page.withdraw()
    global donation_pg
    donation_pg = tkinter.Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = tkinter.Label(donation_pg, image=img3)
    bg_image3.place(x=0, y=0)

    screen_width = donation_pg.winfo_screenwidth()
    screen_height = donation_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    donation_pg.resizable(0, 0)
    donation_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # updation
    tkinter.Label(donation_pg, text="BOOKING DETAILS", font=("Showcard Gothic", 20)).place(x=250, y=20)

    global entry_name
    tkinter.Label(donation_pg, text='NAME :', font=('', 13)).place(x=220, y=95)
    entry_name = tkinter.Entry(donation_pg, font=('', 13), width=25)
    entry_name.place(x=350, y=95)

    global entry_amount
    tkinter.Label(donation_pg, text='CONTACT NO :', font=('', 13)).place(x=220, y=130)
    entry_amount = tkinter.Entry(donation_pg, font=('', 13), width=25)
    entry_amount.place(x=350, y=130)

    global eentry_email_id
    tkinter.Label(donation_pg, text='EMAIL ID :', font=('', 13)).place(x=220, y=165)
    eentry_email_id = tkinter.Entry(donation_pg, font=('', 13), width=25)
    eentry_email_id.place(x=350, y=165)

    global v
    v = tkinter.IntVar()
    tkinter.Label(donation_pg, text="MODE OF \nPAYMENT:", font=('', 13)).place(x=220, y=200)
    tkinter.Radiobutton(donation_pg, text='CASH', variable=v, value=1, font=('', 13)).place(x=350, y=205)
    tkinter.Radiobutton(donation_pg, text='CHEQUE', variable=v, value=2, font=('', 13)).place(x=450, y=205)

    global v1
    v1 = tkinter.IntVar()
    tkinter.Label(donation_pg, text='STATUS:', font=('', 13)).place(x=220, y=255)
    tkinter.Radiobutton(donation_pg, text='PAYED', variable=v1, value=1, font=('', 13)).place(x=350, y=250)
    tkinter.Radiobutton(donation_pg, text='UNPAYED', variable=v1, value=2, font=('', 13)).place(x=450, y=250)

    global v2
    v2 = tkinter.IntVar()
    tkinter.Label(donation_pg, text='PREFERENCES:', font=('', 13)).place(x=220, y=295)
    tkinter.Radiobutton(donation_pg, text='9am to 10am', variable=v2, value=1, font=('', 13)).place(x=355, y=295)

    tkinter.Radiobutton(donation_pg, text='10am to 11am', variable=v2, value=2, font=('', 13)).place(x=355, y=320)

    tkinter.Radiobutton(donation_pg, text='11am to 12pm', variable=v2, value=3, font=('', 13)).place(x=355, y=345)

    global vari1
    vari1 = tkinter.IntVar()
    tkinter.Label(donation_pg, text='Slots once booked cannot be rescheduled', font=('', 13)).place(x=220, y=380)
    Checkbutton(donation_pg, text='Agree', variable=vari1, font=('', 14)).place(x=550, y=370)

    tkinter.Label(donation_pg, text='Cancellation of slots will lead to FINE OF  Rupees 200/- Only',
                  font=('', 13)).place(x=220, y=414)

    tkinter.Button(donation_pg, text='CANCEL SLOT', width=12, font=('', 13), command=donationcancellation).place(x=670,
                                                                                                                 y=410)

    tkinter.Button(donation_pg, text='SUBMIT', width=12, font=('', 13), command=paydonation).place(x=360, y=450)
    tkinter.Button(donation_pg, text='BACK', font=('', 13), width=12, command=donation_to_userfirstpage).place(x=230,
                                                                                                               y=450)

    tkinter.Button(donation_pg, text='RESET', width=12, font=('', 13), command=reset_donation).place(x=490, y=450)

    donation_pg.mainloop()


# ============================================End of Donation module===================================================#


# =============================================Seva Page===============================================================#
def sevasubmit():
    sevaconn = cx.connect("system", "system", "XE")
    sevacursor = sevaconn.cursor()
    seva_name = entry_seva_name.get()
    seva_description = entry_seva_description.get("1.0", END)
    seva_duration = entry_seva_duration.get()
    from_date = entry_from_date.get()
    to_date = entry_to_date.get()
    if var1.get() == 1:
        sevacursor.execute("insert into seva values(:sn,:sd,:sdu,:fd,:td)",
                           {'sn': seva_name, 'sd': seva_description, 'sdu': seva_duration, 'fd': from_date,
                            'td': to_date})
        sevaconn.commit()
        sevaconn.close()
    else:
        ms.showinfo(" ", "Please agree terms and conditions!!!");


def seva_to_userfirstpage():
    seva_pg.destroy()
    user_first_page.deiconify()


def sevareset():
    entry_seva_name.delete("0", END)
    entry_seva_description.delete("1.0", END)
    entry_seva_duration.delete("0", END)
    entry_from_date.delete("0", END)
    entry_to_date.delete("0", END)


def seva():
    user_first_page.withdraw()
    global seva_pg
    seva_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(seva_pg, image=img3)
    bg_image3.place(x=0, y=0)

    screen_width = seva_pg.winfo_screenwidth()
    screen_height = seva_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    seva_pg.resizable(0, 0)
    seva_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    global var1
    var1 = IntVar()
    Label(seva_pg, text="SEVA MODULE", font=("Showcard Gothic", 20)).place(x=350, y=20)

    global entry_seva_name
    Label(seva_pg, text='SEVA NAME :', font=('', 13)).place(x=200, y=75)
    entry_seva_name = Entry(seva_pg, font=('', 14))
    entry_seva_name.place(x=400, y=75)

    global entry_seva_description
    Label(seva_pg, text='DESCRIPTION :', font=('', 13)).place(x=200, y=105)
    entry_seva_description = Text(seva_pg, height=5, width=20)
    entry_seva_description.place(x=400, y=105)

    global entry_seva_duration
    Label(seva_pg, text='DURATION :', font=('', 13)).place(x=200, y=200)
    entry_seva_duration = Entry(seva_pg, font=('', 14))
    entry_seva_duration.place(x=400, y=200)

    global entry_from_date
    Label(seva_pg, text='FROM DATE :', font=('', 13)).place(x=200, y=230)
    entry_from_date = Entry(seva_pg, font=('', 14))
    entry_from_date.place(x=400, y=230)

    global entry_to_date
    Label(seva_pg, text='TO DATE :', font=('', 13)).place(x=200, y=260)
    entry_to_date = Entry(seva_pg, font=('', 14))
    entry_to_date.place(x=400, y=260)

    Label(seva_pg, text='I PERSONALLY AGREE TO ' + "\n" + 'ALL TERMS AND CONDITIONS APPLIED', font=('', 13)).place(x=70,
                                                                                                                   y=290)
    Checkbutton(seva_pg, text='Agree', variable=var1, font=('', 14)).place(x=400, y=295)
    Button(seva_pg, text='SUBMIT', width=10, font=('', 13), command=sevasubmit).place(x=370, y=360)
    Button(seva_pg, text='CANCEL', width=10, font=('', 13), command=seva_to_userfirstpage).place(x=270, y=360)
    Button(seva_pg, text='RESET', width=10, font=('', 13), command=sevareset).place(x=470, y=360)
    seva_pg.mainloop()


# =========================================End of Seva Page============================================================#


# ========================================Add User Page================================================================#
def createaccount():
    createaccountconn = cx.connect("system", "system", "XE")
    createaccountcursor = createaccountconn.cursor()
    firstname = entry_first_name.get()
    lastname = entry_last_name.get()
    dateofbirth = entry_date_of_birth.get()
    gender = entry_gender.get()
    uname = entry_username.get()
    upassword = entry_user_password.get()
    address = entry_address.get()
    mobno = entry_mob_no.get()
    city = entry_city.get()
    pincode = entry_pincode.get()
    state = entry_state.get()
    cntry = entry_country.get()
    adharno = entry_aadharno.get()
    date = dt.datetime.today()
    createaccountcursor.execute(
        "insert into user_registration values(:acd,:fn,:ln,:dob,:g,:un,:up,:ad,:mn,:ci,:pin,:st,:co,:adn)",
        {'acd': date, 'fn': firstname, 'ln': lastname, 'dob': dateofbirth, 'g': gender, 'un': uname, 'up': upassword,
         'ad': address, 'mn': mobno, 'ci': city, 'pin': pincode, 'st': state, 'co': cntry, 'adn': adharno})
    createaccountconn.commit()
    createaccountconn.close()


def adduser_to_adminfirstpage():
    adduser_pg.destroy()
    admin_first_page.deiconify()


def adduser():
    admin_first_page.withdraw()
    global adduser_pg
    adduser_pg = Toplevel(root)

    img3 = ImageTk.PhotoImage(Image.open("temple1.png"))
    bg_image3 = Label(adduser_pg, image=img3)
    bg_image3.place(x=0, y=0)

    screen_width = adduser_pg.winfo_screenwidth()
    screen_height = adduser_pg.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    adduser_pg.resizable(0, 0)
    adduser_pg.geometry("%dx%d+%d+%d" % (width, height, x, y))

    Frame(adduser_pg, padx=10, pady=10)

    global entry_first_name
    Label(adduser_pg, text='First Name: ', font=('', 15), pady=5, padx=3).grid(sticky=W)
    entry_first_name = Entry(adduser_pg, bd=3, font=('', 15))
    entry_first_name.grid(row=0, column=1)

    global entry_last_name
    Label(adduser_pg, text='Last Name: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=0, column=3)
    entry_last_name = Entry(adduser_pg, bd=3, font=('', 15))
    entry_last_name.grid(row=0, column=4)

    global entry_date_of_birth
    Label(adduser_pg, text='Date Of Birth: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=1, column=0)
    entry_date_of_birth = Entry(adduser_pg, bd=3, font=('', 15))
    entry_date_of_birth.grid(row=1, column=1)

    global entry_gender
    Label(adduser_pg, text='Gender: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=1, column=3)
    entry_gender = Entry(adduser_pg, bd=3, font=('', 15))
    entry_gender.grid(row=1, column=4)

    global entry_username
    Label(adduser_pg, text='Username: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=2, column=0)
    entry_username = Entry(adduser_pg, bd=3, font=('', 15))
    entry_username.grid(row=2, column=1)

    global entry_user_password
    Label(adduser_pg, text='Password: ', font=('', 15), pady=5, padx=5).grid(sticky=W, row=3, column=0)
    entry_user_password = Entry(adduser_pg, bd=3, font=('', 15), show='*')
    entry_user_password.grid(row=3, column=1)

    global entry_address
    Label(adduser_pg, text='Address: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=4, column=0)
    entry_address = Entry(adduser_pg, bd=3, font=('', 15))
    entry_address.grid(row=4, column=1)

    global entry_mob_no
    Label(adduser_pg, text='Mobile No: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=4, column=3)
    entry_mob_no = Entry(adduser_pg, bd=3, font=('', 15))
    entry_mob_no.grid(row=4, column=4)

    global entry_city
    Label(adduser_pg, text='City: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=5, column=0)
    entry_city = Entry(adduser_pg, bd=3, font=('', 15))
    entry_city.grid(row=5, column=1)

    global entry_pincode
    Label(adduser_pg, text='Pincode: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=5, column=3)
    entry_pincode = Entry(adduser_pg, bd=3, font=('', 15))
    entry_pincode.grid(row=5, column=4)

    global entry_state
    Label(adduser_pg, text='State: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=6, column=0)
    entry_state = Entry(adduser_pg, bd=3, font=('', 15))
    entry_state.grid(row=6, column=1)

    global entry_country
    Label(adduser_pg, text='Country: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=6, column=3)
    entry_country = Entry(adduser_pg, bd=3, font=('', 15))
    entry_country.grid(row=6, column=4)

    global entry_aadharno
    Label(adduser_pg, text='Adhar No: ', font=('', 15), pady=5, padx=3).grid(sticky=W, row=7, column=0)
    entry_aadharno = Entry(adduser_pg, bd=3, font=('', 15))
    entry_aadharno.grid(row=7, column=1)

    Button(adduser_pg, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=createaccount).grid(column=1)
    Button(adduser_pg, text='Back', bd=3, font=('', 15), padx=5, pady=5, command=adduser_to_adminfirstpage).grid(row=9,
                                                                                                                 column=2)
    adduser_pg.mainloop()


# =======================================End of User Page==============================================================#


main_form()
root.mainloop()
