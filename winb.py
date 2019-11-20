# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifbar.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_wifbar(object):
    def setupUi(self, wifbar):
        wifbar.setObjectName("wifbar")
        wifbar.resize(820, 804)
        self.lb_back = QtWidgets.QLabel(wifbar)
        self.lb_back.setGeometry(QtCore.QRect(0, 0, 821, 801))
        self.lb_back.setText("")
        self.lb_back.setPixmap(QtGui.QPixmap("f.png"))
        self.lb_back.setScaledContents(True)
        self.lb_back.setObjectName("lb_back")
        self.lb_title = QtWidgets.QLabel(wifbar)
        self.lb_title.setGeometry(QtCore.QRect(10, 6, 801, 51))
        self.lb_title.setStyleSheet("background-color: white;\n"
"color: rgb(11, 1, 127);\n"
"border-radius : 25px;\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.lb_title.setObjectName("lb_title")
        self.lb_bar = QtWidgets.QLabel(wifbar)
        self.lb_bar.setGeometry(QtCore.QRect(10, 63, 801, 714))
        self.lb_bar.setText("")
        self.lb_bar.setObjectName("lb_bar")
        pixmap = QtGui.QPixmap('Barfin.png')
        self.lb_bar.setPixmap(pixmap)
        self.lb_bar.setScaledContents(True)

        self.retranslateUi(wifbar)
        QtCore.QMetaObject.connectSlotsByName(wifbar)

    def retranslateUi(self, wifbar):
        _translate = QtCore.QCoreApplication.translate
        wifbar.setWindowTitle(_translate("wifbar", "Dialog"))
        self.lb_title.setText(_translate("wifbar", "BAR GRAPH"))
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wifbar = QtWidgets.QDialog()
    ui = Ui_wifbar()
    ui.setupUi(wifbar)
    wifbar.show()
    sys.exit(app.exec_())

