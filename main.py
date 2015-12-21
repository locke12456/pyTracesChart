import sys
import PyQt4
from PyQt4 import QtGui, QtCore
import random
import time , threading, sched , functools
from chart_sample import Ui_MainWindow

                
def timer (win , lex):
    while 1:
        win.update()
        time.sleep(1)
        
class Gui(QtGui.QMainWindow,Ui_MainWindow):
    _lines = None
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self._lines = [self.chart_1 , self.chart_2 , self.chart_4]
        #ex.show()
        line1 = self.chart_1.AddLine("Line1")
        line1 = self.chart_2.AddLine("Line1")
        line1.SetPenColor(1,0,0,1)
        line1 = self.chart_4.AddLine("Line1")
        line2 = self.chart_4.AddLine("Line2")
        line = self.chart_4.GetLineByName("Line2")
        line.SetPenColor(1,0,0,1)
        for ex in self._lines:
            name = ["Line1","Line2","Line3"]
            ex.SetValueRange(-40, 120)
            for n in name:
                line = ex.GetLineByName(n) 
                if line is not None:
                    value = random.randint(40, 70)
                    line.Description = str(float(value))
                    line.AddValue(value)
                ex.update()

    def paintEvent(self, event = None):
        #time.sleep(1)
        print 1
        #return 
        for ex in self._lines:
            name = ["Line1","Line2","Line3"]
            ex.SetValueRange(-40, 120)
            for n in name:
                line = ex.GetLineByName(n) 
                if line is not None:
                    value = random.randint(40, 70)
                    line.Description = str(float(value))
                    line.AddValue(value)
                ex.update()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    main_w = Gui()
    main_w.show()
    #threading.Timer(1, call ).start()
    #threading.Timer(1, call ).start()
    call = functools.partial( timer , main_w , None )
    #threading.Timer(1, call ).start()
    threading.Timer(1, call ).start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()