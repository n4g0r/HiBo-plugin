# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hibo.ui'
#
# Created: Mon Apr 28 23:20:33 2014
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
        hibo.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(hibo)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(hibo)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), hibo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), hibo.reject)
        QtCore.QMetaObject.connectSlotsByName(hibo)

    def retranslateUi(self, hibo):
        hibo.setWindowTitle(_translate("hibo", "hibo", None))

