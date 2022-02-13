
from tkinter import filedialog as fd
from tkinter import *
from tkinter import Toplevel
import pandas as pd
import numpy as np
import os
import tkinter.font as tkFont


class MainApplication:
    #init function
    def __init__(self, master):
        self.master = master
        #Sets title of app window
        master.title("Edit CSV")

        self.dir_path = StringVar(master)
        self.col = StringVar(master)
        self.row = StringVar(master)

        self.fontStyle = tkFont.Font(family="Arial", size=12)
        self.fontStyle2 = tkFont.Font(family="Arial", size=8)
        self.fontStyle3 = tkFont.Font(family="Arial", size=10)


        self.welcome = Label(master, text='Edit CSV file', font=self.fontStyle).grid(row=0, column=1)
        self.open_file = Button(master, text="Open File", command=self.show_file_browser).grid(row=1, column = 0, padx=10)
        self.header_window = Button(master, text="Add Column", command= lambda: self.create_window(master)).grid(row=1, column=1, padx=10)
        self.quit_b = Button(master, text='Exit', width = 7,height=1, command = quit).grid(row=1, column = 2, padx=10)
        self.filepathText = Label(master, textvariable = self.dir_path, font=self.fontStyle2).grid(rowspan=4, columnspan=3)
        self.row_list = []

    

        
    def create_window(self, master):

        self.window = Toplevel(master)
        self.enter_label = Label(self.window, text = 'Add/Select Column:', font=self.fontStyle3).grid(row=0)
        self.user_label = Label(self.window, textvariable = self.col, font=self.fontStyle3).grid(row=2)

        self.entry= Entry(self.window)
        self.submit = Button(self.window,text='Submit', command= lambda: self.add_header(master))

        self.entry.grid(row=0, column=1)
        self.submit.grid(row=1)

    

    def show_file_browser(self):
            self.filename = fd.askopenfilename()
            self.dir_path.set(self.filename)
            return self.filename
    
    def add_header(self, master):
        #file = pd.read_csv()
        self.col.set(self.entry.get())

        if os.stat(self.filename).st_size==0:
            print('pls')
            self.df = pd.DataFrame()
            self.df[self.entry.get()] = pd.Series(dtype='str')
            self.df.to_csv(self.filename, index = False)
        else:
            self.df = pd.read_csv(self.filename)
            self.df[self.entry.get()] = np.nan
            self.df.to_csv(self.filename, index = False)
        
        
        self.row_wind = Toplevel(master)
        self.row_label = Label(self.row_wind, text = 'Add Row:').grid(row=0)
        self.user_label = Label(self.row_wind, textvariable = self.row, font=self.fontStyle3).grid(row=2)

        self.row_entry= Entry(self.row_wind)
        self.input_row = Button(self.row_wind,text='Add Row', command=self.add_row)
        self.submit_row = Button(self.row_wind,text='Submit', command = self.submit_row_entry)
        
        self.row_entry.grid(row=0, column=1)
        self.input_row.grid(row=1, column = 0)
        self.submit_row.grid(row=1, column =1)
        

    
    def add_row(self):
        self.row.set(self.row_entry.get())
        self.row_list.append(self.row_entry.get())
        return self.row_list


    def submit_row_entry(self):
        self.df = pd.read_csv(self.filename)
        self.df[self.entry.get()] = pd.Series(self.row_list)
        self.df.to_csv(self.filename, index = False)



if __name__ == '__main__':
    root = Tk()
    root.geometry("260x100")
    my_gui = MainApplication(root)
    root.mainloop()


