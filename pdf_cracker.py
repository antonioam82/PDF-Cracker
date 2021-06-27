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

        self.root.mainloop()

if __name__=='__main__':
    App()


