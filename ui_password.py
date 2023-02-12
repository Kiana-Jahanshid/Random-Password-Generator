# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordGvhrBr.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 307)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(171, 238, 246);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rb_standard = QRadioButton(self.centralwidget)
        self.rb_standard.setObjectName(u"rb_standard")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rb_standard.sizePolicy().hasHeightForWidth())
        self.rb_standard.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(10)
        self.rb_standard.setFont(font)
        self.rb_standard.setStyleSheet(u"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.rb_standard, 4, 0, 1, 1)

        self.box = QPlainTextEdit(self.centralwidget)
        self.box.setObjectName(u"box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.box.sizePolicy().hasHeightForWidth())
        self.box.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.box.setFont(font1)
        self.box.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(240, 253, 255);")

        self.gridLayout.addWidget(self.box, 5, 1, 2, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setStyleSheet(u"border-radius: 10px;")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.rb_super = QRadioButton(self.centralwidget)
        self.rb_super.setObjectName(u"rb_super")
        sizePolicy1.setHeightForWidth(self.rb_super.sizePolicy().hasHeightForWidth())
        self.rb_super.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(13)
        self.rb_super.setFont(font2)
        self.rb_super.setStyleSheet(u"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.rb_super, 6, 0, 1, 1)

        self.generate_btn = QPushButton(self.centralwidget)
        self.generate_btn.setObjectName(u"generate_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.generate_btn.sizePolicy().hasHeightForWidth())
        self.generate_btn.setSizePolicy(sizePolicy4)
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.generate_btn.setFont(font3)
        self.generate_btn.setStyleSheet(u"border-radius: 39px ;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 127);")

        self.gridLayout.addWidget(self.generate_btn, 3, 1, 1, 1)

        self.rb_extra = QRadioButton(self.centralwidget)
        self.rb_extra.setObjectName(u"rb_extra")
        sizePolicy1.setHeightForWidth(self.rb_extra.sizePolicy().hasHeightForWidth())
        self.rb_extra.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setPointSize(11)
        self.rb_extra.setFont(font4)
        self.rb_extra.setStyleSheet(u"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.rb_extra, 5, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        font5 = QFont()
        font5.setFamily(u"Berlin Sans FB")
        font5.setPointSize(16)
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.passwordgenerator = QMenuBar(MainWindow)
        self.passwordgenerator.setObjectName(u"passwordgenerator")
        self.passwordgenerator.setGeometry(QRect(0, 0, 552, 26))
        MainWindow.setMenuBar(self.passwordgenerator)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rb_standard.setText(QCoreApplication.translate("MainWindow", u"STANDARD ", None))
        self.box.setPlainText("")
        self.pushButton_3.setText("")
        self.rb_super.setText(QCoreApplication.translate("MainWindow", u"SUPER STRONG", None))
        self.generate_btn.setText(QCoreApplication.translate("MainWindow", u"\u200c\u200c\n"
"GENERATE\n"
"\u200c", None))
        self.rb_extra.setText(QCoreApplication.translate("MainWindow", u"EXTRA STRONG", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"RANDOM PASSWORD GENERATOR", None))
    # retranslateUi

