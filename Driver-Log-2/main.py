from tkinter import *
import numpy as np
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
import ReadLog as RL
import pandas as pd

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # ----- Screen res and title ----- #
        self.geometry("1000x350")
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
        frame_datavar = DataPage(container, self)
        frame_salary = SalaryPage(container, self)

        # V ----- Add frames to dictionary ----- # 

        self.frames["pageIDStart"] = frame_menu
        self.frames["pageIDRead"] = frame_read
        self.frames["pageIDData"] = frame_datavar
        self.frames["pageIDSalary"] = frame_salary

        frame_menu.grid(row=0,column=0,sticky="nsew")
        frame_read.grid(row=0,column=0,sticky="nsew")
        frame_datavar.grid(row=0,column=0,sticky="nsew")
        frame_salary.grid(row=0, clumn=0,sticky="nsew")

        self.show_frame("pageIDStart") # The first page to show when running the app

    # V ----- Change frame ----- #
    def show_frame(self,dest): # dest will take destination as an argument
        if dest == "pageIDStart":
            self.geometry("1000x350")
        else:
            self.geometry("1000x500")
        frame = self.frames[dest]
        frame.tkraise() # raise the destination frame 

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

    def popup(self, popId, string):
        MsgBox = tk.messagebox.askquestion ('Overwrite',f'Are you sure you want to overwrite the {string} files',icon = 'warning')
        if MsgBox == 'yes':
            confirmation = True
            return confirmation

#-----------------------#
#--------FRAMES---------#
#-----------------------#

class StartPage(tk.Frame):
    def __init__(self,parent,frameName,butonName,destination): 
        tk.Frame.__init__(self,parent)
        self.configure(bg="#1f1f1f")

        self.image = Image.open("Driver-Log-2/Graphic asset/Overview.png")
        self.image = self.image.resize((300, 300), Image.ANTIALIAS)
        self.photo_a = ImageTk.PhotoImage(self.image)
        self.image = Image.open("Driver-Log-2/Graphic asset/Data.png")
        self.image = self.image.resize((300, 300), Image.ANTIALIAS)
        self.photo_b = ImageTk.PhotoImage(self.image)
        self.image = Image.open("Driver-Log-2/Graphic asset/Salary.png")
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
        # V----- Open Dialog to open the xlsx file ----- #
    def windowsDialog(self, *arg):
        """ Function to call windows dialog """ 
        loc = askopenfilename(title='Please choose an .xlsx file')
        self.filepath = loc       
        
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
        self.image = Image.open("Driver-Log-2/Graphic asset/OpenFile.png")
        self.image = self.image.resize((131 , 36), Image.ANTIALIAS)
        self.photo_Open = ImageTk.PhotoImage(self.image)
        self.selectFile = Label(self.frame1, image=self.photo_Open)
        self.selectFile.config(bg="#1f1f1f")
        self.selectFile.place(relx = 0.15, rely = 0.05)
        self.selectFile.bind('<Button-1>', self.windowsDialog)

        # Dropdown menu for display option
        self.variable = StringVar()
        self.dropdown = ttk.Combobox(self.frame1, state="readonly", textvariable = self.variable, width=15)
        
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
            RL.Vizu(self, self.variable.get(), self.filepath)

        self.variable.trace('w', change_dropdown) # detect if there is any changes

        # 2nd Frame, data display

        self.frame2 = Frame(self.mainframe)
        self.frame2.configure(bg='#4D201A')
        self.frame2.place(relx=0.17, rely=0, width=830, height=500) 

class DataPage(tk.Frame):
    def __init__(self,parent,frameName):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("mystyle.Treeview", background='#9c9c9c', fieldbackground='#9c9c9c', indent=15, highlightthickness=0, bd=0, font=('Calibri', 8)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 8,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        style.map('mystyle.Treeview', background=[('selected','blue')])

        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.configure(bg='#1f1f1f')
        self.mainframe.place(height=500, width=1000)

        self.frame1 = Frame(self.mainframe)
        self.frame1.configure(bg='#1f1f1f')
        self.frame1.place(relx=0, rely=0, relwidth=0.3, relheight=1)

        #Loader dropdown 
        self.variable = StringVar()
        self.dropdown = ttk.Combobox(self.frame1, state="readonly", textvariable = self.variable, width=20)

        # List of options
        dirlist = os.listdir('Driver-Log-2/DataStore')
        self.dropdown['values'] = (dirlist)
        self.dropdown.place(relx=0.16, rely=0.15)
        try: 
            self.dropdown.current(0)
        except TclError:
            pass
        
        self.dropdown.set('Choose file to load')

        def change_dropdown(*args):
            for i in self.display.get_children():
                self.display.delete(i)
            data = RL.getfile(f'Driver-Log-2/DataStore/{self.variable.get()}')
            data = data.replace(np.nan, regex=True).to_numpy().tolist()
            for row in data:
                self.display.insert("", "end", values=row)
            self.nData.insert(0, self.variable.get())

        self.variable.trace('w', change_dropdown) # detect if there is any changes
        
        self.dropdown.place(relx=0.1, rely=0.2)

        #Initialize all widgets here
        self.nData_ = Label(self.frame1, text="Pricing Group", width=10)
        self.retasi_ = Label(self.frame1, text="Retasi", width=10)
        self.lokasi_ = Label(self.frame1, text="Lokasi", width=10)
        self.type_ = Label(self.frame1, text="Type", width=10)
        self.harga_ = Label(self.frame1, text="Harga", width=10)
        
        self.nData = Entry(self.frame1)
        self.retasi = Entry(self.frame1)
        self.lokasi = Entry(self.frame1)
        self.type = Entry(self.frame1)
        self.harga = Entry(self.frame1)

        self.postButton = Button(self.frame1, width=10, text='Add to List', command=lambda: toTree(self, 
                                                            self.retasi.get(), 
                                                            self.lokasi.get(),
                                                            self.type.get(),
                                                            self.harga.get()))

        self.saveButton = Button(self.frame1, width=10, text='Save list', command=lambda: saveDialog(self,
                                                            self.nData.get()))

        #Place widgets here
        self.nData_.place(relx=0.1, rely=0.275)
        self.retasi_.place(relx=0.1, rely=0.35)
        self.lokasi_.place(relx=0.1, rely=0.425)
        self.type_.place(relx=0.1, rely=0.5)
        self.harga_.place(relx=0.1, rely=0.575)

        self.nData.place(relx=0.4, rely=0.275)
        self.retasi.place(relx=0.4, rely=0.35)
        self.lokasi.place(relx=0.4, rely=0.425)
        self.type.place(relx=0.4, rely=0.5)
        self.harga.place(relx=0.4, rely=0.575)

        self.postButton.place(relx=0.4, rely=0.675)
        self.saveButton.place(relx=0.1, rely=0.675)
        
        self.frame2 = Frame(self.mainframe)
        self.frame2.configure(bg='#4D201A')
        self.frame2.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.display = ttk.Treeview(self.frame2, style='mystyle.Treeview')
        self.display.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)
        self.display['show'] = 'headings'
        self.display['columns'] = ("Retasi","Lokasi", "Type", "Harga")
        self.display.bind('<Delete>', lambda x: delete(self))

        self.display.column('0', width=50, minwidth=50)
        self.display.column('1', width=50, minwidth=50)
        self.display.column('2', width=50, minwidth=50)
        self.display.column('3', width=50, minwidth=50)

        self.display.heading('0', text='Retasi')
        self.display.heading('1', text='Lokasi')
        self.display.heading('2', text='Type')
        self.display.heading('3', text='Harga')

        #all commands down here
        def toTree(self, retasi, lokasi, type, harga):
            self.display.insert("", "end", values=(retasi, lokasi, type, harga))

        def delete(self, event=None):
            self.Selected = self.display.focus() #This will store focused item into the attribute 
            self.display.delete(self.Selected) #This will delete the focused item

        def saveDialog(self, name):
            '''Saving data from add page in form of excel file'''
            dirlist = os.listdir('Driver-Log-2/DataStore')
            values = []
            for child in self.display.get_children():
                values.append(self.display.item(child)["values"] ) # appending the value of treeview, ["values"] will append the value without datatype information
            df = pd.DataFrame(values)
            df.columns = ["Retasi", "Lokasi", "Type", "Harga"]
            filepath = f'Driver-Log-2/DataStore/{name}.xlsx'
            filename = f"{name}.xlsx"
            print(filepath)
            print(dirlist)

            if filename in dirlist:
                confirmation = False
                print("Yes")
                Main.popup(self, 'overwritefile', filename)
                if confirmation == True:
                    df.to_excel(filepath, index=False, header=True)
                else:
                    pass
            else:
                df.to_excel(filepath, index=False, header=True)
            dirlist = os.listdir('Driver-Log-2/DataStore')
            self.dropdown['values'] = (dirlist)
            
class SalaryPage(tk.Frame):
    def __init__(self,parent,framename):
        tk.Frame.__init__(self,parent)
        self.mainframe = Frame(self)
        self.mainframe.configure(bg='#1f1f1f')
        self.mainframe.place(height=500, width=1000)
        self.filepath = ""

        #Frame 1
        self.frame2 = Frame(self.mainframe)
        

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