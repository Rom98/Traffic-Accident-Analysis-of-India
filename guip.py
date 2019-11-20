# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PIe.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formp(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 441)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 531, 411))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 511, 391))
        self.label.setText("")
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        pixmap = QtGui.QPixmap('Piefin.png')
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formp()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

