import sys , random
import PyQt4
from PyQt4 import QtGui, QtCore
class Line(object):
    _description = ""
    _values = None
    _lock = None
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)
        self._color = QtGui.QColor(0,0,0)
        self._lock = QtCore.QMutex()
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
        self._lock.lock()
        max_value = max(self._values)
        min_value = abs(max(self._values))
        self._lock.unlock()
        return max_value+min_value
    def SetSize(self,size):
        self._max = size
    def AddValue(self , value = 0):
        self._lock.lock()
        if len(self._values) > self._max:
            self._values.pop(0)
        self._values.append(value)
        print self.Count
        self._lock.unlock()
    def GetPenColor(self):
        return self._color
    def SetPenColor(self, r , g , b , a):
        self._color.setRgbF(r,g,b,a)
    def GetValue(self,index):
        if index < self.Count:
            self._lock.lock()
            val = self._values[index]
            self._lock.unlock()
            return val
        else :
            return 0
    
class Chart(QtGui.QWidget):
    valueUpdated = QtCore.pyqtSignal(int)
    _x = 0
    _y = 0
    _min_val = 0
    _max_val = 0
    _center = 0.0
    _shift_w = 0.0
    _shift_h = 0.0
    _lines = None
    _lock = None
    def __init__(self , parent ):
        super(Chart, self).__init__(parent)
        self._lock = QtCore.QMutex()
        self._lines = {}   
        self._max = 60
        self.initUI()
    
    def initUI(self): 
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        role = self.backgroundRole()
        palette.setColor(role, QtGui.QColor('white'))
        
        self.setPalette(palette)
        self._color = QtGui.QColor(0,0,0)
    def SetValueRange(self , min_val , max_val):
        center = 0
        self._min_val = min_val
        self._max_val = max_val
        self._center = (float(max_val - center))/float(abs(max_val)+abs(min_val))

    def AddLine(self,name):
        line = Line()
        self._lines[name] = line
        return line
    def GetLineByName(self,name):
        if self._lines.has_key(name):
            return self._lines[name]
        return None
    def paintEvent(self, event = None):
        self._lock.lock()
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawChart(event, qp)
        qp.end()
        self._lock.unlock()
    def _value_to_position_y(self,val):
        return (self._y - val*self._shift_h)
    def _draw(self , qp ,item , pre_pos , index ):
        avg = self._avg_shift_width
        qp.setPen(item.GetPenColor())
        pos =  QtCore.QPointF( avg + pre_pos.x() , pre_pos.y() )
        to_pos =  QtCore.QPointF( avg + index*self._shift_w , self._value_to_position_y( item.GetValue(index) ) )
        pre_pos.setX( index*self._shift_w )
        pre_pos.setY( self._value_to_position_y( item.GetValue(index) ))
        if index != 0:
            qp.drawLine(pos , to_pos)
        return pre_pos
    def _draw_ruler_v(self , qp , avg ):
        back_color = QtGui.QColor(255,0,0,200)
        shift = round(float(abs(self._max_val)+abs(self._min_val))/4,0)
        for offset_y in range(0,5):
            pos =  QtCore.QPointF( avg-avg/2 , self._value_to_position_y( self._min_val + offset_y*shift ) )
            to_pos =  QtCore.QPointF( avg+avg/2 , self._value_to_position_y( self._min_val + offset_y*shift ) )
            qp.drawLine(pos , to_pos)
            pos =  QtCore.QPointF( avg-avg/2 , self._value_to_position_y( self._min_val + offset_y*shift ) )
            self._drawTextTo(qp,str(self._min_val + offset_y*shift),pos , None ,back_color)
    def _draw_ruler_h(self,qp,avg):
        for offset_x in range(0,self._max+1):
            pos =  QtCore.QPointF( avg + offset_x * self._shift_w , self._value_to_position_y( avg/8 ) )
            to_pos =  QtCore.QPointF( avg + offset_x * self._shift_w , self._value_to_position_y( -avg/8 ) )
            qp.drawLine(pos , to_pos)
    def _draw_background(self , qp  ):
        avg = self._avg_shift_width # if self.height()/8 > 16 else 16
        qp.setPen(QtGui.QColor(0,0,0,128))
        pos =  QtCore.QPointF( 0 , self._y )
        to_pos =  QtCore.QPointF( self.width() , self._y )
        qp.drawLine(pos , to_pos)
        self._draw_ruler_v(qp,avg)
        self._draw_ruler_h(qp,avg)
        pos =  QtCore.QPointF( avg , 0 )
        to_pos =  QtCore.QPointF( avg , self.height() )
        qp.drawLine(pos , to_pos)
    
    def _drawTextTo(self, qp , name , pos , color = None , back_color = None):
        if color is None :
            color = QtGui.QColor(255,255,255,255)
        if pos.x() > len(name)*4:
           pos.setX((pos.x()-len(name)*4)-4)
        pos.setX( pos.x()-len(name) )
        if back_color is not None:
            rect = QtCore.QRect(pos.x(),pos.y() - 10 , len(name)*4+8 , 12 )
            qp.fillRect(rect ,back_color)
        pen = qp.pen()
        qp.setPen(color)
        qp.drawText(pos , name)
        qp.setPen(pen)

    def _drawText(self, qp , name , item , pos ):
        name = item.Description
        if pos.x() > len(name)*4:
           pos.setX((pos.x()-len(name)*4)-4)

        pos.setX( self._avg_shift_width + pos.x() )
        qp.drawText(pos , name)
    def _counting_shift_values(self ):
        self._avg_shift_width = avg =  min(self.width(),self.height())/10
        #avg = self.height()/8 if self.height()/8 > 16 else 16
        height = self.height()-avg
        len = abs(self._max_val)+abs(self._min_val)
        max_height = len+avg #if len  height else height
        self._shift_w = float(self.width()-avg*2)/self._max
        self._y = float(self.height())*self._center
        print self._shift_w
        self._shift_h = round( float(height)/float(max_height) , 1 )
        
    def drawChart(self, event, qp):
        self._counting_shift_values()
        self._draw_background(qp)
        for litem in self._lines.items():
            name = litem[0]
            item = litem[1]
            if item.Count == 0:
                continue
            
            pre_x = 0
            pre_y = item.GetValue(0)
            pos =  QtCore.QPointF(pre_x,pre_y)
            for index in range(0,(item.Count)):
                pos = self._draw(qp,item ,pos,index)
            #self._drawText(qp,name,item,pos)
            text_pos = QtCore.QPointF(self._avg_shift_width*2 + pos.x(),pos.y() )
            self._drawTextTo(qp,item.Description , text_pos , item.GetPenColor() , None )