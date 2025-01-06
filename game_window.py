# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(711, 854)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"background-color: rgb(84, 79, 82)")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tokenLayout = QGridLayout()
        self.tokenLayout.setObjectName(u"tokenLayout")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QSize(10, 10))
        self.label_23.setMaximumSize(QSize(100, 100))

        self.tokenLayout.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(10, 10))
        self.label_25.setMaximumSize(QSize(100, 100))

        self.tokenLayout.addWidget(self.label_25, 0, 2, 1, 1)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(10, 10))
        self.label_24.setMaximumSize(QSize(100, 100))

        self.tokenLayout.addWidget(self.label_24, 0, 1, 1, 1)

        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(10, 10))
        self.label_26.setMaximumSize(QSize(100, 100))

        self.tokenLayout.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(10, 10))
        self.label_27.setMaximumSize(QSize(100, 100))

        self.tokenLayout.addWidget(self.label_27, 1, 1, 1, 1)

        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(10, 10))
        self.label_28.setMaximumSize(QSize(100, 100))

        self.tokenLayout.addWidget(self.label_28, 1, 2, 1, 1)


        self.gridLayout.addLayout(self.tokenLayout, 3, 3, 1, 2)

        self.playerLayout = QHBoxLayout()
        self.playerLayout.setObjectName(u"playerLayout")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QSize(10, 10))
        self.label_32.setMaximumSize(QSize(100, 100))

        self.playerLayout.addWidget(self.label_32)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(10, 10))
        self.label_31.setMaximumSize(QSize(100, 100))

        self.playerLayout.addWidget(self.label_31)

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QSize(10, 10))
        self.label_30.setMaximumSize(QSize(100, 100))

        self.playerLayout.addWidget(self.label_30)

        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QSize(10, 10))
        self.label_29.setMaximumSize(QSize(100, 100))

        self.playerLayout.addWidget(self.label_29)


        self.gridLayout.addLayout(self.playerLayout, 4, 0, 1, 6)

        self.deckLayout = QVBoxLayout()
        self.deckLayout.setObjectName(u"deckLayout")
        self.d1 = QLabel(self.centralwidget)
        self.d1.setObjectName(u"d1")
        sizePolicy.setHeightForWidth(self.d1.sizePolicy().hasHeightForWidth())
        self.d1.setSizePolicy(sizePolicy)

        self.deckLayout.addWidget(self.d1)

        self.d2 = QLabel(self.centralwidget)
        self.d2.setObjectName(u"d2")
        sizePolicy.setHeightForWidth(self.d2.sizePolicy().hasHeightForWidth())
        self.d2.setSizePolicy(sizePolicy)

        self.deckLayout.addWidget(self.d2)

        self.d3 = QLabel(self.centralwidget)
        self.d3.setObjectName(u"d3")
        sizePolicy.setHeightForWidth(self.d3.sizePolicy().hasHeightForWidth())
        self.d3.setSizePolicy(sizePolicy)

        self.deckLayout.addWidget(self.d3)


        self.gridLayout.addLayout(self.deckLayout, 1, 0, 3, 1)

        self.cardLayout = QGridLayout()
        self.cardLayout.setObjectName(u"cardLayout")
        self.t11 = QLabel(self.centralwidget)
        self.t11.setObjectName(u"t11")
        sizePolicy.setHeightForWidth(self.t11.sizePolicy().hasHeightForWidth())
        self.t11.setSizePolicy(sizePolicy)
        self.t11.setMinimumSize(QSize(10, 10))
        self.t11.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t11, 2, 0, 1, 1)

        self.t31 = QLabel(self.centralwidget)
        self.t31.setObjectName(u"t31")
        sizePolicy.setHeightForWidth(self.t31.sizePolicy().hasHeightForWidth())
        self.t31.setSizePolicy(sizePolicy)
        self.t31.setMinimumSize(QSize(10, 10))
        self.t31.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t31, 0, 0, 1, 1)

        self.t13 = QLabel(self.centralwidget)
        self.t13.setObjectName(u"t13")
        sizePolicy.setHeightForWidth(self.t13.sizePolicy().hasHeightForWidth())
        self.t13.setSizePolicy(sizePolicy)
        self.t13.setMinimumSize(QSize(10, 10))
        self.t13.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t13, 2, 2, 1, 1)

        self.t32 = QLabel(self.centralwidget)
        self.t32.setObjectName(u"t32")
        sizePolicy.setHeightForWidth(self.t32.sizePolicy().hasHeightForWidth())
        self.t32.setSizePolicy(sizePolicy)
        self.t32.setMinimumSize(QSize(10, 10))
        self.t32.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t32, 0, 1, 1, 1)

        self.t34 = QLabel(self.centralwidget)
        self.t34.setObjectName(u"t34")
        sizePolicy.setHeightForWidth(self.t34.sizePolicy().hasHeightForWidth())
        self.t34.setSizePolicy(sizePolicy)
        self.t34.setMinimumSize(QSize(10, 10))
        self.t34.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t34, 0, 3, 1, 1)

        self.t33 = QLabel(self.centralwidget)
        self.t33.setObjectName(u"t33")
        sizePolicy.setHeightForWidth(self.t33.sizePolicy().hasHeightForWidth())
        self.t33.setSizePolicy(sizePolicy)
        self.t33.setMinimumSize(QSize(10, 10))
        self.t33.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t33, 0, 2, 1, 1)

        self.t24 = QLabel(self.centralwidget)
        self.t24.setObjectName(u"t24")
        sizePolicy.setHeightForWidth(self.t24.sizePolicy().hasHeightForWidth())
        self.t24.setSizePolicy(sizePolicy)
        self.t24.setMinimumSize(QSize(10, 10))
        self.t24.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t24, 1, 3, 1, 1)

        self.t21 = QLabel(self.centralwidget)
        self.t21.setObjectName(u"t21")
        sizePolicy.setHeightForWidth(self.t21.sizePolicy().hasHeightForWidth())
        self.t21.setSizePolicy(sizePolicy)
        self.t21.setMinimumSize(QSize(10, 10))
        self.t21.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t21, 1, 0, 1, 1)

        self.t23 = QLabel(self.centralwidget)
        self.t23.setObjectName(u"t23")
        sizePolicy.setHeightForWidth(self.t23.sizePolicy().hasHeightForWidth())
        self.t23.setSizePolicy(sizePolicy)
        self.t23.setMinimumSize(QSize(10, 10))
        self.t23.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t23, 1, 2, 1, 1)

        self.t12 = QLabel(self.centralwidget)
        self.t12.setObjectName(u"t12")
        sizePolicy.setHeightForWidth(self.t12.sizePolicy().hasHeightForWidth())
        self.t12.setSizePolicy(sizePolicy)
        self.t12.setMinimumSize(QSize(10, 10))
        self.t12.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t12, 2, 1, 1, 1)

        self.t22 = QLabel(self.centralwidget)
        self.t22.setObjectName(u"t22")
        sizePolicy.setHeightForWidth(self.t22.sizePolicy().hasHeightForWidth())
        self.t22.setSizePolicy(sizePolicy)
        self.t22.setMinimumSize(QSize(10, 10))
        self.t22.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t22, 1, 1, 1, 1)

        self.t14 = QLabel(self.centralwidget)
        self.t14.setObjectName(u"t14")
        sizePolicy.setHeightForWidth(self.t14.sizePolicy().hasHeightForWidth())
        self.t14.setSizePolicy(sizePolicy)
        self.t14.setMinimumSize(QSize(10, 10))
        self.t14.setMaximumSize(QSize(100, 100))

        self.cardLayout.addWidget(self.t14, 2, 3, 1, 1)


        self.gridLayout.addLayout(self.cardLayout, 1, 1, 3, 2)

        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)

        self.buttonLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font)

        self.buttonLayout.addWidget(self.pushButton_4, 0, Qt.AlignVCenter)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setFont(font)

        self.buttonLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font)

        self.buttonLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font)

        self.buttonLayout.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font)

        self.buttonLayout.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.buttonLayout, 1, 5, 3, 1)

        self.nobleLayout = QVBoxLayout()
        self.nobleLayout.setObjectName(u"nobleLayout")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(10, 10))
        self.label_21.setMaximumSize(QSize(100, 100))

        self.nobleLayout.addWidget(self.label_21)

        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(10, 10))
        self.label_20.setMaximumSize(QSize(100, 100))

        self.nobleLayout.addWidget(self.label_20)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(10, 10))
        self.label_22.setMaximumSize(QSize(100, 100))

        self.nobleLayout.addWidget(self.label_22)


        self.gridLayout.addLayout(self.nobleLayout, 1, 3, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 4)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.d1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.d2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.d3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t34.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t24.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t23.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.t14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Draw Tokens", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Buy Card", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Reserve Card", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Buy Reserved Card", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Swap Token", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Buy Noble", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

