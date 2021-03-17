from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import DataLoader as DL
import numpy as np
import pandas as pd

def Vizu(self, Argument, Filepath):
    """ Data visualization group to display data in Overview page """
    try: 
        self.frame3.place_forget()
    except AttributeError:
        pass
    DL.read(self, Filepath)
    self.frame3 = Frame(self.frame2)
    self.frame3.configure(bg="#4D201A")
    self.frame3.place(relx=0., rely=0, width=830, height=500)

    style = ttk.Style()
    style.configure("mystyle.Treeview", indent=15, highlightthickness=0, bd=0, font=('Calibri', 8)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 8,'bold'), background="red") # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    # Raw Display
    if Argument == "Entry Data":
        self.display = ttk.Treeview(self.frame3, style="mystyle.Treeview")
        self.display.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        
        self.display["column"] = list(DL.df1.columns) 
        self.display["show"] = "headings"
        vsb = Scrollbar(self.frame3, orient="vertical", command=self.display.yview)
        vsb.place(relx=0.95, rely=0.05, relheight=0.9, relwidth=0.020)

        hsb = Scrollbar(self.frame3, orient="horizontal", command=self.display.xview)
        hsb.place(relx=0.05, rely=0.95, relheight=0.020, relwidth=0.9)
        self.display.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        for column in self.display["columns"]:
            self.display.heading(column, text=column) # column heading = column name
        for column in self.display["columns"]:
            if column == "JML":
                self.display.column(column, minwidth=0, width=20)
            elif column == "Name OP":
                self.display.column(column, minwidth=0, width=200)
            elif column == "BLOCK" or column == "Kode":
                self.display.column(column, minwidth=0, width=40)
            elif column == "DATE" or column == "BERANGKAT":
                self.display.column(column, minwidth=0, width=63)
            else:
                self.display.column(column, minwidth=0, width=60)
        df_rows = DL.df1.replace(np.nan, regex=True).to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            self.display.insert("", "end", values=row) # inserts each list to the treeview
        return None

    # Attendance Display
    elif Argument == "Attendance":
        self.display = ttk.Treeview(self.frame3, style="mystyle.Treeview")
        self.display.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        self.display["column"] = list(DL.df2.columns) 
        self.display["show"] = "headings"
        vsb = Scrollbar(self.frame3, orient="vertical", command=self.display.yview)
        vsb.place(relx=0.95, rely=0.05, relheight=0.9, relwidth=0.020)

        hsb = Scrollbar(self.frame3, orient="horizontal", command=self.display.xview)
        hsb.place(relx=0.05, rely=0.95, relheight=0.020, relwidth=0.9)
        self.display.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        for column in self.display["columns"]:
            if column == 'Name OP':
                self.display.heading(column, text=column, anchor="w")
            else:
                self.display.heading(column, text=column) # column heading = column name
        for column in self.display["columns"]:
            if column == "JML":
                self.display.column(column, minwidth=0, width=20)
            elif column == "Name OP":
                self.display.column(column, minwidth=0, width=200)
            elif column == "BLOCK" or column == "Kode":
                self.display.column(column, minwidth=0, width=40)
            elif column == "DATE" or column == "BERANGKAT":
                self.display.column(column, minwidth=0, width=63)
            else:
                self.display.column(column, minwidth=0, width=60)
        
        dfParent = DL.dfname.replace(np.nan, regex=True).to_numpy().tolist()
        i = 0
        datalist = []
        for row in dfParent:
            self.display.insert(parent='', index='end', iid=i, values=(row,''))
            datalist.append(row)
            i += 1
        df_rows = DL.df2.replace(np.nan, regex=True).to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            i = datalist.index(row[0])
            self.display.insert(parent=i, index="end", values=row) # inserts each list to the treeview, The parent parameter tell which parent the child belongs to

        return None
        
    # Summary of the data
    elif Argument == "Summary":
        pass

    elif Argument == "Profit":
        pass
        
def getfile(strings):
    Template = pd.read_excel(strings)
    return Template

        
    