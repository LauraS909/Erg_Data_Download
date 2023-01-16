"""
This program is intended to help me download and import erg data from concept2's website
"""
try:
    import webHandling as wh 
    import htmlParse as parse
    import dataHandling as dh
except ImportError:
    print('Import error in __main__')
#This just handles the gui
try:
    import tkinter as tk
    from tkinter.filedialog import askdirectory
    from tkcalendar import Calendar, DateEntry
except ImportError:
    print('Import Error for GUI')

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text = 'Don\'t press me',
        command=self.quit)
        self.quitButton.grid(column=4)
        
        self.un_label = tk.Label(self, text = 'Gimme your Username')
        self.un_label.grid(column=0)
        self.unVar = tk.StringVar()
        self.un_entry = tk.Entry(self, textvariable=self.unVar)
        self.un_entry.grid(column=0)
        
        self.pw_label = tk.Label(self, text = 'Gimme your Password')
        self.pw_label.grid(column=0)
        self.pwVar = tk.StringVar()
        self.pw_entry = tk.Entry(self, textvariable=self.pwVar)
        self.pw_entry.grid(column=0)

        self.rememberVar = tk.BooleanVar(self)
        self.rememberCB  = tk.Checkbutton(self, text='Remember me',
        variable=self.rememberVar, onvalue='yes', offvalue='no')
        self.rememberCB.grid(row = 5, column=1)

        self.rememberPath = tk.BooleanVar(self)
        self.rememberPathCB  = tk.Checkbutton(self, text='Remember where I stored data the last time',
        variable=self.rememberPath, onvalue='yes', offvalue='no')
        self.rememberPathCB.grid(row = 6, column=1)
        
        def submit(self=self):
            #Triggers submit event outside of the GUI
            return submitB(self)
        
        self.submitButton = tk.Button(self, text = 'Run da program',
        command= submit)
        self.submitButton.grid(column=4)

        self.date = Calendar(master=None)
        cal = DateEntry(self, variable=self.date,width=30,bg="darkblue",fg="white",year=2010)
        cal.grid()


        
        
def submitB(self):
    if not (app.rememberPath):
        path = askdirectory(title='Please Select a destination Folder') # shows dialog box and return the path
    elif(dh.getCred()):
        path = dh.getCred()['csv path']
    else:
        path = askdirectory(title='Please Select a destination Folder') # shows dialog box and return the path
    
    return [self.unVar, self.pwVar,self.rememberVar, self.rememberPath]


app = App()                       
app.master.title('C2 Downloader')
app.mainloop()

