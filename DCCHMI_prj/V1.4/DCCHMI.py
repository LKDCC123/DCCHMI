import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.pyplot import Figure
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import windnd, base64
import os, sys
from HWbg_png import img as HWb
import Levenshtein

UserDistance = 4

class DataPloter(tk.Tk):

    def __init__(self):
        super().__init__()
        self.CreateHomeWin()    
        self.plotnum = []
        self.filename_old = ''
        self.filename = ''
    
    def CreateHomeWin(self): # decorate the home window
        # window config
        self.title('DataPloter v1.4 (dat内测版)')
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
        HWbg = tk.Label(self, relief = 'flat', image = self.HWbackgroung, text = 'Drop Your File Here', justify = 'right', font = ('times', textsize), compound = tk.CENTER, fg = 'wheat', cursor = 'cross')
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
        
    def OpenFile(self):
        self.filename = filedialog.askopenfilename(title='Open a File', filetype = [('dat', '*.dat'), ('txt', '*.txt')])# [('xlsx', '*.xlsx')])  # [('dat', '*.dat'), ('txt', '*.txt')])
        if self.filename == self.filename_old:
            messagebox.showwarning('emmm..', message='The Same File Selected!')
        self.entryvar.set(self.filename)        
        if not self.filename:
            messagebox.showwarning('oops!', message='No Valide File Selected!')
    
    def DropFile(self, files):
        self.filename = '\n'.join((item.decode('gbk') for item in files))
        Loft = PlotLoft(self.filename, '1200x600')
        Loft.mainloop()
        self.filename_old = self.filename
        print('hehe\n')
    
    def OpenPlot(self):
        if self.filename == '':
            messagebox.showwarning('emmm..', message='No File Selected!')
        elif self.filename == self.filename_old:
            messagebox.showwarning('emmm..', message='You Are Plotting The Same File!')
        else:
            Loft = PlotLoft(self.filename, '1200x600')
            Loft.mainloop()
        self.filename_old = self.filename
        
class PlotLoft(tk.Toplevel): # Toplevel makes IntVal in sonwindows active
    
    def __init__(self, filename, geometry):
        super().__init__()
        self.CreatPlotWin(filename, geometry)
        
    def CreatPlotWin(self, filename, geometry):
        data = pd.read_table(filename, low_memory=False)
        name = pd.read_table(filename, header = None, low_memory=False);
        self.data = data.iloc
        self.name = name.iloc[0, :]
        self.title(filename)
        self.geometry(geometry)
        self.configure(background = 'tan')
        self.HomeFrame = tk.Frame(self, width = 300, bg = 'tan', highlightbackground = 'gold')
        self.LeftFrame = tk.Frame(self.HomeFrame, width = 300, bg = 'wheat', highlightbackground = 'gold')
        self.CheckButtonFrame = tk.Frame(self.HomeFrame, width = 300, bg = 'wheat', highlightbackground = 'gold')
        self.MidLine = tk.Frame(self, height = 650, width = 3, bg = 'wheat', highlightbackground = 'gold')
        self.RightText = tk.Label(self, relief = 'flat', text = 'Plot Robotics With Enthusiasm', anchor = 'center', font = ('times', 15), bg = 'tan', fg = 'papayawhip', cursor = 'cross')
        self.DataNameValIn = StringVar()
        if self.DataNameValIn.get() == '':
            # self.DataNameValIn.set('Input Data Name')
            self.DataNameValIn.set('Period')
        self.DataNameValInList = [''];
        
        # combobox
        self.ComBox = ttk.Combobox(
            self.LeftFrame,
            height = 10,
            width = 20, 
            stat = 'normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor = 'arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font = ('time', 15),  # 字体
            textvariable = self.DataNameValIn,  # 通过StringVar设置可改变的值
            values = self.DataNameValInList,  # 设置下拉框的选项
            )
        self.ComBox.pack(side = 'top')
        self.UpdateComList()
        self.bind("<<ComboboxSelected>>", self.CheckInputData)
        
        # scrollbar
        self.canvas_for_scrollbar = tk.Canvas(self.LeftFrame, width = 300, bg = 'wheat')
        self.ScrollFrame = tk.Frame(self.canvas_for_scrollbar, width = 300, bg = 'wheat')
        self.scrollbar = tk.Scrollbar(self.LeftFrame, relief = 'ridge', width = 28, orient = 'vertical', bg = 'wheat', command = self.canvas_for_scrollbar.yview)
        self.canvas_for_scrollbar.configure(yscrollcommand = self.scrollbar.set)
        
        self.scrollbar.pack(side = 'left', fill = 'y')
        self.canvas_for_scrollbar.pack(side = 'right')
        self.canvas_for_scrollbar.create_window((0, 0), window = self.ScrollFrame, anchor = 'nw')
        self.ScrollFrame.bind('<Configure>', self.Scrollbar_fun)
        
        # dataview
        self.datanum = data.columns.size
        self.ampval = [tk.StringVar(value = '1.0') for num in range(self.datanum)]
        self.ampentry = [tk.Entry() for num in range(self.datanum)]
        self.dataname = [tk.Checkbutton() for num in range(self.datanum)]
        self.datacheck_on = [tk.IntVar() for num in range(self.datanum)]
        for num in range(self.datanum):
            self.ampentry[num] = tk.Entry(self.ScrollFrame, width = 4, textvariable = self.ampval[num])
            self.ampentry[num].grid(column = 0, row = num, sticky = 'w')
            self.dataname[num] = tk.Checkbutton(self.ScrollFrame, text = (self.name[num]), height = 1, width = 25, variable = self.datacheck_on[num], onvalue = 1, offvalue = 0, bg = 'wheat', highlightbackground = 'gold')
            self.dataname[num].grid(column = 1, row = num, sticky = 'w')
        
        # Plot Figure
        self.Fig = Figure(figsize = (5, 4), dpi = 100) # prepare the figure to plot
        self.AX = self.Fig.add_subplot(111)# prepare
        self.canvas = self.canvas = FigureCanvasTkAgg(self.Fig, master = self) # attach the figure on the window 'PlotLoft' of tkinter
        self.toolbar = NavigationToolbar2Tk(self.canvas, self) # init the toolbar
        self.toolbar.forget()
        
        # units
        textsize = 11
        PlotButton = tk.Button(self.CheckButtonFrame, relief = 'ridge', command = self.PlotSelected, text = 'Plot', font = ('times', textsize), height = 2, width = 10, bg = 'goldenrod', activebackground = 'bisque', activeforeground = 'orangered')
        clearButton = tk.Button(self.CheckButtonFrame, relief = 'ridge', command = self.ClearAll, text = 'Clear', font = ('times', textsize), height = 2, width = 10, bg = 'goldenrod', activebackground = 'bisque', activeforeground = 'orangered')
        self.gridcheck_on = tk.IntVar()
        Gridcheck = tk.Checkbutton(self.CheckButtonFrame, text = 'Grid', font = ('times', textsize), height = 1, width = 4, variable = self.gridcheck_on, onvalue = 1, offvalue = 0, bg = 'wheat', highlightbackground = 'gold')
        
        # place
        self.HomeFrame.pack(side = 'left', padx = 3, pady = 3)
        self.MidLine.pack(side = 'left')
        self.RightText.pack()
        self.LeftFrame.grid(row = 0, column = 0, sticky = tk.W)
        self.CheckButtonFrame.grid(row = 1, column = 0)
        PlotButton.grid(row = 0, column = 0)
        clearButton.grid(row = 0, column = 1)
        Gridcheck.grid(row = 0, column = 2)
        
    def Scrollbar_fun(self, event): # this is required for event
        self.canvas_for_scrollbar.configure(scrollregion = self.canvas_for_scrollbar.bbox('all'), width = 200, height = 520)
        
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
                self.AX.plot(float(self.ampval[num].get()) * self.data[:, num], label = (self.name[num])) # prepare to plot
                plotnum = plotnum + 1
        if self.gridcheck_on.get() == 1:
            self.AX.grid() 
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
            
    def UpdateComList(self):
        try:
            DataNameIn = (self.DataNameValIn.get())
            DataProbList = ['']
            for DataNameTemp in self.name:
                DataTemp7 = str(DataNameTemp)[:7] 
                DataTemp6 = str(DataNameTemp)[:6]  
                DataTemp5 = str(DataNameTemp)[:5]
                DataTemp4 = str(DataNameTemp)[:4]
                DataTemp3 = str(DataNameTemp)[:3]
                DataTemp2 = str(DataNameTemp)[:2]
                DataTemp1 = str(DataNameTemp)[:1]
                if Levenshtein.distance(str(DataNameIn).upper(), str(DataNameTemp).upper()) < UserDistance:
                    DataProbList.append(DataNameTemp)
                elif DataNameIn.upper() == DataTemp1.upper():
                    DataProbList.append(DataNameTemp)   
                elif DataNameIn.upper() == DataTemp2.upper():
                    DataProbList.append(DataNameTemp)  
                elif DataNameIn.upper() == DataTemp3.upper():
                    DataProbList.append(DataNameTemp)
                elif DataNameIn.upper() == DataTemp4.upper():
                    DataProbList.append(DataNameTemp)
                elif DataNameIn.upper() == DataTemp5.upper():
                    DataProbList.append(DataNameTemp)
                elif DataNameIn.upper() == DataTemp6.upper():
                    DataProbList.append(DataNameTemp)
                elif DataNameIn.upper() == DataTemp7.upper():
                    DataProbList.append(DataNameTemp)
            
            self.ComBox['values'] = (DataProbList)
            self.after(20, self.UpdateComList) # update every 20 ms
        except WindowsError:
            self.after(20, self.UpdateComList)
            pass
        
    def CheckInputData(self, event):
        datanamein = self.ComBox.get()
        for num in range(self.datanum):
            if self.name[num] == datanamein:
                self.datacheck_on[num].set(1)

if __name__ == '__main__':
    HomeWin = DataPloter()
    windnd.hook_dropfiles(HomeWin, func = HomeWin.DropFile)
    HomeWin.mainloop()
