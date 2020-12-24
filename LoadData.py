# def test(self):
#     pathfile = self.filepath
#     print(pathfile)
#     print(self.variable.get())

import pandas as pd
import tkinter as tk
from tkinter import messagebox

def clear_data(self):
    self.display.delete(*self.display.get_children())
    return None

def Load_excel_data(self):
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = self.filepath
    try:
        excel_filename = r"{}".format(file_path)
        print(excel_filename)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)
    except FileNotFoundError:
        tk.messagebox.showerror("Error", f"{file_path} not found")
        return None
    # else:
    #     tk.messagebox.showerror("Error", "Unexpected Error")
    #     return None
    clear_data(self)
    self.display["column"] = list(df.columns)
    self.display["show"] = "headings"
    for column in self.display["columns"]:
        self.display.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        self.display.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None

