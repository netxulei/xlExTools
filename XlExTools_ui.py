# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'XlExTools.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import XlExTools_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1266, 835)
        icon = QIcon()
        icon.addFile(u":/icons/Excel\u7ba1\u7406.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.labelSrcDir = QLabel(self.centralwidget)
        self.labelSrcDir.setObjectName(u"labelSrcDir")

        self.horizontalLayout_1.addWidget(self.labelSrcDir)

        self.lineEditSrcDir = QLineEdit(self.centralwidget)
        self.lineEditSrcDir.setObjectName(u"lineEditSrcDir")
        self.lineEditSrcDir.setReadOnly(True)

        self.horizontalLayout_1.addWidget(self.lineEditSrcDir)

        self.pushButtonSrcDirHist = QPushButton(self.centralwidget)
        self.pushButtonSrcDirHist.setObjectName(u"pushButtonSrcDirHist")
        icon1 = QIcon()
        icon1.addFile(u":/icons/\u5386\u53f2\u8bb0\u5f55.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSrcDirHist.setIcon(icon1)

        self.horizontalLayout_1.addWidget(self.pushButtonSrcDirHist)

        self.pushButtonSrcDir = QPushButton(self.centralwidget)
        self.pushButtonSrcDir.setObjectName(u"pushButtonSrcDir")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSrcDir.setIcon(icon2)

        self.horizontalLayout_1.addWidget(self.pushButtonSrcDir)

        self.horizontalLayout_1.setStretch(0, 1)
        self.horizontalLayout_1.setStretch(1, 20)

        self.verticalLayout_4.addLayout(self.horizontalLayout_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelDstFile = QLabel(self.centralwidget)
        self.labelDstFile.setObjectName(u"labelDstFile")

        self.horizontalLayout.addWidget(self.labelDstFile)

        self.lineEditDstFile = QLineEdit(self.centralwidget)
        self.lineEditDstFile.setObjectName(u"lineEditDstFile")
        self.lineEditDstFile.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lineEditDstFile)

        self.pushButtonDstFileHis = QPushButton(self.centralwidget)
        self.pushButtonDstFileHis.setObjectName(u"pushButtonDstFileHis")
        self.pushButtonDstFileHis.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonDstFileHis)

        self.checkBoxDstDir = QCheckBox(self.centralwidget)
        self.checkBoxDstDir.setObjectName(u"checkBoxDstDir")
        self.checkBoxDstDir.setCheckable(True)
        self.checkBoxDstDir.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxDstDir)

        self.lineEditDstDir = QLineEdit(self.centralwidget)
        self.lineEditDstDir.setObjectName(u"lineEditDstDir")
        self.lineEditDstDir.setEnabled(False)
        self.lineEditDstDir.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditDstDir)

        self.pushButtonDstDirHis = QPushButton(self.centralwidget)
        self.pushButtonDstDirHis.setObjectName(u"pushButtonDstDirHis")
        self.pushButtonDstDirHis.setEnabled(False)
        self.pushButtonDstDirHis.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButtonDstDirHis)

        self.pushButtonDstDir = QPushButton(self.centralwidget)
        self.pushButtonDstDir.setObjectName(u"pushButtonDstDir")
        self.pushButtonDstDir.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/xlsx.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonDstDir.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButtonDstDir)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonSelAll = QPushButton(self.groupBox_2)
        self.pushButtonSelAll.setObjectName(u"pushButtonSelAll")
        icon4 = QIcon()
        icon4.addFile(u":/icons/\u5168\u9009.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSelAll.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.pushButtonSelAll)

        self.pushButtonSelNo = QPushButton(self.groupBox_2)
        self.pushButtonSelNo.setObjectName(u"pushButtonSelNo")
        icon5 = QIcon()
        icon5.addFile(u":/icons/\u5168\u4e0d\u9009.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSelNo.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.pushButtonSelNo)

        self.pushButtonFresh = QPushButton(self.groupBox_2)
        self.pushButtonFresh.setObjectName(u"pushButtonFresh")
        icon6 = QIcon()
        icon6.addFile(u":/icons/\u5237\u65b0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonFresh.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.pushButtonFresh)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.checkBoxXls = QCheckBox(self.groupBox_2)
        self.checkBoxXls.setObjectName(u"checkBoxXls")
        icon7 = QIcon()
        icon7.addFile(u":/icons/xls.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxXls.setIcon(icon7)
        self.checkBoxXls.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBoxXls)

        self.checkBoxXlsx = QCheckBox(self.groupBox_2)
        self.checkBoxXlsx.setObjectName(u"checkBoxXlsx")
        icon8 = QIcon()
        icon8.addFile(u":/icons/XLSX.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxXlsx.setIcon(icon8)
        self.checkBoxXlsx.setChecked(True)

        self.horizontalLayout_5.addWidget(self.checkBoxXlsx)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.tableWidgetFileList = QTableWidget(self.groupBox_2)
        if (self.tableWidgetFileList.columnCount() < 4):
            self.tableWidgetFileList.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetFileList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetFileList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetFileList.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetFileList.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidgetFileList.setObjectName(u"tableWidgetFileList")
        self.tableWidgetFileList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidgetFileList.setAlternatingRowColors(True)
        self.tableWidgetFileList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidgetFileList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidgetFileList.setIconSize(QSize(32, 32))
        self.tableWidgetFileList.setShowGrid(False)
        self.tableWidgetFileList.setSortingEnabled(True)
        self.tableWidgetFileList.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetFileList.verticalHeader().setVisible(True)
        self.tableWidgetFileList.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.tableWidgetFileList)

        self.splitter.addWidget(self.groupBox_2)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.comboBoxRule = QComboBox(self.groupBox_3)
        self.comboBoxRule.addItem("")
        self.comboBoxRule.addItem("")
        self.comboBoxRule.addItem("")
        self.comboBoxRule.addItem("")
        self.comboBoxRule.addItem("")
        self.comboBoxRule.setObjectName(u"comboBoxRule")
        self.comboBoxRule.setEditable(False)

        self.verticalLayout_2.addWidget(self.comboBoxRule)

        self.splitterRuleRule = QSplitter(self.groupBox_3)
        self.splitterRuleRule.setObjectName(u"splitterRuleRule")
        self.splitterRuleRule.setOrientation(Qt.Vertical)
        self.splitterRulePic = QSplitter(self.splitterRuleRule)
        self.splitterRulePic.setObjectName(u"splitterRulePic")
        self.splitterRulePic.setAutoFillBackground(True)
        self.splitterRulePic.setOrientation(Qt.Vertical)
        self.textEditRuleMemo = QTextEdit(self.splitterRulePic)
        self.textEditRuleMemo.setObjectName(u"textEditRuleMemo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEditRuleMemo.sizePolicy().hasHeightForWidth())
        self.textEditRuleMemo.setSizePolicy(sizePolicy1)
        self.textEditRuleMemo.setReadOnly(True)
        self.splitterRulePic.addWidget(self.textEditRuleMemo)
        self.labelRulePic = QLabel(self.splitterRulePic)
        self.labelRulePic.setObjectName(u"labelRulePic")
        self.labelRulePic.setPixmap(QPixmap(u":/Rules/ps/FNN.png"))
        self.labelRulePic.setScaledContents(True)
        self.labelRulePic.setAlignment(Qt.AlignCenter)
        self.labelRulePic.setWordWrap(True)
        self.labelRulePic.setMargin(0)
        self.splitterRulePic.addWidget(self.labelRulePic)
        self.splitterRuleRule.addWidget(self.splitterRulePic)
        self.layoutWidget = QWidget(self.splitterRuleRule)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonRuleAdd = QPushButton(self.layoutWidget)
        self.pushButtonRuleAdd.setObjectName(u"pushButtonRuleAdd")
        icon9 = QIcon()
        icon9.addFile(u":/icons/\u589e\u52a0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRuleAdd.setIcon(icon9)

        self.horizontalLayout_2.addWidget(self.pushButtonRuleAdd)

        self.pushButtonRuleDel = QPushButton(self.layoutWidget)
        self.pushButtonRuleDel.setObjectName(u"pushButtonRuleDel")
        icon10 = QIcon()
        icon10.addFile(u":/icons/\u51cf\u9664.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRuleDel.setIcon(icon10)

        self.horizontalLayout_2.addWidget(self.pushButtonRuleDel)

        self.pushButtonRuleLoad = QPushButton(self.layoutWidget)
        self.pushButtonRuleLoad.setObjectName(u"pushButtonRuleLoad")
        icon11 = QIcon()
        icon11.addFile(u":/icons/\u5bfc\u5165.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRuleLoad.setIcon(icon11)

        self.horizontalLayout_2.addWidget(self.pushButtonRuleLoad)

        self.pushButtonRuleSave = QPushButton(self.layoutWidget)
        self.pushButtonRuleSave.setObjectName(u"pushButtonRuleSave")
        icon12 = QIcon()
        icon12.addFile(u":/icons/\u5bfc\u51fa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRuleSave.setIcon(icon12)

        self.horizontalLayout_2.addWidget(self.pushButtonRuleSave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tableWidgetRulesUse = QTableWidget(self.layoutWidget)
        if (self.tableWidgetRulesUse.columnCount() < 3):
            self.tableWidgetRulesUse.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetRulesUse.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetRulesUse.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidgetRulesUse.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidgetRulesUse.setObjectName(u"tableWidgetRulesUse")
        self.tableWidgetRulesUse.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidgetRulesUse.setAlternatingRowColors(True)
        self.tableWidgetRulesUse.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.tableWidgetRulesUse)

        self.verticalLayout_3.setStretch(1, 1)
        self.splitterRuleRule.addWidget(self.layoutWidget)

        self.verticalLayout_2.addWidget(self.splitterRuleRule)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEditRow = QLineEdit(self.groupBox_3)
        self.lineEditRow.setObjectName(u"lineEditRow")

        self.horizontalLayout_3.addWidget(self.lineEditRow)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonSum = QPushButton(self.groupBox_3)
        self.pushButtonSum.setObjectName(u"pushButtonSum")
        icon13 = QIcon()
        icon13.addFile(u":/icons/ZoomLarge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSum.setIcon(icon13)

        self.horizontalLayout_3.addWidget(self.pushButtonSum)

        self.pushButtonExit = QPushButton(self.groupBox_3)
        self.pushButtonExit.setObjectName(u"pushButtonExit")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Action_Exit_32x32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonExit.setIcon(icon14)

        self.horizontalLayout_3.addWidget(self.pushButtonExit)

        self.checkBoxTop = QCheckBox(self.groupBox_3)
        self.checkBoxTop.setObjectName(u"checkBoxTop")

        self.horizontalLayout_3.addWidget(self.checkBoxTop)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.splitter.addWidget(self.groupBox_3)

        self.verticalLayout_4.addWidget(self.splitter)

        self.verticalLayout_4.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1266, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonExit.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelSrcDir.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u6587\u4ef6\u6240\u5728\u76ee\u5f55\uff1a", None))
        self.lineEditSrcDir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u5305\u542b\u88ab\u6c47\u603bExcel\u6587\u4ef6\u7684\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSrcDirHist.setToolTip(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u8bb0\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSrcDirHist.setText("")
        self.pushButtonSrcDir.setText(QCoreApplication.translate("MainWindow", u" \u9009\u62e9\u76ee\u5f55\u540d   ", None))
        self.labelDstFile.setText(QCoreApplication.translate("MainWindow", u"\u6c47\u603b\u7ed3\u679c\u6587\u4ef6\u540d\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEditDstFile.setToolTip(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4xlsx\u6587\u4ef6\uff08\u53ef\u5f55\u5165xls\u6216xlsx\u6269\u5c55\u540d\uff09", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditDstFile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5f55\u5165\u6c47\u603b\u540e\u751f\u6210\u7684Excel\u6587\u4ef6\u540d", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDstFileHis.setToolTip(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u8bb0\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDstFileHis.setText("")
        self.checkBoxDstDir.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u4fdd\u5b58\u5728\u5f53\u524d\u76ee\u5f55", None))
        self.lineEditDstDir.setText("")
        self.lineEditDstDir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u7ed3\u679c\u4fdd\u5b58\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDstDirHis.setToolTip(QCoreApplication.translate("MainWindow", u"\u5386\u53f2\u8bb0\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDstDirHis.setText("")
        self.pushButtonDstDir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u7ed3\u679c\u4fdd\u5b58\u76ee\u5f55", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u53c2\u4e0e\u6c47\u603b\u7684\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSelAll.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u4e2d\u6587\u4ef6\u52a0\u5165\u6c47\u603b\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSelAll.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonSelNo.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u4e2d\u6587\u4ef6\u53d6\u6d88\u6c47\u603b\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSelNo.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonFresh.setToolTip(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u6e90\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonFresh.setText("")
#if QT_CONFIG(tooltip)
        self.checkBoxXls.setToolTip(QCoreApplication.translate("MainWindow", u"\u663e\u793aXLS\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxXls.setText(QCoreApplication.translate("MainWindow", u"XLS", None))
#if QT_CONFIG(tooltip)
        self.checkBoxXlsx.setToolTip(QCoreApplication.translate("MainWindow", u"\u663e\u793aXLSX\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxXlsx.setText(QCoreApplication.translate("MainWindow", u"XLSX", None))
        ___qtablewidgetitem = self.tableWidgetFileList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem1 = self.tableWidgetFileList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f", None));
        ___qtablewidgetitem2 = self.tableWidgetFileList.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem3 = self.tableWidgetFileList.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u671f", None));
#if QT_CONFIG(tooltip)
        self.tableWidgetFileList.setToolTip(QCoreApplication.translate("MainWindow", u"\u53cc\u51fb\u6253\u5f00\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u63d0\u53d6\u6c47\u603b\u89c4\u5219", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u53d6\u89c4\u5219", None))
        self.comboBoxRule.setItemText(0, QCoreApplication.translate("MainWindow", u"F00 \u6587\u672c\u5185\u5bb9\u2192\u76ee\u6807\u8868\u6307\u5b9a\u5355\u5143\u683c", None))
        self.comboBoxRule.setItemText(1, QCoreApplication.translate("MainWindow", u"F11 \u5355\u6587\u4ef6\u6307\u5b9a\u5355\u5143\u683c\u2192\u76ee\u6807\u8868\u6307\u5b9a\u5355\u5143\u683c", None))
        self.comboBoxRule.setItemText(2, QCoreApplication.translate("MainWindow", u"F1N \u5355\u6587\u4ef6\u8fde\u7eed\u5355\u5143\u683c\u2192\u76ee\u6807\u8868\u8fde\u7eed\u5355\u5143\u683c", None))
        self.comboBoxRule.setItemText(3, QCoreApplication.translate("MainWindow", u"FN1 \u591a\u6587\u4ef6\u6307\u5b9a\u5355\u5143\u683c\u2192\u76ee\u6807\u8868\u8fde\u7eed\u5355\u5143\u683c", None))
        self.comboBoxRule.setItemText(4, QCoreApplication.translate("MainWindow", u"FNN \u591a\u6587\u4ef6\u8fde\u7eed\u5355\u5143\u683c\u2192\u76ee\u6807\u8868\u8fde\u7eed\u5355\u5143\u683c", None))

        self.comboBoxRule.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c4\u5219", None))
        self.textEditRuleMemo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u89c4\u5219\u8bf4\u660e", None))
        self.labelRulePic.setText("")
        self.pushButtonRuleAdd.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u89c4\u5219", None))
        self.pushButtonRuleDel.setText(QCoreApplication.translate("MainWindow", u"\u2191\u5220\u9664\u89c4\u5219", None))
        self.pushButtonRuleLoad.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u89c4\u5219", None))
        self.pushButtonRuleSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u89c4\u5219", None))
        ___qtablewidgetitem4 = self.tableWidgetRulesUse.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u89c4\u5219\u4ee3\u53f7", None));
        ___qtablewidgetitem5 = self.tableWidgetRulesUse.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u8868\u6570\u636e", None));
        ___qtablewidgetitem6 = self.tableWidgetRulesUse.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u8868\u6570\u636e", None));
#if QT_CONFIG(tooltip)
        self.tableWidgetRulesUse.setToolTip(QCoreApplication.translate("MainWindow", u"\u53cc\u51fb\u6570\u636e\u4fee\u6539\u5730\u5740", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6c47\u603bExcel\u989d\u5916\u884c\u6570", None))
#if QT_CONFIG(tooltip)
        self.lineEditRow.setToolTip(QCoreApplication.translate("MainWindow", u"\u4e00\u822c\u884c\u6570\u4e3a\u6c47\u603b\u7684\u6587\u4ef6\u6570+1\uff0c\u6b64\u5904\u5f55\u5165\u6587\u4ef6\u6570\u91cf\u4e4b\u5916\u7684\u884c\u6570", None))
#endif // QT_CONFIG(tooltip)
        self.lineEditRow.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButtonSum.setText(QCoreApplication.translate("MainWindow", u"\u6c47\u603b", None))
        self.pushButtonExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.checkBoxTop.setText(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3\u7f6e\u9876", None))
    # retranslateUi

