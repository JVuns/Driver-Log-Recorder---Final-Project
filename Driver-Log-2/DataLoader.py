import pandas as pd
import numpy
from tkinter import messagebox
import tkinter as tk

def read(self, path):
    """Reading the excel entry data"""
    try:
        global df1, df2, dfname
        df1 = pd.read_excel(path, sheet_name="Entry Data", header=7, usecols="A:AD", dtype=str)
        df1 = df1.drop(columns=["DAY","Cek Opt"])
        df1 = df1.drop(df1.index[0])
        df2 = df1.sort_values(['NAMA OP','DATE'], ascending=[True,True])
        df2 = df2.filter(['NAMA OP','DATE','SPEC','UNIT NO','PIT','Ret'])
        df2['NAMA OP'] = df2['NAMA OP'].str.upper()
        dfname = df2.groupby('NAMA OP', as_index = False).count()
        dfname = dfname['NAMA OP']
        print(df2)
        print(dfname)
        return df1, df2, dfname
    except FileNotFoundError:
        tk.messagebox.showerror("Error", f"{path} File not found")

        return None
