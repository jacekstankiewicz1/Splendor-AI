# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_widget.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QListWidget,
    QListWidgetItem, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CardWidget(object):
    def setupUi(self, CardWidget):
        if not CardWidget.objectName():
            CardWidget.setObjectName(u"CardWidget")
        CardWidget.resize(240, 226)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CardWidget.sizePolicy().hasHeightForWidth())
        CardWidget.setSizePolicy(sizePolicy)
        CardWidget.setStyleSheet(u"border-radius: 50px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #7eb3ff, stop:1 #446fad);\n"
"padding: 20px;\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(CardWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CardWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Berlin Sans FB Demi"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-radius: 25px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #59b9ff, stop:1 #004aad);\n"
"padding: 12px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(CardWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setSizeIncrement(QSize(0, 0))
        self.listWidget.setStyleSheet(u"border-radius: 25px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #59b9ff, stop:1 #004aad);\n"
"padding: 12px;\n"
"\n"
"")
        self.listWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout.addWidget(self.listWidget)


        self.retranslateUi(CardWidget)

        QMetaObject.connectSlotsByName(CardWidget)
    # setupUi

    def retranslateUi(self, CardWidget):
        CardWidget.setWindowTitle(QCoreApplication.translate("CardWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("CardWidget", u"7", None))
    # retranslateUi

