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
        self.root.geometry('779x480')

        self.main_display = Pmw.ScrolledText(self.root,text_width=64,text_height=20)
        self.main_display.place(x=10,y=0)

        self.root.mainloop()

if __name__=='__main__':
    App()


