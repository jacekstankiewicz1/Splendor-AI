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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CardWidget(object):
    def setupUi(self, CardWidget):
        if not CardWidget.objectName():
            CardWidget.setObjectName(u"CardWidget")
        CardWidget.resize(239, 421)
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
        self.cardValue = QLabel(CardWidget)
        self.cardValue.setObjectName(u"cardValue")
        font = QFont()
        font.setFamilies([u"Berlin Sans FB Demi"])
        font.setBold(True)
        self.cardValue.setFont(font)
        self.cardValue.setStyleSheet(u"border-radius: 25px;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #59b9ff, stop:1 #004aad);\n"
"padding: 12px;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.cardValue)

        self.tokenContainer = QWidget(CardWidget)
        self.tokenContainer.setObjectName(u"tokenContainer")
        self.verticalLayout_3 = QVBoxLayout(self.tokenContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout.addWidget(self.tokenContainer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(CardWidget)

        QMetaObject.connectSlotsByName(CardWidget)
    # setupUi

    def retranslateUi(self, CardWidget):
        CardWidget.setWindowTitle(QCoreApplication.translate("CardWidget", u"Form", None))
        self.cardValue.setText(QCoreApplication.translate("CardWidget", u"7", None))
    # retranslateUi

