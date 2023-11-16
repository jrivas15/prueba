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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(546, 554)
        Form.setStyleSheet(u"QLineEdit{\n"
"border-radius:10px;\n"
"border: 1px solid black;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab)
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
        self.numero1_lineEdit = QLineEdit(self.tab)
        self.numero1_lineEdit.setObjectName(u"numero1_lineEdit")
        self.numero1_lineEdit.setMinimumSize(QSize(0, 28))
        self.numero1_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.numero1_lineEdit.setStyleSheet(u"border-radius:10px;")

        self.horizontalLayout_3.addWidget(self.numero1_lineEdit)

        self.numero2_lineEdit = QLineEdit(self.tab)
        self.numero2_lineEdit.setObjectName(u"numero2_lineEdit")
        self.numero2_lineEdit.setMinimumSize(QSize(0, 28))
        self.numero2_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.numero2_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.comboBox = QComboBox(self.tab)
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
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(21)
        self.label_2.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.resultado_label = QLabel(self.tab)
        self.resultado_label.setObjectName(u"resultado_label")
        font3 = QFont()
        font3.setPointSize(22)
        self.resultado_label.setFont(font3)

        self.horizontalLayout_4.addWidget(self.resultado_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buton_suma = QPushButton(self.tab)
        self.buton_suma.setObjectName(u"buton_suma")
        font4 = QFont()
        font4.setPointSize(15)
        self.buton_suma.setFont(font4)
        icon = QIcon()
        icon.addFile(u":/iconos/assets/iconos/plus2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buton_suma.setIcon(icon)
        self.buton_suma.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.buton_suma)

        self.boton_borrar = QPushButton(self.tab)
        self.boton_borrar.setObjectName(u"boton_borrar")
        self.boton_borrar.setFont(font4)
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/iconos/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_borrar.setIcon(icon1)
        self.boton_borrar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.boton_borrar)

        self.boton_cerrar = QPushButton(self.tab)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setFont(font4)
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/iconos/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.boton_cerrar.setIcon(icon2)
        self.boton_cerrar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.boton_cerrar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(20)
        self.label_4.setFont(font5)

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.buscar_line = QLineEdit(self.tab_2)
        self.buscar_line.setObjectName(u"buscar_line")

        self.horizontalLayout_2.addWidget(self.buscar_line)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.alumnos_tableWidget = QTableWidget(self.tab_2)
        if (self.alumnos_tableWidget.columnCount() < 4):
            self.alumnos_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.alumnos_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.alumnos_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.alumnos_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.alumnos_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.alumnos_tableWidget.rowCount() < 3):
            self.alumnos_tableWidget.setRowCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.alumnos_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.alumnos_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.alumnos_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.alumnos_tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.alumnos_tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.alumnos_tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.alumnos_tableWidget.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.alumnos_tableWidget.setItem(1, 1, __qtablewidgetitem11)
        self.alumnos_tableWidget.setObjectName(u"alumnos_tableWidget")
        self.alumnos_tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.alumnos_tableWidget)

        self.btn_actualizar = QPushButton(self.tab_2)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setMaximumSize(QSize(150, 100))
        self.btn_actualizar.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_actualizar)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tab 1", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"SQL", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Buscar", None))
        ___qtablewidgetitem = self.alumnos_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.alumnos_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"nombre", None));
        ___qtablewidgetitem2 = self.alumnos_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"apellido", None));
        ___qtablewidgetitem3 = self.alumnos_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"asistencia", None));
        ___qtablewidgetitem4 = self.alumnos_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem5 = self.alumnos_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem6 = self.alumnos_tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"3", None));

        __sortingEnabled = self.alumnos_tableWidget.isSortingEnabled()
        self.alumnos_tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.alumnos_tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem8 = self.alumnos_tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"jonathan", None));
        ___qtablewidgetitem9 = self.alumnos_tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"rivas", None));
        ___qtablewidgetitem10 = self.alumnos_tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"SI", None));
        self.alumnos_tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_actualizar.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Alumnos", None))
    # retranslateUi

