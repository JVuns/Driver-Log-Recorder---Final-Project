import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *

w = OptionMenu(master, variable, "one", "two", "three")  
w.config(bg = "GREEN")  # Set background color to green

# Set this to what you want, I'm assuming "green"...
w["menu"].config(bg="GREEN")

w.pack()  