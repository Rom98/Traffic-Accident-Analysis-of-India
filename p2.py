# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pg2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1659, 926)
        Form.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 981, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 30, 651, 511))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 600, 1641, 271))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(50, 230, 881, 21))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 180, 841, 31))
        self.horizontalSlider.setMinimum(2001)
        self.horizontalSlider.setMaximum(2014)
        self.horizontalSlider.setProperty("value", 2001)
        self.horizontalSlider.setSliderPosition(2001)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(280, 10, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(1110, 60, 451, 41))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(1010, 30, 91, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(1170, 150, 381, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(990, 0, 20, 271))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(1270, 220, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(1020, 10, 621, 561))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(240, 290, 70, 21))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 590, 1641, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(10, 870, 1651, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(1000, 0, 20, 601))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "2001     2002     2003      2004      2005      2006      2007      2008      2009      2010      2011      2012    2013    2014 "))
        self.label_2.setText(_translate("Form", "YEAR OF ACCIDENT"))
        self.comboBox_2.setItemText(0, _translate("Form", "Andaman and Nicobar\n"
""))
        self.comboBox_2.setItemText(1, _translate("Form", "Andhra Pradesh\n"
""))
        self.comboBox_2.setItemText(2, _translate("Form", "Arunachal Pradesh\n"
""))
        self.comboBox_2.setItemText(3, _translate("Form", "Assam\n"
""))
        self.comboBox_2.setItemText(4, _translate("Form", "Bihar\n"
""))
        self.comboBox_2.setItemText(5, _translate("Form", "Chandigarh\n"
""))
        self.comboBox_2.setItemText(6, _translate("Form", "Chhattisgarh\n"
""))
        self.comboBox_2.setItemText(7, _translate("Form", "Dadra and Nagar Haveli\n"
""))
        self.comboBox_2.setItemText(8, _translate("Form", "Daman and Diu\n"
""))
        self.comboBox_2.setItemText(9, _translate("Form", "Delhi\n"
""))
        self.comboBox_2.setItemText(10, _translate("Form", "Goa\n"
""))
        self.comboBox_2.setItemText(11, _translate("Form", "Gujarat\n"
""))
        self.comboBox_2.setItemText(12, _translate("Form", "Haryana\n"
""))
        self.comboBox_2.setItemText(13, _translate("Form", "Himachal Pradesh\n"
""))
        self.comboBox_2.setItemText(14, _translate("Form", "Jammu and Kashmir\n"
""))
        self.comboBox_2.setItemText(15, _translate("Form", "Jharkhand\n"
""))
        self.comboBox_2.setItemText(16, _translate("Form", "Karnataka\n"
""))
        self.comboBox_2.setItemText(17, _translate("Form", "Kerala\n"
""))
        self.comboBox_2.setItemText(18, _translate("Form", "Lakshadweep\n"
""))
        self.comboBox_2.setItemText(19, _translate("Form", "Madhya Pradesh\n"
""))
        self.comboBox_2.setItemText(20, _translate("Form", "Maharashtra\n"
""))
        self.comboBox_2.setItemText(21, _translate("Form", "Manipur\n"
""))
        self.comboBox_2.setItemText(22, _translate("Form", "Meghalaya\n"
""))
        self.comboBox_2.setItemText(23, _translate("Form", "Mizoram\n"
""))
        self.comboBox_2.setItemText(24, _translate("Form", "Nagaland\n"
""))
        self.comboBox_2.setItemText(25, _translate("Form", "Odisha\n"
""))
        self.comboBox_2.setItemText(26, _translate("Form", "Puducherry\n"
""))
        self.comboBox_2.setItemText(27, _translate("Form", "Punjab\n"
""))
        self.comboBox_2.setItemText(28, _translate("Form", "Rajasthan\n"
""))
        self.comboBox_2.setItemText(29, _translate("Form", "Sikkim\n"
""))
        self.comboBox_2.setItemText(30, _translate("Form", "Tamil Nadu\n"
""))
        self.comboBox_2.setItemText(31, _translate("Form", "Tripura\n"
""))
        self.comboBox_2.setItemText(32, _translate("Form", "Uttar Pradesh\n"
""))
        self.comboBox_2.setItemText(33, _translate("Form", "Uttarakhand\n"
""))
        self.comboBox_2.setItemText(34, _translate("Form", "West Bengal\n"
""))
        self.label_4.setText(_translate("Form", "STATE :"))
        self.checkBox.setText(_translate("Form", "Complete Analysis"))
        self.pushButton.setText(_translate("Form", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

