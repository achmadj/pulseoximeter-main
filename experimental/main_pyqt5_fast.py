import gui as gui
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt
import sys
import pyqtgraph as pg
from serialthread import ThreadData
pg.setConfigOption("background", '#000a12')

class Window(QWidget, gui.Ui_Form):
  def __init__(self):
    super().__init__()

    self.maximum_ = 256
    
    self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    self.setupUi(self)
    self.setStyleSheet("background-color: black;")
    

    self.graphwidget.getPlotItem().hideAxis("left")

    self.serials = ThreadData()
    self.graphwidget.setYRange(0, self.maximum_, padding=0)
    self.graphwidget.setXRange(0, self.serials.maxValueGraph, padding=0)

    self.progressBar.setMaximum(self.maximum_)

    # self.showFullScreen()
    self.control_button.clicked.connect(self.eventHandler)

    # plot
    self.lines = self.graphwidget.plot(pen=pg.mkPen('w'), connect="finite")
    

  def onDataChanged(self, spo_value, pulse_value, arr, status_value, color, counter, time):
    self.spo_value.setText(str(spo_value))
    self.pulse_value.setText(str(pulse_value))
    self.lines.setData(range(len(arr)), arr, connect="finite")
    self.status_label.setText(status_value)
    self.status_label.setStyleSheet(color + "background-color: white; border-radius: 2px;")
    if counter%500==0:
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
    if self.serials.isRunning() and self.serials.isrunnings==False:
      self.serials.start_()
      self.control_button.setText("Stop")
    elif self.serials.isRunning():
      self.control_button.setText("Start")
      self.serials.stop()
    else:
      self.control_button.setText("Stop")
      self.serials.start()
      self.serials.dataChanged.connect(self.onDataChanged)



if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  sys.exit(app.exec_())
