# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chart_sample.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Chart import Chart
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(627, 429)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.chart_1 = Chart(self.centralwidget)
        self.chart_1.setGeometry(QtCore.QRect(0, 10, 480, 240))
        self.chart_1.setMinimumSize(QtCore.QSize(480, 240))
        self.chart_1.setMaximumSize(QtCore.QSize(480, 240))
        self.chart_1.setObjectName(_fromUtf8("chart_1"))
        self.chart_2 = Chart(self.centralwidget)
        self.chart_2.setGeometry(QtCore.QRect(490, 10, 128, 240))
        self.chart_2.setMinimumSize(QtCore.QSize(128, 240))
        self.chart_2.setMaximumSize(QtCore.QSize(128, 240))
        self.chart_2.setObjectName(_fromUtf8("chart_2"))
        self.chart_3 = QtGui.QWidget(self.centralwidget)
        self.chart_3.setGeometry(QtCore.QRect(830, 320, 128, 240))
        self.chart_3.setMinimumSize(QtCore.QSize(128, 240))
        self.chart_3.setMaximumSize(QtCore.QSize(128, 240))
        self.chart_3.setObjectName(_fromUtf8("chart_3"))
        self.chart_4 = Chart(self.centralwidget)
        self.chart_4.setGeometry(QtCore.QRect(0, 260, 620, 128))
        self.chart_4.setMinimumSize(QtCore.QSize(620, 128))
        self.chart_4.setMaximumSize(QtCore.QSize(620, 128))
        self.chart_4.setObjectName(_fromUtf8("chart_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 17))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

