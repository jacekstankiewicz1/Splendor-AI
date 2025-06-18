# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'token_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_tokenWidget(object):
    def setupUi(self, tokenWidget):
        if not tokenWidget.objectName():
            tokenWidget.setObjectName(u"tokenWidget")
        tokenWidget.resize(195, 232)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tokenWidget.sizePolicy().hasHeightForWidth())
        tokenWidget.setSizePolicy(sizePolicy)
        self.tokenCircle = QWidget(tokenWidget)
        self.tokenCircle.setObjectName(u"tokenCircle")
        self.tokenCircle.setEnabled(True)
        self.tokenCircle.setGeometry(QRect(0, 0, 50, 50))
        sizePolicy.setHeightForWidth(self.tokenCircle.sizePolicy().hasHeightForWidth())
        self.tokenCircle.setSizePolicy(sizePolicy)
        self.tokenCircle.setMinimumSize(QSize(50, 50))
        self.tokenCircle.setStyleSheet(u"background-color: rgb(56, 116, 255);\n"
"border-radius: 25px;")
        self.tokenNumber = QLabel(self.tokenCircle)
        self.tokenNumber.setObjectName(u"tokenNumber")
        self.tokenNumber.setGeometry(QRect(0, 17, 47, 14))

        self.retranslateUi(tokenWidget)

        QMetaObject.connectSlotsByName(tokenWidget)
    # setupUi

    def retranslateUi(self, tokenWidget):
        tokenWidget.setWindowTitle(QCoreApplication.translate("tokenWidget", u"Form", None))
        self.tokenNumber.setText(QCoreApplication.translate("tokenWidget", u"5", None))
    # retranslateUi

