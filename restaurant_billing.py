import tkinter as tk
import data as dk
from tkinter import ttk
from datetime import datetime
import random
from PIL import ImageTk, Image


selected_items = []
r = random.randint(10000,999999)


# Showing the list of deleted items
def saldellist(tree):
    tree.delete(*tree.get_children())
    rows = dk.get_all_deleted()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


# View deleted bills
def deleted_bills(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    tree = ttk.Treeview(t)
    b = tk.Button(t, text="SHOW", command=lambda: saldellist(tree), fg="white", bg="#1966ff")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="USER ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor="center")  
    tree.column("one", anchor="center")  
    tree.column("two", anchor="center")
    tree.column("three", anchor="center")
    b.pack()
    tree.pack()
    return t


# Check and delete bill
def delete_bill(ref):
    if ref and ref.isnumeric():
        dk.delete_bill_db(int(ref))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Showing the list of sales for specific user
def sal_del(tree, username):
    tree.delete(*tree.get_children())
    rows = dk.get_all_sales_related(int(username))
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[2], i[3]))


# Remove bill
def remove_bill(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    l = tk.Label(t, text="ENTER REFNO:", fg="white", bg="#660066")
    e = tk.Entry(t)
    b = tk.Button(t, text="DELETE", fg="white", bg="#1966ff", command= lambda: delete_bill(e.get()))
    l.pack()
    e.pack()
    b.pack()
    tree = ttk.Treeview(t)
    tree["columns"] = ("two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor="center")  
    tree.column("two", anchor="center")
    tree.column("three", anchor="center")
    b = tk.Button(t, text="SHOW", command=lambda: sal_del(tree, username), fg="white", bg="#1966ff")
    b.pack()
    tree.pack()
    return t


# Check and edit price
def ck_and_edit_price(item, price):
    if item and price.isnumeric():
        dk.update_price(item, int(price))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Change price of item
def change_price_of_item(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    rows = dk.get_items()
    options = []
    for i in rows:
        options.append(i[1])
    clicked = tk.StringVar()
    clicked.set(options[0])
    drop = tk.OptionMenu(t, clicked, *options)
    l = tk.Label(t, text="ENTER NEW PRICE:", fg="white", bg="#660066")
    c = tk.Entry(t)
    b = tk.Button(t, text="UPDATE PRICE", command= lambda: ck_and_edit_price(clicked.get(), c.get()), fg="white", bg="#1966ff")
    drop.pack()
    l.pack()
    c.pack()
    b.pack()
    return t


# Check and delete item
def exec_del_item(iid):
    if iid.isnumeric():
        dk.remove_item(int(iid))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Delete item
def delete_item(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    l1 = tk.Label(t, text="Enter item id: ", fg="white", bg="#660066")
    e1 = tk.Entry(t)    
    b = tk.Button(t, text="REMOVE", command= lambda: exec_del_item(e1.get()), fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    b.grid(row=2, column=1)
    return t


# Check and delete user
def exec_del_user(uid):
    if uid.isnumeric():
        dk.remove_user(int(uid))
        popup("DONE")
    else:
        popup("ENTER VALID DETAILS")


# Delete user
def delete_user(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    l1 = tk.Label(t, text="Enter user id: ", fg="white", bg="#660066")
    e1 = tk.Entry(t)    
    b = tk.Button(t, text="REMOVE", command= lambda: exec_del_user(e1.get()), fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    b.grid(row=2, column=1)
    return t


# Validate and add item
def ck_and_add_item(itemid, name, cost):
    row = dk.ck_item_exists(itemid)
    if name and itemid.isnumeric() and cost.isnumeric() and row == None:
        dk.add_item_to_db_data(int(itemid), name, int(cost))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Add items to database
def add_item_to_db(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    l1 = tk.Label(t, text="Enter item id: ", fg="white", bg="#660066")
    e1 = tk.Entry(t)
    l2 = tk.Label(t, text="Enter name: ", fg="white", bg="#660066")
    e2 = tk.Entry(t)
    l3 = tk.Label(t, text="Enter cost: ", fg="white", bg="#660066")
    e3 = tk.Entry(t)
    b = tk.Button(t, text="ADD", command= lambda:ck_and_add_item(e1.get(),e2.get(),e3.get()),
     fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    b.grid(row=4, column=1)
    return t


# Showing the list of items
def show_item_list(tree):
    tree.delete(*tree.get_children())
    rows = dk.get_items()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2]))


# List items
def list_items(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    tree = ttk.Treeview(t)
    b = tk.Button(t, text="SHOW", command=lambda: show_item_list(tree), fg="white", bg="#1966ff")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="ID")
    tree.heading("one", text="NAME")
    tree.heading("two", text="COST")
    tree.column("#0", anchor="center")  
    tree.column("one", anchor="center")  
    tree.column("two", anchor="center")
    b.pack()
    tree.pack()
    return t


# Validate and add user
def ck_and_add(username, name, password, phno):
    row = dk.get_user_details(username)
    if name and password and username.isnumeric() and phno.isnumeric() and row == None:
        dk.add_user_to_db(int(username), name, password, int(phno))
        popup("DONE")
    else:
        popup("PLEASE ENTER VALID DETAILS")


# Add user
def add_user(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    l1 = tk.Label(t, text="Enter user id: ", fg="white", bg="#660066")
    e1 = tk.Entry(t)
    l2 = tk.Label(t, text="Enter name: ", fg="white", bg="#660066")
    e2 = tk.Entry(t)
    l3 = tk.Label(t, text="Enter user password: ", fg="white", bg="#660066")
    e3 = tk.Entry(t)
    l4 = tk.Label(t, text="Enter PHNO: ", fg="white", bg="#660066")
    e4 = tk.Entry(t)
    b = tk.Button(t, text="ADD", command= lambda:ck_and_add(e1.get(),e2.get(),e3.get(),e4.get()),
     fg="white", bg="#1966ff")
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    l3.grid(row=2, column=0)
    e3.grid(row=2, column=1)
    l4.grid(row=3, column=0)
    e4.grid(row=3, column=1)
    b.grid(row=4, column=1)
    return t


# Showing the list of sales
def sal(tree):
    tree.delete(*tree.get_children())
    rows = dk.get_all_sales()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3]))


# List sales
def sales(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    tree = ttk.Treeview(t)
    b = tk.Button(t, text="SHOW", command=lambda: sal(tree), fg="white", bg="#1966ff")
    tree["columns"] = ("one", "two", "three")
    tree.heading("#0", text="DATE/TIME")
    tree.heading("one", text="USER ID")
    tree.heading("two", text="AMOUNT")
    tree.heading("three", text="REFNO")
    tree.column("#0", anchor="center")  
    tree.column("one", anchor="center")  
    tree.column("two", anchor="center")
    tree.column("three", anchor="center")
    b.pack()
    tree.pack()
    return t


# Showing the list of employees
def s(tree):
    tree.delete(*tree.get_children())
    rows = dk.get_all_employees()
    for i in rows:
        tree.insert("", 0, text=i[0], values=(i[1], i[3]))


#List employees
def list_emp(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    tree = ttk.Treeview(t)
    b = tk.Button(t, text="SHOW", command=lambda: s(tree), fg="white", bg="#1966ff")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="ID")
    tree.heading("one", text="NAME")
    tree.heading("two", text="PHNO")
    tree.column("#0", anchor="center")  
    tree.column("one", anchor="center")  
    tree.column("two", anchor="center")
    b.pack()
    tree.pack()
    return t


# Function for resetting the bill
def resetf():
    global selected_items
    global r
    selected_items.clear()
    r = random.randint(10000,999999)



# Print/Show the bill
def get_bill(username):
    cost = 0
    items = []
    global selected_items
    for i in selected_items:
        cost = cost + int(i[2])
        items.append(i[0])
    tax = round(cost * 0.2, 2)
    service = round(cost/99, 2)
    total_cost = round(cost+tax+service)
    t = tk.Toplevel()
    t.geometry("350x700")
    t.title("BILL")
    t.configure(bg="#91f26e")
    date = tk.Label(t, text="DATE: "+datetime.now().strftime("%d-%m-%Y"), fg="black", bg="#91f26e")
    time = tk.Label(t, text="TIME: "+datetime.now().strftime("%H:%M"), fg="black", bg="#91f26e")
    ref = tk.Label(t, text="REF NO: "+str(r), fg="black", bg="#91f26e")
    emp = tk.Label(t, text="USER ID: "+str(username), fg="black", bg="#91f26e")
    costl = tk.Label(t, text="COST: "+str(cost), fg="black", bg="#91f26e")
    taxl = tk.Label(t, text="TAX: "+str(tax), fg="black", bg="#91f26e")
    servicel = tk.Label(t, text="SERVICE CHARGES: "+str(service), fg="black", bg="#91f26e")
    total_costl = tk.Label(t, text="TOTAL COST: "+str(total_cost), fg="black", bg="#91f26e")
    date.pack()
    time.pack()
    ref.pack()
    emp.pack()
    costl.pack()
    taxl.pack()
    servicel.pack()
    total_costl.pack()
    tk.Label(t, text="ITEMS:", fg="black", bg="#91f26e").pack()
    for it in range(len(selected_items)):
        tk.Label(t, text=selected_items[it][0] + "( X "+str(selected_items[it][1])+" )", fg="black", bg="#91f26e").pack()
    if  total_cost:
        dk.store(datetime.now(), username, total_cost, r)
    return t


# Add items to the bill
def add_item(item, itemno):
    cost = dk.get_cost(item)
    selected_items.append((item, itemno, cost))
    return
 

# Show the various items added to the bill when refresh is clicked
def two(tree):
    tree.delete(*tree.get_children())
    for row in selected_items:
        tree.insert("", 0, text=row[0], values=(row[1], row[2]))


# Show the various items added to the bill
def show_items(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    tree = ttk.Treeview(t)
    b = tk.Button(t, text="REFRESH", command=lambda: two(tree), fg="white", bg="#1966ff")
    b2 = tk.Button(t, text="SUBMIT", command=lambda: get_bill(username), fg="white", bg="#1966ff")
    reset = tk.Button(t, text="RESET", command= lambda: resetf(), fg="white", bg="#1966ff")
    tree["columns"] = ("one", "two")
    tree.heading("#0", text="NAME")
    tree.heading("one", text="NO")
    tree.heading("two", text="COST")
    tree.column("#0", anchor="center")  
    tree.column("one", anchor="center")  
    tree.column("two", anchor="center")  
    b.pack()
    b2.pack()
    reset.pack()
    tree.pack()
    return t


# Billing section 
def bill(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    rows = dk.get_items()
    options = []
    for i in rows:
        options.append(i[1])
    clicked = tk.StringVar()
    clicked.set(options[0])
    cl = tk.IntVar()
    cl.set(1) 
    drop = tk.OptionMenu(t, clicked, *options)
    l = tk.Label(t, text="SELECT QUANTITY:", fg="white", bg="#660066")
    q = tk.OptionMenu(t, cl, 1,2,3,4,5,6,7,8,9)
    b = tk.Button(t, text="ADD", command= lambda: add_item(clicked.get(), cl.get()), fg="white", bg="#1966ff")
    reset = tk.Button(t, text="RESET", command= lambda: resetf(), fg="white", bg="#1966ff")
    drop.pack()
    l.pack()
    q.pack()
    b.pack()
    reset.pack()
    return t


# Employee details
def user_details(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    data = dk.get_user_details(int(username))
    lname = tk.Label(t, text="NAME: "+data[1], fg="white", bg="#660066")
    lid = tk.Label(t, text="ID: "+str(data[0]), fg="white", bg="#660066")
    lphno =tk.Label(t, text="PHNO: "+str(data[2]), fg="white", bg="#660066")
    lname.config(font=("Courier", 34))
    lid.config(font=("Courier", 34))
    lphno.config(font=("Courier", 34))
    lname.pack()
    lid.pack()
    lphno.pack()
    tempimg = Image.open(r"user_logo.png")
    tempimg = tempimg.resize((300, 300), Image.ANTIALIAS)
    tempimg = ImageTk.PhotoImage(tempimg)
    panel = tk.Label(t, image = tempimg , bg="#660066")
    panel.photo = tempimg
    panel.place(x = 450, y = 200 , width=300, height=550)
    return t


# Admin details
def admin_details(tab_main, username):
    t = tk.Frame(tab_main, background="#660066")
    data = dk.get_admin_details(int(username))
    lname = tk.Label(t, text="NAME: "+data[1], fg="white", bg="#660066")
    lid = tk.Label(t, text="ID: "+str(data[0]), fg="white", bg="#660066")
    lphno = tk.Label(t, text="PHNO: "+str(data[2]), fg="white", bg="#660066")
    lname.config(font=("Courier", 44))
    lid.config(font=("Courier", 44))
    lphno.config(font=("Courier", 44))
    lname.pack()
    lid.pack()
    lphno.pack()
    tempimg = Image.open(r"admin_logo.jpg")
    tempimg = tempimg.resize((300, 300), Image.ANTIALIAS)
    tempimg = ImageTk.PhotoImage(tempimg)
    panel = tk.Label(t, image = tempimg , bg="#660066")
    panel.photo = tempimg
    panel.place(x = 450, y = 200 , width=300, height=550)
    #panel.pack()
    #panel.grid(pady=20)
    return t


# POPUP for displaying errors
def popup(msg):
    pop = tk.Toplevel()
    pop.geometry("200x60")
    pop.title("MESSAGE")
    pop.configure(bg="#660066")
    l = tk.Label(pop, text=msg, fg="white", bg="#660066")
    exitb = tk.Button(pop, text="OK", fg="white", bg="#1966ff", command= lambda: pop.destroy())
    l.pack()
    exitb.pack()


# Employee dashboard
def ud(username):
    ud = tk.Toplevel()
    ud.geometry("700x500")
    ud.title("USER DASH")
    ud.configure(bg="#660066")
    tab_main = ttk.Notebook(ud)
    t1 = user_details(tab_main, username)
    t2 = bill(tab_main, username)
    t3 = show_items(tab_main, username)
    t4 = remove_bill(tab_main, username)
    tab_main.add(t1, text="USER DETAILS")
    tab_main.add(t2, text="BILLING")
    tab_main.add(t3, text="VIEW BILL")
    tab_main.add(t4, text="REMOVE BILL")
    tab_main.pack(expand=1, fill='both')


# Admin dashboard
def ad(username):
    ad = tk.Toplevel()
    ad.geometry("900x700")
    ad.title("ADMIN DASH")
    ad.configure(bg="#660066")
    tab_main = ttk.Notebook(ad)
    t1 = admin_details(tab_main, username)
    t2 = list_emp(tab_main, username)
    t3 = sales(tab_main, username)
    t4 = add_user(tab_main, username)
    t5 = list_items(tab_main, username)
    t6 = add_item_to_db(tab_main, username)
    t7 = delete_user(tab_main, username)
    t8 = delete_item(tab_main, username)
    t9 = change_price_of_item(tab_main, username)
    t10 = deleted_bills(tab_main, username)
    tab_main.add(t1, text="ADMIN DETAILS")
    tab_main.add(t2, text="USER DETAILS")
    tab_main.add(t3, text="SALES")
    tab_main.add(t4, text="ADD USER")
    tab_main.add(t5, text="SHOW ITEMS")
    tab_main.add(t6, text="ADD ITEM")
    tab_main.add(t7, text="DELETE USER")
    tab_main.add(t8, text="DELETE ITEM")
    tab_main.add(t9, text="CHANGE PRICE")
    tab_main.add(t10, text="DELETED BILLS")
    tab_main.pack(expand=1, fill='both')


# Employee authentication
def user_auth(username, password):
    if username and password and username.isnumeric():
        if dk.ck_details_emp(int(username), password):
            ud(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


# Admin authentication
def admin_auth(username, password):
    if username and password and username.isnumeric():
        if dk.ck_details_admin(int(username), password):
            ad(username)
        else:
            popup("ERROR WRONG DETAILS")
    else:
        popup("ERROR WRONG DETAILS")


# Employee login
def user_login():
    ul = tk.Toplevel()
    ul.geometry("250x100")
    ul.title("USER LOGIN")
    ul.configure(bg="#660066")
    l1= tk.Label(ul, text="ENTER EID: ", fg="white", bg="#660066")
    e1= tk.Entry(ul)
    l2= tk.Label(ul, text="ENTER PASSWORD: ", fg="white", bg="#660066")
    e2= tk.Entry(ul, show="*")
    sb= tk.Button(ul, text= "LOGIN", fg="white", bg="#1966ff", command= lambda: user_auth(e1.get(),e2.get()))
    l1.grid(row=0, column=0)
    e1.grid(row=0, column=1)
    l2.grid(row=1, column=0)
    e2.grid(row=1, column=1)
    sb.grid(row=2, column=1)


# Admin login
def admin_login():
    al = tk.Toplevel()
    al.geometry("250x100")
    al.title("ADMIN LOGIN")
    al.configure(bg="#660066")
    l1= tk.Label(al, text="ENTER AID: ", fg="white", bg="#660066")
    e1= tk.Entry(al)
    l2= tk.Label(al, text="ENTER PASSWORD: ", fg="white", bg="#660066")
    e2= tk.Entry(al, show="*")
    sb= tk.Button(al, text= "LOGIN", fg="white", bg="#1966ff", command= lambda: admin_auth(e1.get(),e2.get()))
    l1.grid(row=1, column=0)
    e1.grid(row=1, column=1)
    l2.grid(row=2, column=0)
    e2.grid(row=2, column=1)
    sb.grid(row=3, column=1)


# Initial setup 
root = tk.Tk()
root.geometry("1000x700")
root.title("Restaurant Billing System")
root.configure(bg="#ffff00")
# =============================================================================
# adminB = tk.Button(root, text="ADMIN", fg="white", bg="#1966ff", padx=16, 
# pady=8, bd=7,relief="groove", width=10, anchor="center", command= admin_login)
# userB = tk.Button(root, text="USER", fg="white", bg="#1966ff", padx=16, 
# pady=8, bd=7,relief="groove", width=10, anchor="center", command= user_login)
# adminB.grid(row= 0, column = 0)
# userB.grid(row= 0, column = 1)
# =============================================================================
 
btn_f = tk.Frame(root,bd=7,bg="#730664",relief="groove")      
btn_f.place(x=0,y=0, height=150) 
btn_f.pack(fill=tk.X)


admin_btn=tk.Button(btn_f,command=admin_login,text="Admin",bd=7,bg="#1966ff",fg="white",pady=20,width=10,font="arial 15 bold")
admin_btn.grid(row = 0 ,column=0,padx=20,pady=20)
#admin_btn.place(x=20,y=20,width=150,height=100)                          


tempimg = Image.open(r"admin_logo.jpg")
tempimg = tempimg.resize((100, 100), Image.ANTIALIAS)
tempimg = ImageTk.PhotoImage(tempimg)
panel = tk.Label(btn_f, image = tempimg , bg="#660066")
panel.photo = tempimg
panel.grid(row = 0 ,column=1,padx=40,pady=20)


user_btn=tk.Button(btn_f,command=user_login,text="User",bd=7,bg="#1966ff",fg="white",pady=20,width=10,font="arial 15 bold")
user_btn.grid(row=0,column=2,padx=20,pady=20)  
#user_btn.place(x=10,y=20,width=150,height=100) 


tempimg = Image.open(r"user_logo.png")
tempimg = tempimg.resize((100, 100), Image.ANTIALIAS)
tempimg = ImageTk.PhotoImage(tempimg)
panel = tk.Label(btn_f, image = tempimg , bg="#660066")
panel.photo = tempimg
panel.grid(row = 0 ,column=3,padx=40,pady=20)


DBMS = tk.Label(btn_f, text="DBMS MINI PROJECT", relief="groove",font="arial 30 bold" , fg="white", bg="#660066").grid(row = 0 ,column=4,padx=40)


tempimg = Image.open(r"restaurent logo.jpg")
tempimg = tempimg.resize((1000, 600), Image.ANTIALIAS)
tempimg = ImageTk.PhotoImage(tempimg)
panel = tk.Label(root, image = tempimg , bg="white")
panel.photo = tempimg
panel.place(x = 0, y = 0 , width=300, height=550)
 
panel.pack(side = "left", fill = "x", expand = "yes")

root.mainloop()