# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wif2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import temp_final as tp
from win3 import Ui_wif3
class Ui_wif2(object):
    select_state = ""
    select_year = ""
    select_i_year = 2001
    safe = ""
    def onGen(self):
        mystate = str(self.comboBox_2.currentText())[:-1]
        self.select_state = mystate
        myyear = self.select_year
        myiyear = self.select_i_year
        print("State : ",mystate)
        print("Year : ",myyear)
        tp.safest_month_time(mystate)
        #pies
        tp.state_time_pie(mystate,myiyear)
        tp.state_month_pie(mystate,myiyear)
        #bars
        tp.type_barchart(mystate,myiyear)
        tp.cause_barchart(mystate)
        tp.monthlyAcc(mystate,myiyear)
        #analysis
        tp.total_acc_scatter()
        tp.vehicle_type_sales()
        tp.safest_month_time(mystate)
        tp.time_acc(mystate,myiyear)
        self.TW = QtWidgets.QMainWindow()
        self.ui = Ui_wif3()
        self.ui.setupUi(self.TW)
        #Form = QtWidgets.QWidget()
        #Form.hide()
        self.TW.show()
        
    def onChan(self):
        self.lb_year.setText(str(self.sliderv.value()))
        self.select_year = self.lb_year.text()
        self.select_i_year = self.sliderv.value()
        self.disp()
        
    def onCheck(self):
        
        if self.comcheck.isChecked() == True:
            self.sliderv.setDisabled(True)
            self.lb_year.setText("...")
            self.select_year ='Total'
            self.select_i_year = 111
        else:
            self.sliderv.setDisabled(False)
            self.select_year =str(self.sliderv.value())
            self.lb_year.setText(self.select_year)
            self.select_year = self.lb_year.text()
            self.select_i_year = self.sliderv.value()
        self.disp()
         
    def disp(self):
        myvaluei = self.select_i_year
        tp.acctype_piechart(myvaluei)
        pieg2 = QtGui.QPixmap('pieg2.png')
        self.img_pie.setPixmap(pieg2)
        self.img_pie.setScaledContents(True)
        myvalue = self.select_year
        if myvalue == '2001': 
            pixmap = QtGui.QPixmap('2001.png')
        if myvalue == '2002': 
            pixmap = QtGui.QPixmap('2002.png')
        if myvalue == '2003': 
            pixmap = QtGui.QPixmap('2003.png')
        if myvalue == '2004': 
            pixmap = QtGui.QPixmap('2004.png')
        if myvalue == '2005': 
            pixmap = QtGui.QPixmap('2005.png')
        if myvalue == '2006': 
            pixmap = QtGui.QPixmap('2006.png')
        if myvalue == '2007': 
            pixmap = QtGui.QPixmap('2007.png')
        if myvalue == '2008': 
            pixmap = QtGui.QPixmap('2008.png')
        if myvalue == '2009': 
            pixmap = QtGui.QPixmap('2009.png')
        if myvalue == '2010': 
            pixmap = QtGui.QPixmap('2010.png')
        if myvalue == '2011': 
            pixmap = QtGui.QPixmap('2011.png')
        if myvalue == '2012': 
            pixmap = QtGui.QPixmap('2012.png')
        if myvalue == '2013': 
            pixmap = QtGui.QPixmap('2013.png')
        if myvalue == '2014': 
            pixmap = QtGui.QPixmap('2014.png')
        if myvalue == 'Total':
            pixmap = QtGui.QPixmap('Total.png')    
        self.img_map.setPixmap(pixmap)
        
        
    def setupUi(self, wif2):
        wif2.setObjectName("wif2")
        wif2.setWindowModality(QtCore.Qt.NonModal)
        wif2.setEnabled(True)
        wif2.resize(1152, 658)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wif2.setWindowIcon(icon)
        wif2.setToolTip("")
        wif2.setStatusTip("")
        wif2.setWhatsThis("")
        self.lb_u1 = QtWidgets.QLabel(wif2)
        self.lb_u1.setGeometry(QtCore.QRect(660, 480, 231, 41))
        self.lb_u1.setStyleSheet("font: 17pt \"MS Shell Dlg 2\";\n"
"color : white;")
        self.lb_u1.setObjectName("lb_u1")
        self.lb_year = QtWidgets.QLabel(wif2)
        self.lb_year.setGeometry(QtCore.QRect(865, 477, 116, 48))
        self.lb_year.setStyleSheet("color: white;")
        self.lb_year.setText("")
        self.lb_year.setObjectName("lb_year")
        self.lb_year.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color : white;")
        self.comcheck = QtWidgets.QCheckBox(wif2)
        self.comcheck.setGeometry(QtCore.QRect(930, 540, 161, 25))
        self.comcheck.stateChanged.connect(self.onCheck)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.comcheck.setFont(font)
        self.comcheck.setStyleSheet("color: white;\n"
"")
        self.comcheck.setObjectName("comcheck")
        self.img_pie = QtWidgets.QLabel(wif2)
        self.img_pie.setGeometry(QtCore.QRect(640, 10, 491, 441))
        self.img_pie.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.img_pie.setText("")
        self.img_pie.setObjectName("img_pie")
        self.genbtn = QtWidgets.QPushButton(wif2)
        self.genbtn.setGeometry(QtCore.QRect(930, 590, 112, 34))
        self.genbtn.setObjectName("genbtn")
        self.genbtn.clicked.connect(self.onGen)
        self.genbtn.setFont(font)
        self.sliderv = QtWidgets.QSlider(wif2)
        self.sliderv.setGeometry(QtCore.QRect(610, 20, 21, 631))
        self.sliderv.setMinimum(2001)
        self.sliderv.setMaximum(2014)
        self.sliderv.setOrientation(QtCore.Qt.Vertical)
        self.sliderv.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.sliderv.setTickInterval(1)
        self.sliderv.setObjectName("sliderv")
        self.sliderv.valueChanged.connect(self.onChan)
        self.label_2 = QtWidgets.QLabel(wif2)
        self.label_2.setGeometry(QtCore.QRect(310, 630, 151, 21))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.img_map = QtWidgets.QLabel(wif2)
        self.img_map.setGeometry(QtCore.QRect(20, 10, 581, 641))
        self.img_map.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.img_map.setText("")
        self.img_map.setObjectName("img_map")
        self.lb_bck = QtWidgets.QLabel(wif2)
        self.lb_bck.setGeometry(QtCore.QRect(0, 0, 1161, 661))
        self.lb_bck.setStyleSheet("")
        self.lb_bck.setText("")
        self.lb_bck.setPixmap(QtGui.QPixmap("dark-background-with-star-like-dots_bkpaotdgh__F0000.png"))
        self.lb_bck.setScaledContents(True)
        self.lb_bck.setObjectName("lb_bck")
        self.formLayoutWidget_2 = QtWidgets.QWidget(wif2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(740, 540, 181, 23))
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
        self.comboBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n")
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
        self.lb_menu_bk = QtWidgets.QLabel(wif2)
        self.lb_menu_bk.setGeometry(QtCore.QRect(640, 460, 491, 181))
        self.lb_menu_bk.setStyleSheet("background-image: url(:/img/Dark-Navy-580x580.jpg);")
        self.lb_menu_bk.setText("")
        self.lb_menu_bk.setObjectName("lb_menu_bk")
        self.lb_u2 = QtWidgets.QLabel(wif2)
        self.lb_u2.setGeometry(QtCore.QRect(660, 540, 71, 16))
        self.lb_u2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color : white;")
        self.lb_u2.setObjectName("lb_u2")
        self.lb_menu_bk.raise_()
        self.lb_bck.raise_()
        self.lb_u1.raise_()
        self.lb_year.raise_()
        self.comcheck.raise_()
        self.img_pie.raise_()
        self.genbtn.raise_()
        self.sliderv.raise_()
        self.label_2.raise_()
        self.img_map.raise_()
        self.formLayoutWidget_2.raise_()
        self.lb_u2.raise_()
        self.select_state = self.comboBox_2.currentText()
        self.select_year = "2001"
        self.select_i_year = 2001
        
        tp.acctype_piechart(2001)
        pieg2 = QtGui.QPixmap('pieg2.png')
        self.img_pie.setPixmap(pieg2)
        self.img_pie.setScaledContents(True)
        
        pixmap = QtGui.QPixmap('2001.png')
        self.img_map.setPixmap(pixmap)
        self.img_map.setScaledContents(True)
      
        
        print(self.select_state)
        self.retranslateUi(wif2)
        QtCore.QMetaObject.connectSlotsByName(wif2)

    def retranslateUi(self, wif2):
        _translate = QtCore.QCoreApplication.translate
        wif2.setWindowTitle(_translate("wif2", "Dialog"))
        self.lb_u1.setText(_translate("wif2", "SELECTED YEAR :"))
        self.comcheck.setText(_translate("wif2", "Complete Analysis"))
        self.genbtn.setText(_translate("wif2", "Generate"))
        self.comboBox_2.setItemText(0, _translate("wif2", "A & N Islands\n"
""))
        self.comboBox_2.setItemText(1, _translate("wif2", "Andhra Pradesh\n"
""))
        self.comboBox_2.setItemText(2, _translate("wif2", "Arunachal Pradesh\n"
""))
        self.comboBox_2.setItemText(3, _translate("wif2", "Assam\n"
""))
        self.comboBox_2.setItemText(4, _translate("wif2", "Bihar\n"
""))
        self.comboBox_2.setItemText(5, _translate("wif2", "Chandigarh\n"
""))
        self.comboBox_2.setItemText(6, _translate("wif2", "Chhattisgarh\n"
""))
        self.comboBox_2.setItemText(7, _translate("wif2", "D & N Haveli\n"
""))
        self.comboBox_2.setItemText(8, _translate("wif2", "Daman and Diu\n"
""))
        self.comboBox_2.setItemText(9, _translate("wif2", "Delhi (Ut)\n"
""))
        self.comboBox_2.setItemText(10, _translate("wif2", "Goa\n"
""))
        self.comboBox_2.setItemText(11, _translate("wif2", "Gujarat\n"
""))
        self.comboBox_2.setItemText(12, _translate("wif2", "Haryana\n"
""))
        self.comboBox_2.setItemText(13, _translate("wif2", "Himachal Pradesh\n"
""))
        self.comboBox_2.setItemText(14, _translate("wif2", "Jammu and Kashmir\n"
""))
        self.comboBox_2.setItemText(15, _translate("wif2", "Jharkhand\n"
""))
        self.comboBox_2.setItemText(16, _translate("wif2", "Karnataka\n"
""))
        self.comboBox_2.setItemText(17, _translate("wif2", "Kerala\n"
""))
        self.comboBox_2.setItemText(18, _translate("wif2", "Lakshadweep\n"
""))
        self.comboBox_2.setItemText(19, _translate("wif2", "Madhya Pradesh\n"
""))
        self.comboBox_2.setItemText(20, _translate("wif2", "Maharashtra\n"
""))
        self.comboBox_2.setItemText(21, _translate("wif2", "Manipur\n"
""))
        self.comboBox_2.setItemText(22, _translate("wif2", "Meghalaya\n"
""))
        self.comboBox_2.setItemText(23, _translate("wif2", "Mizoram\n"
""))
        self.comboBox_2.setItemText(24, _translate("wif2", "Nagaland\n"
""))
        self.comboBox_2.setItemText(25, _translate("wif2", "Odisha\n"
""))
        self.comboBox_2.setItemText(26, _translate("wif2", "Puducherry\n"
""))
        self.comboBox_2.setItemText(27, _translate("wif2", "Punjab\n"
""))
        self.comboBox_2.setItemText(28, _translate("wif2", "Rajasthan\n"
""))
        self.comboBox_2.setItemText(29, _translate("wif2", "Sikkim\n"
""))
        self.comboBox_2.setItemText(30, _translate("wif2", "Tamil Nadu\n"
""))
        self.comboBox_2.setItemText(31, _translate("wif2", "Tripura\n"
""))
        self.comboBox_2.setItemText(32, _translate("wif2", "Uttar Pradesh\n"
""))
        self.comboBox_2.setItemText(33, _translate("wif2", "Uttarakhand\n"
""))
        self.comboBox_2.setItemText(34, _translate("wif2", "West Bengal\n"
""))
        self.lb_u2.setText(_translate("wif2", "STATE :"))
        self.lb_year.setText(_translate("wif2", "2001"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wif2 = QtWidgets.QDialog()
    ui = Ui_wif2()
    ui.setupUi(wif2)
    wif2.show()
    sys.exit(app.exec_())

