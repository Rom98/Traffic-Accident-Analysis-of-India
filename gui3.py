# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pg3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from guib import Ui_Formb
from guic import Ui_Formc
from guip import Ui_Formp
from PIL import Image
import temp_final as tp
class Ui_Form3(object):
    def onbargen(self):
        s = str(self.comboBox_2.currentText())
        print("BAR TYPE:",s)
        if s == "Type of Accident":
            im1 = Image.open('tb.png')
        elif s == 'Monthly':
            im1 = Image.open('mA.png')
        else:
            im1 = Image.open('cb.png')
        im1.save('Barfin.png')
        
        self.cW = QtWidgets.QMainWindow()
        self.ui = Ui_Formb()
        self.ui.setupUi(self.cW)
       # Form = QtWidgets.QWidget()
        #Form.hide()
        self.cW.show()
        
    def onpiegen(self):
        s = str(self.comboBox.currentText())
        print("GRAPH TYPE:",s)
        if s != "Based on Month":
            im1 = Image.open('stp.png')
        else:
            im1 = Image.open('smp.png')
        im1.save('Piefin.png')
        self.hW = QtWidgets.QMainWindow()
        self.ui = Ui_Formp()
        self.ui.setupUi(self.hW)
       # Form = QtWidgets.QWidget()
        #Form.hide()
        self.hW.show()
        
    def ontrendgen(self):
        self.lW = QtWidgets.QMainWindow()
        self.ui = Ui_Formc()
        self.ui.setupUi(self.lW)
       # Form = QtWidgets.QWidget()
        #Form.hide()
        self.lW.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(863, 472)
        Form.setStyleSheet("background-color: rgb(148, 164, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 701, 41))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(510, 110, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 150, 221, 27))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(510, 150, 221, 27))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.trendgen = QtWidgets.QPushButton(Form)
        self.trendgen.setGeometry(QtCore.QRect(360, 200, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.trendgen.setFont(font)
        self.trendgen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.trendgen.setFlat(False)
        self.trendgen.setObjectName("trendgen")
        self.piegen = QtWidgets.QPushButton(Form)
        self.piegen.setGeometry(QtCore.QRect(160, 200, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.piegen.setFont(font)
        self.piegen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.piegen.setFlat(False)
        self.piegen.setObjectName("piegen")
        self.bargen = QtWidgets.QPushButton(Form)
        self.bargen.setGeometry(QtCore.QRect(560, 200, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bargen.setFont(font)
        self.bargen.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(170, 255, 127, 255), stop:1 rgba(255, 255, 255, 255));")
        self.bargen.setFlat(False)
        self.bargen.setObjectName("bargen")
        self.safetimelab = QtWidgets.QLabel(Form)
        self.safetimelab.setGeometry(QtCore.QRect(110, 370, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.safetimelab.setFont(font)
        self.safetimelab.setText(tp.safestat)
        self.safetimelab.setObjectName("safetimelab")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "GRAPH BASED DATA ANALYSIS"))
        self.label_2.setText(_translate("Form", "PIE CHARTS:"))
        self.label_3.setText(_translate("Form", "BAR GRAPHS:"))
        self.comboBox.setItemText(0, _translate("Form", "Select Category"))
        self.comboBox.setItemText(1, _translate("Form", "Based on Month"))
        self.comboBox.setItemText(2, _translate("Form", "Based on Time Slot"))
        self.comboBox_2.setItemText(0, _translate("Form", "Select Category"))
        self.comboBox_2.setItemText(1, _translate("Form", "Type of Accident"))
        self.comboBox_2.setItemText(2, _translate("Form", "Monthly"))
        self.comboBox_2.setItemText(3, _translate("Form", "According to Time Slot"))
        self.trendgen.setText(_translate("Form", "TREND PLOT"))
        self.piegen.setText(_translate("Form", "Generate"))
        self.bargen.setText(_translate("Form", "Generate"))
        self.trendgen.clicked.connect(self.ontrendgen)
        self.piegen.clicked.connect(self.onpiegen)
        self.bargen.clicked.connect(self.onbargen)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

