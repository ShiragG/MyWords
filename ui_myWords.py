# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_myWords.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_MyWords(object):
    def setupUi(self, MyWords):
        if not MyWords.objectName():
            MyWords.setObjectName(u"MyWords")
        MyWords.resize(358, 543)
        self.centralwidget = QWidget(MyWords)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelEng = QLabel(self.centralwidget)
        self.labelEng.setObjectName(u"labelEng")
        self.labelEng.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_2.addWidget(self.labelEng)

        self.wordEng = QLineEdit(self.centralwidget)
        self.wordEng.setObjectName(u"wordEng")
        self.wordEng.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.wordEng)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelRu = QLabel(self.centralwidget)
        self.labelRu.setObjectName(u"labelRu")
        self.labelRu.setMinimumSize(QSize(130, 0))

        self.horizontalLayout.addWidget(self.labelRu)

        self.wordRu = QLineEdit(self.centralwidget)
        self.wordRu.setObjectName(u"wordRu")
        self.wordRu.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.wordRu)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.addBtn = QPushButton(self.centralwidget)
        self.addBtn.setObjectName(u"addBtn")

        self.verticalLayout_3.addWidget(self.addBtn)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelTable = QLabel(self.centralwidget)
        self.labelTable.setObjectName(u"labelTable")
        self.labelTable.setMinimumSize(QSize(130, 0))

        self.horizontalLayout_4.addWidget(self.labelTable)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.removeWordBtn = QPushButton(self.centralwidget)
        self.removeWordBtn.setObjectName(u"removeWordBtn")

        self.verticalLayout.addWidget(self.removeWordBtn)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.randomBtn = QPushButton(self.centralwidget)
        self.randomBtn.setObjectName(u"randomBtn")
        self.randomBtn.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.randomBtn)

        self.randomWord = QLineEdit(self.centralwidget)
        self.randomWord.setObjectName(u"randomWord")
        self.randomWord.setEnabled(False)
        self.randomWord.setMinimumSize(QSize(200, 0))
        self.randomWord.setReadOnly(False)

        self.horizontalLayout_5.addWidget(self.randomWord)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBtn = QPushButton(self.centralwidget)
        self.checkBtn.setObjectName(u"checkBtn")
        self.checkBtn.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.checkBtn)

        self.answerWord = QLineEdit(self.centralwidget)
        self.answerWord.setObjectName(u"answerWord")
        self.answerWord.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.answerWord)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.allWordRBtn = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MyWords)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.allWordRBtn)
        self.allWordRBtn.setObjectName(u"allWordRBtn")
        self.allWordRBtn.setChecked(True)

        self.verticalLayout_4.addWidget(self.allWordRBtn)

        self.onlyEngRBtn = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.onlyEngRBtn)
        self.onlyEngRBtn.setObjectName(u"onlyEngRBtn")

        self.verticalLayout_4.addWidget(self.onlyEngRBtn)

        self.onlyRuRBnt = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.onlyRuRBnt)
        self.onlyRuRBnt.setObjectName(u"onlyRuRBnt")

        self.verticalLayout_4.addWidget(self.onlyRuRBnt)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        MyWords.setCentralWidget(self.centralwidget)

        self.retranslateUi(MyWords)

        QMetaObject.connectSlotsByName(MyWords)
    # setupUi

    def retranslateUi(self, MyWords):
        MyWords.setWindowTitle(QCoreApplication.translate("MyWords", u"My Words", None))
        self.labelEng.setText(QCoreApplication.translate("MyWords", u"\u0421\u043b\u043e\u0432\u043e \u043d\u0430 \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u043e\u043c:", None))
        self.labelRu.setText(QCoreApplication.translate("MyWords", u"\u0421\u043b\u043e\u0432\u043e \u043d\u0430 \u0440\u0443\u0441\u0441\u043a\u043e\u043c:", None))
        self.addBtn.setText(QCoreApplication.translate("MyWords", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.labelTable.setText(QCoreApplication.translate("MyWords", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043b\u043e\u0432:", None))
        self.removeWordBtn.setText(QCoreApplication.translate("MyWords", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0441\u043b\u043e\u0432\u043e", None))
        self.randomBtn.setText(QCoreApplication.translate("MyWords", u"\u0420\u0430\u043d\u0434\u043e\u043c\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.checkBtn.setText(QCoreApplication.translate("MyWords", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.allWordRBtn.setText(QCoreApplication.translate("MyWords", u"\u0412\u0441\u0435 \u0441\u043b\u043e\u0432\u0430", None))
        self.onlyEngRBtn.setText(QCoreApplication.translate("MyWords", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0435", None))
        self.onlyRuRBnt.setText(QCoreApplication.translate("MyWords", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0420\u0443\u0441\u0441\u043a\u0438\u0435", None))
    # retranslateUi

