import pandas as pd
from tkinter import *
import tkinter as tk
import numpy as np
from tkinter import messagebox
from tkinter import ttk
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
import ast

def clear_data(self):
    ''' Clearing data from treeview'''
    self.display.delete(*self.display.get_children())
    try:
        self.bar1.get_tk_widget().place_forget()
    except AttributeError:
        pass
    return None

def Load_excel_data(self):
    '''Load choosen data to process into statistics based on variable that is passed'''
    file_path = self.filepath
    # ----- Driver Log ----- #
    if self.variable.get() == "Driver Log":
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
        self.display["show"] = "headings"
        for column in self.display["columns"]:
            self.display.heading(column, text=column) # column heading = column name
        
        df_rows = df.replace(np.nan,'', regex=True).to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            self.display.insert("", "end", values=row) # inserts each list to the treeview
        return None
    # ----- Driver Productivity ----- #
    elif self.variable.get() == "Driver Productivity":
        clear_data(self)
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
        tempvar=[]
        name=[]
        count=[]
        date=[]
        df2 = df.sort_values(by=['Name','Date','Route','Vehicle'])
        df3 = df2.groupby(['Name','Date']).count()

        for index, row in df2.iterrows():
            if [row[0],row[3]] != tempvar:
                name.append(row[0])
                date.append(row[3])
                tempvar = [row[0],row[3]]
        for number in df3['Route'].values:
            count.append(number)
        data3 = zip(name,date,count)
        mergedData = list(data3)
        self.display["columns"] = ["No", "Name", "Date", "Activity"]
        self.display.heading('#0,', text='No')
        self.display.column('#0', anchor="center", width=0)
        self.display.heading('#1', text='Name')
        self.display.column('#1', anchor="center", width=200)
        self.display.heading('#2', text='Date')
        self.display.column('#2', anchor="center", width=260)
        self.display.heading('#3', text='Activity')
        self.display.column('#3', anchor="center", width=250)
        index = iid = 0
        for row in mergedData:
            self.display.insert("", index, iid, values=row)
            index = iid = index + 1

    # ----- Production Graph ----- #
    elif self.variable.get() == "Production Graph":
        clear_data(self)
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
        # if self.targetE.get().isdigit() == True:
            # tk.messagebox.showerror("Error", f"Target field is empty")
        else:
            df2 = df.sort_values(by=['Name','Date','Route','Vehicle'])
            df3 = df2.groupby(['Date'], as_index=False).count()
            df3.columns = ['Date', 'Total Activity','','']
            # print(df3)
            figure1 = plt.Figure(figsize=(8,4), dpi=88)
            ax1 = figure1.add_subplot(111)
            self.bar1 = FigureCanvasTkAgg(figure1, self.frame2)
            self.bar1.get_tk_widget().place(relx=0.001, rely=0.09)
            if self.targetE.get().isdigit() == True:
                ax1.axhline(y=int(self.targetE.get()), color='r', linestyle='dashed')
            df3.plot(x='Date', y='Total Activity', kind='line', ax=ax1)


    # ----- Misc Load ----- #
def misc_load(self):
    '''Loading data from excel '''
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
    ''' Posting data from draft treeview into final treeview'''
    if not name.strip(): #Raise error if recieved empty string or space only input
        tk.messagebox.showerror("Empty Entry","Name Entry is empty")
        return None
    if not vehicle.strip():
        tk.messagebox.showerror("Empty Entry","vehicle Entry is empty")
        return None
    if not route.strip():
        tk.messagebox.showerror("Empty Entry","Route Entry is empty")
        return None
    self.displayDraft.heading('#0', text=' ')
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

def varPostV(self,name,value):
    if not name.strip():
        tk.messagebox.showerror("Empty entry","The variable name for vehicle is empty")
        return None
    if not value.strip():
        tk.messagebox.showerror("Empty entry","The variable value for vechicle is empty")
        return None
    self.varDispV.heading('#0', text='Vehicle')
    self.varDispV.heading('#1', text='Value')
    self.varDispV.column('#0', anchor='w')
    self.varDispV.column('#1', anchor='w')
    self.varVContent = self.varDispV
    self.varVContent.insert("",index="end",text=name,value=(value))

def varPostR(self,name,value):
    if not name.strip():
        tk.messagebox.showerror("Empty entry","The variable name for route is empty")
        return None
    if not value.strip():
        tk.messagebox.showerror("Empty entry","The variable value for route is empty")
        return None
    self.varDispR.heading('#0', text='Route')
    self.varDispR.heading('#1', text='Value')
    self.varDispR.column('#0', anchor='w')
    self.varDispR.column('#1', anchor='w')
    self.varRContent = self.varDispR
    self.varRContent.insert("",index="end",text=name,value=(value))
    
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

def LoadPay(self, DName):
    # Load data
    varfilepath = f"Driver-Log-Recorder---Final-Project/Saved variable/{self.filename}"
    try:
        excel_filename = r"{}".format(varfilepath)
        # print(excel_filename)
        if excel_filename[-4:] == ".csv":
            dfvar = pd.read_csv(excel_filename)
        else:
            dfvar = pd.read_excel(excel_filename)
    except FileNotFoundError:
        tk.messagebox.showerror("Error", f"{varfilepath} File not found")
        return None
    try:
        excel_filename = r"{}".format(self.filepath)
        # print(excel_filename)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)
    except FileNotFoundError:
        tk.messagebox.showerror("Error", f"{self.filepath} File not found")
        return None

    # Add driver log into treeview
    dflog = df.loc[df['Name'] == self.driverNameE.get()]
    self.display["columns"] = ["Name", "Route", "Vehicle", "Date"]
    self.display.heading('#0,', text='No')
    self.display.column('#0', anchor="center", width=30)
    self.display.heading('#1', text='Name')
    self.display.column('#1', anchor="center", width=60)
    self.display.heading('#2', text='Route')
    self.display.column('#2', anchor="center", width=50)
    self.display.heading('#3', text='Vehicle')
    self.display.column('#3', anchor="center", width=50)
    self.display.heading('#4', text='Date')
    self.display.column('#4', anchor="center", width=60)
    for index, row in dflog.iterrows():
        # print(row.values)
        self.display.insert("",index="end",text=len(self.display.get_children()),value=(row.values[0],row.values[1],row.values[2],row.values[3]))
    render(self)
    
    # Calculation
    datastore = {}
    datastore2 = []
    datastore3 = {}
    tuples = [tuple(x) for x in dflog.values]
    for liste in tuples:
        row = '-'.join(liste)
        if not row in datastore:
            datastore[row] = 1
        elif row in datastore:
                datastore[row] += 1
    # print(datastore)
    for data in datastore.items():
        new_id = (data[0].split("-"))
        new_id.append(data[1])
        datastore2.append(new_id)
    # print(datastore2)
    for data in datastore2:
        if (data[1],data[2]) not in datastore3:
            datastore3[data[1],data[2]]={'C1':0, 'C2':0,'C3':0}
    for data in datastore2:
        if data[4] <= 3:
            datastore3[data[1],data[2]]['C1']+=int(data[4])
        elif data[4] > 3 and data[4] <= 5:
            datastore3[data[1],data[2]]['C1']+=3
            datastore3[data[1],data[2]]['C2']+=int(data[4]-3)
        else:
            datastore3[data[1],data[2]]['C1']+=3
            datastore3[data[1],data[2]]['C2']+=2
            datastore3[data[1],data[2]]['C3']+=int(data[4]-5)
    # print(datastore3)
    # for combination in datastore3.items():
    #     print(combination[0])

    self.payDisplay = ttk.Treeview(self.framepay)
    self.payDisplay.place(relx=0.035, rely=0.09, relwidth=0.925, relheight=0.5)
    self.TLabel = Label(self.mainframe, text="Total")
    self.TLabel.place(relx=0.78, rely=0.65) 

    self.payDisplay["columns"] = ["Name", "Route", "Vehicle", "Date"]
    self.payDisplay.heading('#0,', text='No')
    self.payDisplay.column('#0', anchor='center', width=30)
    self.payDisplay.heading('#1', text='Route, Vehicle')
    self.payDisplay.column('#1', anchor='center', width=60)
    self.payDisplay.heading('#2', text='C1')
    self.payDisplay.column('#2', anchor='center', width=50)
    self.payDisplay.heading('#3', text='C2')
    self.payDisplay.column('#3', anchor='center', width=50)
    self.payDisplay.heading('#4', text='C3')
    self.payDisplay.column('#4', anchor='center', width=60)
    for combination in datastore3.items():
        # print(row.values)
        self.payDisplay.insert("",index="end",text=(len(self.payDisplay.get_children())+1),value=(combination[0],combination[1]['C1'],
        combination[1]['C3'],
        combination[1]['C2']))

    C1 = dfvar.loc[0,'Category A']
    C2 = dfvar.loc[0,'Category B']
    C3 = dfvar.loc[0,'Category C']
    Base = dfvar.loc[0,'Base wage']
    
    vehicleData = {}
    for row in dfvar['Vehicle']:
        exstring = ast.literal_eval(row)
        vehicleData[exstring[0]] = exstring[1][0]
    # print(vehicleData)
    routeData = {}
    for row in dfvar['Route']:
        exstring = ast.literal_eval(row)
        routeData[exstring[0]] = exstring[1][0]
    # print(routeData)
    displayData = []
    newdata = []
    for child in self.payDisplay.get_children():
        displayData.append(self.payDisplay.item(child)["values"])
    # print(displayData)
    totalmoney = []
    for data in displayData:
        x = data[0].split()
        newdata.append([x,data[1],data[2],data[3]])
    for datavar in newdata:
        totalmoney.append(float(Base)*float(C1)*float(routeData[datavar[0][0]])*float(vehicleData[datavar[0][1]])*datavar[1])
        totalmoney.append(float(Base)*float(C2)*float(routeData[datavar[0][0]])*float(vehicleData[datavar[0][1]])*datavar[2])
        totalmoney.append(float(Base)*float(C3)*float(routeData[datavar[0][0]])*float(vehicleData[datavar[0][1]])*datavar[3])
    self.Money = ("{:,}".format(sum(totalmoney)))
    
    self.TLabel = Label(self.mainframe, text=f"{self.Money}", width=20, borderwidth=2,bg="white", relief="groove")
    self.TLabel.place(relx=0.82, rely=0.65) 


def Setpath(self):
    filename = self.variable.get()
    print(filename)
    self.filename = filename

def render(self):
    self.payName = Label(self.framepay, text="Driver name: ")
    self.payName.place(relx=0.02, rely=0.02)
    self.payName = Label(self.framepay, text=self.driverNameE.get())
    self.payName.place(relx=0.25, rely=0.02)