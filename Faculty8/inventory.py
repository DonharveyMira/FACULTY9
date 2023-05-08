from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from meds_db import Meds_Database
from equipmentDB import Equipment_Database
import os

meds_db = Meds_Database("meds.db")
equipment_db = Equipment_Database("equipments.db")
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

equipment_name= StringVar()
equipment_quantity= StringVar()
description= StringVar()
meds_name= StringVar()
quantity= StringVar()

#Medicine Record
medicinePan = Frame(root, bg="#FBF0D7")
medicinePan.place(x=210, y=39, width=500, height=720)

medListLab = Label(medicinePan, text="MEDICINE LIST", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
medListLab.place(relx=0.5, rely=0.03, anchor="center")

medNameLab = Label(medicinePan, text="Medicine Name", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
medNameLab.place(relx=0.04, rely=0.1, anchor=W)
medNameEnt = Entry(medicinePan,textvariable=meds_name, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
medNameEnt.place(relx=0.663, rely=0.1, anchor=CENTER)

descLab = Label(medicinePan, text="Description", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
descLab.place(relx=0.04, rely=0.2, anchor=W)
descEnt = Entry(medicinePan,textvariable=description, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
descEnt.place(relx=0.663, rely=0.2, anchor=CENTER)

quantLab = Label(medicinePan, text="Quantity", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
quantLab.place(relx=0.04, rely=0.3, anchor=W)
quantEnt = Entry(medicinePan,textvariable=quantity, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
quantEnt.place(relx=0.663, rely=0.3, anchor=CENTER)

#Equip Record
equipPan = Frame(root, bg="#FBF0D7")
equipPan.place(x=719, y=39, width=480, height=720)

medEquipTl = Label(equipPan, text="MEDICAL EQUIPMENTS", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
medEquipTl.place(relx=0.5, rely=0.03, anchor="center")

eqpLabel = Label(equipPan, text="Equiment Name", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
eqpLabel.place(relx=0.04, rely=0.1, anchor=W)
eqpEnt = Entry(equipPan,textvariable=equipment_name, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
eqpEnt.place(relx=0.663, rely=0.1, anchor=CENTER)

eqQuantLab = Label(equipPan, text="Quantity", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
eqQuantLab.place(relx=0.04, rely=0.193, anchor=W)
eqQuantEnt = Entry(equipPan, textvariable=equipment_quantity, font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=30)
eqQuantEnt.place(relx=0.663, rely=0.193, anchor=CENTER)

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
def homeBtn():
    root.withdraw() 
    os.system('python homepage.py')
    root.destroy() 

cvHomeIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvHomeIC.pack()
imgHome = PhotoImage(file='images//home.png')
cvHomeIC.create_image(25, 25, image=imgHome, anchor=CENTER)
cvHomeIC.configure(background='#FBF0D7')
cvHomeIC.place(relx=0.0069, rely=0.17)

home_label = Label(root, text="Home", bg="#FBF0D7", fg="#497687")
home_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
home_label.place(relx=0.07, rely=0.2, anchor=CENTER)
home_label.bind("<Button-1>", lambda event: homeBtn())

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
imgInv = PhotoImage(file='images//inventory2.png')
cvinventoryIC.create_image(25, 25, image=imgInv, anchor=CENTER)
cvinventoryIC.configure(background='#FBF0D7') 
cvinventoryIC.place(relx=0.007, rely=0.47)

inventory_label = Label(root, text="Inventory", bg="#FBF0D7", fg="#1E3037")
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

def getEquipData(event):
    selected_row = equipment_tv.focus()
    data = equipment_tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    equipment_name.set(row[1])
    equipment_quantity.set(row[2])

def clearEquip():
    eqpEnt.delete(0, END)
    eqQuantEnt.delete(0, END)
   

btnReset = Button(equipPan, text="Clear", command=clearEquip, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.53, rely=0.95, anchor=CENTER)

def addEquip():
    #tempo-command
    try:
        int(equipment_quantity.get())
        if equipment_name.get() == "" or equipment_quantity.get() == "" :
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
        equipment_db.insert(equipment_name.get(), equipment_quantity.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearEquip()
        dispalyAllEquip()
        
    except ValueError:
        messagebox.showerror("Error input!", "Please input the number of quantity")

btnNew = Button(equipPan, text="Add", command=addEquip, 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnNew.place(relx=0.93, rely=0.95, anchor=CENTER)

def deleteEquip():
    #tempo-command
    equipment_db.remove(row[0])
    clearEquip()
    dispalyAllEquip()

btnNew = Button(equipPan, text="Delete", command=deleteEquip    , 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnNew.place(relx=0.658, rely=0.95, anchor=CENTER)

def updateEquip():
    if equipment_name.get() == "" or equipment_quantity.get() == "" :
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    equipment_db.update(row[0],equipment_name.get(), equipment_quantity.get())
    messagebox.showinfo("Success", "Record Update")
    clearEquip()
    dispalyAllEquip()

def dispalyAllEquip():
    equipment_tv.delete(*equipment_tv.get_children())
    for row in equipment_db.fetch():
        equipment_tv.insert("", END, values=row)

btnSave = Button(equipPan, text="Update", command=updateEquip, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.8, rely=0.95, anchor=CENTER)


# Table Frame for equipments
equipment_frame = Frame(equipPan, bg="#ecf0f1")
equipment_frame.place(x=9, y=270, width=463, height=387)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
equipment_tv = ttk.Treeview(equipment_frame, columns=(1, 2, 3,), style="mystyle.Treeview")
equipment_tv.heading("1", text="ID")
equipment_tv.column("1", width=2, stretch=FALSE)
equipment_tv.heading("2", text="Equipment Name")
equipment_tv.column("2", width=5)
equipment_tv.heading("3", text="Equipment Quantity")
equipment_tv.column("3", width=5)
equipment_tv['show'] = 'headings'
equipment_tv.bind("<ButtonRelease-1>", getEquipData)
equipment_tv.pack(fill=X)


def getMedsData(event):
    selected_row = meds_tv.focus()
    data = meds_tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    description.set(row[1])
    meds_name.set(row[2])
    quantity.set(row[3])


def clearMeds():
    medNameEnt.delete(0, END)
    descEnt.delete(0, END)
    quantEnt.delete(0, END)
   

def validQInteger():
    try:
        int(quantity.get())
        clearMeds()
    except ValueError:
        messagebox.showerror("Enter an integer number for quantity")

btnReset = Button(medicinePan, text="Clear", command=clearMeds, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 10),cursor="hand2")
btnReset.place(relx=0.616, rely=0.95, anchor=CENTER)


def addMeds():
    #tempo-command
    try:
        int(quantity.get())       
        if description.get() == ""or meds_name.get() == "" or quantity.get() == "":
                messagebox.showerror("Erorr in Input", "Please Fill All the Details")
                return
        meds_db.insertMeds(description.get(), meds_name.get(), quantity.get())
        messagebox.showinfo("Success", "Record Inserted")
        clearMeds()
        dispalyAllMeds()
    except ValueError:
        messagebox.showerror("Error input!", "Please input the number of quantity")
    

btnNew = Button(medicinePan, text="Add", command=addMeds, 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 10),cursor="hand2")
btnNew.place(relx=0.93, rely=0.95, anchor=CENTER)

def deleteMeds():
    meds_db.remove(row[0])
    clearMeds()
    dispalyAllMeds()

btnDel = Button(medicinePan, text="Delete", command=deleteMeds, 
                      bg="#497687", fg="#ffffff")
btnDel.config(font=("Microsoft JhengHei", 10),cursor="hand2")
btnDel.place(relx=0.716, rely=0.95, anchor=CENTER)

def updateMeds():
    if description.get() == "" or meds_name.get() == "" or quantity.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    meds_db.updateMeds(row[0], description.get(), meds_name.get(), quantity.get())
    messagebox.showinfo("Success", "Record Update")
    clearMeds()
    dispalyAllMeds()

def dispalyAllMeds():
    meds_tv.delete(*meds_tv.get_children())
    for row in meds_db.fetchMeds():
        meds_tv.insert("", END, values=row)
        searchEntry.delete(0, END)

btnSave = Button(medicinePan, text="Update", command=updateMeds, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 10),cursor="hand2")
btnSave.place(relx=0.83, rely=0.95, anchor=CENTER)

# Table Frame for meds
meds_frame = Frame(medicinePan, bg="#ecf0f1")
meds_frame.place(x=9, y=270, width=480, height=387)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9), rowheight=50) 
style.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 12), foreground='#497687')
meds_tv = ttk.Treeview(meds_frame, columns=(1, 2, 3, 4), style="mystyle.Treeview")
meds_tv.heading("1", text="ID")
meds_tv.column("1", width=2, stretch=FALSE)
meds_tv.heading("2", text="Description")
meds_tv.column("2", width=120)
meds_tv.heading("3", text="Product Name")
meds_tv.column("3", width=10)
meds_tv.heading("4", text="Quantity")
meds_tv.column("4", width=5)
meds_tv['show'] = 'headings'
meds_tv.bind("<ButtonRelease-1>", getMedsData)
table_sbar = ttk.Scrollbar(meds_frame, orient="vertical", command=meds_tv.yview)
table_sbar.pack(side='right', fill='y')
meds_tv.configure(yscrollcommand=table_sbar.set)
meds_tv.pack(fill=X)

divEqpPan = ttk.Separator(equipPan, orient='horizontal')
divEqpPan.pack(fill='x', pady=240)

divMedPan = ttk.Separator(medicinePan, orient='horizontal')
divMedPan.pack(fill='x', pady=240)

#SEARCH BAR
def search():
    search_text = searchEntry.get().lower()

    items = meds_tv.get_children()
    for item in items:
        values = meds_tv.item(item, 'values')
        if search_text in values[1].lower() or search_text in values[2].lower():  
            meds_tv.selection_set(item)
            meds_tv.focus(item)
        else:
            meds_tv.delete(item)
    if not meds_tv.selection():
        messagebox.showinfo("Information", f"No match found for '{searchEntry.get()}'.")

searchLabel = Label(medicinePan, text="SEARCH", bg="#FBF0D7", fg="#497687")
searchLabel.config(font=("Microsoft JhengHei", 11, "bold"))
searchLabel.place(relx=0.08, rely=0.95, anchor=CENTER)

searchEntry = Entry(medicinePan, bg="#FFFFFF", fg="#497687", width=14)
searchEntry.config(font=("Microsoft JhengHei", 11),cursor="hand2")
searchEntry.place(relx=0.28, rely=0.95, anchor=CENTER)

loadBtn = Button(medicinePan, text="↻", bg="#FBF0D7", fg="#497687", command=dispalyAllMeds, width=1, justify=CENTER)
loadBtn.config(font=("Microsoft JhengHei", 13, "bold"), padx=5, pady=5, highlightthickness=0, borderwidth=0)
loadBtn.place(relx=0.5, rely=0.95, anchor=CENTER)

searchBtn = Button(medicinePan, text="🔍︎", bg="#FBF0D7", fg="#497687", command=search, width=3, justify=RIGHT)
searchBtn.config(font=("Microsoft JhengHei", 10, "bold"), padx=5, pady=5, highlightthickness=0, borderwidth=0)
searchBtn.place(relx=0.45, rely=0.95, anchor=CENTER)

dispalyAllEquip()
dispalyAllMeds()
root.mainloop()