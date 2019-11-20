# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifpie.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_wifpie(object):
    def setupUi(self, wifpie):
        wifpie.setObjectName("wifpie")
        wifpie.resize(738, 608)
        self.lb_back = QtWidgets.QLabel(wifpie)
        self.lb_back.setGeometry(QtCore.QRect(0, 0, 741, 611))
        self.lb_back.setPixmap(QtGui.QPixmap("dark-background-with-star-like-dots_bkpaotdgh__F0000.png"))
        self.lb_back.setScaledContents(True)
        self.lb_back.setObjectName("lb_back")
        self.lb_title = QtWidgets.QLabel(wifpie)
        self.lb_title.setGeometry(QtCore.QRect(300, 0, 131, 61))
        self.lb_title.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 90);\n"
"color : white;\n"
"border-radius: 20px;")
        self.lb_title.setObjectName("lb_title")
        self.lb_pie = QtWidgets.QLabel(wifpie)
        self.lb_pie.setGeometry(QtCore.QRect(50, 90, 651, 481))
        self.lb_pie.setText("")
        self.lb_pie.setObjectName("lb_pie")
        pixmap = QtGui.QPixmap('Piefin.png')
        self.lb_pie.setPixmap(pixmap)
        self.lb_pie.setScaledContents(True)
        self.retranslateUi(wifpie)
        QtCore.QMetaObject.connectSlotsByName(wifpie)

    def retranslateUi(self, wifpie):
        _translate = QtCore.QCoreApplication.translate
        wifpie.setWindowTitle(_translate("wifpie", "Dialog"))
        self.lb_title.setText(_translate("wifpie", "   PIE CHART"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wifpie = QtWidgets.QDialog()
    ui = Ui_wifpie()
    ui.setupUi(wifpie)
    wifpie.show()
    sys.exit(app.exec_())

