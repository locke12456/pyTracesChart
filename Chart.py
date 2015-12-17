import sys , random
import PyQt4
from PyQt4 import QtGui, QtCore
class Line(object):
    _description = ""
    _values = None
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)
        self._color = QtGui.QColor(0,0,0)
        self._values = []
        self._max = 60
    @property 
    def Count(self):
        return len(self._values)
    @property
    def Description(self):
        return self._description
    @Description.setter
    def Description(self , str ):
        self._description = str
    def AddValue(self , value = 0):
        if len(self._values) > self._max:
            self._values.pop(0)
        self._values.append(value)
    def GetPenColor(self):
        return self._color
    def SetPenColor(self, r , g , b , a):
        self._color.setRgbF(r,g,b,a)
    def GetValue(self,index):
        return self._values[index]

class Chart(QtGui.QWidget):
    valueUpdated = QtCore.pyqtSignal(int)
    _x = 0
    _y = 0
    _shift = 0.0
    _lines = None
    def __init__(self , parent ):
        super(Chart, self).__init__(parent)
        self._lines = {}   
        self._max = 60
        self.initUI()
    
    def initUI(self): 
        self._color = QtGui.QColor(0,0,0)
    def AddLine(self,name):
        self._lines[name] = Line()
    def GetLineByName(self,name):
        if self._lines.has_key(name):
            return self._lines[name]
        return None
    def paintEvent(self, event = None):
        #if len(self._values) == 0:
        #    return
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawChart(event, qp)
        qp.end()
    def _draw(self , qp ,item , pre_pos , index ):
        qp.setPen(item.GetPenColor())
        pos =  QtCore.QPointF( pre_pos.x() , pre_pos.y() )
        to_pos =  QtCore.QPointF( index*self._shift , self._y - item.GetValue(index) )
        pre_pos.setX(index*self._shift)
        pre_pos.setY(self._y - item.GetValue(index))
        if index != 0:
            qp.drawLine(pos , to_pos)
        return pre_pos
    def drawChart(self, event, qp):
        
        self._shift = float(self.width())/self._max
        self._y = float(self.height())/2

        qp.setPen(self._color)

        for litem in self._lines.items():
            name = litem[0]
            item = litem[1]
            if item.Count == 0:
                continue
            pre_x = 0
            pre_y = item.GetValue(0)
            pre_pos =  QtCore.QPointF(pre_x,pre_y)
            for x in range(0,(item.Count)):
                pre_pos = self._draw(qp,item ,pre_pos,x)
            pos = pre_pos
            name = item.Description
            if pos.x() > len(name)*4:
                pos.setX((pos.x()-len(name)*4)-4)
            qp.drawText(pos , name)