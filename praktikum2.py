# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'praktikum2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1058, 642)
        Form.setMinimumSize(QtCore.QSize(1058, 642))
        Form.setMaximumSize(QtCore.QSize(1058, 642))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 641, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-50, -20, 681, 441))
        self.frame_2.setMaximumSize(QtCore.QSize(1280, 720))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1061, 661))
        self.frame_3.setStyleSheet("background-color: #1D4F42;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(680, 20, 561, 421))
        self.label_10.setStyleSheet("image: url(:/newPrefix/12.png);\n"
"background-color: transparent;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(520, 80, 741, 681))
        self.label_11.setStyleSheet("image: url(:/newPrefix/11.png);\n"
"background-color: transparent;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 240, 341, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setEnabled(True)
        self.radioButton.setAcceptDrops(True)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.radioButton.setChecked(True)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setTabletTracking(False)
        self.radioButton_2.setAcceptDrops(True)
        self.radioButton_2.setAutoFillBackground(False)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoRepeat(True)
        self.radioButton_2.setAutoRepeatDelay(297)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 140, 341, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 140, 301, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 79, 66);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertBeforeCurrent)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 79, 66);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertBeforeCurrent)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.comboBox_6 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(29, 79, 66);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_6)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_3.addWidget(self.label_20)
        self.comboBox_7 = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(29, 79, 66);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.comboBox_7.setEditable(False)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_7)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;\n"
"background-color: transparent;\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 20;")
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;\n"
"background-color: rgb(254, 186, 31);\n"
"border-radius: 10px; \n"
"border: 1px solid rgb(254, 186, 31); \n"
"height: 30;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(-100, 420, 421, 281))
        self.label_24.setStyleSheet("image: url(:/newPrefix/7.png);\n"
"background: transparent;\n"
"\n"
"")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(60, 440, 321, 341))
        self.label_26.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.label_26.setStyleSheet("image: url(:/newPrefix/8.png);\n"
"background: transparent;\n"
"\n"
"")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 81, 41))
        self.label_7.setMaximumSize(QtCore.QSize(100, 100))
        self.label_7.setStyleSheet("image: url(:/newPrefix/10.png);\n"
"background: transparent;")
        self.label_7.setLineWidth(0)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(80, 0, 179, 39))
        self.label.setStyleSheet("font: 13pt \"Geometr415 Blk BT\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 380, 341, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 41))
        self.lineEdit_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px; \n"
"border: 1px solid rgb(254, 186, 31); ")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(268, 60, 221, 59))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Playball\";\n"
"font-weight: 600;")
        self.label_12.setObjectName("label_12")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 241, 59))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("color: rgb(254, 186, 31);\n"
"font: 75 30pt \"MS Shell Dlg 2\";\n"
"font-weight: 600;")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(-40, 0, 1141, 681))
        self.label_4.setStyleSheet("image: url(:/newPrefix/9.png);\n"
"background-color: transparent;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(700, 280, 381, 441))
        self.label_18.setStyleSheet("image: url(:/newPrefix/1.png);\n"
"background: transparent;\n"
"\n"
"")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 461, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"font-weight: 200;")
        self.label_2.setObjectName("label_2")
        self.label_11.raise_()
        self.label_4.raise_()
        self.label_10.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.label_24.raise_()
        self.label_26.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.lineEdit_4.raise_()
        self.label_12.raise_()
        self.label_6.raise_()
        self.label_18.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_22.setText(_translate("Form", "Do you need your coffee iced?"))
        self.radioButton.setText(_translate("Form", "Yes"))
        self.radioButton_2.setText(_translate("Form", "No"))
        self.label_23.setText(_translate("Form", "Any instructions or additional requests?"))
        self.label_13.setText(_translate("Form", "Full name"))
        self.lineEdit.setPlaceholderText(_translate("Form", "First Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Last Name"))
        self.label_15.setText(_translate("Form", "Coffee size"))
        self.comboBox.setCurrentText(_translate("Form", "Small"))
        self.comboBox.setItemText(0, _translate("Form", "Small"))
        self.comboBox.setItemText(1, _translate("Form", "Medium"))
        self.comboBox.setItemText(2, _translate("Form", "Large"))
        self.label_16.setText(_translate("Form", "Coffee type"))
        self.comboBox_2.setCurrentText(_translate("Form", "Espresso"))
        self.comboBox_2.setItemText(0, _translate("Form", "Espresso"))
        self.comboBox_2.setItemText(1, _translate("Form", "Americano"))
        self.comboBox_2.setItemText(2, _translate("Form", "Mocha"))
        self.comboBox_2.setItemText(3, _translate("Form", "Cappuccino"))
        self.comboBox_2.setItemText(4, _translate("Form", "Latte"))
        self.label_19.setText(_translate("Form", "Milk Preference"))
        self.comboBox_6.setCurrentText(_translate("Form", "Regular"))
        self.comboBox_6.setItemText(0, _translate("Form", "Regular"))
        self.comboBox_6.setItemText(1, _translate("Form", "Almond"))
        self.comboBox_6.setItemText(2, _translate("Form", "Soy"))
        self.comboBox_6.setItemText(3, _translate("Form", "Oat"))
        self.label_20.setText(_translate("Form", "Additional toppings"))
        self.comboBox_7.setCurrentText(_translate("Form", "Whipped cream"))
        self.comboBox_7.setItemText(0, _translate("Form", "Whipped cream"))
        self.comboBox_7.setItemText(1, _translate("Form", "Caramel sauce"))
        self.comboBox_7.setItemText(2, _translate("Form", "Chocolate syrup"))
        self.comboBox_7.setItemText(3, _translate("Form", "Vanilla syrup"))
        self.comboBox_7.setItemText(4, _translate("Form", "Cinamon powder"))
        self.label_9.setText(_translate("Form", "Quantity"))
        self.pushButton.setText(_translate("Form", "Order"))
        self.label.setText(_translate("Form", "ZAFFEE BREW"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "ex: add extra shots of espresso"))
        self.label_12.setText(_translate("Form", "form"))
        self.label_6.setText(_translate("Form", "ORDER"))
        self.label_2.setText(_translate("Form", "Developed by Zakiyya Khairani"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
