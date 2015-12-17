import sys
import PyQt4
from PyQt4 import QtGui, QtCore
import random
import time , threading, sched , functools
from chart_sample import Ui_MainWindow

                
def timer (lex):
    while 1:
        time.sleep(0.2)
        for ex in lex:
            name = ["Line1","Line2","Line3"]
            for n in name:
                line = ex.GetLineByName(n) 
                if line is not None:
                    value = random.randint(-128, 128)
                    line.Description = str(value)
                    line.AddValue(value)
                ex.update()
class Gui(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    main_w = Gui()
    main_w.show()
    ex = [main_w.chart_1 , main_w.chart_2 , main_w.chart_4]
    #ex.show()
    line1 = main_w.chart_1.AddLine("Line1")
    line2 = main_w.chart_1.AddLine("Line2")
    line2.SetPenColor(1,0,0,1)
    line3 = main_w.chart_1.AddLine("Line3")
    line3.SetPenColor(1,0,1,1)
    line1 = main_w.chart_2.AddLine("Line1")
    line1.SetPenColor(1,0,0,1)
    line1 = main_w.chart_4.AddLine("Line1")
    line2 = main_w.chart_4.AddLine("Line2")
    line = main_w.chart_4.GetLineByName("Line2")
    line.SetPenColor(1,0,0,1)
    call = functools.partial( timer , ex )
    threading.Timer(1, call ).start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()