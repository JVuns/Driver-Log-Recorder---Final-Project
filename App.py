from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter as tk
from tkinter import ttk
import LoadData as LD
from misc import *
import os

class Main(tk.Tk):
    def __init__(self):
        startupLoad(self)
        tk.Tk.__init__(self)

        # ----- Screen res and title ----- #
        self.geometry("1000x500")
        self.title("Project")

        # ----- Menubar ----- #
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Main Menu", command=lambda: self.show_frame("pageIDStart"))
        menubar.add_cascade(label="Shortcut", menu=filemenu)
        self.config(menu=menubar)

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True) # args make screen expand to the south and fill the screen

        container.grid_rowconfigure(0,weight=1) 
        container.grid_columnconfigure(0,weight=1)

        self.frames = {} # <----- The dictionary

        frame_menu = StartPage(container,self,"pageIDStart","pageone")
        frame_read = ReadPage(container,self)
        frame_add = AddPage(container,self)
        frame_del = DelPage(container,self)
        frame_pay = PayPage(container,self)

        # V ----- Add frames to dictionary ----- # 

        self.frames["pageIDStart"] = frame_menu
        self.frames["pageIDRead"] = frame_read
        self.frames["pageIDAdd"] = frame_add
        self.frames["pageIDDel"] = frame_del
        self.frames["pageIDPay"] = frame_pay

        frame_menu.grid(row=0,column=0,sticky="nsew")
        frame_read.grid(row=0,column=0,sticky="nsew")
        frame_add.grid(row=0,column=0,sticky="nsew")
        frame_del.grid(row=0,column=0,sticky="nsew")
        frame_pay.grid(row=0,column=0,sticky="nsew")

        self.show_frame("pageIDStart") # The first 6

    # V ----- Change frame ----- #
    def show_frame(self,cont): # cont will take destination as an argument
        frame = self.frames[cont]
        frame.tkraise()

    # V----- Open Dialog to open the xlsx file ----- #
    def windowsDialog(self):
        """ Function to call windows dialog """ 
        loc = askopenfilename(title='Please choose an .xlsx file')
        self.filepath = loc
        self.listBox.delete(0)
        self.listBox.insert("end",self.filepath)
        Main.CreateToolTip(self.buttonpath, text=f"Path: {self.filepath}")

    def windowsDialog2(self):
        """ Function to call windows dialog """ 
        loc = askopenfilename(title='Please choose an .xlsx file')
        self.filepath = loc
        Main.CreateToolTip(self.buttonpath, text=f"Path: {self.filepath}") 

    # V----- Detect mouse event for tooltip
    def CreateToolTip(self, text):
        """ Function for tooltip """
        toolTip = ToolTip(self)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        self.bind('<Enter>', enter) #Binding enter event to enter function
        self.bind('<Leave>', leave) #Binding leave event to leave function

#-----------------------#
#--------FRAMES---------#
#-----------------------#

class StartPage(tk.Frame):
    def __init__(self,parent,frameName,butonName,destination): 
        tk.Frame.__init__(self,parent)
        self.configure(bg="gray")
        self.button1 = tk.Button(self, height=2, width=15, text ="Read data",command=lambda: frameName.show_frame("pageIDRead"))
        self.button1.pack(anchor="w", padx=(10,10), pady=(10,10))
        self.button2 = tk.Button(self, height=2, width=15, text ="Add data",command=lambda: frameName.show_frame("pageIDAdd"))
        self.button2.pack(anchor="w", padx=(10,10), pady=(10,10))
        self.button3 = tk.Button(self, height=2, width=15, text="Add variable",command=lambda: frameName.show_frame("pageIDDel"))
        self.button3.pack(anchor="w", padx=(10,10), pady=(10,10))
        self.button4 = tk.Button(self, height=2, width=15, text="Driver's Salary",command=lambda: frameName.show_frame("pageIDPay"))
        self.button4.pack(anchor="w", padx=(10,10), pady=(10,10))        
        
class ReadPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        # self.mainframe.configure(bg='red')
        self.mainframe.place(height=500, width=1000)
        self.filepath = ""

        # 1st Frame, interactables
        self.frame1 = Frame(self.mainframe)
        self.frame1.grid(column="0",row="0", ipadx=10, ipady=10,sticky=N)
        self.button = tk.Button(self.frame1,text="Return",command=lambda: frameName.show_frame("pageIDStart"), width=7)
        self.button.pack(anchor="w", pady=(10,30),padx=(65,10))
        self.buttonpath = tk.Button(self.frame1,text="Open file",command=lambda: Main.windowsDialog(self))
        self.buttonpath.pack(anchor="w",padx=(65,10),pady=(0,10))
        self.listBox = Listbox(self.frame1,width=30,height=1)
        self.listBox.pack(anchor="w",padx=(10,10))

        #Dropdown menu for display option
        self.variable = StringVar(self)     
        self.option = ['Driver Log','Driver Productivity','Production Graph']
        self.variable.set('Display Option')

        # Arguments for dropdown menu
        self.optionDP = Frame(self.mainframe)
        self.optionDP.place(relx=0.02, rely=0.35, height=30, width=150)
        self.targetL = tk.Label(self.optionDP, text="Target")
        self.targetL.place(relx=0.1, rely=0.1)
        self.targetE = tk. Entry(self.optionDP, width=10)
        self.targetE.place(relx=0.4, rely=0.1)
        Main.CreateToolTip(self.targetE, text=f"""Takes number of activity desired per choosen interval""")

        popupMenu = OptionMenu(self.frame1, self.variable, *self.option)
        popupMenu.pack(anchor = "w", padx=(45,10), pady=(10,10))
        
        def change_dropdown(*args):
            LD.Load_excel_data(self)

        self.variable.trace('w', change_dropdown)

        # 2nd Frame, data display
        self.frame2 = Frame(self.mainframe)
        self.frame2.place(relx=0.2, rely=0,width=800, height=500)
        self.display = ttk.Treeview(self.frame2)
        self.display.place(relheight=0.9, relwidth=0.9)
        self.scrollx1 = Scrollbar(self.frame2, orient='horizontal', command=self.display.xview)
        self.scrolly2 = Scrollbar(self.frame2, orient='vertical', command=self.display.yview)
        self.display.configure(xscrollcommand=self.scrollx1.set, yscrollcommand=self.scrolly2.set)
        self.scrollx1.pack(side="bottom", fill="x") 
        self.scrolly2.pack(side="right", fill="y")
        
class AddPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.place(height=500,width=1000)
        # self.mainframe.configure(bg="red")

        #1st Frame, data entry
        self.frame1 = Frame(self.mainframe)
        self.frame1.place(relx=0,rely=0,height=250,width=500)
        self.filepath = ""
        self.configure(bg="gray")
        self.label1 = Label(self.frame1, text="Name")
        self.label1.grid(column=0,row=0,padx=(10,10),pady=(10,10))   
        self.entry1 = Entry(self.frame1, width=30)
        self.entry1.grid(column=1, row=0,padx=(10,10),pady=(10,10))
        self.label2 = Label(self.frame1, text="Route")
        self.label2.grid(column=0, row=1,padx=(10,10),pady=(10,10))
        self.entry2 = Entry(self.frame1, width=30)
        self.entry2.grid(column=1,row=1,padx=(10,10),pady=(10,10))
        self.label3 = Label(self.frame1,text="Vehicle Type")
        self.label3.grid(column=0,row=2,padx=(10,10),pady=(10,10))
        self.entry3 = Entry(self.frame1, width=30)
        self.entry3.grid(column=1,row=2,padx=(10,10),pady=(10,10))
        self.buttonpath = tk.Button(self.frame1,text="Open file",command=lambda: Main.windowsDialog(self))
        self.buttonpath.grid(column=0,row=3,padx=(10,0),pady=(20,10))
        self.listBox = Listbox(self.frame1,width=40,height=1)
        self.listBox.grid(column=1,row=3,padx=(0,0),pady=(20,10))

        self.buttonadd = Button(self.frame1,text="Add", width=4, command=lambda: LD.post(self,
        self.entry1.get(),
        self.entry2.get(),
        self.entry3.get()
        )) #Passing all the entry into post function in LoadData File
        self.buttonadd.grid(column=3,row=2, padx=(10,10), pady=(10,10))

        self.buttonload = Button(self.frame1,text="Load", width=8, command=self.Load)
        self.buttonload.grid(column=1,row=4 ,padx=(0,80) ,pady=(10,10))
        self.buttonremove = Button(self.frame1,text="Remove", width=8, command=self.Delete)
        self.buttonremove.grid(column=1,row=4 ,padx=(80,0) ,pady=(10,10))
        
    #2nd Frame, Draft table
        self.frame2 = Frame(self.mainframe)
        self.frame2.place(relx=0.5,rely=0,height=250,width=500)
        self.displayDraft = ttk.Treeview(self.frame2, column=("Name","Vehicle","Route","Date"))
        self.displayDraft.place(relheight=0.9, relwidth=0.8)
        self.displayDraft.bind('<Delete>', self.delete) #Bind Delete key to delete function
        self.button = Button(self.frame2,text="Post", command=self.transfer)
        self.button.place(relx=0.8,rely=0.8)

    #3rd Frame, Actual table
        self.frame3 = Frame(self.mainframe)
        self.frame3.place(relx=0.05, rely=0.5, height=250, width=1000)
        self.display = ttk.Treeview(self.frame3, column=("Name","Vehicle","Route","Date"))
        self.display.place(relheight=0.9, relwidth=0.85)
        self.savebutton = Button(self.frame3, text="Save", command=self.Save)
        self.savebutton.place(rely=0.8,relx=0.85)

    def delete(self, event=None): #suppose to be in the LoadData.py
        self.Selected = self.displayDraft.focus() #This will store focused item into the attribute 
        self.displayDraft.delete(self.Selected) #This will delete the focused item
    #Should've use lambda but didn't
    def Load(self):
        LD.misc_load(self)
    def Delete(self):
        LD.clear_data(self)
        self.listBox.delete(0)
    def Save(self):
        saveDialog(self)
    def transfer(self):
        LD.transferdata(self)

class DelPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.place(height=500,width=1000)
        # self.mainframe.configure(bg="red")
        self.returnbutton = Button(self.mainframe,text="Return",command=lambda: frameName.show_frame("pageIDStart"), width=7)
        self.returnbutton.place(relx=0.03,rely=0.015)
        self.savebutton = Button(self.mainframe,text="Save variable", command=lambda: SaveVar(self))
        self.savebutton.place(relx=0.1, rely=0.015)
        self.savenameL = Label(self.mainframe, text="Variable name")
        self.savenameL.place(relx=0.2, rely=0.02)
        self.savenameE = Entry(self.mainframe)
        self.savenameE.place(relx=0.3, rely=0.02)

        # Frame for streak variable
        self.frameStreak= Frame(self.mainframe,borderwidth=2, relief="groove")
        self.frameStreak.place(relx=0.03, rely= 0.085, relwidth=0.45, relheight=0.4)
        self.label = Label(self.frameStreak,text="Streak modifier")
        self.label.place(relx=0.05,rely=0)
        self.label2 = Label(self.frameStreak, text="Category 1-3")
        self.label2.place(relx=0.1, rely=0.3)
        self.label3 = Label(self.frameStreak, text="Category 4-5")
        self.label3.place(relx=0.1, rely=0.5)
        self.label4 = Label(self.frameStreak, text="Category 6 Up")
        self.label4.place(relx=0.1, rely=0.7)
        self.streakA = Entry(self.frameStreak)
        self.streakA.place(relx=0.5, rely=0.3)
        self.streakB = Entry(self.frameStreak)
        self.streakB.place(relx=0.5, rely=0.5)
        self.streakC = Entry(self.frameStreak)
        self.streakC.place(relx=0.5, rely=0.7)

        # Frame for base wage 
        self.frameWage = Frame(self.mainframe,borderwidth=2, relief="groove")
        self.frameWage.place(relx=0.50, rely=0.085, relwidth=0.45, relheight=0.4)
        self.label = Label(self.frameWage,text="Base Wage")
        self.label.place(relx=0.05,rely=0)
        self.label2 = Label(self.frameWage,text="Base Wage")
        self.label2.place(rely=0.45,relx=0.1,)
        self.baseWage = Entry(self.frameWage, width=40)
        self.baseWage.place(rely=0.45,relx=0.3)

        # Frame for route variable
        self.frameRoute = Frame(self.mainframe,borderwidth=2, relief="groove")
        self.frameRoute.place(relx=0.03, rely=0.52, relwidth=0.45, relheight=0.4)
        self.label = Label(self.frameRoute,text="Route modifier")
        self.label.place(relx=0.05,rely=0)
        self.label1 = Label(self.frameRoute, text="Route")
        self.label1.place(relx=0.1, rely=0.2)
        self.route = Entry(self.frameRoute)
        self.route.place(relx=0.3, rely=0.2)
        self.label2 = Label(self.frameRoute, text="Modifier")
        self.label2.place(relx=0.1, rely=0.4)
        self.routeM = Entry(self.frameRoute)
        self.routeM.place(relx=0.3, rely=0.4)
        self.buttonPost = Button(self.frameRoute,text="Post",command=lambda: LD.varPostR(self, self.route.get(), self.routeM.get()))
        self.buttonPost.place(relx=0.87, rely=0.38)

        self.varDispR = ttk.Treeview(self.frameRoute, column=("Route","Modifier"))
        self.varDispR.place(relx=0.05, rely=0.55, relheight=0.4, relwidth=0.9)

        # Frame for vehicle
        self.frameVehicle = Frame(self.mainframe,borderwidth=2, relief="groove")
        self.frameVehicle.place(relx=0.50, rely=0.52, relwidth=0.45, relheight=0.4)
        self.label = Label(self.frameVehicle,text="Vehicle modifier")
        self.label.place(relx=0.05,rely=0)
        self.label1 = Label(self.frameVehicle, text="Vehicle")
        self.label1.place(relx=0.1, rely=0.2)
        self.vehicle = Entry(self.frameVehicle)
        self.vehicle.place(relx=0.3, rely=0.2)
        self.label2 = Label(self.frameVehicle, text="Modifier")
        self.label2.place(relx=0.1, rely=0.4)
        self.vehicleM = Entry(self.frameVehicle)
        self.vehicleM.place(relx=0.3, rely=0.4)
        self.buttonPost = Button(self.frameVehicle,text="Post", command=lambda: LD.varPostV(self, self.vehicle.get(), self.vehicleM.get()))
        self.buttonPost.place(relx=0.87, rely=0.38)

        self.varDispV = ttk.Treeview(self.frameVehicle, column=("Vehicle","Modifier"))
        self.varDispV.place(relx=0.05, rely=0.55, relheight=0.4, relwidth=0.9)

class PayPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.place(relx=0, rely=0, width=1000, height=500)
        self.returnbutton = Button(self.mainframe,text="Return",command=lambda: frameName.show_frame("pageIDStart"), width=7)
        self.returnbutton.place(relx=0.03,rely=0.015)

        arr = os.listdir('Driver-Log-Recorder---Final-Project/Saved variable')
        self.variable = StringVar(self)     
        self.option = arr
        
        popupMenu = OptionMenu(self.mainframe, self.variable, *self.option)
        popupMenu.place(relx= 0.03, rely=0.090, relwidth=0.1)
        def change_dropdown(*args):
            LD.Setpath(self)
        self.variable.trace('w', change_dropdown)
        self.variable.set('Variable')

        self.driverNameL = Label(self.mainframe, text="Driver's name")
        self.driverNameL.place(relx=0.03, rely=0.2)
        self.driverNameE = Entry(self.mainframe)
        self.driverNameE.place(relx=0.13, rely=0.2)
        self.driverNameB = Button(self.mainframe, text="Load", command= lambda: LD.LoadPay(self, self.driverNameE.get()))
        self.driverNameB.place(relx= 0.27, rely=0.191)
        self.buttonpath = tk.Button(self.mainframe,text="Open file",command=lambda: Main.windowsDialog2(self))
        self.buttonpath.place(relx=0.15, rely=0.096)

        # Log
        self.framelog = Frame(self.mainframe, borderwidth=2, relief="groove")
        self.framelog.place(relx=0.03, rely=0.25, width=280, height=370)
        self.logL = Label(self.framelog, text="Driver's Log")
        self.logL.place(relx=0.05,rely=0)
        self.display = ttk.Treeview(self.framelog, column=("Route", "Vehicle", "Date"))
        self.display.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        # Paycheck
        self.framepay = Frame(self.mainframe, borderwidth=2, relief="groove")
        self.framepay.place(relx=0.32, rely=0.1, relwidth=0.675, relheight=0.89)

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="white", relief=SOLID, borderwidth=1,
                      font=("calibri", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

if __name__ == "__main__":    
    root = Main()
    root.mainloop()