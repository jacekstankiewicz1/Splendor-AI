# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GeneralGameLayout.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QStatusBar, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 745)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Create main layout for central widget
        self.mainLayout = QGridLayout(self.centralwidget)
        self.mainLayout.setObjectName(u"mainLayout")

        # Grid layout for game board
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        for i in range(3):
            for j in range(5):
                label = QLabel(self.centralwidget)
                label.setObjectName(f"label_{i}_{j}")
                label.setMinimumSize(QSize(10, 10))
                label.setMaximumSize(QSize(100, 100))
                label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
                self.gridLayout.addWidget(label, i, j)

        self.mainLayout.addLayout(self.gridLayout, 0, 0)

        # Vertical layout for buttons
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.buttons = []
        button_texts = ["Draw Tokens", "Buy Card", "Reserve Card", "Buy Reserved Card", "Swap Token", "Buy Noble"]
        for text in button_texts:
            button = QPushButton(self.centralwidget)
            button.setObjectName(text.replace(" ", "_"))
            button.setFont(QFont("", 14))
            button.setText(QCoreApplication.translate("MainWindow", text, None))
            self.verticalLayout.addWidget(button)
            self.buttons.append(button)

        self.mainLayout.addLayout(self.verticalLayout, 0, 1)

        # Horizontal layout for additional elements
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        for i in range(4):
            label = QLabel(self.centralwidget)
            label.setObjectName(f"horizontal_label_{i}")
            label.setMinimumSize(QSize(10, 10))
            label.setMaximumSize(QSize(100, 100))
            label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
            self.horizontalLayout.addWidget(label)

        self.mainLayout.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = MainWindow.menuBar()
        self.menubar.setObjectName(u"menubar")
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
