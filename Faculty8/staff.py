from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from staff_db import Staff_Database
import os

db = Staff_Database("staff.db")
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
cvStaffIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvStaffIC.pack()
imgStaff = PhotoImage(file='images//staff2.png')
cvStaffIC.create_image(25, 25, image=imgStaff, anchor=CENTER)
cvStaffIC.configure(background='#FBF0D7')
cvStaffIC.place(relx=0.0069, rely=0.37)

staff_label = Label(root, text="Staff", bg="#FBF0D7", fg="#1E3037")
staff_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
staff_label.place(relx=0.0648, rely=0.4, anchor=CENTER)

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

name= StringVar()
contact= StringVar()
address= StringVar()
username= StringVar()
password= StringVar()

#main screen
# STAFF AND NURSE INFO
infoPanel = Frame(root, bg="#FBF0D7")
infoPanel.place(x=210, y=48, width=1000, height=720)

ptntRec = Label(infoPanel, text="STAFF'S INFORMATION", 
                font=("Microsoft JhengHei", 14, "bold"), bg="#FBF0D7", fg="#497687")
ptntRec.place(relx=0.5, rely=0.037, anchor=CENTER) 

nameLabel = Label(infoPanel, text="Full Name", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
nameLabel.place(relx=0.08, rely=0.1, anchor=CENTER) 
nameEntry = Entry(infoPanel,textvariable=name, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
nameEntry.place(relx=0.29, rely=0.1, anchor=CENTER) 

contLabel = Label(infoPanel, text="Contact #", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
contLabel.place(relx=0.08, rely=0.19, anchor=CENTER) 
contEntry = Entry(infoPanel, textvariable= contact, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
contEntry.place(relx=0.29, rely=0.19, anchor=CENTER) 

addressLabel = Label(infoPanel, text="Address", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
addressLabel.place(relx=0.08, rely=0.28, anchor=CENTER) 
addressEntry = Entry(infoPanel, textvariable=address, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
addressEntry.place(relx=0.29, rely=0.28, anchor=CENTER) 

sexLabel = Label(infoPanel, text="Sex", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
sexLabel.place(relx=0.56, rely=0.1, anchor=CENTER) 
sexCmBox = Combobox(infoPanel, font=("Microsoft JhengHei", 11), 
                            values=["Male", "Female"], width=30, state="readonly")
sexCmBox.place(relx=0.77, rely=0.1, anchor=CENTER) 

usnLabel = Label(infoPanel, text="Username", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
usnLabel.place(relx=0.56, rely=0.19, anchor=CENTER) 
usnEntry = Entry(infoPanel, textvariable= username, font=("Microsoft JhengHei", 11), fg="#497687", width=32)
usnEntry.place(relx=0.77, rely=0.19, anchor=CENTER) 

noteLabel = Label(infoPanel, text="*Username and password will serve as staff's login info", 
                 font=("Microsoft JhengHei", 8), bg="#FBF0D7", fg="gray")
noteLabel.place(relx=0.769, rely=0.314, anchor=CENTER)

passLabel = Label(infoPanel, text="Password", font=("Microsoft JhengHei", 11, "bold"), 
                    bg="#FBF0D7", fg="#497687")
passLabel.place(relx=0.56, rely=0.28, anchor=CENTER) 
passEntry = Entry(infoPanel, textvariable= password, show="•", font=("Microsoft JhengHei", 11), 
                        fg="#497687", width=32)
passEntry.place(relx=0.77, rely=0.28, anchor=CENTER) 

def passVisibility():
    if passEntry['show'] == '':
        passEntry.configure(show='•')
        btnShow.configure(text='Show')
    else:
        passEntry.configure(show='')
        btnShow.configure(text='Hide')

btnShow = Button(infoPanel, text='Show', command=passVisibility,
                              bg='#497687', fg='#ffffff')
btnShow.config(font=("Microsoft JhengHei", 7),cursor="hand2")
btnShow.place(relx=0.9, rely=0.28, anchor=CENTER)

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

def clear():
    nameEntry.delete(0, END)
    passEntry.delete(0, END)
    usnEntry.delete(0, END)
    addressEntry.delete(0, END)
    contEntry.delete(0, END)
    sexCmBox.set("")

btnReset = Button(root, text="Clear", command=clear, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.77, rely=0.925, anchor=CENTER)

def delete():
    db.remove(row[0])
    clear()
    displayAll()

btnNew = Button(root, text="Delete", command=delete, 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnNew.place(relx=0.822, rely=0.925, anchor=CENTER)

def update():
    if nameEntry.get() == "" or passEntry.get() == "" or usnEntry.get() == "" or addressEntry.get() == "" or sexCmBox.get()== "" or contEntry.get()=="":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],nameEntry.get(), contEntry.get(), addressEntry.get(), sexCmBox.get(), usnEntry.get(), passEntry.get())
    messagebox.showinfo("Success", "Record Update")
    clear()
    displayAll()

btnSave = Button(root, text="Update", command=update, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.878, rely=0.925, anchor=CENTER)
    
def add():
    #tempo-command
    if nameEntry.get() == "" or passEntry.get() == "" or usnEntry.get() == "" or addressEntry.get() == "" or sexCmBox.get()== "" or contEntry.get()=="":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(nameEntry.get(), contEntry.get(), addressEntry.get() , sexCmBox.get() ,usnEntry.get(), passEntry.get())
    messagebox.showinfo("Success", "Record Inserted")
    clear()
    displayAll()

btnSave = Button(root, text="Add", command=add, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.93, rely=0.925, anchor=CENTER)


# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=215, y=286, width=990, height=425)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 9, "bold"), foreground='#497687')

tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=2, stretch= FALSE)
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

#SEARCH BAR
def search():
    search_text = searchEntry.get().lower()

    items = tv.get_children()
    for item in items:
        values = tv.item(item, 'values')
        if search_text in values[1].lower() or search_text in values[2].lower():  
            tv.selection_set(item)
            tv.focus(item)
        else:
            tv.delete(item)
    if not tv.selection():
        messagebox.showinfo("Information", f"No match found for '{searchEntry.get()}'.")

searchLabel = Label(root, text="SEARCH", bg="#FBF0D7", fg="#497687")
searchLabel.config(font=("Microsoft JhengHei", 12, "bold"))
searchLabel.place(relx=0.21, rely=0.925, anchor=CENTER)

searchBtn = Button(root, text="🔍︎", bg="#FBF0D7", fg="#497687", command=search, width=3, justify=CENTER)
searchBtn.config(font=("Microsoft JhengHei", 13, "bold"), padx=5, pady=5, highlightthickness=0, borderwidth=0)
searchBtn.place(relx=0.62, rely=0.923, anchor=CENTER)

searchEntry = Entry(root, bg="#FFFFFF", fg="#497687", width=43)
searchEntry.config(font=("Microsoft JhengHei", 13),cursor="hand2")
searchEntry.place(relx=0.42, rely=0.925, anchor=CENTER)

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)
        searchEntry.delete(0, END)
displayAll()

loadBtn = Button(root, text="↻", bg="#FBF0D7", fg="#497687", command=displayAll, width=1, justify=CENTER)
loadBtn.config(font=("Microsoft JhengHei", 16, "bold"), padx=5, pady=5, highlightthickness=0, borderwidth=0)
loadBtn.place(relx=0.64, rely=0.923, anchor=CENTER)


root.mainloop()