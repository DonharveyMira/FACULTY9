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

# Create a horizontal divider
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

root.mainloop()
