# def test(self):
#     pathfile = self.filepath
#     print(pathfile)
#     print(self.variable.get())

import pandas as pd
import tkinter as tk
import numpy as np
from tkinter import messagebox

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

def post(self,name,vehicle,route):
    print(name)
    print(vehicle)
    print(route)
