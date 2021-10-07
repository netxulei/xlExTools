from XLCommon import xlCommon as xl
import configparser
import os
import sys
import time
import re
import unicodedata

import numpy as np
import pandas as pd
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QTranslator, QRegExp
from PySide2.QtGui import QPixmap, QRegExpValidator
from PySide2.QtWidgets import QMessageBox, QFileDialog, QFileIconProvider, QTableWidgetItem

from XlExTools_ui import Ui_MainWindow


class XLExTool(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.splitter.setStretchFactor(0, 4)
        self.splitter.setStretchFactor(1, 1)
        self.splitterRulePic.setStretchFactor(0, 1)
        self.splitterRulePic.setStretchFactor(1, 4)
        self.splitterRuleRule.setStretchFactor(0, 1)
        self.splitterRuleRule.setStretchFactor(1, 10)
        self.setWindowTitle('Excel多文件数据提取汇总工具--2021.10.01--  Lane')
        # self.setWindowIcon(QIcon('chkrptmain.ico'))  #  改为使用资源文件
        # 读取配置和数据文件
        self.configRead()

        if self.win_top == "1":
            self.checkBoxTop.setChecked(True)
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)  # 窗口置顶
        else:
            self.checkBoxTop.setChecked(False)
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
        self.resize(int(self.last_win_width), int(self.last_win_height))
        # self.resize(1280,800)

        # 设置QtableWidget表头
        # self.tableWidgetRpt.horizontalHeader().setFixedHeight(50)  # 高度
        # self.tableWidgetDir.horizontalHeader().setFixedHeight(50)  # 高度
        # 设置选中行的背景色（失去焦点也不变）
        self.tableWidgetFileList.setStyleSheet("selection-background-color:rgb(0,124,255)")
        # tableWidget->setStyleSheet("selection-background-color:rgb(135,206,235)")
        # 恢复上次汇总时的源文件目录
        if os.path.exists(self.src_dir) and not os.path.isfile(self.src_dir):
            self.lineEditSrcDir.setText(self.src_dir)
        else:
            self.lineEditSrcDir.setText('')
        # 恢复上次汇总时的目标文件目录
        if os.path.exists(self.dst_dir) and not os.path.isfile(self.dst_dir):
            self.lineEditDstDir.setText(self.dst_dir)
        else:
            self.lineEditDstDir.setText('')
        # 恢复上次汇总时的目标文件名称
        self.lineEditDstFile.setText(self.dst_file)

        # 恢复上次汇总时确定的文件类型check
        # print(self.src_xls)
        if self.src_xls == "1":
            self.checkBoxXls.setChecked(True)
        else:
            self.checkBoxXls.setChecked(False)

        if self.src_xlsx == "1":
            self.checkBoxXlsx.setChecked(True)
        else:
            self.checkBoxXlsx.setChecked(False)
        # 设置文件扩展名列表
        # self.file_ext_list = ["XLS", "XLSX"]
        # 填充tableWidegetSrcDir
        self.file_ext_sum()  # 同时fillSrcDir

        # 恢复汇总目录是否源文件目录
        if self.dst_loc == "1":
            self.checkBoxDstDir.setChecked(True)
        else:
            self.checkBoxDstDir.setChecked(False)
        self.dstDirEnable()

        # -------------------- 规则初始化---------------------------------
        self.sys_rule_list = [['F00', '文本信息', 'A1',
                               '<b>·规则名称：</b>设定文本信息→汇总文件中指定的单元格<br><b>·源表数据规则：</b>文本信息<br><b>·目标表数据规则：</b>指定单元格地址（A1）'],
                              ['F11', 'B1', 'B1',
                               '<b>·规则名称：<、b>一个源文件指定单元格→汇总文件中指定单元格<br><b>·源表数据规则：</b>指定单元格地址（B1）<br><b>·目标表数据规则：</b>指定单元格地址（B1）'],
                              ['F1N', 'A2:A4', 'C1:E1',
                               '<b>·规则名称：</b>一个源文件“列”连续单元格→汇总文件“行”连续单元格<br><b>·源表数据规则：</b>“列”连续单元格地址范围（A2:A5）<br><b>·目标表数据规则：</b>“行”连续单元格地址范围（C1:F1）'],
                              ['FN1', 'A1', 'A2',
                               '<b>·规则名称：</b>多个源文件指定单元格→汇总文件“行”连续单元格<br><b>·源表数据规则：</b>指定单元格地址（A1）<br><b>·目标表数据规则：</b>“行”连续单元格起始单元格地址（A2）'],
                              ['FNN', 'B2:B4', 'C2:E2',
                               '<b>·规则名称：</b>多个源文件“列”连续单元格→汇总文件“行”连续单元格<br><b>·源表数据规则：</b>“列”连续单元格地址范围（B2:B4）<br><b>·目标表数据规则：</b>起始“行”连续单元格地址范围（C2:E2）']]
        self.comboBoxRule.setCurrentIndex(1)  # 设置选择第一个列表
        self.ruleIndex()  # 显示该规则说明和图示
        # 上次存盘时或执行汇总的规则文件若存在，则调取规则
        if os.path.exists(self.last_rule_name) and os.path.isfile(self.last_rule_name):
            self.ruleDirectLoad(self.last_rule_name)

        # for i in range(len(self.sys_rule_list)):
        #     print(self.sys_rule_list[i])
        # ------------------- 规则初始化结束-------------------
        # 信号
        self.pushButtonSelAll.clicked.connect(self.selAll)
        self.pushButtonSelNo.clicked.connect(self.selNo)
        self.pushButtonFresh.clicked.connect(self.selFresh)
        self.checkBoxXls.clicked.connect(self.file_ext_sum)
        self.checkBoxXlsx.clicked.connect(self.file_ext_sum)
        self.checkBoxDstDir.clicked.connect(self.dstDirEnable)

        self.pushButtonSrcDir.clicked.connect(self.srcDir)
        self.pushButtonDstDir.clicked.connect(self.dstDir)
        self.pushButtonSum.clicked.connect(self.excelSum)

        # 源文件处理.双击打开目录
        self.tableWidgetFileList.doubleClicked.connect(self.openCurDir)

        # ---规则处理-----
        self.comboBoxRule.currentIndexChanged.connect(self.ruleIndex)
        self.pushButtonRuleDel.clicked.connect(self.ruleDel)
        self.pushButtonRuleAdd.clicked.connect(self.ruleAdd)

        self.pushButtonRuleSave.clicked.connect(self.ruleSave)
        self.pushButtonRuleLoad.clicked.connect(self.ruleLoad)
        self.tableWidgetRulesUse.itemChanged.connect(self.cellValid)
        self.tableWidgetRulesUse.itemClicked.connect(self.outSelect)
        # --------------------
        # self.checkBoxTop.clicked.connect(self.win_top)
        # self.checkBoxOnly.clicked.connect(self.rptFilter)
        # self.tableWidgetDir.doubleClicked.connect(self.openCurDir)
        # self.window.pushButton_Excel.clicked.connect(
        #     lambda: self.excelFile('asdsadv'))  # 信号中的槽函数不能加括号，否则一运行程序就执行;要带参数。就在槽函数前加lambda

    # -------------处理规则开始-------------------------------------------------------------------------------------------
    def ruleIndex(self):  # 选取一个规则，显示说明和示意图。规则列表变化时槽函数
        i = self.comboBoxRule.currentIndex()
        self.textEditRuleMemo.setText(self.sys_rule_list[i][3])
        picName = u":/Rules/ps/" + self.sys_rule_list[i][0] + ".png"  # 示意图已加入资源管理器
        # print(picName)
        self.labelRulePic.setPixmap(QPixmap(picName))

    def ruleAdd(self):  # 规则加入用户规则列表
        self.tableWidgetRulesUse.blockSignals(True)  # 关闭tablewidget信号，避免增加行列式触发该信号
        i = self.comboBoxRule.currentIndex()  # 选中的规则索引
        row = self.tableWidgetRulesUse.rowCount()  # 总行数
        self.tableWidgetRulesUse.insertRow(row)  # row下插入一行
        # 单元格加入带有正则表达式的QlineEdit---------目前解决不了问题，用cellchanged信号或itemchanged信号
        #         regx = QRegExp("[0-9]*")  # 正则表达式
        #         ceil = QtWidgets.QLineEdit()  # 新建一个qlineedit来装正则表达式
        #         validator = QRegExpValidator(regx)
        #         ceil.setValidator(validator)
        #         ceil.setPlaceholderText("请输入参数")
        #         self.tableWidgetRulesUse.setCellWidget(row, 1, ceil)  # 利用table widget可以装其他组件的方式来实现
        # --------------------------------
        item1 = QTableWidgetItem(self.sys_rule_list[i][0])  # 规则代号
        item1.setFlags(QtCore.Qt.ItemIsEnabled)
        item2 = QTableWidgetItem(self.sys_rule_list[i][1])  # 源数据
        item3 = QTableWidgetItem(self.sys_rule_list[i][2])  # 目标数据
        # # 放入单元格
        self.tableWidgetRulesUse.setItem(row, 0, item1)
        self.tableWidgetRulesUse.setItem(row, 1, item2)
        self.tableWidgetRulesUse.setItem(row, 2, item3)
        self.tableWidgetRulesUse.blockSignals(False)  # 打开tablewidget信号，恢复单元格修改时触发发该信号

    def ruleDel(self):  # 删除当前行规则
        self.tableWidgetRulesUse.blockSignals(True)  # 关闭tablewidget信号，避免增加行列式触发该信号
        row = self.tableWidgetRulesUse.currentRow()
        if row < 0:
            QMessageBox.information(self, '信息', '请将光标定位规则所在行', QMessageBox.Ok)
            return
        self.tableWidgetRulesUse.removeRow(row)
        # self.comboBoxRule.setCurrentIndex(-1)
        # self.lineEditRuleCode.setText('')
        # self.lineEditSrcData.setText('')
        # self.lineEditDstData.setText('')
        self.tableWidgetRulesUse.blockSignals(False)  # 打开tablewidget信号，恢复单元格修改时触发发该信号

    def ruleSave(self):  # 保存规则
        rule_file = QFileDialog.getSaveFileName(self, "输入或选择规则文件名称", '', '规则文件 (*.csv)')
        if len(rule_file[0]) <= 0:
            return
        row = self.tableWidgetRulesUse.rowCount()
        col = self.tableWidgetRulesUse.columnCount()
        # print(row, col)
        dest_pd = pd.DataFrame(np.empty(shape=(row, col), dtype=str))
        for i in range(row):
            for j in range(col):
                dest_pd.iloc[(i, j)] = self.tableWidgetRulesUse.item(i, j).text()
        dest_pd.to_csv(rule_file[0], index=False)  # save
        self.configWriteRule(rule_file[0])

    def configWriteRule(self, ruleFileName):  # 保存的规则文件名称写入配置文件
        # if self.last_path != self.tmp_last_path or self.key_file != self.tmp_key_file:
        # self.src_dir = self.lineEditSrcDir
        # 读取配置文件
        self.config.read(self.cfg_file, encoding='utf-8')
        # 修改配置文件项
        self.config.set("Rules", "last_rule_name", ruleFileName)
        with open(self.cfg_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    def ruleLoad(self):  # 对话框导入规则
        rule_file = QFileDialog.getOpenFileNames(self, "清选择规则文件名称", '', '规则文件 (*.csv)')
        # print(rule_file[0])
        if len(rule_file[0]) <= 0:
            return
        self.last_rule_name = rule_file[0][0]  # 调用规则的文件名称
        self.ruleDirectLoad(self.last_rule_name)

    def ruleDirectLoad(self, ruleFielName):  # 直接根据文件名导入规则
        self.tableWidgetRulesUse.blockSignals(True)  # 关闭tablewidget信号，避免增加行列式触发该信号
        dest_pd = pd.read_csv(ruleFielName)
        row = dest_pd.shape[0]
        col = dest_pd.shape[1]  # 固定为3列
        self.tableWidgetRulesUse.setRowCount(row)
        # self.tableWidgetRulesUse.setColumnCount(col)
        for i in range(row):
            # print(dest_pd.iloc[i][0], dest_pd.iloc[i][1], dest_pd.iloc[i][2])
            item1 = QTableWidgetItem(dest_pd.iloc[i][0])  # 规则代号
            item1.setFlags(QtCore.Qt.ItemIsEnabled)
            item2 = QTableWidgetItem(dest_pd.iloc[i][1])  # 源数据
            item3 = QTableWidgetItem(dest_pd.iloc[i][2])  # 目标数据
            # # 放入单元格
            self.tableWidgetRulesUse.setItem(i, 0, item1)
            self.tableWidgetRulesUse.setItem(i, 1, item2)
            self.tableWidgetRulesUse.setItem(i, 2, item3)
            # print(row)
        self.tableWidgetRulesUse.blockSignals(False)  # 打开tablewidget信号，恢复单元格修改时触发发该信号

    def outSelect(self, Item):  # 记录修改前的单元格值，不符合校验时，恢复原值
        # if Item == None:
        #     return
        self.tmp_itemText = Item.text()
        # print(self.tmp_itemText)

    def cellValid(self, curItem):  # 校验单元格是否符合规范录入
        self.tableWidgetRulesUse.blockSignals(True)  # 关闭tablewidget信号，避免增加行列式触发该信号
        cur_index = self.tableWidgetRulesUse.currentIndex()
        row = cur_index.row()
        col = cur_index.column()
        cur_cell = curItem.text()
        cur_rule = self.tableWidgetRulesUse.item(row, 0).text()  # 读取当前单元格同行的规则名称列
        if cur_rule == 'F00':  # F00规则录入校验

            if col == 1:
                pass
            if col == 2:
                cur_cell = xl.stringQ2B(cur_cell).upper()  # 全角变半角,变大写
                if (re.match(r"(^(\$?)[a-zA-Z]+\2[0-9]*$)|(^\$?[0-9]+$)", cur_cell)):  # 单地址
                    self.tableWidgetRulesUse.currentItem().setText(cur_cell)  # 写回原单元格
                else:
                    QMessageBox.information(self, '信息', 'F00规则目标表数据应为单元格单个地址', QMessageBox.Ok)
                    self.tableWidgetRulesUse.currentItem().setText(self.tmp_itemText)
        if cur_rule == 'F11' or cur_rule == 'FN1':  # F11规则录入校验
            cur_cell = xl.stringQ2B(cur_cell).upper()  # 全角变半角,变大写
            if (re.match(r"(^(\$?)[a-zA-Z]+\2[0-9]*$)|(^\$?[0-9]+$)", cur_cell)):  # 单地址
                self.tableWidgetRulesUse.currentItem().setText(cur_cell)  # 写回原单元格
            else:
                QMessageBox.information(self, '信息', 'F11、FN1规则的源表和目标表数据都应为单元格单个地址', QMessageBox.Ok)
                self.tableWidgetRulesUse.currentItem().setText(self.tmp_itemText)
        if cur_rule == 'F1N' or cur_rule == 'FNN':  # F11规则录入校验
            cur_cell = xl.stringQ2B(cur_cell).upper()  # 全角变半角,变大写
            if (re.match(r"((^(\$?)[a-zA-Z]+\3[0-9]*)|(^(\$?)[0-9]+)):(((\3)[a-zA-Z]+\3[0-9]*$)|(\5[0-9]+$))",
                         cur_cell)):  # 范围地址
                self.tableWidgetRulesUse.currentItem().setText(cur_cell)  # 写回原单元格
            else:
                QMessageBox.information(self, '信息', 'F1N、FNN规则的源表和目标表数据都应为单元格范围地址', QMessageBox.Ok)
                self.tableWidgetRulesUse.currentItem().setText(self.tmp_itemText)

        # print(self.tableWidgetRulesUse.currentItem().text())
        self.tableWidgetRulesUse.blockSignals(False)  # 关闭tablewidget信号，避免增加行列式触发该信号

        # print()

        # ---------------------处理规则结束----------------------------------------------------------------------------------

        # -------------配置文件处理开始-------------------

    def configRead(self):  # 读配置文件
        self.cfg_file = 'configEx.ini'
        self.config = configparser.ConfigParser()
        # 读取文件
        self.config.read(self.cfg_file, encoding='utf-8')
        # 取得last_path
        self.src_dir = self.config.get("FilePath", "src_dir")  # 源文件目录
        self.src_xls = self.config.get("FilePath", "src_xls")  # 源文件类型
        self.src_xlsx = self.config.get("FilePath", "src_xlsx")  # 源文件类型
        self.dst_file = self.config.get("FilePath", "dst_file")  # 汇总文件名
        self.dst_loc = self.config.get("FilePath", "dst_loc")  # 结果是否存在当前目录
        self.dst_dir = self.config.get("FilePath", "dst_dir")  # 结果目录名

        self.last_rule_name = self.config.get("Rules", "last_rule_name")

        self.last_win_width = self.config.get("Win", "width")
        self.last_win_height = self.config.get("Win", "height")
        self.win_top = self.config.get("Win", "win_top")

    def configWrite(self):  # 写配置文件
        # if self.last_path != self.tmp_last_path or self.key_file != self.tmp_key_file:
        # self.src_dir = self.lineEditSrcDir

        # 读取配置文件
        self.config.read(self.cfg_file, encoding='utf-8')
        # 修改配置文件项
        self.config.set('FilePath', 'src_dir', self.src_dir)
        self.config.set('FilePath', 'src_xls', self.src_xls)
        self.config.set('FilePath', 'src_xlsx', self.src_xlsx)
        self.config.set('FilePath', 'dst_file', self.dst_file)
        self.config.set('FilePath', 'dst_loc', self.dst_loc)
        self.config.set('FilePath', 'dst_dir', self.dst_dir)
        self.config.set('Win', 'width', str(self.width()))
        self.config.set('Win', 'height', str(self.height()))
        self.config.set("Win", "win_top", self.win_top)
        with open(self.cfg_file, 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)

    # -------------------配置文件结束------------------

    # 汇总文件保存目录方式
    def dstDirEnable(self):
        self.lineEditDstDir.setEnabled(not self.checkBoxDstDir.isChecked())
        self.pushButtonDstDirHis.setEnabled(not self.checkBoxDstDir.isChecked())
        self.pushButtonDstDir.setEnabled(not self.checkBoxDstDir.isChecked())

        # def excelFile(self):

    #     # 多重过滤用2个分号分割吗，如"Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)"
    #     # 返回元组，文件名和文件类型
    #     # ('D:/MyPycharm/ChkRptSide6/淮南市反洗钱人员联系表69家 0703版.xlsx', 'Excel文件 (*.xls *.xlsx)')
    #     key_file_new = QFileDialog.getOpenFileName(self,
    #                                                "选取Excel文件",
    #                                                '',
    #                                                "Excel文件 (*.xls *.xlsx)"
    #                                                )
    #     # print(key_file_new)
    #     if len(key_file_new[0]) > 0:
    #         self.lineEditExcel.setText(key_file_new[0])
    #         self.tmp_key_file = self.lineEditExcel.text()
    # --------------选择源文件目录并填充源文件目录--------------------------------
    def srcDir(self):
        dir_name = QFileDialog.getExistingDirectory(self, "选择被汇总文件所在的目录",
                                                    self.src_dir,
                                                    QFileDialog.ShowDirsOnly
                                                    | QFileDialog.DontResolveSymlinks
                                                    )
        # print(dir_name,self.last_path)
        # print(dir_name)
        # print(self.src_dir)
        if len(dir_name) > 0 and (dir_name != self.src_dir):
            # print(dir_name)
            # 改变选择目录输入框
            self.lineEditSrcDir.setText(dir_name)
            self.src_dir = dir_name
            self.fillSrcDir()
            # 清空检测结果
            # self.tableWidgetRpt.setRowCount(0)  # 设置表格的行数,否则一直新增
            # self.tableWidgetRpt.clearContents()  # 清除内容，不清除表头（clear())

    # 选择目标文件目录
    def dstDir(self):
        dir_name = QFileDialog.getExistingDirectory(self, "请选择汇总结果文件保存目录",
                                                    self.dst_dir,
                                                    QFileDialog.ShowDirsOnly
                                                    | QFileDialog.DontResolveSymlinks
                                                    )
        # print(dir_name,self.last_path)
        if len(dir_name) > 0 and (dir_name != self.dst_dir):
            # print(dir_name)
            # 改变选择目录输入框
            self.lineEditDstDir.setText(dir_name)
            self.dst_dir = dir_name
            # self.fillDir()
            # 清空检测结果
            # self.tableWidgetRpt.setRowCount(0)  # 设置表格的行数,否则一直新增
            # self.tableWidgetRpt.clearContents()  # 清除内容，不清除表头（clear())

    #  填充源文件目录
    def fillSrcDir(self):  # 文件名和相关信息填入表格
        self.tableWidgetFileList.setRowCount(0)  # 设置表格的行数,否则一直新增
        self.tableWidgetFileList.clearContents()  # 清除内容，不清除表头（clear())
        # print(self.lineEditSrcDir.text())
        # print(self.src_dir)
        # 获得文件列表及属性
        # file_lists = self.getFileLists(self.lineEditSrcDir.text(), 0, self.file_ext_list)
        file_lists = self.getFileLists(self.src_dir, 0, self.file_ext_list)
        # 图标提供者，主要靠他获取图标
        provider = QFileIconProvider()

        # 循环添加到tableWidget
        # print(file_lists)
        for i in range(len(file_lists)):
            # 获取文件名后缀
            file_ext = os.path.splitext(file_lists[i][0])[-1][1:]
            # print(file_ext.upper())

            row = self.tableWidgetFileList.rowCount()  # 总行数
            self.tableWidgetFileList.insertRow(row)  # 原表下添加一行
            file_icon = provider.icon(file_lists[i][0])
            dir_icon = provider.icon(QFileIconProvider.Folder)
            # -------------------处理文件名------------------------------------------------------------
            item = QTableWidgetItem(file_lists[i][0])  # 文件名
            item.setCheckState(QtCore.Qt.Unchecked)  # 全部未checked
            if file_lists[i][1]:  # 根据返回列表中是否目录标识设置（i，0）单元格的图标
                item.setIcon(file_icon)  # 设置文件图标
            else:
                item.setIcon(dir_icon)  # 设置目录图标
            # 设置单元格是否可选择、可编辑、可拖动、可drop、用户可check、有效、三态（tristate）等
            item.setFlags(
                QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable)

            self.tableWidgetFileList.setItem(i, 0, item)  # 文件名

            # ------------------文件大小-----------------------------------------------------------------
            item = QTableWidgetItem(file_lists[i][2])  # 文件大小
            # ------解决整数排序(整数无法添加至tablewidget）
            if type(file_lists[i][2]) == int:
                item.setData(QtCore.Qt.DisplayRole, file_lists[i][2])
            else:
                item.setText(file_lists[i][2])
            self.tableWidgetFileList.setItem(i, 1, item)  # 文件大小
            # ------------------文件类型---------------------------------------------
            item = QTableWidgetItem(os.path.splitext(file_lists[i][0])[-1][1:].upper())
            self.tableWidgetFileList.setItem(i, 2, item)

            # # -----------文件创建日期------------------------------------------------------------
            # item = QTableWidgetItem(file_lists[i][3])  # 文件创建日期
            # self.tableWidgetFileList.setItem(i, 3, item)
            # -------文件修改日期---------------------------------------------------------------------------------
            item = QTableWidgetItem(file_lists[i][4])  # 文件修改日期
            self.tableWidgetFileList.setItem(i, 3, item)
            # -------------------------------------------------------------------------------------------
        self.tableWidgetFileList.resizeColumnsToContents()  # 内容适应表格

    # 获取指定路径文件列表。
    # 获取给定目录下文件列表，返回[[文件名],[是否文件],[大小],[创建时间],[修改时间],[访问时间]]
    # dirName:目录名；file_dir_flag：0 所有 1 文件 2 目录；file_ext_list文件扩展名列表
    def getFileLists(self, dirName, file_dir_flag, file_ext_list):
        file_lists = []
        for entries in os.scandir(dirName):
            # print('文件绝对路径：', entries.path)
            # print('是否文件夹:', entries.is_dir())
            # print('是否文件：', entries.is_file())
            # print('文件属性：', entries.stat())
            # print('文件属性：', entries.stat())
            # print('文件名:', entries.name)
            # print('文件大小：', entries.stat(follow_symlinks=False).st_size)
            # print('创建时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entries.stat(follow_symlinks=False).st_ctime)))
            # print('修改时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entries.stat(follow_symlinks=False).st_mtime)))
            # print('访问时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entries.stat(follow_symlinks=False).st_atime)))

            if file_dir_flag == 0 or file_dir_flag == 1 and entries.is_file() or file_dir_flag == 2 and entries.is_dir():
                if len(file_ext_list) != 0 and os.path.splitext(entries.name)[-1][1:].upper() not in file_ext_list:
                    continue
                file_list = []
                file_list.append(entries.name)
                file_list.append(entries.is_file())
                file_list.append(entries.stat(follow_symlinks=False).st_size)
                file_list.append(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entries.stat(follow_symlinks=False).st_ctime)))
                file_list.append(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entries.stat(follow_symlinks=False).st_mtime)))
                file_list.append(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entries.stat(follow_symlinks=False).st_atime)))
                file_lists.append(file_list)
        return (file_lists)

    # 根据扩展名填充src_dir列表，xlsCheck和xlsxCheck的click的槽函数
    def file_ext_sum(self):
        if self.checkBoxXls.isChecked() and self.checkBoxXlsx.isChecked():
            self.file_ext_list = ["XLS", "XLSX"]
            self.src_xls = 1
            self.src_xlsx = 1
        if not (self.checkBoxXls.isChecked() and self.checkBoxXlsx.isChecked()):
            self.file_ext_list = []
            self.src_xls = 0
            self.src_xlsx = 0
        if self.checkBoxXls.isChecked() and not self.checkBoxXlsx.isChecked():
            self.file_ext_list = ["XLS"]
            self.src_xls = 1
            self.src_xlsx = 0
        if not self.checkBoxXls.isChecked() and self.checkBoxXlsx.isChecked():
            self.file_ext_list = ["XLSX"]
            self.src_xls = 0
            self.src_xlsx = 1

        if os.path.exists(self.src_dir) and not os.path.isfile(self.src_dir):
            self.fillSrcDir()

    # ------------------------------------------------------------------------------
    # 选中行全部设为checked
    def selAll(self):
        for i in self.getSelRow():
            self.tableWidgetFileList.item(i, 0).setCheckState(QtCore.Qt.Checked)

    # 选中行全部设为unchecked
    def selNo(self):
        for i in self.getSelRow():
            self.tableWidgetFileList.item(i, 0).setCheckState(QtCore.Qt.Unchecked)

    # 刷新源文件列表
    def selFresh(self):
        self.file_ext_sum()

    # 获取table中选中行的行号，返回列表
    def getSelRow(self):
        selected_row = list()
        item = self.tableWidgetFileList.selectedItems()
        for i in item:
            if self.tableWidgetFileList.indexFromItem(i).row() not in selected_row:
                selected_row.append(self.tableWidgetFileList.indexFromItem(i).row())
        return sorted(selected_row)

    # -------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------
    # 获取文件列表checked状态的文件列表
    def getFileList(self):
        file_list = list()
        for i in range(self.tableWidgetFileList.rowCount()):
            item = self.tableWidgetFileList.item(i, 0)
            if item.checkState() == QtCore.Qt.Checked:
                file_list.append(item.text())
        return file_list

    # 双击打开文件
    def openCurDir(self, index):
        table_column = index.column()
        table_row = index.row()
        current_item = self.tableWidgetFileList.item(table_row, 0).text()  # 当前单元格文字内容
        print(current_item)
        # os.system("start explorer %s" % self.tmp_last_path)
        os.startfile(self.src_dir + '/' + current_item)

    # 执行汇总
    def excelSum(self):
        # 判断文件或目录是否存在
        self.src_dir = self.lineEditSrcDir.text()
        self.dst_file = self.lineEditDstFile.text()
        self.dst_dir = self.lineEditDstDir.text()

        # 处理目标文件扩展名
        file_ext = os.path.splitext(self.dst_file)[-1]
        if len(file_ext) == 0 or file_ext.upper() != '.XLS' and file_ext.upper() != '.XLSX':
            self.dst_file = self.dst_file + '.xlsx'

        # print(type(self.dst_dir))
        # return
        if self.checkBoxXls.isChecked():
            self.src_xls = "1"
        else:
            self.src_xls = "0"
        if self.checkBoxXlsx.isChecked():
            self.src_xlsx = "1"
        else:
            self.src_xlsx = "0"
        if self.checkBoxDstDir.isChecked():
            self.dst_loc = "1"
        else:
            self.dst_loc = "0"
        if self.checkBoxTop.isChecked():
            self.win_top = "1"
        else:
            self.win_top = "0"

            # 明确目标文件夹使用那个变量
        if self.dst_loc == "1":
            self.dst_file_path = self.src_dir
        else:
            self.dst_file_path = self.lineEditDstDir.text()
            if not (os.path.exists(self.src_dir) and not os.path.isfile(self.src_dir)):
                QMessageBox.information(self, '信息', '要保存汇总文件的目录不存在，请重新选择', QMessageBox.Ok)
                return

        if len(self.src_dir.strip()) == 0:
            QMessageBox.information(self, '信息', '请选择确定源文件所在目录', QMessageBox.Ok)
            return
        if not (os.path.exists(self.src_dir) and not os.path.isfile(self.src_dir)):
            QMessageBox.information(self, '信息', '源文件所在目录不存在，请重新选择', QMessageBox.Ok)
            return
        if len(self.dst_file.strip()) == 0:
            QMessageBox.information(self, '信息', '请录入合法的汇总文件的名称', QMessageBox.Ok)
            return

        # 保存界面状态
        self.configWrite()
        # 保存规则名称
        self.configWriteRule(self.last_rule_name)
        # 开始处理汇总----------------

        max_row = 0  # 根据源文件数量计算
        max_col = 0  # 根据规则中目标表最大列计算
        # 获得源文件列表（源文件目录self.src_dir、目标文件self.dst_file、目标文件目录self.dst_file_path
        file_list = self.getFileList()
        max_row = len(file_list)
        if max_row == 0:
            QMessageBox.information(self, '信息', '至少选取一个汇总文件，汇总才能进行', QMessageBox.Ok)
            return
        max_row = max_row + int(self.lineEditRow.text())
        # ----------------从规则中获得规则列表用于后续计算----------------
        # 准备计算规则中目标表最大行和列，用于定义dataframe维度
        row = self.tableWidgetRulesUse.rowCount()
        col = self.tableWidgetRulesUse.columnCount()
        # print(row, col)
        # 获取个规则列表
        f00_list = []
        f11_list = []
        f1n_list = []
        fn1_list = []
        fnn_list = []

        for i in range(row):
            # 遍历一次规则，分别保存到list后，再处理。
            # 同时，找到规则中最大的行和列
            src_item_text = self.tableWidgetRulesUse.item(i, 1).text()  # 源文件地址
            dst_item_text = self.tableWidgetRulesUse.item(i, 2).text()  # 目标文件地址
            # print(dst_item_text, xl.excel_item_to_rowcol("dst_item_text"))

            # row_char=self.tableWidgetRulesUse.item(i, 1).text()
            # col_char = self.tableWidgetRulesUse.item(i, 1).text()
            if self.tableWidgetRulesUse.item(i, 0).text() == 'F00':
                f00_list.append(
                    [src_item_text, xl.excel_item_to_rowcol(dst_item_text)])
                # -----获得最大列------
                # print(f00_list[0][1][1])
                if max_col < f00_list[0][1][1]:
                    # print('max_col:{0},f00_list[1][1]:{1}'.format(max_col, f00_list[0][1][1]))
                    max_col = f00_list[0][1][1]
                # -----获得最大列------

            if self.tableWidgetRulesUse.item(i, 0).text() == 'F11':
                f11_list.append(
                    [xl.excel_item_to_rowcol(src_item_text), xl.excel_item_to_rowcol(dst_item_text)])
                # -----获得最大列------
                if max_col < f11_list[0][1][1]:
                    max_col = f11_list[0][1][1]
                # -----获得最大列------
            if self.tableWidgetRulesUse.item(i, 0).text() == 'F1N':
                f1n_list.append(
                    [xl.excel_item_to_rowcol(src_item_text.split(':')[0]),
                     xl.excel_item_to_rowcol(src_item_text.split(':')[1]),
                     xl.excel_item_to_rowcol(dst_item_text.split(':')[0]),
                     xl.excel_item_to_rowcol(dst_item_text.split(':')[1])])
                # -----范围地址获得最大列------
                if max_col < f1n_list[0][1][1]:
                    max_col = f1n_list[0][1][1]
                if max_col < f1n_list[0][3][1]:
                    max_col = f1n_list[0][3][1]
                # -----范围地址获得最大列------
            if self.tableWidgetRulesUse.item(i, 0).text() == 'FN1':
                fn1_list.append(
                    [xl.excel_item_to_rowcol(src_item_text), xl.excel_item_to_rowcol(dst_item_text)])
                # -----获得最大列------
                if max_col < fn1_list[0][1][1]:
                    max_col = fn1_list[0][1][1]
                # -----获得最大列------
            if self.tableWidgetRulesUse.item(i, 0).text() == 'FNN':
                fnn_list.append(
                    [xl.excel_item_to_rowcol(src_item_text.split(':')[0]),
                     xl.excel_item_to_rowcol(src_item_text.split(':')[1]),
                     xl.excel_item_to_rowcol(dst_item_text.split(':')[0]),
                     xl.excel_item_to_rowcol(dst_item_text.split(':')[1])])
                # -----范围地址获得最大列------
                if max_col < fnn_list[0][1][1]:
                    max_col = fnn_list[0][1][1]
                if max_col < fnn_list[0][3][1]:
                    max_col = fnn_list[0][3][1]
                # -----范围地址获得最大列------
        # print(f00_list,
        #       f11_list,
        #       f1n_list,
        #       fn1_list,
        #       fnn_list)
        # print('max_col:{0}'.format(max_col))
        # dest_pd.to_csv(rule_file[0], index=False)
        # ----------------------------------------------------------------
        # 根据规则和文件数量确定目标dataframe的维度
        # 定义目标文件的dataframe
        dst_pd = pd.DataFrame(np.empty(shape=(max_row, max_col + 1), dtype=str))
        # ----------------涉及单个文件提取数据的处理--------------------------------
        # 读取第一个excel文件到src_pd进行处理
        src_filename = os.path.join(self.src_dir, file_list[0])  # 连接路径与文件名。可能是这样的D:/MyPycharm/Excel数据\产品A.xls。不影响运行
        # print(src_filename)
        src_pd = pd.read_excel(src_filename, header=None)

        # F00规则汇总处理。遍历f00_list列表
        # f00_list = [['文本信息', (0, 0)]]
        for i in range(len(f00_list)):
            src_cell = f00_list[i][0]
            dst_cell = f00_list[i][1]
            dst_pd.iloc[dst_cell] = src_cell

        # # F11规则汇总处理。遍历f11_list列表
        # f11_list = [[(0, 1), (0, 1)]]
        for i in range(len(f11_list)):
            src_cell = f11_list[i][0]
            dst_cell = f11_list[i][1]
            dst_pd.iloc[dst_cell] = src_pd.iloc[src_cell]
        # # F1N规则汇总处理。遍历f1N_list列表
        # f1N_list = [[(1, 0), (3, 0), (0, 2), (0, 4)]]
        # 范围地址需要列出中间所有地址
        for i in range(len(f1n_list)):
            src_bgn = f1n_list[i][0]
            src_end = f1n_list[i][1]
            dst_bgn = f1n_list[i][2]
            dst_end = f1n_list[i][3]
            # 源文件所有单元格地址形成列表
            x_coords = [x for x in range(src_bgn[0], src_end[0] + 1)]
            y_coords = [y for y in range(src_bgn[1], src_end[1] + 1)]
            # output = list(itertools.product(x_coords, y_coords))
            src_list = [(x, y) for x in x_coords for y in y_coords]
            # print('---------------')
            # print(src_list)
            x_coords = [x for x in range(dst_bgn[0], dst_end[0] + 1)]
            y_coords = [y for y in range(dst_bgn[1], dst_end[1] + 1)]
            # output = list(itertools.product(x_coords, y_coords))
            dst_list = [(x, y) for x in x_coords for y in y_coords]
            # print(dst_list)
            # print('---------------')
            if len(src_list) != len(dst_list):
                QMessageBox.information(self, '信息', 'F1N规则：源文件地址范围与目标文件地址范围数量不一致', QMessageBox.Ok)
                return
            for j in range(len(src_list)):
                # print(src_list[i])
                dst_pd.iloc[dst_list[j]] = src_pd.iloc[src_list[j]]

        # ----------------涉及多个源文件提取数据的处理，同时处理，避免多次打开源文件--------------------------------
        # fn1_list =[[(0, 0), (1, 0)], [(0, 2), (1, 1)]]
        # fnn_list = [[(1, 1), (3, 1), (1, 2), (1, 4)]]
        # 循环原始表
        for i_file in range(len(file_list)):
            # print("---------")
            src_filename = os.path.join(self.src_dir, file_list[i_file])
            src_pd = pd.read_excel(src_filename, header=None)
            # FN1规则，循环处理多文件固定单元格→目标表起始单元格
            for i in range(len(fn1_list)):
                src_cell = fn1_list[i][0]
                dst_bgn = fn1_list[i][1]
                # print(src_pd.iloc[src_cell])
                # print(i + dest_bgn[0])
                dst_pd.iloc[i_file + dst_bgn[0], dst_bgn[1]] = src_pd.iloc[src_cell]
            # FNN规则，循环处理多文件批量单元格→目标表起始单元格
            for i in range(len(fnn_list)):
                # 获得源文件范围地址地开始和结束地址；目标文件开始范围地址的开始和结束地址
                src_bgn = fnn_list[i][0]  # （2,2）
                src_end = fnn_list[i][1]  # (5,2)
                dst_bgn = fnn_list[i][2]  # (2,3)
                dst_end = fnn_list[i][3]  # (2,6)
                # 获得开始和结束地址之间所有纸质列表
                x_coords = [x for x in range(src_bgn[0], src_end[0] + 1)]
                y_coords = [y for y in range(src_bgn[1], src_end[1] + 1)]
                # output = list(itertools.product(x_coords, y_coords))
                src_list = [(x, y) for x in x_coords for y in y_coords]
                # print(src_list)
                x_coords = [x for x in range(dst_bgn[0], dst_end[0] + 1)]
                y_coords = [y for y in range(dst_bgn[1], dst_end[1] + 1)]
                # output = list(itertools.product(x_coords, y_coords))
                dst_list = [(x + i_file, y) for x in x_coords for y in y_coords]  #
                # print(dest_list)
                for i in range(len(src_list)):
                    #     # print(src_list[i])
                    dst_pd.iloc[dst_list[i]] = src_pd.iloc[src_list[i]]
        # -------------------------------------------------------------------------------
        # print(src_pd)
        # print(dst_pd)
        # print(self.dst_file)
        # print(self.dst_file_path)
        file_dst = os.path.join(self.dst_file_path, self.dst_file)
        # print(file_dst)
        dst_pd.to_excel(file_dst, header=None, index=None)
        self.file_ext_sum()  # 刷新源文件列表
        QMessageBox.information(self, '信息', '汇总文件完毕，已生成' + file_dst, QMessageBox.Ok)

    # # self.splitter.setStretchFactor(6, 6)
    # self.tableWidgetRpt.setRowCount(0)  # 设置表格的行数,否则一直新增
    # self.tableWidgetRpt.clearContents()  # 清除内容，不清除表头（clear())
    # self.rptdst()
    # self.rptFilter()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    trans = QTranslator()  # 2
    trans.load('qt_zh_CN.qm')  # 国际化-中文，将\venv\Lib\site-packages\PySide2\translations中的此文件付出当前目录
    app.installTranslator(trans)
    window = XLExTool()
    # window.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)
    window.show()
    sys.exit(app.exec_())
