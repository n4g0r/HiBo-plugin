# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_hibo.ui'
#
# Created: Wed May  7 21:55:35 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

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

class Ui_hibo(object):
    def setupUi(self, hibo):
        hibo.setObjectName(_fromUtf8("hibo"))
        hibo.resize(272, 78)
        self.label = QtGui.QLabel(hibo)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.load_button = QtGui.QPushButton(hibo)
        self.load_button.setGeometry(QtCore.QRect(170, 40, 97, 31))
        self.load_button.setAutoDefault(True)
        self.load_button.setDefault(False)
        self.load_button.setObjectName(_fromUtf8("load_button"))
        self.cancel_button = QtGui.QPushButton(hibo)
        self.cancel_button.setGeometry(QtCore.QRect(10, 40, 97, 31))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))

        self.retranslateUi(hibo)
        QtCore.QMetaObject.connectSlotsByName(hibo)

    def retranslateUi(self, hibo):
        hibo.setWindowTitle(_translate("hibo", "hibo", None))
        self.label.setText(_translate("hibo", "Please load an image of a historical map.", None))
        self.load_button.setText(_translate("hibo", "load", None))
        self.cancel_button.setText(_translate("hibo", "cancel", None))

