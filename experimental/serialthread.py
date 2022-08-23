from PyQt5.QtCore import QThread, pyqtSignal
from collections import deque
import serial
import numpy as np
import pandas as pd
from datetime import datetime

class ThreadData(QThread):
  dataChanged = pyqtSignal(int, int, deque, str, str, int, str)
  flag = 0
  spoValue = 0
  pulseValue = 0
  status = 0
  status_value = ""
  counter = 0
  plethys = deque([])
  color = ""

  def __init__(self):
    QThread.__init__(self)
    self.isrunnings = True
    self.serial = serial.Serial("COM7")
    self.maxValueGraph = 500

  def stop(self):
    self.isrunnings = False
    # self.serial.close()

  def start_(self):
    self.isrunnings = True
    # self.serial.open()

  def run(self):
    while True:
      if self.isrunnings==True:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        data = self.serial.read()
        data = int.from_bytes(data, "big")

        if self.flag == 1:
          self.spoValue = data
          self.flag = 0
        elif self.flag == 2:
          self.pulseValue = data
          self.flag = 0
        elif self.flag == 4:
          self.status = data
          self.flag = 0
          if self.status==0:
            self.status_value = "OK"
            self.color = "color: green;"
          elif self.status==2:
            self.status_value = "No finger in probe!"
            self.color = "color: red;"
          elif self.status==1:
            self.status_value = "No sensor connected!"
            self.color = "color: red;"
        
        elif self.flag == 3:
          if data == 249:
            self.flag = 1
          elif data == 250:
            self.flag = 2
          elif len(self.plethys)==self.maxValueGraph:
            self.plethys[self.counter] = data
            self.counter+=1
            try:
              for i in range(1,10):
                self.plethys[self.counter+i] = np.nan
            except:
              pass
            if self.counter==self.maxValueGraph:
              self.counter = 0
          else:
            self.plethys.append(data)
        elif data == 249:
          self.flag = 1
        elif data == 250:
          self.flag = 2
        elif data == 248:
          self.flag = 3
        elif data == 251:
          self.flag = 4


        self.dataChanged.emit(self.spoValue, 
                              self.pulseValue, 
                              self.plethys, 
                              self.status_value, 
                              self.color, 
                              self.counter,
                              current_time)
      else:
        pass