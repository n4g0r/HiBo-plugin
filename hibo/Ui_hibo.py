# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

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

class Ui_hibo(QtGui.QDialog):
        
    def __init__(self): 
        QtGui.QDialog.__init__(self)
	self.createComponents()
	self.setupUi()

    def setupUi(self):
	# QDialog (self) is base for GUI-Elements

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("hibo", "hibo", None))

    def createComponents(self):
        pass

        
