# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file Ui_hibo.ui
# Created with: PyQt4 UI code generator 4.4.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_hibo(object):
    def setupUi(self, hibo):
        hibo.setObjectName("hibo")
        hibo.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(hibo)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(hibo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), hibo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), hibo.reject)
        QtCore.QMetaObject.connectSlotsByName(hibo)

    def retranslateUi(self, hibo):
        hibo.setWindowTitle(QtGui.QApplication.translate("hibo", "hibo", None, QtGui.QApplication.UnicodeUTF8))
