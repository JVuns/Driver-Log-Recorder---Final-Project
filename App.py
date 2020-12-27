from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
import LoadData as LD

class Main(tk.Tk):
    def __init__(self):
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
        frame_delEmployee = Delsub(container,self,"Employee")
        frame_delVechile = Delsub(container,self,"vehicle")

        # V ----- Add frames to dictionary ----- # 

        self.frames["pageIDStart"] = frame_menu
        self.frames["pageIDRead"] = frame_read
        self.frames["pageIDAdd"] = frame_add
        self.frames["pageIDDel"] = frame_del
        self.frames["pageIDEmployeeDel"] = frame_delEmployee
        self.frames["pageIDVehicleDel"] = frame_delVechile

        frame_menu.grid(row=0,column=0,sticky="nsew")
        frame_read.grid(row=0,column=0,sticky="nsew")
        frame_add.grid(row=0,column=0,sticky="nsew")
        frame_del.grid(row=0,column=0,sticky="nsew")
        frame_delEmployee.grid(row=0,column=0,sticky="nsew")
        frame_delVechile.grid(row=0,column=0,sticky="nsew")

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
        
class ReadPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        # self.mainframe.configure(bg='red')
        self.mainframe.place(height=500, width=1000)
        self.filepath = ""

        # SubFrame for interactables
        self.frame1 = Frame(self.mainframe)
        self.frame1.grid(column="0",row="0", ipadx=10, ipady=10,sticky=N)
        self.button = tk.Button(self.frame1,text="Return",command=lambda: frameName.show_frame("pageIDStart"), width=7)
        self.button.pack(anchor="w", pady=(10,30),padx=(65,10))
        self.buttonpath = tk.Button(self.frame1,text="Open file",command=lambda: Main.windowsDialog(self))
        self.buttonpath.pack(anchor="w",padx=(65,10),pady=(0,10))
        self.listBox = Listbox(self.frame1,width=30,height=1)
        self.listBox.pack(anchor="w",padx=(10,10))

        self.variable = StringVar(self)    #Dropdown menu for display option 
        self.option = ['Driver Log','Driver Productivity','Production Graph']
        self.variable.set('Display Option')

        popupMenu = OptionMenu(self.frame1, self.variable, *self.option)
        popupMenu.pack(anchor = "w", padx=(45,10), pady=(10,10))
        
        def change_dropdown(*args):
            LD.Load_excel_data(self)

        self.variable.trace('w', change_dropdown)

        # SubFrame for displaying data
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
        self.mainframe.configure(bg="red")
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
        self.listBox = Listbox(self.frame1,width=50,height=1)
        self.listBox.grid(column=1,row=3,padx=(0,0),pady=(20,10))
        self.button = Button(self.frame1,text="Add", command=lambda: LD.post(self,
        self.entry1.get(),
        self.entry2.get(),
        self.entry3.get()
        ))
        self.button.grid(column=3,row=4, padx=(10,10), pady=(10,10))

        self.frame2 = Frame(self.mainframe)
        self.frame2.place(relx=0.5,rely=0,height=250,width=500)
        self.display = ttk.Treeview(self.frame2)
        self.display.place(relheight=0.9, relwidth=0.9)

class DelPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.button = tk.Button(self,text="Delete employee data",command=lambda: frameName.show_frame("pageIDEmployeeDel"))
        self.button.pack()
        self.button2 = tk.Button(self,text="Delete vehicle data",command=lambda: frameName.show_frame("pageIDVehicleDel"))
        self.button2.pack()

class Delsub(tk.Frame):
    def __init__(self,parent,frameName,subtype):
        tk.Frame.__init__(self,parent)
        self.label = tk.Label(self,text=f"{subtype} page")
        self.label.pack()
        self.button = tk.Button(self,text="Go back",command=lambda: frameName.show_frame("pageIDDel"))
        self.button.pack()

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