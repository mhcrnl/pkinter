import tkinter as tk
from tkinter import ttk

#link

__title__ = "Toolbar"
__version__ = "1.0.0"
__author__ = "DeflatedPickle"

class Toolbar (ttk.Frame):
    """
            -----DESCRIPTION-----

            -----USAGE-----

            -----CONTENTS-----
    ---VARIABLES---

    ---WIDGETS---
    Self

    ---FUNCTIONS---
    """
    def __init__ (self, parent, *args):
        ttk.Frame.__init__ (self, parent, *args)

    def add_button (self, text = "", image = "", side = "left"):
        ttk.Button (self, text = text, image = image, style = "Toolbutton").pack (side = side)

    def add_checkbutton (self, text = "", image = "", variable = "", side = "left"):
        ttk.Checkbutton (self, text = text, image = image, variable = variable, style = "Toolbutton").pack (side = side)

    def add_radiobutton (self, text = "", image = "", variable = "", value = "", side = "left"):
        ttk.Radiobutton (self, text = text, image = image, variable = variable, value = value, style = "Toolbutton").pack (side = side)

    def add_separator (self):
        ttk.Separator (self, orient = "vertical").pack (side = "left", fill = "y", padx = 3, pady = 1)

##################################################

if __name__ == "__main__":
    root = tk.Tk ()
    tbar = Toolbar (root)
    tbar.pack (expand = True, fill = "x", padx = 5, pady = 5)
    tbar.add_button (text = "A Button")
    variable1 = tk.IntVar ()
    variable2 = tk.IntVar ()
    tbar.add_checkbutton (text = "Check", variable = variable1)
    tbar.add_checkbutton (text = "Check", variable = variable2)
    tbar.add_separator ()
    variable3 = tk.IntVar ()
    tbar.add_radiobutton (text = "One", variable = variable3, value = 0)
    tbar.add_radiobutton (text = "Two", variable = variable3, value = 1)
    tbar.add_radiobutton (text = "Three", variable = variable3, value = 2)
    tbar.add_separator ()
    tbar.add_button (text = "Right", side = "right")
    root.mainloop ()
