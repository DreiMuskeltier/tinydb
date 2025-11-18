# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Beispiel.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(687, 650)
        self.actionBeenden = QAction(MainWindow)
        self.actionBeenden.setObjectName(u"actionBeenden")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelName = QLabel(self.centralwidget)
        self.labelName.setObjectName(u"labelName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelName)

        self.inputName = QLineEdit(self.centralwidget)
        self.inputName.setObjectName(u"inputName")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.inputName)

        self.labelAge = QLabel(self.centralwidget)
        self.labelAge.setObjectName(u"labelAge")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelAge)

        self.inputAge = QLineEdit(self.centralwidget)
        self.inputAge.setObjectName(u"inputAge")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.inputAge)

        self.labelCity = QLabel(self.centralwidget)
        self.labelCity.setObjectName(u"labelCity")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.labelCity)

        self.inputCity = QLineEdit(self.centralwidget)
        self.inputCity.setObjectName(u"inputCity")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.inputCity)

        self.buttonSave = QPushButton(self.centralwidget)
        self.buttonSave.setObjectName(u"buttonSave")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.buttonSave)

        self.logOutput = QTextEdit(self.centralwidget)
        self.logOutput.setObjectName(u"logOutput")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logOutput.sizePolicy().hasHeightForWidth())
        self.logOutput.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.logOutput)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.tableWidget)

        self.pushLoadDB = QPushButton(self.centralwidget)
        self.pushLoadDB.setObjectName(u"pushLoadDB")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.pushLoadDB)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonDelete = QPushButton(self.centralwidget)
        self.buttonDelete.setObjectName(u"buttonDelete")

        self.verticalLayout.addWidget(self.buttonDelete)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 687, 33))
        self.menuDatei = QMenu(self.menubar)
        self.menuDatei.setObjectName(u"menuDatei")
        MainWindow.setMenuBar(self.menubar)

        MainWindow.addAction(self.actionBeenden)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menuDatei.addAction(self.actionBeenden)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Daten in TinyDB laden", None))
        self.actionBeenden.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.labelAge.setText(QCoreApplication.translate("MainWindow", u"Alter:", None))
        self.labelCity.setText(QCoreApplication.translate("MainWindow", u"Stadt:", None))
        self.buttonSave.setText(QCoreApplication.translate("MainWindow", u"In TinyDB speichern", None))
        self.logOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Status / R\u00fcckmeldungen\u2026", None))
        self.pushLoadDB.setText(QCoreApplication.translate("MainWindow", u"Datenbank laden", None))
        self.buttonDelete.setText(QCoreApplication.translate("MainWindow", u"Eintrag l\u00f6schen", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
    # retranslateUi

