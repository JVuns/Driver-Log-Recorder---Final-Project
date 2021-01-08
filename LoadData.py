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
            if [row[0],row[3]] != tempvar: # adding all unique combination to the list 
                name.append(row[0])
                date.append(row[3])
                tempvar = [row[0],row[3]]
        for number in df3['Route'].values:
            count.append(number) # count how many activity
        data3 = zip(name,date,count) # combining the data for easier use
        mergedData = list(data3)
        # Your common display insertion (Driver activity) 
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
            df3.columns = ['Date', 'Total Activity','',''] # Only use date and total activity, obsolete data were left blank
            # print(df3)
            # Display
            figure1 = plt.Figure(figsize=(8,4), dpi=88) 
            ax1 = figure1.add_subplot(111)
            self.bar1 = FigureCanvasTkAgg(figure1, self.frame2)
            self.bar1.get_tk_widget().place(relx=0.001, rely=0.09)
            if self.targetE.get().isdigit() == True:
                ax1.axhline(y=int(self.targetE.get()), color='r', linestyle='dashed') # Straight line for target line
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

    # Your common display insertion (Draft from add data display) 
    self.displayDraft['show'] = 'headings'
    self.displayDraft.heading('#1', text='Name')
    self.displayDraft.heading('#2', text='Route')
    self.displayDraft.heading('#3', text='Vehicle')
    self.displayDraft.heading('#4', text='Date')
    self.displayDraft.column('#1', anchor="center", width=85)
    self.displayDraft.column('#2', anchor="center", width=85)
    self.displayDraft.column('#3', anchor="center", width=85)
    self.displayDraft.column('#4', anchor="center", width=143)
    self.displaycontent = self.displayDraft
    self.displaycontent.insert("",index="end",text=f" ",value=(name,route,vehicle,datetime.datetime.now().strftime("%x")))

def varPostV(self,name,value):
    """ Moving all the data from entry to treeview """
    if not name.strip():
        tk.messagebox.showerror("Empty entry","The variable name for vehicle is empty")
        return None
    if not value.strip():
        tk.messagebox.showerror("Empty entry","The variable value for vechicle is empty")
        return None
    self.varVContent = self.varDispV
    self.varVContent.insert("",index="end",text=name,value=float(value))

def varPostR(self,name,value):
    if not name.strip():
        tk.messagebox.showerror("Empty entry","The variable name for route is empty")
        return None
    if not value.strip():
        tk.messagebox.showerror("Empty entry","The variable value for route is empty")
        return None
    self.varRContent = self.varDispR
    self.varRContent.insert("",index="end",text=name,value=float(value)) #Float to keep the data consistent

def transferdata(self):
    # Your usuall display insertion (Posted data to be saved)
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
        self.displayPost.insert("",index="end",text=len(self.display.get_children())+1,value=self.displayDraft.item(item)["values"])

def LoadPay(self, DName):
    clear_data(self)
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

    # Your common display insertion (Add driver log into treeview) 
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
    # Inserting the log into dataframe
    for index, row in dflog.iterrows():
        # print(row.values)
        self.display.insert("",index="end",text=len(self.display.get_children())+1,value=(row.values[0],row.values[1],row.values[2],row.values[3]))
    render(self)
    
    # Calculation
    datastore = {}
    datastore2 = []
    datastore3 = {}
    tuples = [tuple(x) for x in dflog.values]

    # Naming the combination by combination in route-vehicle-name-date order ie: South-Mini-Andy-Boomcar
    # And counting the occurrence of the combination
    for liste in tuples:
        row = '-'.join(liste) # Making space character in variable name impossible
        if not row in datastore:
            datastore[row] = 1
        elif row in datastore:
                datastore[row] += 1

    # Splitting the data for neat display
    for data in datastore.items():
        new_id = (data[0].split("-"))
        new_id.append(data[1])
        datastore2.append(new_id)

    # Adding the dictionary to seperate each streak category
    for data in datastore2:
        if (data[1],data[2]) not in datastore3:
            datastore3[data[1],data[2]]={'C1':0, 'C2':0,'C3':0} # < --- Each combination will have that nested dictionary

    # Evaluate the data 
    for data in datastore2:
        print(data[4])
        if data[4] <= 3:
            datastore3[data[1],data[2]]['C1']+=int(data[4]) # if the occurrence count is <= 3 add the value to C1
        elif data[4] > 3 and data[4] <= 5:
            datastore3[data[1],data[2]]['C1']+=3                # if the occurrence is > 3 and <= 5 add 3 to C1 (maximum value C1 could get)
            datastore3[data[1],data[2]]['C2']+=int(data[4]-3)   # and subtract 3 (taken for C1 maximum value)
        elif data[4] > 5:
            datastore3[data[1],data[2]]['C1']+=3                # if the occurrence is > 5 follow the same pattern for C1
            datastore3[data[1],data[2]]['C2']+=2                # add 2 to C1 (maximum value C2 could get)
            datastore3[data[1],data[2]]['C3']+=int(data[4]-5)   # and subtract 5 (taken for C1 and C2 maximum value)

    # Your common display insertion and initialization (for displaying combination and category)
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
        combination[1]['C2'],
        combination[1]['C3']))

    # Paycheck calculation
    C1 = dfvar.loc[0,'Category A']
    C2 = dfvar.loc[0,'Category B']
    C3 = dfvar.loc[0,'Category C']
    Base = dfvar.loc[0,'Base wage']
    
        # Taking the data from variable xlsx file to be matched with data from display 
    vehicleData = {}
    for row in dfvar['Vehicle']:
        try:
            exstring = ast.literal_eval(row) # Make list that somehow turned into string list again
            vehicleData[exstring[0]] = exstring[1][0]
        except ValueError:
            pass

    routeData = {}
    for row in dfvar['Route']:
        try:
            exstring = ast.literal_eval(row)
            routeData[exstring[0]] = exstring[1][0]
        except ValueError:
            pass

    displayData = []
    newdata = []
    for child in self.payDisplay.get_children():
        displayData.append(self.payDisplay.item(child)["values"])

    # Append the money to a list and sum it 
    totalmoney = []
    for data in displayData:
        x = data[0].split()
        newdata.append([x,data[1],data[2],data[3]])
        print(newdata)
    for datavar in newdata: # Base wage x streak count(C1 or C2 or C3) x Route modifier x Vehicle modifier x streak count(C1 or C2 or C3)
        totalmoney.append(float(Base)*float(C1)*float(routeData[datavar[0][0]])*float(vehicleData[datavar[0][1]])*datavar[1])
        totalmoney.append(float(Base)*float(C2)*float(routeData[datavar[0][0]])*float(vehicleData[datavar[0][1]])*datavar[2])
        totalmoney.append(float(Base)*float(C3)*float(routeData[datavar[0][0]])*float(vehicleData[datavar[0][1]])*datavar[3])
    self.Money = ("{:,}".format(sum(totalmoney))) # Summing it and adding coma to the total money  
    
    self.TLabel = Label(self.mainframe, text=f"{self.Money}", width=20, borderwidth=2,bg="white", relief="groove")
    self.TLabel.place(relx=0.82, rely=0.65) 


def Setpath(self): # set path from the dropdown as instance to make it easier to be called later
    filename = self.variable.get()
    print(filename)
    self.filename = filename

def render(self): # render the label of Driver name: 
    self.payName = Label(self.framepay, text="Driver name: ")
    self.payName.place(relx=0.02, rely=0.02)
    self.payName = Label(self.framepay, text=self.driverNameE.get())
    self.payName.place(relx=0.25, rely=0.02)