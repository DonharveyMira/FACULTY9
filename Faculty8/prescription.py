from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from patientDb import Patient_Database
import os

db = Patient_Database("patient.db")

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

name = StringVar()
age = StringVar()
pulse = StringVar()
bodytemp = StringVar()
address = StringVar()
prevCheckup = StringVar()
contact = StringVar()
martial = StringVar()
home = StringVar()
work = StringVar()
 

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1]) 
    age.set(row[4])
    pulse.set(row[9])
    bodytemp.set(row[10])
    home.set(row[10])
    work.set(row(11))


def normalCmb():
    if pr_entry.get() == "101":
        normalTxt() 
    else:
         disableTxt()

def normalTxt():
    hbCmbQ1.config(state='normal')
    hbCmbQ2.config(state='normal')
    hbCmbQ3.config(state='normal')
    hbCmbQ4.config(state='normal')
    hbCmbQ5.config(state='normal')

def disableTxt():
    hbCmbQ1.config(state='disable')
    hbCmbQ2.config(state='disable')
    hbCmbQ3.config(state='disable')
    hbCmbQ4.config(state='disable')
    hbCmbQ5.config(state='disable')
    
#button to allow normalcmb()
btnShow = Button(root, text="Ref", command=normalCmb, 
                      bg="#b12a2a", fg="#ffffff")
btnShow.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnShow.place(relx=0.75, rely=0.91, anchor=CENTER)
        
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
cvPtntIC = Canvas(root, width=50, height=50, highlightthickness=0) 
cvPtntIC.pack()
imgPtnt = PhotoImage(file='images//patient2.png')
cvPtntIC.create_image(25, 25, image=imgPtnt, anchor=CENTER)
cvPtntIC.configure(background='#FBF0D7')
cvPtntIC.place(relx=0.0069, rely=0.27)

patient_label = Label(root, text="Patient", bg="#FBF0D7", fg="#1E3037")
patient_label.config(font=("Microsoft JhengHei", 11, "bold"), cursor="hand2")
patient_label.place(relx=0.071, rely=0.3, anchor=CENTER)

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

#main code - homepage ---------------------
#Patient Record
ptntRec_panel = Frame(root, bg="#FBF0D7")
ptntRec_panel.place(x=210, y=34, width=450, height=200)

ptntRec = Label(ptntRec_panel, text="PATIENT RECORDS", font=("Microsoft JhengHei", 14, "bold"), 
                bg="#FBF0D7", fg="#497687")
ptntRec.place(relx=0.5, rely=0.13, anchor=CENTER)

name_label = Label(ptntRec_panel, text="Name", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687")
name_label.place(relx=0.05, rely=0.28, anchor=W) 
name_entry = Entry(ptntRec_panel, textvariable= name, font=("Microsoft JhengHei", 11), 
                   fg="#497687", width=27, state='disabled')
name_entry.place(relx=0.65, rely=0.28, anchor=CENTER) 

age_label = Label(ptntRec_panel, text="Age", font=("Microsoft JhengHei", 11, "bold"), 
                      bg="#FBF0D7", fg="#497687")
age_label.place(relx=0.05, rely=0.48, anchor=W) 
age_entry = Entry(ptntRec_panel, textvariable= age, font=("Microsoft JhengHei", 11), 
                      fg="#497687", width=27, state='disabled')
age_entry.place(relx=0.65, rely=0.48, anchor=CENTER) 

pr_label = Label(ptntRec_panel, text="Pulse Rate", font=("Microsoft JhengHei", 11, "bold"), 
                       bg="#FBF0D7", fg="#497687")
pr_label.place(relx=0.05, rely=0.67, anchor=W) 
pr_entry = Entry(ptntRec_panel, textvariable= pulse, font=("Microsoft JhengHei", 11), 
                       fg="#497687", width=22, state='disabled')
pr_entry.place(relx=0.6, rely=0.67, anchor=CENTER) 
bpm_label = Label(ptntRec_panel, text="bpm", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
bpm_label.place(relx=0.88, rely=0.67, anchor=CENTER) 

bt_label = Label(ptntRec_panel, text="Body Temperature", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
bt_label.place(relx=0.05, rely=0.88, anchor=W) 
bt_entry = Entry(ptntRec_panel,textvariable= bodytemp, font=("Microsoft JhengHei", 11), 
                  fg="#497687", width=22, state='disabled')
bt_entry.place(relx=0.6, rely=0.88, anchor=CENTER) 
cel_label = Label(ptntRec_panel, text="°C", font=("Microsoft JhengHei", 11, "bold"), 
                  bg="#FBF0D7", fg="#497687")
cel_label.place(relx=0.87, rely=0.88, anchor=CENTER) 

#Medical Record
medPan = Frame(root, bg="#FBF0D7")
medPan.place(x=210, y=250, width=450, height=433)

medLab = Label(medPan, text="MEDICAL HISTORY", font=("Microsoft JhengHei", 14, "bold"), 
                bg="#FBF0D7", fg="#497687")
medLab.place(relx=0.5, rely=0.06, anchor=CENTER)

quest1Lab = Label(medPan,  text="Are you currently residing with \nan individual who has tested \npositive for COVID-19?", 
                  font=("Microsoft JhengHei", 11, "bold"),
                   bg="#FBF0D7", fg="#497687", justify="left")
quest1Lab.place(relx=0.05, rely=0.11) 
quest1Cmb = Combobox(medPan, font=("Microsoft JhengHei", 11),  textvariable= home,
                            values=["Yes", "No"], width=11)
quest1Cmb.place(relx=0.76, rely=0.18, anchor=CENTER)

quest2Lab = Label(medPan, text="Are you currently working or \nspending time in an enclosed \nspace with someone who has \ntested positive for COVID-19?", 
                  font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
quest2Lab.place(relx=0.05, rely=0.28) 
quest2Cmb = Combobox(medPan, font=("Microsoft JhengHei", 11), textvariable= work, values=["Yes", "No"], width=11)
quest2Cmb.place(relx=0.76, rely=0.35, anchor=CENTER)

quest3Lab = Label(medPan, text="Do you recently have any of the following?", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
quest3Lab.place(relx=0.05, rely=0.5)

#FEVER
fever = Label(medPan, text="Fever/Lagnat", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
fever.place(relx=0.12, rely=0.56)
feverVar = StringVar(value="No")
feverFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(feverFrame, text="Yes", variable=feverVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(feverFrame, text="No", variable=feverVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

feverFrame.place(relx=0.75, rely=0.59, anchor=CENTER)
fevOpt = feverVar.get()

#COUGH
cough = Label(medPan, text="Cough/Ubo", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
cough.place(relx=0.12, rely=0.62)
coughVar = StringVar(value="No")
coughFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(coughFrame, text="Yes", variable=coughVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(coughFrame, text="No", variable=coughVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

coughFrame.place(relx=0.75, rely=0.65, anchor=CENTER)
coughOpt = coughVar.get()

#colds
colds = Label(medPan, text="Colds/Sipon", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
colds.place(relx=0.12, rely=0.68)
coldsVar = StringVar(value="No")
coldsFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(coldsFrame, text="Yes", variable=coldsVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(coldsFrame, text="No", variable=coldsVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

coldsFrame.place(relx=0.75, rely=0.71, anchor=CENTER)
coldsOpt = coldsVar.get()

#diarrhea
diarrhea = Label(medPan, text="Diarrhea/Pagtatae", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
diarrhea.place(relx=0.12, rely=0.74)
diaVar = StringVar(value="No")
diaFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(diaFrame, text="Yes", variable=diaVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(diaFrame, text="No", variable=diaVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

diaFrame.place(relx=0.75, rely=0.77, anchor=CENTER)
diaOpt = diaVar.get()

#sore throat
soreThroat = Label(medPan, text="Sore Throat", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
soreThroat.place(relx=0.12, rely=0.8)
thrtVar = StringVar(value="No")
thrtFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(thrtFrame, text="Yes", variable=thrtVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(thrtFrame, text="No", variable=thrtVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

thrtFrame.place(relx=0.75, rely=0.83, anchor=CENTER)
thrtOpt = thrtVar.get()

#body pain
bodyPain = Label(medPan, text="Body Pain", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
bodyPain.place(relx=0.12, rely=0.86)
bpVar = StringVar(value="No")
bpFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(bpFrame, text="Yes", variable=bpVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(bpFrame, text="No", variable=bpVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

bpFrame.place(relx=0.75, rely=0.89, anchor=CENTER)
bpOpt = bpVar.get()

#difficulty breathing
diffBreath = Label(medPan, text="Difficulty in breathing", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
diffBreath.place(relx=0.12, rely=0.92)
dpVar = StringVar(value="No")
dpFrame = Frame(medPan, bg="#FBF0D7")
Radiobutton(dpFrame, text="Yes", variable=dpVar, value="Yes", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT, padx=(0, 10))
Radiobutton(dpFrame, text="No", variable=dpVar, value="No", font=("Microsoft JhengHei", 11), 
            bg="#FBF0D7", fg="#497687", justify="left").pack(side=LEFT)

dpFrame.place(relx=0.75, rely=0.95, anchor=CENTER)
dpOpt = dpVar.get()

#high-bpm
highBpmPan = Frame(root, bg="#FBF0D7")
highBpmPan.place(x=683, y=250, width=530, height=433)

highBpmLab = Label(highBpmPan, text="FOR HIGH BPM PATIENTS", font=("Microsoft JhengHei", 14, "bold"), 
                bg="#FBF0D7", fg="#497687")
highBpmLab.place(relx=0.5, rely=0.06, anchor=CENTER)

hbNote = Label(highBpmPan, text="Since the patient's bpm is above 100, they are advised to respond to these questions.", font=("Microsoft JhengHei", 9), 
                   bg="#FBF0D7", fg="gray", justify="center")
hbNote.place(relx=0.5, rely=0.12, anchor=CENTER)

hbLabQ1 = Label(highBpmPan, text="When did you first notice \nyour heart rate was high?", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
hbLabQ1.place(relx=0.05, rely=0.15) 
hbCmbQ1 = Combobox(highBpmPan, font=("Microsoft JhengHei", 11), 
                            values=["Recently (few hours/days ago)", 
                                    "Past week/s", "About a month ago"], width=23, state='disabled')
hbCmbQ1.place(relx=0.73, rely=0.2, anchor=CENTER)

hbLabQ2 = Label(highBpmPan, text="Have you been feeling \nstressed or anxious lately?", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
hbLabQ2.place(relx=0.05, rely=0.32) 
hbCmbQ2 = Combobox(highBpmPan, font=("Microsoft JhengHei", 11), 
                            values=["Yes", "No"], width=23, state='disabled')
hbCmbQ2.place(relx=0.73, rely=0.357, anchor=CENTER)

hbLabQ3 = Label(highBpmPan, text="Have you recently consumed \nany caffeine or alcohol?", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
hbLabQ3.place(relx=0.05, rely=0.5) 
hbCmbQ3 = Combobox(highBpmPan, font=("Microsoft JhengHei", 11), 
                            values=["Yes", "No"], width=23, state='disabled')
hbCmbQ3.place(relx=0.73, rely=0.546, anchor=CENTER)

hbLabQ4 = Label(highBpmPan, text="Have you been feeling \nfatigued or lightheaded?", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
hbLabQ4.place(relx=0.05, rely=0.67)
hbCmbQ4 = Combobox(highBpmPan, font=("Microsoft JhengHei", 11), 
                   values=["Yes", "No"], width=23, state= 'disabled')
hbCmbQ4.place(relx=0.73, rely=0.705, anchor=CENTER)

hbLabQ5 = Label(highBpmPan, text="Have you experienced any \nirregular heartbeats \nor palpitations?", font=("Microsoft JhengHei", 11, "bold"), 
                   bg="#FBF0D7", fg="#497687", justify="left")
hbLabQ5.place(relx=0.05, rely=0.826)
hbCmbQ5 = Combobox(highBpmPan, font=("Microsoft JhengHei", 11), 
                   values=["Yes, occasionally", "Yes, a few instances",
                           "No, I haven't experienced"], width=23,state='disabled')
hbCmbQ5.place(relx=0.73, rely=0.86, anchor=CENTER)


def clear():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    pr_entry.delete(0, END)
    bt_entry.delete(0, END)

btnReset = Button(root, text="Clear", command=clear, 
                      bg="#497687", fg="#ffffff")
btnReset.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnReset.place(relx=0.19, rely=0.91, anchor=CENTER)


def update():
    #tempo-command
    if  quest1Cmb.get()=="" or quest2Cmb.get()== "":
            messagebox.showerror("Erorr in Input", "Please Fill All the Details")
            return
    db.updateMeds(row[0],quest1Cmb.get(), quest2Cmb.get())
    messagebox.showinfo("Success", "Record Update")
    clear()
    displayAll()

btnSave = Button(root, text="Update", command=update, 
                      bg="#497687", fg="#ffffff")
btnSave.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnSave.place(relx=0.3, rely=0.91, anchor=CENTER)

def delete():
    db.remove(row[0])
    clear()
    displayAll()

btnNew = Button(root, text="Delete", command=delete, 
                      bg="#497687", fg="#ffffff")
btnNew.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnNew.place(relx=0.24, rely=0.91, anchor=CENTER)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=683, y=72, width=530, height=161)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Microsoft JhengHei', 9),rowheight=30) 
style.configure("mystyle.Treeview.Heading", font=('Microsoft JhengHei', 9), foreground='#497687')
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=1, stretch=FALSE)
tv.heading("2", text="Name")
tv.column("2", width=1)
tv.heading("3", text="Address")
tv.column("3", width=1)
tv.heading("4", text="Previous Check-up Date")
tv.column("4", width=1)

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

searchLabel = Label(root, text="SEARCH", bg="#DFEEED", fg="#497687")
searchLabel.config(font=("Microsoft JhengHei", 13, "bold"))
searchLabel.place(relx=0.58, rely=0.059, anchor=CENTER)

searchEntry = Entry(root, bg="#FFFFFF", fg="#497687", width=35)
searchEntry.config(font=("Microsoft JhengHei", 13),cursor="hand2")
searchEntry.place(relx=0.76, rely=0.059, anchor=CENTER)

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

#Exit Form
def exitForm():
    root.destroy() 

exitLogo = Canvas(root, width=30, height=30, highlightthickness=0) 
exitLogo.pack()
imgExitLogo = PhotoImage(file='images//exit.png')
exitLogo.create_image(15, 15, image=imgExitLogo, anchor=CENTER)
exitLogo.configure(background='#DFEEED', cursor="hand2")
exitLogo.place(relx=0.97, rely=0.009)
exitLogo.bind("<Button-1>", lambda event: exitForm())

loadBtn = Button(root, text="↻", bg="#DFEEED", fg="#497687", command=displayAll, width=1, justify=CENTER)
loadBtn.config(font=("Microsoft JhengHei", 16, "bold"), padx=5, pady=5, highlightthickness=0, borderwidth=0)
loadBtn.place(relx=0.95, rely=0.059, anchor=CENTER)

searchBtn = Button(root, text="🔍︎", bg="#DFEEED", fg="#497687", command=search, width=3, justify=CENTER)
searchBtn.config(font=("Microsoft JhengHei", 13, "bold"), padx=5, pady=5, highlightthickness=0, borderwidth=0)
searchBtn.place(relx=0.925, rely=0.059, anchor=CENTER)

def presc():
    root.withdraw() 
    os.system('python patient.py')
    root.destroy() 
    
btnPresc = Button(root, text="Edit Patient Information >>", command=presc, 
                      bg="#b12a2a", fg="#ffffff")
btnPresc.config(font=("Microsoft JhengHei", 11),cursor="hand2")
btnPresc.place(relx=0.888, rely=0.91, anchor=CENTER)

normalCmb()
displayAll()
root.mainloop()
