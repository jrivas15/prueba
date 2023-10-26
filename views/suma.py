# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suma.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(359, 364)
        Form.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.numero1_lineEdit = QLineEdit(Form)
        self.numero1_lineEdit.setObjectName(u"numero1_lineEdit")
        self.numero1_lineEdit.setMinimumSize(QSize(0, 28))
        self.numero1_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.numero1_lineEdit.setStyleSheet(u"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.numero1_lineEdit)

        self.numero2_lineEdit = QLineEdit(Form)
        self.numero2_lineEdit.setObjectName(u"numero2_lineEdit")
        self.numero2_lineEdit.setMinimumSize(QSize(0, 28))
        self.numero2_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.numero2_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)

        self.horizontalLayout_5.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(21)
        self.label_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.resultado_label = QLabel(Form)
        self.resultado_label.setObjectName(u"resultado_label")
        font3 = QFont()
        font3.setPointSize(22)
        self.resultado_label.setFont(font3)

        self.horizontalLayout_4.addWidget(self.resultado_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buton_suma = QPushButton(Form)
        self.buton_suma.setObjectName(u"buton_suma")
        font4 = QFont()
        font4.setPointSize(15)
        self.buton_suma.setFont(font4)
        icon = QIcon()
        icon.addFile(u":/iconos/assets/iconos/plus2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buton_suma.setIcon(icon)
        self.buton_suma.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.buton_suma)

        self.boton_borrar = QPushButton(Form)
        self.boton_borrar.setObjectName(u"boton_borrar")
        self.boton_borrar.setFont(font4)
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/iconos/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_borrar.setIcon(icon1)
        self.boton_borrar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.boton_borrar)

        self.boton_cerrar = QPushButton(Form)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setFont(font4)
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/iconos/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_cerrar.setIcon(icon2)
        self.boton_cerrar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.boton_cerrar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CALCULAR", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Operaciones", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"SUMA", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"RESTA", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"MULTIPLICACION", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"DIVISI\u00d3N", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Resultado =", None))
        self.resultado_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.buton_suma.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.boton_borrar.setText(QCoreApplication.translate("Form", u"BORRAR", None))
        self.boton_cerrar.setText(QCoreApplication.translate("Form", u"CERRAR", None))
    # retranslateUi

