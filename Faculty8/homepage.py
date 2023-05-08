from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from patientDb import Patient_Database
from staff_db import Staff_Database
from meds_db import Meds_Database
from equipmentDB import Equipment_Database

import os

root = Tk()
root.config(highlightthickness=0, background="#DFEEED")

window_width = 1250
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.overrideredirect(True)

#Exit Form
def exitForm():
    root.withdraw() 
    root.destroy() 

exitLogo = Canvas(root, width=30, height=30, highlightthickness=0) 
exitLogo.pack()
imgExitLogo = PhotoImage(file='images//exit.png')
exitLogo.create_image(15, 15, image=imgExitLogo, anchor=CENTER)
exitLogo.configure(background='#DFEEED', cursor="hand2")
exitLogo.place(relx=0.97, rely=0.009)
exitLogo.bind("<Button-1>", lambda event: exitForm())

sidebar_frame = Frame(root, bg="#FBF0D7")
sidebar_frame.place(relx=0, rely=0, relheight=1, relwidth=0.14)

# sidebar logo
cvsbrLogo = Canvas(root, width=100, height=80, highlightthickness=0) 
cvsbrLogo.pack()
imgsbrLogo = PhotoImage(file='images//sbrLogo.png')
cvsbrLogo.create_image(48, 44, image=imgsbrLogo, anchor=CENTER)
cvsbrLogo.configure(background='#FBF0D7')
cvsbrLogo.place(relx=0.03, rely=0.043)

# home icon/button
cvHomeIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvHomeIC.pack()
imgHome = PhotoImage(file='images//home2.png')
cvHomeIC.create_image(25, 25, image=imgHome, anchor=CENTER)
cvHomeIC.configure(background='#FBF0D7')
cvHomeIC.place(relx=0.0069, rely=0.17)

home_label = Label(root, text="Home", bg="#FBF0D7", fg="#1E3037")
home_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
home_label.place(relx=0.07, rely=0.2, anchor=CENTER)

# patient icon/button
def ptntBtn():
    root.withdraw() 
    os.system('python patient.py')
    root.destroy() 

cvPtntIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvPtntIC.pack()
imgPtnt = PhotoImage(file='images//patient.png')
cvPtntIC.create_image(25, 25, image=imgPtnt, anchor=CENTER)
cvPtntIC.configure(background='#FBF0D7')
cvPtntIC.place(relx=0.0069, rely=0.27)

patient_label = Label(root, text="Patient", bg="#FBF0D7", fg="#497687")
patient_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
patient_label.place(relx=0.071, rely=0.3, anchor=CENTER)
patient_label.bind("<Button-1>", lambda event: ptntBtn())

# staff icon/button
def staffBtn():
    root.withdraw() 
    os.system('python staff.py')
    root.destroy() 

cvStaffIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvStaffIC.pack()
imgStaff = PhotoImage(file='images//staff.png')
cvStaffIC.create_image(25, 25, image=imgStaff, anchor=CENTER)
cvStaffIC.configure(background='#FBF0D7')
cvStaffIC.place(relx=0.0069, rely=0.37)

staff_label = Label(root, text="Staff", bg="#FBF0D7", fg="#497687")
staff_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
staff_label.place(relx=0.0648, rely=0.4, anchor=CENTER)
staff_label.bind("<Button-1>", lambda event: staffBtn())

# inventory icon/button
def invBtn():
    root.withdraw() 
    os.system('python inventory.py')
    root.destroy() 

cvinventoryIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvinventoryIC.pack()
imgInv = PhotoImage(file='images//inventory.png')
cvinventoryIC.create_image(25, 25, image=imgInv, anchor=CENTER)
cvinventoryIC.configure(background='#FBF0D7') 
cvinventoryIC.place(relx=0.007, rely=0.47)

inventory_label = Label(root, text="Inventory", bg="#FBF0D7", fg="#497687")
inventory_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
inventory_label.place(relx=0.078, rely=0.5, anchor=CENTER)
inventory_label.bind("<Button-1>", lambda event: invBtn())

# logout icon/button
def logoutBtn():
    root.withdraw() 
    os.system('python login_admin.py')
    root.destroy() 

cvLogoutIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvLogoutIC.pack()
imgLogout = PhotoImage(file='images//logout.png')
cvLogoutIC.create_image(25, 25, image=imgLogout, anchor=CENTER)
cvLogoutIC.configure(background='#FBF0D7') 
cvLogoutIC.place(relx=0.009, rely=0.88)

logout_label = Label(root, text="Logout", bg="#FBF0D7", fg="#497687")
logout_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
logout_label.place(relx=0.065, rely=0.91, anchor=CENTER) 
logout_label.bind("<Button-1>", lambda event: logoutBtn())

# HOVER EFFECTS 
def txtEnter(e):
    e.widget.config(font=("Microsoft JhengHei", 11, "bold"), fg="#b12a2a")

def txtLeave(e):
    e.widget.config(font=("Microsoft JhengHei", 10, "bold"), fg="#274B58")

#registered patient
regPtsPan = Frame(root, bg="#F4E7CA")
regPtsPan.place(x=707, y=37, width=500, height=210)
regPtsLabel = Label(regPtsPan, text="Registered Patients", font=("Microsoft JhengHei", 13, "bold"), 
              bg="#F4E7CA", fg="#497687")
regPtsLabel.place(relx=0.23, rely=0.16, anchor="center")

regLink = Label(regPtsPan, text="「View Patients」", font=("Microsoft JhengHei", 10, "bold"), 
              bg="#F4E7CA", fg="#274B58", cursor="hand2")
regLink.place(relx=0.83, rely=0.83, anchor="center")
regLink.bind("<Button-1>", lambda event: ptntBtn())
regLink.bind("<Enter>", txtEnter)
regLink.bind("<Leave>", txtLeave)


#staff count
staffPanel = Frame(root, bg="#FBF0D7")
staffPanel.place(x=200, y=37, width=500, height=210)
staffPLab = Label(staffPanel, text="Registered Staffs", font=("Microsoft JhengHei", 13, "bold"), 
              bg="#FBF0D7", fg="#497687")
staffPLab.place(relx=0.2, rely=0.16, anchor="center")

StaffLink = Label(staffPanel, text="「View Staffs」", font=("Microsoft JhengHei", 10, "bold"), 
              bg="#FBF0D7", fg="#274B58", cursor="hand2")
StaffLink.place(relx=0.83, rely=0.83, anchor="center")
StaffLink.bind("<Button-1>", lambda event: staffBtn())
StaffLink.bind("<Enter>", txtEnter)
StaffLink.bind("<Leave>", txtLeave)


#Available medicines
avlMedsPan = Frame(root, bg="#FBF0D7")
avlMedsPan.place(x=707, y=255, width=500, height=210)
avlMedsLab = Label(avlMedsPan, text="Available Medicines", font=("Microsoft JhengHei", 13, "bold"), 
              bg="#FBF0D7", fg="#497687")
avlMedsLab.place(relx=0.23, rely=0.16, anchor="center")
avlMedsLink = Label(avlMedsPan, text="「View Inventory」", font=("Microsoft JhengHei", 10, "bold"), 
              bg="#FBF0D7", fg="#274B58", cursor="hand2")
avlMedsLink.place(relx=0.83, rely=0.83, anchor="center")
avlMedsLink.bind("<Button-1>", lambda event: invBtn())
avlMedsLink.bind("<Enter>", txtEnter)
avlMedsLink.bind("<Leave>", txtLeave)

#Available equips
avlEqpsPan = Frame(root, bg="#F4E7CA")
avlEqpsPan.place(x=200, y=255, width=500, height=210)
avlEqpsLab = Label(avlEqpsPan, text="Available Equipments", font=("Microsoft JhengHei", 13, "bold"), 
              bg="#F4E7CA", fg="#497687")
avlEqpsLab.place(relx=0.23, rely=0.16, anchor="center")
avlEqpsLink = Label(avlEqpsPan, text="「View Inventory」", font=("Microsoft JhengHei", 10, "bold"), 
              bg="#F4E7CA", fg="#274B58", cursor="hand2")
avlEqpsLink.place(relx=0.83, rely=0.83, anchor="center")
avlEqpsLink.bind("<Button-1>", lambda event: invBtn())
avlEqpsLink.bind("<Enter>", txtEnter)
avlEqpsLink.bind("<Leave>", txtLeave)

#FOR STAFF COUNT
dbStaff = Staff_Database("staff.db")

name= StringVar()
contact= StringVar()
address= StringVar()
username= StringVar()
password= StringVar()
sexCmBox = Combobox(root, font=("Microsoft JhengHei", 11), 
                            values=["Male", "Female"], width=30, state="readonly")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    contact.set(row[2])
    address.set(row[3])
    sexCmBox.set(row[4])
    username.set(row[5])
    password.set(row[6])

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=2)
tv.heading("2", text="Name")
tv.column("2", width=5)
tv.heading("3", text="Contact")
tv.column("3", width=5)
tv.heading("4", text="Address")
tv.column("4", width=10)
tv.heading("5", text="Sex")
tv.column("5", width=5)
tv.heading("6", text="Username")
tv.column("6", width=5)
tv.heading("7", text="Password")
tv.column("7", width=5)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
table_sbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tv.yview)
table_sbar.pack(side='right', fill='y')
tv.configure(yscrollcommand=table_sbar.set)
tv.pack(fill=X)

def displayAll():
    tv.delete(*tv.get_children())
    for row in dbStaff.fetch():
        tv.insert("", END, values=row)

displayAll()

#COUNT ROWS
rows = tv.get_children()
counterStaff = len(rows)

if counterStaff < 10:
    counterStaff = '0{}'.format(counterStaff)

staffNum = Label(staffPanel, text="", font=("Microsoft JhengHei", 22, "bold"), 
              bg="#FBF0D7", fg="#497687")
staffNum.place(relx=0.11, rely=0.38, anchor="center")
staffNum.config(text=counterStaff)

#FOR PATIENT COUNT
dbPatient = Patient_Database("patient.db")

name = StringVar()
address = StringVar()
birthday = StringVar()
age = StringVar()
contact = StringVar()
martial = StringVar()
height = StringVar()
weight = StringVar()
pulse = StringVar()
bodytemp = StringVar()

def getData(event):
    selected_row = tv2.focus()
    data = tv2.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1]) 
    address.set(row[2])
    age.set(row[3])
    birthday.set(row[4])
    contact.set(row[5])
    martial.set(row[6])
    height.set(row[7])
    weight.set(row[8])
    pulse.set(row[9])
    bodytemp.set(row[10])

# Table Frame
tree_frame2 = Frame(root, bg="#ecf0f1")

style2 = ttk.Style()
style2.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9),rowheight=50) 
style2.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 9), foreground='#497687')
tv2 = ttk.Treeview(tree_frame2, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11), style="mystyle.Treeview")
tv2.heading("1", text="ID")
tv2.column("1", width=1, stretch=FALSE)
tv2.heading("2", text="Name")
tv2.column("2", width=1)
tv2.heading("3", text="Address")
tv2.column("3", width=1)
tv2.heading("4", text="Birthday")
tv2.column("4", width=1)
tv2.heading("5", text="Age")
tv2.column("5", width=1)
tv2.heading("6", text="Contact")
tv2.column("6", width=1)
tv2.heading("7", text="Marital")
tv2.column("7", width=1)
tv2.heading("8", text="Height")
tv2.column("8", width=1)
tv2.heading("9", text="Weight")
tv2.column("9", width=5)
tv2.heading("10", text="Pulse Rate")
tv2.column("10", width=1)
tv2.heading("11", text="Body Temp")
tv2.column("11", width=1)

tv2['show'] = 'headings'
tv2.bind("<ButtonRelease-1>", getData)

table_sbar2 = ttk.Scrollbar(tree_frame, orient="vertical", command=tv.yview)
table_sbar2.pack(side='right', fill='y')
tv2.configure(yscrollcommand=table_sbar.set)

def displayAll2():
    tv2.delete(*tv2.get_children())
    for row in dbPatient.fetch():
        tv2.insert("", END, values=row)

displayAll2()

#COUNT ROWS
rows = tv2.get_children()
counterPtns = len(rows)

if counterPtns < 10:
    counterPtns = '0{}'.format(counterPtns)

regPtsNum = Label(regPtsPan, text="", font=("Microsoft JhengHei", 22, "bold"), 
              bg="#F4E7CA", fg="#497687")
regPtsNum.place(relx=0.12, rely=0.38, anchor="center")
regPtsNum.config(text=counterPtns)

#FOR EQUIP COUNT------------
dbEquip = Equipment_Database("equipments.db")

equipment_name= StringVar()
equipment_quantity= StringVar()

def getEquipData(event):
    selected_row = tv3.focus()
    data = tv3.item(selected_row)
    global row
    row = data["values"]
    equipment_name.set(row[1])
    equipment_quantity.set(row[2])

# Table Frame
tree_frame3 = Frame(root, bg="#ecf0f1")

style3 = ttk.Style()
style3.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9),rowheight=50) 
style3.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 9), foreground='#497687')
tv3 = ttk.Treeview(tree_frame3, columns=(1, 2, 3,), style="mystyle.Treeview")
tv3.heading("1", text="ID")
tv3.column("1", width=2)
tv3.heading("2", text="Equipment Name")
tv3.column("2", width=5)
tv3.heading("3", text="Equipment Quantity")
tv3.column("3", width=5)
tv3['show'] = 'headings'
tv3.bind("<ButtonRelease-1>", getEquipData)
tv3.pack(fill=X)

def displayAll3():
    tv3.delete(*tv3.get_children())
    for row in dbEquip.fetch():
        tv3.insert("", END, values=row)

displayAll3()

#COUNT ROWS
rows = tv3.get_children()
countEquip = len(rows)

if countEquip < 10:
    countEquip = '0{}'.format(countEquip)

avlEqpsNum = Label(avlEqpsPan, text="", font=("Microsoft JhengHei", 22, "bold"), 
              bg="#F4E7CA", fg="#497687")
avlEqpsNum.place(relx=0.12, rely=0.38, anchor="center")
avlEqpsNum.config(text=countEquip)

#FOR MED COUNT------------
dbMeds = Meds_Database("meds.db")

equipment_name= StringVar()
equipment_quantity= StringVar()
description= StringVar()
meds_name= StringVar()
quantity= StringVar()

def getMedsData(event):
    selected_row = tv4.focus()
    data = tv4.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    description.set(row[1])
    meds_name.set(row[2])
    quantity.set(row[3])

# Table Frame
tree_frame4 = Frame(root, bg="#ecf0f1")

style4 = ttk.Style()
style4.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9),rowheight=50) 
style4.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 9), foreground='#497687')
tv4 = ttk.Treeview(tree_frame4, columns=(1, 2, 3, 4), style="mystyle.Treeview")

tv4.heading("1", text="ID")
tv4.column("1", width=2, stretch=FALSE)
tv4.heading("2", text="Description")
tv4.column("2", width=5)
tv4.heading("3", text="Product Neme")
tv4.column("3", width=5)
tv4.heading("4", text="Quantity")
tv4.column("4", width=5)

tv4['show'] = 'headings'
tv4.bind("<ButtonRelease-1>", getMedsData)
tv4.pack(fill=X)

def displayAll4():
    tv4.delete(*tv4.get_children())
    for row in dbMeds.fetchMeds():
        tv4.insert("", END, values=row)
displayAll4()

rows = tv4.get_children()
countMed = len(rows)

if countMed < 10:
    countMed = '0{}'.format(countMed)

avlMedsNum = Label(avlMedsPan, text="", font=("Microsoft JhengHei", 22, "bold"), 
              bg="#FBF0D7", fg="#497687")
avlMedsNum.place(relx=0.12, rely=0.38, anchor="center")
avlMedsNum.config(text=countMed)

#out of stock products
tree_frame5 = Frame(root, bg="#ecf0f1")
tree_frame5.place(x=707, y=520, width=500, height=245)

oosLabel = Label(root, text="Nearly and Out-of-Stock Medicines", font=("Microsoft JhengHei", 15, "bold"), 
                    bg="#DFEEED", fg="#497687")
oosLabel.place(x=707, y=485)

style5 = ttk.Style()
style5.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9), rowheight=50) 
style5.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 12), foreground='#497687')
tv5 = ttk.Treeview(tree_frame5, columns=(1, 2, 3, 4), style="mystyle.Treeview")

tv5.heading("1", text="ID")
tv5.column("1", width=2, stretch=FALSE)
tv5.heading("2", text="Description")
tv5.column("2", width=120)
tv5.heading("3", text="Product Name")
tv5.column("3", width=50)
tv5.heading("4", text="Quantity")
tv5.column("4", width=2)
tv5['show'] = 'headings'
tv5.bind("<ButtonRelease-1>", getData)
table_sbar = ttk.Scrollbar(tree_frame5, orient="vertical", command=tv5.yview)
table_sbar.pack(side='right', fill='y')
tv5.configure(yscrollcommand=table_sbar.set)
tv5.pack(fill=X)

def displayOOS():
    tv4.delete(*tv4.get_children())
    tv5.delete(*tv5.get_children())

    rows = dbMeds.fetchMeds()
    rows.sort(key=lambda row: int(row[3]))  
    for row in rows:
        if int(row[3]) >= 10:
            tv4.insert("", END, values=row)
        else:
            tv5.insert("", END, values=row)
displayOOS()

root.mainloop()