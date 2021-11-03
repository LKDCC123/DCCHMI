import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.pyplot import Figure
# import xlrd
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

import base64
from HWbg_png import img as HWb

class DataPloter(tk.Tk):

    def __init__(self):
        super().__init__()
        self.CreateHomeWin()    
        self.plotnum = []
        self.filename_old = ''
        self.filename = ''
    
    def CreateHomeWin(self): # decorate the home window
        # window config
        self.title('DataPloter v1.0 (dat朴素版)')
        self.geometry('350x200')
        self.entryvar = tk.StringVar()
        self.configure(background = 'tan')
        TopFrame = tk.Frame(self, height = 80, bg = 'tan')
        TopFrame.pack(side = tk.TOP)
        
        # decorate
        textsize = 15
        tmp = open('HWbg.png', 'wb')        # build a temp png
        tmp.write(base64.b64decode(HWb))    # uncode the figure into png format
        tmp.close()  
        self.HWbackgroung = tk.PhotoImage(file = 'HWbg.png')
        HWbg = tk.Label(self, relief = 'flat', image = self.HWbackgroung, text = 'Beijing Institute of Technology', justify = 'right', font = ('times', textsize), compound = tk.CENTER, fg = 'wheat', cursor = 'cross')
        HWbg.pack()
        
        # units
        textsize = 11
        HWlabel = tk.Label(TopFrame, relief = 'flat', text = 'File Path:', font = ('times', textsize), bg = 'tan')
        HWentry = tk.Entry(TopFrame, relief = 'groove', textvariable = self.entryvar, font = ('times', textsize), bg = 'wheat', fg = 'saddlebrown', selectbackground = 'darkgoldenrod', selectforeground = 'oldlace')
        HWbutton = tk.Button(TopFrame, relief = 'ridge', command = self.OpenFile, text = 'Select A File', font = ('times', textsize), bg = 'goldenrod', highlightcolor = 'burlywood', activebackground = 'bisque', activeforeground = 'orangered')
        HWplot = tk.Button(TopFrame, relief = 'ridge', command = self.OpenPlot, text = 'Plot', font = ('times', textsize), bg = 'goldenrod', activebackground = 'bisque', activeforeground = 'orangered')        
        
        # place
        HWlabel.grid(row = 0, column = 0, sticky = tk.W)
        HWentry.grid(row = 0, column = 1)
        HWbutton.grid(row = 0, column = 2)
        HWplot.grid(row = 0, column = 3)
        
    def CreateSonWin(self, geometry, title): # creat a new son window
        name = tk.Tk()
        name.geometry(geometry)
        name.title(title)
        return name
        
    def OpenFile(self):
        self.filename = filedialog.askopenfilename(title='Open a File', filetype = [('dat', '*.dat'), ('txt', '*.txt')])# [('xlsx', '*.xlsx')])  # [('dat', '*.dat'), ('txt', '*.txt')])
        if self.filename == self.filename_old:
            messagebox.showwarning('emmm..', message='The Same File Selected!')
        self.entryvar.set(self.filename)        
        if not self.filename:
            messagebox.showwarning('oops!', message='No Valide File Selected!')
            
    def OpenPlot(self):
        if self.filename == '':
            messagebox.showwarning('emmm..', message='No File Selected!')
        elif self.filename == self.filename_old:
            messagebox.showwarning('emmm..', message='You Are Plotting The Same File!')
        else:
            self.plotnum.append(1)
            plottimes = len(self.plotnum)
            if plottimes < 6: # read data and create a new plotloft
                if plottimes == 1:
                    Loft_1 = PlotLoft(self.filename, '1200x600')
                elif plottimes == 2:
                    Loft_2 = PlotLoft(self.filename, '1200x600')
                elif plottimes == 3:
                    Loft_3 = PlotLoft(self.filename, '1200x600')
                elif plottimes == 4:
                    Loft_4 = PlotLoft(self.filename, '1200x600')
                elif plottimes == 5:
                    Loft_5 = PlotLoft(self.filename, '1200x600')
            else:
                messagebox.showwarning('ohhh!', message='No More Files!')
        self.filename_old = self.filename
        
        if plottimes > 0:
            Loft_1.mainloop()
        if plottimes > 1:
            Loft_2.mainloop()
        if plottimes > 2:
            Loft_3.mainloop()
        if plottimes > 3:
            Loft_4.mainloop()
        if plottimes > 4:
            Loft_5.mainloop()
        
class PlotLoft(tk.Toplevel): # Toplevel makes IntVal in sonwindows active
    
    def __init__(self, filename, geometry):
        super().__init__()
        self.CreatPlotWin(filename, geometry)
        
    def CreatPlotWin(self, filename, geometry):
        # txt ---------------------------------------------------------------------------------------
        # self.data = np.loadtxt(filename) # read file
        data = pd.read_table(filename)
        self.data = data.iloc
        # txt ---------------------------------------------------------------------------------------
        # xls ---------------------------------------------------------------------------------------
        # book = pd.read_excel(filename, sheet_name = 0) # read file
        # self.data = book.iloc
        # xls ---------------------------------------------------------------------------------------
        self.title(filename)
        self.geometry(geometry)
        self.configure(background = 'tan')
        self.HomeFrame = tk.Frame(self, width = 200, bg = 'tan', highlightbackground = 'gold')
        self.LeftFrame = tk.Frame(self.HomeFrame, width = 200, bg = 'wheat', highlightbackground = 'gold')
        self.CheckButtonFrame = tk.Frame(self.HomeFrame, width = 200, bg = 'wheat', highlightbackground = 'gold')
        self.MidLine = tk.Frame(self, height = 600, width = 3, bg = 'wheat', highlightbackground = 'gold')
        self.RightText = tk.Label(self, relief = 'flat', text = 'Plot Robotics WithIn Enthusiasm', anchor = 'center', font = ('times', 15), bg = 'tan', fg = 'papayawhip', cursor = 'cross')
        
        # scrollbar
        self.canvas_for_scrollbar = tk.Canvas(self.LeftFrame, width = 200, bg = 'wheat')
        self.ScrollFrame = tk.Frame(self.canvas_for_scrollbar, width = 200, bg = 'wheat')
        self.scrollbar = tk.Scrollbar(self.LeftFrame, relief = 'ridge', width = 28, orient = 'vertical', bg = 'wheat', command = self.canvas_for_scrollbar.yview)
        self.canvas_for_scrollbar.configure(yscrollcommand = self.scrollbar.set)
        
        self.scrollbar.pack(side = 'left', fill = 'y')
        self.canvas_for_scrollbar.pack(side = 'right')
        self.canvas_for_scrollbar.create_window((0, 0), window = self.ScrollFrame, anchor = 'nw')
        self.ScrollFrame.bind('<Configure>', self.Scrollbar_fun)
        
        # dataview
        # txt ---------------------------------------------------------------------------------------
        # size = np.shape(self.data)
        # self.datanum = size[1]
        self.datanum = data.columns.size
        # txt ---------------------------------------------------------------------------------------
        # xls ---------------------------------------------------------------------------------------
        # size = book.columns.size 
        # self.datanum = size
        # xls ---------------------------------------------------------------------------------------
        self.dataname = [tk.Checkbutton() for num in range(self.datanum)]
        self.datacheck_on = [tk.IntVar() for num in range(self.datanum)]
        for num in range(self.datanum):
            self.dataname[num] = tk.Checkbutton(self.ScrollFrame, text = (self.data[0, num]), height = 1, width = 25, variable = self.datacheck_on[num], onvalue = 1, offvalue = 0, bg = 'wheat', highlightbackground = 'gold')
            self.dataname[num].pack()
        
        # Plot Figure
        self.Fig = Figure(figsize = (5, 4), dpi = 100) # prepare the figure to plot
        self.AX = self.Fig.add_subplot(111)# prepare
        self.canvas = self.canvas = FigureCanvasTkAgg(self.Fig, master = self) # attach the figure on the window 'PlotLoft' of tkinter
        self.toolbar = NavigationToolbar2Tk(self.canvas, self) # init the toolbar
        self.toolbar.forget()
        
        # units
        textsize = 11
        PlotButton = tk.Button(self.CheckButtonFrame, relief = 'ridge', command = self.PlotSelected, text = 'Plot', font = ('times', textsize), height = 2, width = 15, bg = 'goldenrod', activebackground = 'bisque', activeforeground = 'orangered')
        clearButton = tk.Button(self.CheckButtonFrame, relief = 'ridge', command = self.ClearAll, text = 'Clear', font = ('times', textsize), height = 2, width = 15, bg = 'goldenrod', activebackground = 'bisque', activeforeground = 'orangered')
        
        # place
        self.HomeFrame.pack(side = 'left', padx = 3, pady = 3)
        self.MidLine.pack(side = 'left')
        self.RightText.pack()
        self.LeftFrame.grid(row = 0, column = 0, sticky = tk.W)
        self.CheckButtonFrame.grid(row = 1, column = 0)
        PlotButton.grid(row = 0, column = 0)
        clearButton.grid(row = 0, column = 1)
        
    def Scrollbar_fun(self, event): # this is required for event
        self.canvas_for_scrollbar.configure(scrollregion = self.canvas_for_scrollbar.bbox('all'), width = 200, height = 550)
        
    def PlotSelected(self):
        plotnum = 0
        
        # clear previous figure
        self.Fig.clf()
        self.AX.clear()
        self.canvas._tkcanvas.pack_forget()
        self.toolbar.forget()
        self.Fig = Figure(figsize = (5, 4), dpi = 100) # prepare the figure to plot
        self.Fig.set_facecolor('wheat')
        self.AX = self.Fig.add_subplot(111)# prepare
        self.canvas = self.canvas = FigureCanvasTkAgg(self.Fig, master = self) # attach the figure on the window 'PlotLoft' of tkinter
        #self.toolbar.
        
        for num in range(self.datanum):
            if self.datacheck_on[num].get() == 1:
                self.AX.plot(self.data[:, num], label = (self.data[0, num])) # prepare to plot
                plotnum = plotnum + 1
        self.AX.legend() # prepare the legend
        self.canvas.draw() # subtitution of show
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self) # put the buttons of matplotlib on the window 'PlotLoft' of tkinter
        self.toolbar.update()
        self.canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
                
    def ClearAll(self):
        self.Fig.clf()
        self.AX.clear()
        self.canvas._tkcanvas.pack_forget()
        for num in range(self.datanum):
            self.dataname[num].deselect()
        
        
        

if __name__ == '__main__':
    HomeWin = DataPloter()
    HomeWin.mainloop()
