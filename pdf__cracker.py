from tkinter import *
from tkinter import filedialog, messagebox
import os

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('PDF CRACKER')
        self.root.geometry('700x400')

        self.currentDir = StringVar()
        self.currentDir.set(os.getcwd())

        self.entry = Entry(self.root,textvariable=self.currentDir,width=116)
        self.entry.place(x=0,y=0)

        self.root.mainloop()

if __name__=='__main__':
    App()
