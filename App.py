from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk
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
        self.resizable(width=False, height=False)
        # iconpath = PhotoImage(file = 'C:/Users/afu/Desktop/tk/Git.png')
        # program.iconphoto(False, iconpath)

        # ----- Menubar ----- #
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Main Menu", command=lambda: self.show_frame("pageIDStart"))
        menubar.add_cascade(label="Shortcut", menu=filemenu)
        self.config(menu=menubar)

        # ----- Making Frames ----- #

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True) # args make screen expand to the bottom and fill the screen

        container.grid_rowconfigure(0,weight=1) 
        container.grid_columnconfigure(0,weight=1)

        self.frames = {} # <----- The dictionary

        frame_menu = StartPage(container,self,"pageIDStart","pageone")
        frame_read = ReadPage(container,self)

        # V ----- Add frames to dictionary ----- # 

        self.frames["pageIDStart"] = frame_menu
        self.frames["pageIDRead"] = frame_read

        frame_menu.grid(row=0,column=0,sticky="nsew")
        frame_read.grid(row=0,column=0,sticky="nsew")

        self.show_frame("pageIDStart") # The first page to show when running the app

    # V ----- Change frame ----- #
    def show_frame(self,dest): # dest will take destination as an argument
        frame = self.frames[dest]
        frame.tkraise() # raise the destination frame 

    # V----- Open Dialog to open the xlsx file ----- #
    def windowsDialog(self):
        """ Function to call windows dialog """ 
        loc = askopenfilename(title='Please choose an .xlsx file')
        self.filepath = loc
        # Main.CreateToolTip(self.buttonpath, text=f"Path: {self.filepath}")

    def windowsDialog2(self):
        """ Function to call windows dialog """ 
        loc = askopenfilename(title='Please choose an .xlsx file')
        self.filepath = loc
        Main.CreateToolTip(self.buttonpath, text=f"Path: {self.filepath}") 

    # V----- Detect mouse event for tooltip
    def CreateToolTip(self, text):
        """ Function for tooltip (self, text to show) """
        toolTip = ToolTip(self)
        def enter(event):
            toolTip.showtip(text)
        def leave(event):
            toolTip.hidetip()
        self.bind('<Enter>', enter) # Binding enter event to enter function
        self.bind('<Leave>', leave) # Binding leave event to leave function

#-----------------------#
#--------FRAMES---------#
#-----------------------#

class StartPage(tk.Frame):
    def __init__(self,parent,frameName,butonName,destination): 
        tk.Frame.__init__(self,parent)
        self.configure(bg="#1f1f1f")

        self.image = Image.open("Driver-Log-Recorder---Final-Project/Graphic asset/Overview.png")
        self.image = self.image.resize((300, 300), Image.ANTIALIAS)
        self.photo_a = ImageTk.PhotoImage(self.image)
        self.image = Image.open("Driver-Log-Recorder---Final-Project/Graphic asset/Data.png")
        self.image = self.image.resize((300, 300), Image.ANTIALIAS)
        self.photo_b = ImageTk.PhotoImage(self.image)
        self.image = Image.open("Driver-Log-Recorder---Final-Project/Graphic asset/Salary.png")
        self.image = self.image.resize((300, 300), Image.ANTIALIAS)
        self.photo_c = ImageTk.PhotoImage(self.image)

        self.button1 = Label(self, image = self.photo_a, highlightthickness = 0, bd = 0)
        self.button1.place(relx = 0.025, rely = 0.05)
        self.button1.bind('<Button-1>', lambda argument: frameName.show_frame("pageIDRead"))
        self.button2 = Label(self, image = self.photo_b, highlightthickness = 0, bd = 0)
        self.button2.place(relx = 0.350, rely = 0.05)
        self.button2.bind('<Button-1>', lambda argument: frameName.show_frame("pageIDData"))
        self.button3 = Label(self, image = self.photo_c, highlightthickness = 0, bd = 0)
        self.button3.place(relx = 0.675, rely = 0.05)
        self.button3.bind('<Button-1>', lambda argument: frameName.show_frame("pageIDSalary")) 
        
class ReadPage(tk.Frame):
    def __init__(self,parent,frameName):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.configure(bg='#1f1f1f')
        self.mainframe.place(height=500, width=1000)
        self.filepath = ""

        # 1st Frame, interactables
        self.frame1 = Frame(self.mainframe)
        self.frame1.configure(bg='#1f1f1f')
        self.frame1.place(relx=0, rely=0, width=170, height=500)
        self.image = Image.open("Driver-Log-Recorder---Final-Project/Graphic asset/OpenFile.png")
        self.image = self.image.resize((131 , 36), Image.ANTIALIAS)
        self.photo_Open = ImageTk.PhotoImage(self.image)
        self.selectFile = Label(self.frame1, image=self.photo_Open)
        self.selectFile.config(bg="#1f1f1f")
        self.selectFile.place(relx = 0.15, rely = 0.05)
        self.selectFile.bind('<Button-1>', Main.windowsDialog)

        # Dropdown menu for display option
        self.variable = StringVar()
        self.dropdown = ttk.Combobox(self.frame1, textvariable = self.variable, width=15)

        # List of options
        self.dropdown['values'] = (
            "Entry Data",
            "Attendance",
            "Summary",
            "Profit"
        )
        self.dropdown.place(relx=0.16, rely=0.15)
        self.dropdown.current(0)
        
        def change_dropdown(*args):
            # LD.Load_excel_data(self)
            print(self.variable.get())

        self.variable.trace('w', change_dropdown) # detect if there is any changes

        # 2nd Frame, data display
        self.frame2 = Frame(self.mainframe)
        self.frame2.configure(bg='#4D201A')
        self.frame2.place(relx=0.17, rely=0, width=830, height=500)
        

class ToolTip(object): # Praise Stackoverflow for this class https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
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