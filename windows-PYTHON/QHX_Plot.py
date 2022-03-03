# https://blog.csdn.net/weixin_43593330/article/details/89882187 numpy.loadtxt

import matplotlib
matplotlib.use("Qt5Agg") 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import time,sys;
from PyQt5.Qt import *
from PyQt5.QtGui import *;
from PyQt5.QtCore import *;
from PyQt5.QtWidgets import QCompleter;
import numpy as np
import pandas as pd

from MatplotQT import *;
from ui_MY_DATA import *;
# from DataConfigure import *;
from JumpDataConfigure import *;

class MyWindow(QMainWindow, Ui_MainWindow):

  def __init__(self, parent=None):
      super(MyWindow, self).__init__(parent);
      self.initUI();
	  
  def initUI(self):
      self.setupUi(self);
      
      self.dcf = DataConfigure();
      
      # self.peroidTime.clicked.connect(self.click_Callback_peroidTime);
      
      self.rleg0Angle.clicked.connect(self.click_Callback_rleg0Angle);
      self.rleg1Angle.clicked.connect(self.click_Callback_rleg1Angle);
      self.rleg2Angle.clicked.connect(self.click_Callback_rleg2Angle);
      self.rleg3Angle.clicked.connect(self.click_Callback_rleg3Angle);
      self.rleg4Angle.clicked.connect(self.click_Callback_rleg4Angle);
      self.rleg5Angle.clicked.connect(self.click_Callback_rleg5Angle);
      self.lleg0Angle.clicked.connect(self.click_Callback_lleg0Angle);
      self.lleg1Angle.clicked.connect(self.click_Callback_lleg1Angle);
      self.lleg2Angle.clicked.connect(self.click_Callback_lleg2Angle);
      self.lleg3Angle.clicked.connect(self.click_Callback_lleg3Angle);
      self.lleg4Angle.clicked.connect(self.click_Callback_lleg4Angle);
      self.lleg5Angle.clicked.connect(self.click_Callback_lleg5Angle);
      
      self.rleg0Torque.clicked.connect(self.click_Callback_rleg0Torque);
      self.rleg1Torque.clicked.connect(self.click_Callback_rleg1Torque);
      self.rleg2Torque.clicked.connect(self.click_Callback_rleg2Torque);
      self.rleg3Torque.clicked.connect(self.click_Callback_rleg3Torque);
      self.rleg4Torque.clicked.connect(self.click_Callback_rleg4Torque);
      self.rleg5Torque.clicked.connect(self.click_Callback_rleg5Torque);
      self.lleg0Torque.clicked.connect(self.click_Callback_lleg0Torque);
      self.lleg1Torque.clicked.connect(self.click_Callback_lleg1Torque);
      self.lleg2Torque.clicked.connect(self.click_Callback_lleg2Torque);
      self.lleg3Torque.clicked.connect(self.click_Callback_lleg3Torque);
      self.lleg4Torque.clicked.connect(self.click_Callback_lleg4Torque);
      self.lleg5Torque.clicked.connect(self.click_Callback_lleg5Torque);
      
      self.rarmAngle.clicked.connect(self.click_Callback_rarmAngle);
      self.rarmTorque.clicked.connect(self.click_Callback_rarmTorque);
      self.larmAngle.clicked.connect(self.click_Callback_larmAngle);
      self.larmTorque.clicked.connect(self.click_Callback_larmTorque);
  
      self.rlegForce.clicked.connect(self.click_Callback_rlegForce);
      self.llegForce.clicked.connect(self.click_Callback_llegForce);
      
      self.roll.clicked.connect(self.click_Callback_roll);
      self.pitch.clicked.connect(self.click_Callback_pitch);
  
      self.ComX.clicked.connect(self.click_Callback_ComX);
      self.ComZ.clicked.connect(self.click_Callback_ComZ);
      
      self.Clear.clicked.connect(self.click_Callback_Clear);
      
      self.lineEdit.editingFinished.connect(self.enter_Callback_lineEdit);
      
      self.figure = MatplotQT(width=5, height=4, dpi=100);

      self.figure_ntb = NavigationToolbar(self.figure, self);
      
      self.matplotFigure.addWidget(self.figure);
      self.matplotFigure.addWidget(self.figure_ntb);
      
      self.setAcceptDrops(True);
                
  def dragEnterEvent(self, event):
       if event.mimeData().text().endswith('.dat'):
           event.accept()
       else:
           event.ignore()
          
  def dropEvent(self, event):
      self.data_file_name = event.mimeData().text().replace('file:///', '')
      self.data = pd.read_table(self.data_file_name, sep='\t')
      Temp=''
      for value in self.data.columns.values:
          Temp = Temp+''.join(value)+'\n'
      self.textBrowser.clear()
      self.textBrowser.append(Temp)
  
      # 自动补全
      item_list = self.data.columns.values.tolist()
      for i in range(len(item_list)):
          self.combobox.addItem(item_list[i])
      self.combobox.setCurrentIndex(-1)
      self.completer = QCompleter(item_list)
      self.completer.setFilterMode(Qt.MatchContains)
      self.completer.setCompletionMode(QCompleter.PopupCompletion)
      self.lineEdit.setCompleter(self.completer)
      self.combobox.setCompleter(self.completer)


  def click_Callback_peroidTime(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.PeriodTimeOrder],label='periodT');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_rleg0Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip1Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip1Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
      
  def click_Callback_rleg1Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip2Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip2Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_rleg2Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip3Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip3Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_rleg3Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RKneeOrder+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RKneeOrder+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_rleg4Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RAnkle5Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RAnkle5Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
   
  def click_Callback_rleg5Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RAnkle6Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RAnkle6Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_lleg0Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip1Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip1Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
      
  def click_Callback_lleg1Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip2Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip2Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_lleg2Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip3Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip3Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_lleg3Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LKneeOrder+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LKneeOrder+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_lleg4Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LAnkle5Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LAnkle5Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_lleg5Angle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LAnkle6Order+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LAnkle6Order+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_rleg0Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip1Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
      
  def click_Callback_rleg1Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip2Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_rleg2Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RHip3Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_rleg3Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RKneeOrder+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_rleg4Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RAnkle5Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_rleg5Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RAnkle6Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();       
       
  def click_Callback_lleg0Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip1Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
      
  def click_Callback_lleg1Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip2Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_lleg2Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LHip3Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_lleg3Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LKneeOrder+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_lleg4Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LAnkle5Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();      
       
  def click_Callback_lleg5Torque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LAnkle6Order+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_rarmAngle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RArmOrder+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.RArmOrder+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
	   
  def click_Callback_rarmTorque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RArmOrder+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
	   
  def click_Callback_larmAngle(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LArmOrder+self.dcf.RealAngOrder],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.LArmOrder+self.dcf.RefAngOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
	   
  def click_Callback_larmTorque(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LArmOrder+self.dcf.RefTauOrder],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
	   
  def click_Callback_rlegForce(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.RlegForceActX],label='actFX');
       # self.figure.axes.plot(self.data.values[:,self.dcf.RlegForceRefX],label='refX');
       self.figure.axes.plot(self.data.values[:,self.dcf.RlegForceActY],label='actFY');
       # self.figure.axes.plot(self.data.values[:,self.dcf.RlegForceRefY],label='refY');
       self.figure.axes.plot(self.data.values[:,self.dcf.RlegForceActZ],label='actFZ');
       # self.figure.axes.plot(self.data.values[:,self.dcf.RlegForceRefZ],label='refZ');
       self.figure.axes.plot(self.data.values[:,self.dcf.RlegTorqueActX],label='actTX')
       self.figure.axes.plot(self.data.values[:,self.dcf.RlegTorqueActY],label='actTY')
       self.figure.axes.plot(self.data.values[:,self.dcf.RlegTorqueActZ],label='actTZ')
       self.figure.axes.legend();
       self.figure.draw();

  def click_Callback_llegForce(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.LlegForceActX],label='actFX');
       # self.figure.axes.plot(self.data.values[:,self.dcf.LlegForceRefX],label='refX');
       self.figure.axes.plot(self.data.values[:,self.dcf.LlegForceActY],label='actFY');
       # self.figure.axes.plot(self.data.values[:,self.dcf.LlegForceRefY],label='refY');
       self.figure.axes.plot(self.data.values[:,self.dcf.LlegForceActZ],label='actFZ');
       # self.figure.axes.plot(self.data.values[:,self.dcf.LlegForceRefZ],label='refZ');
       self.figure.axes.plot(self.data.values[:,self.dcf.LlegTorqueActX],label='actTX')
       self.figure.axes.plot(self.data.values[:,self.dcf.LlegTorqueActY],label='actTY')
       self.figure.axes.plot(self.data.values[:,self.dcf.LlegTorqueActZ],label='actTZ')
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_roll(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.TorsoRollActOrder],label='act');
       self.figure.axes.legend();
       self.figure.draw();       

  def click_Callback_pitch(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.TorsoPitchActOrder],label='act');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_ComX(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.ComActX],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.ComRefX],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_ComZ(self):
       self.figure.axes.cla();
       self.figure.axes.plot(self.data.values[:,self.dcf.ComActZ],label='act');
       self.figure.axes.plot(self.data.values[:,self.dcf.ComRefZ],label='ref');
       self.figure.axes.legend();
       self.figure.draw();
       
  def click_Callback_Clear(self):
       self.figure.axes.cla();
       self.figure.draw();
       
  def enter_Callback_lineEdit(self):
       self.figure.axes.plot(self.data.xs(self.lineEdit.text(),1).values)
       self.figure.draw();
       
if __name__ == '__main__':
  app = QApplication(sys.argv);
  ex = MyWindow();
  ex.show()
  sys.exit(app.exec_());