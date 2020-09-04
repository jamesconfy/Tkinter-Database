from tkinter import *
        
class CreateLabel():
    def __init__(self, root1, text1=None, row1=0, column1=0, columnspan1=0, width1=20, bg1='#66ccff', fg1='#666', sticky1='we', pady1=1, padx1=1, relief='flat'):
        self.label = Label(root1, text=text1, width=width1, bg=bg1, fg=fg1)
        self.label.grid(row=row1, column=column1, padx=padx1, pady=pady1, sticky=sticky1)

class EntryBox():
    def __init__(self, root1,  row1=0, column1=0, columnspan1=0, width1=15, sticky1='we', pady1=1, padx1=1, relief='flat'):
        self.entry = Entry(root1, width=width1)
        self.entry.grid(row=row1, column=column1, padx=padx1, pady=pady1, sticky=sticky1)
        self.entry.grid_columnconfigure(row1, weight=1)
        self.entry.grid_rowconfigure(column1, weight=1)

    def getvalue(self):
        return self.entry.get()

    def deletevalue(self):
        self.entry.delete(0, END)

class CreateButton():
    def __init__(self, root1, text1=None, command1=None, row1=0, column1=0, columnspan1=0, pady1=1, padx1=1, ipadx1=100, ipady1=100, width1=15, bg1='#66ccff', fg1='#666', sticky1='we', relief='flat', height1=None, activebackground1='white', activeforeground1='red'):
        self.button = Button(root1, text=text1,command=command1, width=width1, height=height1, bg=bg1, fg=fg1, activebackground=activebackground1, activeforeground=activeforeground1)
        self.button.grid(row=row1, column=column1, columnspan=columnspan1, padx=padx1, pady=pady1, ipadx=ipadx1, ipady=ipady1, sticky=sticky1)
        self.button.grid_columnconfigure(row1, weight=1)
        self.button.grid_rowconfigure(column1, weight=1)

