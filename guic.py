# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comp.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formc(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1029, 541)
        Form.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 491, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 471, 491))
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap = QtGui.QPixmap('TOTacc.png')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(530, 20, 481, 501))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 471, 191))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        pixmap2 = QtGui.QPixmap('veh.png')
        self.label_2.setPixmap(pixmap2)
        self.label_2.setScaledContents(True)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formc()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

