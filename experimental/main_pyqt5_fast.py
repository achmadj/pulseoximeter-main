from collections import deque
import gui as gui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
import sys
import pyqtgraph as pg
from serialthread import ThreadData
import pandas as pd
pg.setConfigOption("background", '#000a12')

class Window(QWidget, gui.Ui_Form):
  def __init__(self):
    super().__init__()
    # flag untuk collect data csv
    self.collecting = False

    # prep data csv
    self.identity = {"name": "", "id": "", "sex": "", "age": ""}
    self.df = pd.DataFrame(columns=["time", "spo2", "pulse", "status"])
    self.data = {"time": [], "spo2": [], "pulse": [],"status": []}

    self.maximum_ = 256 # y limit plot
    
    self.setWindowFlag(Qt.WindowType.FramelessWindowHint) # no border window
    self.setupUi(self)
    self.setStyleSheet("background-color: black;") 

    self.serials = ThreadData()

    # rapihin plot
    self.graphwidget.getPlotItem().hideAxis("left")
    self.graphwidget.setYRange(0, self.maximum_, padding=0)
    self.graphwidget.setXRange(0, self.serials.maxValueGraph, padding=0)

    # progress bar
    self.progressBar.setMaximum(self.maximum_)

    # self.showFullScreen()

    # button handler
    self.control_button.clicked.connect(self.eventHandler)
    self.control_reset_button.clicked.connect(self.reset)
    self.control_io_button.clicked.connect(self.save)
    self.control_exit_button.clicked.connect(self.exits)

    # plot
    self.lines = self.graphwidget.plot(pen=pg.mkPen('w'), connect="finite")

    #start thread
    self.serials.start()
    self.serials.dataChanged.connect(self.onDataChanged)    

  def onDataChanged(self, spo_value, pulse_value, arr, status_value, color, counter, time):
    sets = [time, spo_value, pulse_value, status_value]
    if self.collecting:
      for key, value in zip(self.data, sets):
        self.data[key].append(value)
    self.spo_value.setText(str(spo_value))
    self.pulse_value.setText(str(pulse_value))
    self.lines.setData(range(len(arr)), arr, connect="finite")
    self.status_label.setText(status_value)
    self.status_label.setStyleSheet(color + "background-color: white; border-radius: 2px;")
    if counter%250==0:
      self.history_value.append(f"{time}\tSpO₂: {spo_value}\tPulse: {pulse_value}\t")

    try:
      if len(arr)==500:
        raise IndexError
      else:
        self.progressBar.setValue(int(arr[-1]))
    except:
      try: self.progressBar.setValue(int(arr[counter-1]))
      except: pass
  
  def eventHandler(self):
    if self.collecting==False:
      self.control_button.setStyleSheet("background-color: rgb(255, 76, 32);")
      self.control_button.setText("Stop")
      self.collecting = True
    else:
      self.control_button.setStyleSheet("background-color: rgb(41, 255, 148)")
      self.control_button.setText("Start")
      self.collecting = False

  def reset(self):
    self.spo_value.setText("--")
    self.pulse_value.setText("--")
    self.lines.setData([], [], connect="finite")
    self.status_label.setText("--")
    self.history_value.setText("")

  def save(self):
    self.identity["name"] = self.name_value.text()
    self.identity["id"] = self.id_value.text()
    self.identity["age"] = self.age_value.text()
    self.identity["sex"] = self.sex_value.currentText()
    name = (self.identity["name"]).split(" ")
    name = "_".join(name)

    with open(f"{name}.csv", "a") as f:
      f.write(f'# Name: {self.identity["name"]}\n# ID: {self.identity["id"]}\n# Sex: {self.identity["sex"]}\n# Age: {self.identity["age"]}\n')
      for col, value in zip(self.df.columns, self.data.values()):
        self.df[col] = value
      self.df.to_csv(f, index=None)

  def exits(self):
    QApplication.instance().quit()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec_())
