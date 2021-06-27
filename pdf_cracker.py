#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog, messagebox
import Pmw
import os


class App:
    def __init__(self):
        self.root = Pmw.initialise(fontScheme = 'pmw1')
        self.root.title('PDF CRACKER')
        self.root.geometry('945x480')

        self.main_display = Pmw.ScrolledText(self.root,text_width=62,text_height=20,hscrollmode='none')
        self.main_display.place(x=10,y=25)
        self.second_display = Pmw.ScrolledText(self.root,text_width=36,text_height=23,vscrollmode='dynamic')
        self.second_display.place(x=599,y=25)

        self.root.mainloop()

if __name__=='__main__':
    App()



