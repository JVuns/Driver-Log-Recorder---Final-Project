import pandas as pd
from tkinter.filedialog import asksaveasfilename
import tkinter as tk

def saveDialog(self):
    '''Saving data from add page in form of excel file'''
    values = []
    for child in self.display.get_children():
        values.append(self.display.item(child)["values"] ) # appending the value of treeview, ["values"] will append the value without datatype information
    print(values)
    df = pd.DataFrame(values)
    df.columns = ["Name", "Route", "Vehicle", "Date"]
    filepath = asksaveasfilename(defaultextension=".xlsx")
    df.to_excel(filepath, index=False, header=True)

def startupLoad(self):
    try:
        with open("setting.txt", mode="r") as config:
            defaultvar = config.read()
            print(defaultvar)
    except FileNotFoundError:
        # file = open("Setting.txt", "x")
        # file.write("default")
        return None

def SaveVar(self):
    '''passing all the value in the variable page and turning it into data frame'''
    userfilename = self.savenameE.get()
    baseWage = self.baseWage.get()
    CatA = self.streakA.get()
    CatB = self.streakB.get()
    CatC = self.streakC.get()
    vechileList = []
    routeList = []
    for child in self.varDispV.get_children():
        vechileList.append([self.varDispV.item(child)["text"],self.varDispV.item(child)["values"]])
    for child in self.varDispR.get_children():
        routeList.append([self.varDispR.item(child)["text"],self.varDispR.item(child)["values"]])
    df = pd.DataFrame({
        "Category A": CatA,
        "Category B": CatB,
        "Category C": CatC,
        "Vehicle": vechileList,
        "Route": routeList,
        "Base wage": baseWage
    })
    print(df)
    path = f"Driver-Log-Recorder---Final-Project/Saved variable/{userfilename}.xlsx"
    df.to_excel(path)
    