from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter as tk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # ----- Screen res and title ----- #
        self.geometry("1000x500")
        self.title("Project")

        # ----- Menubar ----- #
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Blank")
        menubar.add_cascade(label="File", menu=filemenu)
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
        loc = askopenfilename(title='Please choose an .xlsx file')
        self.filepath = loc
        self.listBox.insert("end",self.filepath)
        Main.CreateToolTip(self.button1, text=f"Path: {self.filepath}")

    # V----- Detect mouse event for tooltip
    def CreateToolTip(self, text):
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
        self.button3 = tk.Button(self, height=2, width=15, text="Delete data",command=lambda: frameName.show_frame("pageIDDel"))
        self.button3.pack(anchor="w", padx=(10,10), pady=(10,10))
        
class ReadPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.grid(column=0,row=0)

        # SubFrame for interactables
        self.frame1 = Frame(self.mainframe)
        self.frame1.grid(column="0",row="0", ipadx=10, ipady=10)
        self.filepath = ""
        self.configure(bg="gray")
        self.button = tk.Button(self.frame1,text="Return",command=lambda: frameName.show_frame("pageIDStart"), width=7)
        self.button.pack(anchor="w", pady=(10,30),padx=(65,10))
        self.button1 = tk.Button(self.frame1,text="Open file",command=lambda: Main.windowsDialog(self))
        self.button1.pack(anchor="w",padx=(65,10),pady=(0,10))
        self.listBox = Listbox(self.frame1,width=30,height=1)
        self.listBox.pack(anchor="w",padx=(10,10))

        self.variable = StringVar(self)    #Dropdown menu for filter 
        self.option = ['Driver Log','Driver Productivity','Production Graph']
        self.variable.set('Select Filter')

        popupMenu = OptionMenu(self.frame1, self.variable, *self.option)
        popupMenu.pack(anchor = "w", padx=(45,10), pady=(10,10))
        
        def change_dropdown(*args):
            print(self.variable.get())

        self.variable.trace('w', change_dropdown)

        # SubFrame for displaying data
        self.frame2 = Frame(self.mainframe)
        self.frame2.grid(column="1",row="0",ipady=(30))
        self.listBox1 = Listbox(self.frame2,width=120)
        self.listBox1.pack(padx=(0,50),pady=(10,0))

class AddPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.filepath = ""
        self.configure(bg="gray")
        self.button = tk.Button(self,text="Go back",command=lambda: frameName.show_frame("pageIDStart"))
        self.button.pack()      
        self.button1 = tk.Button(self,text="Open file",command=lambda: Main.windowsDialog(self))
        self.button1.pack()

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
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("calibri", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def placeholder():
    pass
        
root = Main()
root.mainloop()
