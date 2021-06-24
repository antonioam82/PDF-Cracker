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
        self.file_name = StringVar()

        self.canvas = Canvas(self.root,width=217,height=355)
        self.canvas.place(x=550,y=25)
        self.combi = Listbox(self.canvas,width=36,height=22,bg="black")
        self.combi.pack()
        self.entry = Entry(self.root,textvariable=self.currentDir,width=129)
        self.entry.place(x=0,y=0)
        self.display = scrolledtext.ScrolledText(self.root,width=64,height=20)
        self.display.place(x=10,y=25)
        Button(self.root,text="SEARCH",width=10).place(x=10,y=353)
        self.nameEntry = Entry(self.root,textvariable=self.file_name,width=39,font=('Arial',14))
        self.nameEntry.place(x=94,y=353)
        Button(self.root,text='START',width=73).place(x=10,y=390)

        self.root.mainloop()

if __name__=='__main__':
    App()

