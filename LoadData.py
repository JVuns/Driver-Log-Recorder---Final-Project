import pandas as pd
import tkinter as tk
import numpy as np
from tkinter import messagebox
import datetime

def clear_data(self):
    self.display.delete(*self.display.get_children())
    return None

def Load_excel_data(self):
    # ----- Driver Log ----- #
    if self.variable.get() == "Driver Log":
        file_path = self.filepath
        try:
            excel_filename = r"{}".format(file_path)
            print(excel_filename)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", f"{file_path} File not found")
            return None

        clear_data(self)
        self.display["column"] = list(df.columns.notna()) 
        self.display["show"] = "headings"
        for column in self.display["columns"]:
            self.display.heading(column, text=column) # column heading = column name
        
        df_rows = df.replace(np.nan,'', regex=True).to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            self.display.insert("", "end", values=row) # inserts each list to the treeview
        return None
    # ----- Driver Productivity ----- #
    elif self.variable.get() == "Driver Productivity":
        try:
            excel_filename = r"{}".format(file_path)
            print(excel_filename)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", f"{file_path} File not found")
            return None
    # ----- Production Graph ----- #
    elif self.variable.get() == "Production Graph":
        print("Also TBD")
    # ----- Misc Load ----- #
def misc_load(self):
    file_path = self.filepath
    try:
        excel_filename = r"{}".format(file_path)
        # print(excel_filename)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)
    except FileNotFoundError:
        tk.messagebox.showerror("Error", f"{file_path} File not found")
        return None
    clear_data(self)
    self.display["column"] = list(df.columns) 
    # print(self.display["column"])
    self.display["show"] = "headings"
    for column in self.display["columns"]:
        self.display.heading(column, text=column) # column heading = column name
    
    df_rows = df.replace(np.nan,'', regex=True).to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        self.display.insert("", "end", values=row) # inserts each list to the treeview
    self.display.column('#0', anchor="center", width=50)
    self.display.column('#1', anchor="center", width=170)
    self.display.column('#2', anchor="center", width=120)
    self.display.column('#3', anchor="center", width=120)
    self.display.column('#4', anchor="center", width=400)
    return None

# ----- Post for adding data ----- #
def post(self,name,route,vehicle):
    if not name.strip():
        tk.messagebox.showerror("Empty Entry","Name Entry is empty")
        return None
    if not vehicle.strip():
        tk.messagebox.showerror("Empty Entry","vehicle Entry is empty")
        return None
    if not route.strip():
        tk.messagebox.showerror("Empty Entry","Route Entry is empty")
        return None
    self.displayDraft.heading('#0', text='No')
    self.displayDraft.heading('#1', text='Name')
    self.displayDraft.heading('#2', text='Route')
    self.displayDraft.heading('#3', text='Vehicle')
    self.displayDraft.heading('#4', text='Date')
    self.displayDraft.column('#0', anchor="center", width=50)
    self.displayDraft.column('#1', anchor="center", width=85)
    self.displayDraft.column('#2', anchor="center", width=60)
    self.displayDraft.column('#3', anchor="center", width=60)
    self.displayDraft.column('#4', anchor="center", width=140)
    self.displaycontent = self.displayDraft
    self.displaycontent.insert("",index="end",text=f"{len(self.displayDraft.get_children())}",value=(name,route,vehicle,datetime.datetime.now().strftime("%x")))
    # print(name)
    # print(vehicle)
    # print(route)
    # print(datetime.datetime.now().strftime("%x"))

def transferdata(self):
    
    self.display.heading('#0', text='No')
    self.display.heading('#1', text='Name')
    self.display.heading('#2', text='Route')
    self.display.heading('#3', text='Vehicle')
    self.display.heading('#4', text='Date')
    self.display.column('#0', anchor="center", width=50)
    self.display.column('#1', anchor="center", width=170)
    self.display.column('#2', anchor="center", width=120)
    self.display.column('#3', anchor="center", width=120)
    self.display.column('#4', anchor="center", width=400)
    self.displayPost = self.display
    for item in self.displayDraft.get_children():
        self.displayPost.insert("",index="end",text=f"{len(self.displayDraft.get_children())}",value=self.displayDraft.item(item)["values"])
