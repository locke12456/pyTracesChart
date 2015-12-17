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
    @property 
    def MaxLenth(self):
        max_value = max(self._values)
        min_value = abs(max(self._values))
        return max_value+min_value
    def AddValue(self , value = 0):
        if len(self._values) > self._max:
            self._values.pop(0)
        self._values.append(value)
    def GetPenColor(self):
        return self._color
    def SetPenColor(self, r , g , b , a):
        self._color.setRgbF(r,g,b,a)
    def GetValue(self,index):
        if index < self.Count:
            return self._values[index]
        else :
            return 0
    
class Chart(QtGui.QWidget):
    valueUpdated = QtCore.pyqtSignal(int)
    _x = 0
    _y = 0
    _shift_w = 0.0
    _shift_h = 0.0
    _lines = None
    def __init__(self , parent ):
        super(Chart, self).__init__(parent)
        self._lines = {}   
        self._max = 60
        self.initUI()
    
    def initUI(self): 
        self._color = QtGui.QColor(0,0,0)
    def AddLine(self,name):
        line = Line()
        self._lines[name] = line
        return line
    def GetLineByName(self,name):
        if self._lines.has_key(name):
            return self._lines[name]
        return None
    def paintEvent(self, event = None):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawChart(event, qp)
        qp.end()
    def _draw(self , qp ,item , pre_pos , index ):
        qp.setPen(item.GetPenColor())
        pos =  QtCore.QPointF( pre_pos.x() , pre_pos.y() )
        to_pos =  QtCore.QPointF( index*self._shift_w , (self._y - item.GetValue(index)*self._shift_h) )
        pre_pos.setX(index*self._shift_w)
        pre_pos.setY((self._y - item.GetValue(index)*self._shift_h))
        if index != 0:
            qp.drawLine(pos , to_pos)
        return pre_pos
    def _drawText(self, qp , name , item , pos ):
        name = item.Description
        if pos.x() > len(name)*4:
           pos.setX((pos.x()-len(name)*4)-4)
        qp.drawText(pos , name)
    def _counting_shift_values(self , item ):
        avg = self.height()/8 if self.height()/8 > 16 else 16
        height = self.height()-avg
        max_height = item.MaxLenth+(avg) if item.MaxLenth > height else height
        self._shift_w = float(self.width())/self._max
        self._y = float(self.height())/2
        self._shift_h = round( float(height)/float(max_height) , 1 )
        
    def drawChart(self, event, qp):
        for litem in self._lines.items():
            name = litem[0]
            item = litem[1]
            if item.Count == 0:
                continue
            self._counting_shift_values(item)
            pre_x = 0
            pre_y = item.GetValue(0)
            pos =  QtCore.QPointF(pre_x,pre_y)
            for index in range(0,(item.Count)):
                pos = self._draw(qp,item ,pos,index)
            self._drawText(qp,name,item,pos)