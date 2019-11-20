# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wif3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from winp import Ui_wifpie
from winb import Ui_wifbar
from wift import Ui_Dialog
import temp_final as tp
from PIL import Image

class Ui_wif3(object):
    
    def onTren(self):
        
        self.lW = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.lW)
       # Form = QtWidgets.QWidget()
        #Form.hide()
        self.lW.show()
        
    def onPIEbtn(self):
        s = str(self.comboBox.currentText())
        print("GRAPH TYPE:",s)
        if s != "Based On Month":
            im1 = Image.open('stp.png')
        else:
            im1 = Image.open('smp.png')
        im1.save('Piefin.png')
        self.TW = QtWidgets.QMainWindow()
        self.ui = Ui_wifpie()
        self.ui.setupUi(self.TW)
        #Form = QtWidgets.QWidget()
        #Form.hide()
        self.TW.show()
    def onBARbtn(self):
        s = str(self.comboBox_2.currentText())
        print("BAR TYPE:",s)
        if s == "Type Of Accident":
            im1 = Image.open('tb.png')
        elif s == 'Monthly':
            im1 = Image.open('mA.png')
        elif s == 'According To Time Slot':
            im1 = Image.open('cb.png')
        else:
            im1 = Image.open('tt.png')
        im1.save('Barfin.png')
        
        self.cW = QtWidgets.QMainWindow()
        self.ui = Ui_wifbar()
        self.ui.setupUi(self.cW)
       # Form = QtWidgets.QWidget()
        #Form.hide()
        self.cW.show()
        
    def setupUi(self, wif3):
        wif3.setObjectName("wif3")
        wif3.resize(840, 647)
        wif3.setMinimumSize(QtCore.QSize(840, 647))
        wif3.setMaximumSize(QtCore.QSize(840, 647))
        wif3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wif3.setWindowIcon(icon)
        wif3.setWindowOpacity(0.979)
        self.lb_back = QtWidgets.QLabel(wif3)
        self.lb_back.setGeometry(QtCore.QRect(0, 0, 841, 651))
        self.lb_back.setText("")
        self.lb_back.setPixmap(QtGui.QPixmap("yy.jpg"))
        self.lb_back.setScaledContents(True)
        self.lb_back.setObjectName("lb_back")
        self.piebtn = QtWidgets.QPushButton(wif3)
        self.piebtn.setGeometry(QtCore.QRect(10, 260, 261, 251))
        self.piebtn.setStyleSheet("background-image: url(5a04024e5197733bb7d51d4398f7f375.png);\n"
"border-radius : 15px;")
        self.piebtn.setText("")
        self.piebtn.clicked.connect(self.onPIEbtn)
        self.piebtn.setObjectName("piebtn")
        self.barbtn = QtWidgets.QPushButton(wif3)
        self.barbtn.setGeometry(QtCore.QRect(600, 250, 600, 250))
        self.barbtn.setMinimumSize(QtCore.QSize(600, 250))
        self.barbtn.setMaximumSize(QtCore.QSize(600, 250))
        self.barbtn.setStyleSheet("border-radius: 30p;\n"
"background-image: url(bar-chart-png-image-37240.png);")
        self.barbtn.setText("")
        self.barbtn.clicked.connect(self.onBARbtn)
        self.barbtn.setObjectName("barbtn")
        self.trendbtn = QtWidgets.QPushButton(wif3)
        self.trendbtn.setGeometry(QtCore.QRect(310, 260, 261, 231))
        self.trendbtn.setStyleSheet("background-image: url(upward-trend (1).png);\n"
"border-radius : 15px;")
        self.trendbtn.setText("")
        self.trendbtn.clicked.connect(self.onTren)
        self.trendbtn.setObjectName("trendbtn")
        self.label = QtWidgets.QLabel(wif3)
        self.label.setGeometry(QtCore.QRect(0, 530, 841, 101))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(wif3)
        self.label_4.setGeometry(QtCore.QRect(0, 520, 851, 121))
        self.label_4.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(wif3)
        self.comboBox.setGeometry(QtCore.QRect(50, 560, 211, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(wif3)
        self.comboBox_2.setGeometry(QtCore.QRect(620, 560, 211, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(wif3)
        self.label_2.setGeometry(QtCore.QRect(360, 550, 181, 51))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color : white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.lb_state = QtWidgets.QLabel(wif3)
        self.lb_state.setGeometry(QtCore.QRect(170, 40, 201, 81))
        self.lb_state.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 30px;\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"")
        self.lb_state.setObjectName("lb_state")
        self.lb_state_in = QtWidgets.QLabel(wif3)
        self.lb_state_in.setGeometry(QtCore.QRect(390, 40, 331, 81))
        self.lb_state_in.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius: 30px")
        self.lb_state_in.setText(tp.statekk)
        self.lb_state_in.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_state_in.setObjectName("lb_state_in")
        self.label_6 = QtWidgets.QLabel(wif3)
        self.label_6.setGeometry(QtCore.QRect(60, 130, 731, 91))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.desc = QtWidgets.QLabel(wif3)
        self.desc.setGeometry(QtCore.QRect(40, 140, 771, 101))
        self.desc.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 30px;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.desc.setObjectName("desc")
        self.desc.setText(tp.safestat)
        self.desc.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_back.raise_()
        self.label_4.raise_()
        self.piebtn.raise_()
        self.barbtn.raise_()
        self.trendbtn.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.lb_state.raise_()
        self.lb_state_in.raise_()
        self.label_6.raise_()
        self.desc.raise_()

        self.retranslateUi(wif3)
        QtCore.QMetaObject.connectSlotsByName(wif3)

    def retranslateUi(self, wif3):
        _translate = QtCore.QCoreApplication.translate
        wif3.setWindowTitle(_translate("wif3", "GRAPH SELECT"))
        self.comboBox.setItemText(0, _translate("wif3", "Based On Month"))
        self.comboBox.setItemText(1, _translate("wif3", "Based On Time Slot"))
        self.comboBox_2.setItemText(0, _translate("wif3", "Type Of Accident"))
        self.comboBox_2.setItemText(1, _translate("wif3", "Monthly"))
        self.comboBox_2.setItemText(2, _translate("wif3", "According To Time Slot"))
        self.comboBox_2.setItemText(3, _translate("wif3", "Based On Causes"))
        self.label_2.setText(_translate("wif3", "TREND PLOT"))
        self.lb_state.setText(_translate("wif3", "STATE"))
        self.lb_state.setAlignment(QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wif3 = QtWidgets.QDialog()
    ui = Ui_wif3()
    ui.setupUi(wif3)
    wif3.show()
    sys.exit(app.exec_())

