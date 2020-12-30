import pandas as pd
from tkinter.filedialog import asksaveasfilename
import tkinter as tk

def saveDialog(self):
    values = []
    for child in self.display.get_children():
        values.append(self.display.item(child)["values"])
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
    