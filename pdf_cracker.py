#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as scrolledtext
import os


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('PDF CRACKER')
        self.root.geometry('779x480')

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        self.entry = Entry(self.root,textvariable=self.currentDir,width=129)
        self.entry.place(x=0,y=0)
        self.display = scrolledtext.ScrolledText(self.root,width=64,height=20)
        self.display.place(x=10,y=25)

        self.root.mainloop()

if __name__=='__main__':
    App()