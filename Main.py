# coding: UTF-8
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtWidgets, QtGui
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.TrillionV2 import Ui_MainWindow

from db.classification_dao import ClassificationDao
from db.transfer_dao import TransferDao
from db.inventory_dao import InventoryDao
from db.product_search_dao import ProductSearchDao
from db.checkcount_dao import CheckCountDao
from db.productout_dao import ProductOutDao
from db.productin_dao import ProductInDao

# from lines.productsearch.ProductSearch import ProductSearch


class eventMonitor(QtCore.QObject):  # 构建事件监控类
    EnterKeyPressed = QtCore.pyqtSignal()
    GetCurrentText = QtCore.pyqtSignal()

    def eventFilter(self, objwatched, event):
        eventType = event.type()
        flag = eventType == QtCore.QEvent.KeyPress
        if flag:
            ch = event.key()
            # print(f"In eventMonitor eventFilter:键盘按下，按键为：{event.key()}、{event.text()}")
            if ch == QtCore.Qt.Key_Return:
                # print("回车键按下了")
                self.EnterKeyPressed.emit()
        ret = super().eventFilter(objwatched, event)
        return False


class ComFunction(QMainWindow):

    def __init__(self):
        super(ComFunction, self).__init__()
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("./static/icon/sharethis-3-256.ico"))

        # 数据库实例化
        self.db = ProductInDao()
        self.search_db = ProductSearchDao()
        # self.ProductSearch = ProductSearch()
        self.classciffication = ClassificationDao()
        self.tranfer_db = TransferDao()
        self.checkcount_db = CheckCountDao()
        self.out_db = ProductOutDao()

        # 共同变量
        self.HomePagePB = self.main_ui.HomePagePB
        self.ProductInPB = self.main_ui.ProductInPB
        self.ProductSearchPB = self.main_ui.ProductSearchPB
        self.ClassificationPB = self.main_ui.ClassificationPB
        self.TransferPB = self.main_ui.TransferPB
        self.InventoryPB = self.main_ui.InventoryPB
        self.CheckCountPB = self.main_ui.CheckCountPB
        self.ProductOutPB = self.main_ui.ProductOutPB
        self.ComingPB = self.main_ui.ComingPB
        self.ImportDataPB = self.main_ui.ImportDataPB
        self.ClearPB = self.main_ui.ClearPB
        self.IEMItableWidget = self.main_ui.IEMItableWidget
        self.tabWidget = self.main_ui.tabWidget
        self.statusbar = self.main_ui.statusbar

        self.IEMItableWidget.setRowCount(1000)

        self.page1 = self.main_ui.page_1
        self.page2 = self.main_ui.page_2
        self.page3 = self.main_ui.page_3
        self.page4 = self.main_ui.page_4
        self.page5 = self.main_ui.page_5
        self.page6 = self.main_ui.page_6
        self.page7 = self.main_ui.page_7
        self.page8 = self.main_ui.page_8
        self.page9 = self.main_ui.page_9

        # 禁用即将到货模块
        self.ComingPB.setDisabled(True)

        # 商品入库模块对象
        self.in_type_CB = self.main_ui.in_type_CB
        self.in_color_CB = self.main_ui.in_color_CB
        self.in_storage_CB = self.main_ui.in_storage_CB
        self.InTime_DE = self.main_ui.InTime_DE
        self.InCompany_CB = self.main_ui.InCompany_CB
        self.InCompany_lotNo_LE = self.main_ui.InCompany_lotNo_LE
        self.ProductLine_CB_2 = self.main_ui.ProductLine_CB_2
        self.BoolStorage_CB = self.main_ui.BoolStorage_CB
        self.Remark_LE = self.main_ui.Remark_LE
        self.submitPB = self.main_ui.submitPB
        self.PrinterPB = self.main_ui.PrinterPB

        self.InTime_DE.setDate(QtCore.QDate.currentDate())
        self.submitPB.clicked.connect(self.save_to_db)

        # 商品查询模块对象
        self.search_IEMI_LE = self.main_ui.search_IEMI_LE
        self.search_Info_TW = self.main_ui.search_Info_TW
        self.search_type_CB = self.main_ui.search_type_CB
        self.search_color_CB = self.main_ui.search_color_CB
        self.search_storage_CB = self.main_ui.search_sotrage_CB
        self.search_time_DE = self.main_ui.search_time_DE
        self.search_incompany_CB = self.main_ui.search_incompany_LE
        self.search_bsotrage_CB = self.main_ui.search_bsotrage_CB
        self.search_remark_LE = self.main_ui.search_remark_LE
        self.search_lines_CB = self.main_ui.search_lines_CB
        self.search_submit_PB = self.main_ui.pushButton_22

        self.search_time_DE.setDate(QtCore.QDate.currentDate())
        self.search_Info_TW.setRowCount(1000)

        # self.InfoTW = self.search_Info_TW
        # print(self.InfoTW)
        # self.IEMILE_2 = self.search_IEMI_LE
        # self.StorageCB = self.search_sotrage_CB
        # self.BoolStorageCB = self.search_bsotrage_CB
        # self.TypeCB = self.search_type_CB
        # self.InTimeDE = self.search_time_DE
        # self.RemarkLE = self.search_remark_LE
        # self.ColorCB = self.search_color_CB
        # self.InCompanyCB = self.search_incompany_LE
        # self.ProductLineCB = self.search_lines_CB
        #
        # self.ConfirmChangePB = self.pushButton_22
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("./static/img/check-mark-3-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.ConfirmChangePB.setIcon(icon)
        # self.ConfirmChangePB.clicked.connect(self.product_info_change)

        self.search_submit_PB.clicked.connect(self.product_info_change)

        # 分级模块对象
        self.class_info_TW = self.main_ui.class_info_TW
        self.class_grade_CB = self.main_ui.class_grade_CB
        self.class_remark_LE = self.main_ui.class_remark_LE
        self.class_submit_PB = self.main_ui.class_submit_PB
        self.class_info_TW.setRowCount(1000)

        self.class_submit_PB.clicked.connect(self.submit_class)

        # 周转模块对象
        self.transfer_fromline_CB = self.main_ui.transfer_fromline_CB
        self.transfer_toline_CB = self.main_ui.transfer_toline_CB
        self.transfer_submit_PB = self.main_ui.transfer_submit_PB
        self.transfer_search_TW = self.main_ui.transfer_search_TW
        self.transfer_result_TW = self.main_ui.transfer_result_TW
        self.transfer_fromtime_DE = self.main_ui.transfer_fromtime_DE
        self.transfer_totime_DE = self.main_ui.transfer_totime_DE
        self.transfer_search_PB = self.main_ui.transfer_search_PB
        self.transfer_sumresult_TW = self.main_ui.transfer_sumresult_TW

        self.transfer_fromtime_DE.setDate(QtCore.QDate.currentDate())
        self.transfer_totime_DE.setDate(QtCore.QDate.currentDate())


        self.transfer_search_TW.setRowCount(1000)
        self.transfer_result_TW.setRowCount(1000)
        self.transfer_sumresult_TW.setRowCount(1000)

        self.transfer_submit_PB.clicked.connect(self.submit_transfer)
        self.transfer_search_PB.clicked.connect(self.sum_transfer)

        self.info_list = []
        self.all_info_list = []
        self.all_info_list_with_IEMI = []

        self.line_dict = {
            "仓库": "warehouseline",
            "测试": "testline",
            "维修": "repaireline",
            "换屏": "changeline",
            "打磨": "polishedline",
            "返修": "returnline",
        }



        # 盘点模块对象
        self.inventory_lines_CB = self.main_ui.inventory_lines_CB
        self.inventory_search_PB = self.main_ui.inventory_search_PB
        self.inventory_search_TW = self.main_ui.inventory_search_TW
        self.inventory_result_tab = self.main_ui.inventory_result_tab
        self.inventory_result_page_1_TW = self.main_ui.inventory_result_page_1_TW
        self.inventory_result_page_2_TW = self.main_ui.inventory_result_page_2_TW
        self.inventory_result_page_3_TW = self.main_ui.inventory_result_page_3_TW
        self.inventory_result_page_4_TW = self.main_ui.inventory_result_page_4_TW
        self.inventory_start_RB = self.main_ui.inventory_start_RB
        self.inventory_complete_RB = self.main_ui.inventory_complete_RB
        self.inventory_sum_search_PB = self.main_ui.inventory_sum_search_PB
        self.inventory_sum_search_1_TW = self.main_ui.ShowDataTW_16
        self.inventory_sum_search_2_TW = self.main_ui.ShowDataTW_17
        self.inventory_sum_search_3_TW = self.main_ui.ShowDataTW_18
        self.inventory_sum_search_4_TW = self.main_ui.ShowDataTW_19

        self.inventory_search_TW.setRowCount(1000)
        self.inventory_result_page_1_TW.setRowCount(1000)
        self.inventory_result_page_2_TW.setRowCount(1000)
        self.inventory_result_page_3_TW.setRowCount(1000)
        self.inventory_result_page_4_TW.setRowCount(1000)
        self.inventory_sum_search_1_TW.setRowCount(1000)
        self.inventory_sum_search_2_TW.setRowCount(1000)
        self.inventory_sum_search_3_TW.setRowCount(1000)
        self.inventory_sum_search_4_TW.setRowCount(1000)

        self.actual_count = []
        self.theory_count = []
        self.inventory_db = InventoryDao()
        self.inventory_search_PB.clicked.connect(self.check_list)
        self.FLAG = True
        self.check_status()
        self.inventory_start_RB.clicked.connect(self.check_status)
        self.inventory_complete_RB.clicked.connect(self.check_status)
        self.inventory_sum_search_PB.clicked.connect(self.all_check)


        # 库存查找模块对象
        self.checkcount_type_CB = self.main_ui.checkcount_type_CB
        self.checkcount_search_PB = self.main_ui.checkcount_search_PB
        self.checkcount_result_treeWidget = self.main_ui.checkcount_result_treeWidget

        self.page7_set_iphone_type()
        self.page7_set_iphone_storage()
        self.page7_set_iphone_color()

        self.page7_table_name = self.checkcount_type_CB.currentText().replace(" ", "").lower()
        self.page7_condition = ["A+", "A", "AB", "B", "", "仓库", "测试", "维修", "换屏", "返修", "打磨"]
        self.page7_lines_condition = ["仓库", "测试", "维修", "换屏", "返修", "打磨"]

        self.checkcount_search_PB.clicked.connect(self.check_count)



        # 出库模块对象
        self.out_search_TW = self.main_ui.out_search_TW
        self.out_result_TW = self.main_ui.out_result_TW
        self.out_time_DE = self.main_ui.out_time_DE
        self.out_seller_CB = self.main_ui.out_seller_CB
        self.out_bstorage_CB = self.main_ui.out_bstorage_CB
        self.out_tocompany_LE = self.main_ui.out_tocompany_LE
        self.out_salenumber_LE = self.main_ui.out_salenumber_LE
        self.out_trackingnumber_LE = self.main_ui.out_trackingnumber_LE
        self.out_remarks_LE = self.main_ui.out_remarks_LE
        self.out_submit_PB = self.main_ui.out_submit_PB

        self.out_time_DE.setDate(QtCore.QDate.currentDate())


        self.out_search_TW.setRowCount(1000)
        self.out_result_TW.setRowCount(1000)

        self.out_submit_PB.clicked.connect(self.submit_out)

        self.HomePagePB.clicked.connect(lambda: self.check_pushbutton_checked(self.HomePagePB))
        self.ProductInPB.clicked.connect(lambda: self.check_pushbutton_checked(self.ProductInPB))
        self.ProductSearchPB.clicked.connect(lambda: self.check_pushbutton_checked(self.ProductSearchPB))
        self.ClassificationPB.clicked.connect(lambda: self.check_pushbutton_checked(self.ClassificationPB))
        self.TransferPB.clicked.connect(lambda: self.check_pushbutton_checked(self.TransferPB))
        self.InventoryPB.clicked.connect(lambda: self.check_pushbutton_checked(self.InventoryPB))
        self.CheckCountPB.clicked.connect(lambda: self.check_pushbutton_checked(self.CheckCountPB))
        self.ProductOutPB.clicked.connect(lambda: self.check_pushbutton_checked(self.ProductOutPB))
        # self.ComingPB.clicked.connect(self.check_checked(self.ComingPB))
        # 捕获tabWidget页面切换信号
        self.tabWidget.currentChanged.connect(self.check_page_selected)

        # 清除IEMI表格中的数据
        self.ClearPB.clicked.connect(self.clear_IEMI_tableWidget)
        # 打开excel
        self.ImportDataPB.clicked.connect(self.openfile)

        self.IEMItableWidget.setRowCount(1000)
        # self.IEMItableWidget.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

        self.set_iphone_lines()
        self.set_iphone_color()
        self.set_iphone_type()
        self.set_iphone_storage()
        self.set_in_company()

    def enterKeyPressed(self):  # 回车键按键响应槽函数
        try:
            rowCount = self.IEMItableWidget.rowCount()
            currentRow = self.IEMItableWidget.currentRow()

            self.IEMItableWidget.setCurrentCell(currentRow + 1, 0)
        except:
            message = "录入数量超过范围....."
            self.statusbar.showMessage(message)

    def get_current_text(self):
        try:
            currentRow = self.IEMItableWidget.currentRow()
            self.current_text = self.IEMItableWidget.item(currentRow - 1, 0).text()
            current_page = self.check_page_selected()

            if current_page.objectName() == self.page3.objectName():
                self.search_show_data(self.current_text)
            if current_page.objectName() == self.page4.objectName():
                self.show_scan_data(self.current_text, currentRow,self.classciffication, self.class_info_TW)
            if current_page.objectName() == self.page5.objectName():
                self.show_scan_data(self.current_text, currentRow,self.tranfer_db, self.transfer_search_TW)
            if current_page.objectName() == self.page8.objectName():
                self.show_scan_data(self.current_text, currentRow, self.out_db, self.out_search_TW)
            if current_page.objectName() == self.page6.objectName():
                print("kkkkkkkkkkkkk")
                self.show_scan_data(self.current_text, currentRow, self.inventory_db, self.inventory_search_TW)

            # if current_page.objectName() == self.page7.objectName():
            #     self.search_show_data(self.current_text)
            # if current_page.objectName() == self.page8.objectName():
            #     self.search_show_data(self.current_text)
            # if current_page.objectName() == self.page9.objectName():
            #     self.search_show_data(self.current_text)
        except:
            pass

    # 菜单切换功能
    def check_pushbutton_checked(self, pushbutton):
        """
        将菜单切换键与tabWidget页面切换相连接
        :param pushbutton:
        :return:
        """
        push_button_dict = {self.HomePagePB: self.page1,
                            self.ProductInPB: self.page2,
                            self.ProductSearchPB: self.page3,
                            self.ClassificationPB: self.page4,
                            self.TransferPB: self.page5,
                            self.InventoryPB: self.page6,
                            self.CheckCountPB: self.page7,
                            self.ProductOutPB: self.page8,
                            self.ComingPB: self.page9}
        if self.sender():
            objectName = self.sender().objectName()
            if objectName == pushbutton.objectName():
                pushbutton.setChecked(True)
                current_page = push_button_dict.pop(pushbutton)
                self.tabWidget.setCurrentWidget(current_page)
                for button in push_button_dict.keys():
                    button.setChecked(False)

    def check_page_selected(self):
        """
        将tabWidget页面切换与菜单切换键相连接
        :return:
        """
        push_button_dict = {self.HomePagePB: self.page1,
                            self.ProductInPB: self.page2,
                            self.ProductSearchPB: self.page3,
                            self.ClassificationPB: self.page4,
                            self.TransferPB: self.page5,
                            self.InventoryPB: self.page6,
                            self.CheckCountPB: self.page7,
                            self.ProductOutPB: self.page8,
                            self.ComingPB: self.page9}
        current_page = self.tabWidget.currentWidget()
        for pushbutton, page in push_button_dict.items():
            if current_page == page:
                pushbutton.setChecked(True)
                current_page = page
            else:
                pushbutton.setChecked(False)
        return current_page

    def clear_IEMI_tableWidget(self):
        """
        清除IEMI表格中的数据
        :return:
        """
        self.IEMItableWidget.clearContents()
        self.IEMItableWidget.setRowCount(1000)

        current_page = self.check_page_selected()
        if current_page.objectName() == self.page3.objectName():
            self.info_list = []
            self.all_info_list = []
            self.search_Info_TW.clearContents()
        if current_page.objectName() == self.page4.objectName():
            self.class_info_TW.clearContents()
            self.info_list = []
            self.all_info_list = []
            self.class_info_TW.setRowCount(1000)
        if current_page.objectName() == self.page5.objectName():
            self.info_list = []
            self.all_info_list = []
            self.transfer_search_TW.clearContents()
            self.transfer_search_TW.setRowCount(1000)
            self.transfer_result_TW.clearContents()
            self.transfer_result_TW.setRowCount(1000)
            self.transfer_sumresult_TW.clearContents()
            self.transfer_sumresult_TW.setRowCount(1000)
        if current_page.objectName() == self.page8.objectName():
            self.info_list = []
            self.all_info_list = []
            self.all_info_list_with_IEMI = []
            self.out_search_TW.clearContents()
            self.out_result_TW.clearContents()
            self.out_search_TW.setRowCount(1000)
            self.out_result_TW.setRowCount(1000)
        if current_page.objectName() == self.page6.objectName():
            self.info_list = []
            self.all_info_list = []
            self.actual_count = []
            self.inventory_search_TW.clearContents()
            self.inventory_result_page_1_TW.clearContents()
            self.inventory_result_page_2_TW.clearContents()
            self.inventory_result_page_3_TW.clearContents()
            self.inventory_result_page_4_TW.clearContents()
            self.inventory_sum_search_1_TW.clearContents()
            self.inventory_sum_search_2_TW.clearContents()
            self.inventory_sum_search_3_TW.clearContents()
            self.inventory_sum_search_4_TW.clearContents()

            self.inventory_search_TW.setRowCount(1000)
            self.inventory_result_page_1_TW.setRowCount(1000)
            self.inventory_result_page_2_TW.setRowCount(1000)
            self.inventory_result_page_3_TW.setRowCount(1000)
            self.inventory_result_page_4_TW.setRowCount(1000)
            self.inventory_sum_search_1_TW.setRowCount(1000)
            self.inventory_sum_search_2_TW.setRowCount(1000)
            self.inventory_sum_search_3_TW.setRowCount(1000)
            self.inventory_sum_search_4_TW.setRowCount(1000)

    # 页面加载读取数据 Page1
    def get_iphone_type(self):
        iphone_type_list = []
        self.iphone_type = self.db.get_iphone_type()
        for item in self.iphone_type:
            iphone_type_list.append(list(item)[0])

        return iphone_type_list

    def set_iphone_type(self):
        iphone_type_list = self.get_iphone_type()

        for i in range(len(iphone_type_list)):
            self.in_type_CB.addItem(iphone_type_list[i])
            self.search_type_CB.addItem(iphone_type_list[i])
            self.checkcount_type_CB.addItem(iphone_type_list[i])

    def get_iphone_color(self):
        iphone_color_list = []
        self.iphone_color = self.db.get_iphone_color()
        for item in self.iphone_color:
            iphone_color_list.append(list(item)[0])

        return iphone_color_list

    def set_iphone_color(self):
        iphone_color_list = self.get_iphone_color()

        for i in range(len(iphone_color_list)):
            self.in_color_CB.addItem(iphone_color_list[i])
            self.search_color_CB.addItem(iphone_color_list[i])

    def get_iphone_storage(self):
        iphone_storage_list = []
        self.iphone_storage = self.db.get_iphone_storage()
        for item in self.iphone_storage:
            iphone_storage_list.append(list(item)[0])

        return iphone_storage_list

    def set_iphone_storage(self):
        iphone_storage_list = self.get_iphone_storage()

        for i in range(len(iphone_storage_list)):
            self.in_storage_CB.addItem(iphone_storage_list[i])
            self.search_storage_CB.addItem(iphone_storage_list[i])

    def get_product_lines(self):
        product_lines_list = []
        self.product_lines = self.db.get_product_lines()
        for item in self.product_lines:
            product_lines_list.append(list(item)[0])

        return product_lines_list

    def set_iphone_lines(self):
        product_lines_list = self.get_product_lines()
        print(product_lines_list)

        for i in range(len(product_lines_list)):
            self.ProductLine_CB_2.addItem(product_lines_list[i])
            self.search_lines_CB.addItem(product_lines_list[i])
            self.transfer_fromline_CB.addItem(product_lines_list[i])
            self.transfer_toline_CB.addItem(product_lines_list[i])
            self.inventory_lines_CB.addItem(product_lines_list[i])

    def get_in_company(self):
        in_company_list = []
        self.in_company = self.db.get_in_company()
        for item in self.in_company:
            in_company_list.append(list(item)[0])

        return in_company_list

    def set_in_company(self):
        in_company_list = self.get_in_company()

        for i in range(len(in_company_list)):
            self.InCompany_CB.addItem(in_company_list[i])
            self.search_incompany_CB.addItem(in_company_list[i])

    def openfile(self):
        self.IEMItableWidget.clearContents()
        openfile_name = QFileDialog.getOpenFileName(caption='select file', directory='',
                                                    filter='Excel files(*.xlsx , *.xls)', initialFilter='')
        path_openfile_name = openfile_name[0]
        if path_openfile_name:
            # 获胜excel表中的数据信息
            self.input_table = pd.read_excel(path_openfile_name)
            self.input_table = self.input_table.drop_duplicates()
            self.input_table_rows = self.input_table.shape[0]
            self.input_table_columns = self.input_table.shape[1]
            # 设置数据行数
            self.IEMItableWidget.setRowCount(self.input_table_rows)
            current_page = self.check_page_selected()
            self.showData()
            if current_page.objectName() == self.page4.objectName():
                self.class_info_TW.setRowCount(self.input_table_rows)
                self.class_show_data()
            if current_page.objectName() == self.page5.objectName():
                self.transfer_search_TW.setRowCount(self.input_table_rows)
                self.page5_showData()
            if current_page.objectName() == self.page8.objectName():
                self.out_search_TW.setRowCount(self.input_table_rows)
                self.page8_showData()
            if current_page.objectName() == self.page6.objectName():
                self.out_search_TW.setRowCount(self.input_table_rows)
                self.page6_showData()

    def showData(self):
        ###遍历表格每个元素==========================================================
        for i in range(self.input_table_rows):
            input_table_rows_values = self.input_table.iloc[[i]]
            input_table_rows_values_array = np.array(input_table_rows_values)
            self.input_table_rows_values_list = input_table_rows_values_array.tolist()
            for j in range(self.input_table_columns):
                input_table_items_list = self.input_table_rows_values_list
                ###==============将遍历的元素添加到tablewidget中并显示=======================
                input_table_items = str(input_table_items_list[0][0])
                newItem = QTableWidgetItem(input_table_items)
                # 设置显示居中
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.IEMItableWidget.setItem(i, j, newItem)

    # Page2
    def get_data(self):
        # IEMI = self.product_in.tableWidget.text()
        check_box = self.check_input_info()
        if check_box == QMessageBox.Ok:
            pass
        else:
            iphonetype = self.in_type_CB.currentText().replace(' ', '').lower()
            color = self.in_color_CB.currentText()
            storage = self.in_storage_CB.currentText()
            intime = self.InTime_DE.text()
            incompany = self.InCompany_CB.currentText()
            lotNo = self.InCompany_lotNo_LE.text()

            productline = self.ProductLine_CB_2.currentText()
            bstorage = self.BoolStorage_CB.currentText()
            remark = self.Remark_LE.text()

            return iphonetype, storage, color, incompany, productline, bstorage, remark, lotNo

    def check_input_info(self):
        if self.InCompany_lotNo_LE.text().strip() == "":
            self.check_box = QMessageBox.information(self, '提示', "请输入进货单Lot号！！！", QMessageBox.Ok)
            return self.check_box
    def out_check_input_info(self):
        if self.out_tocompany_LE.text().strip() == "":
            self.check_box = QMessageBox.information(self, '提示', "请输入销售公司", QMessageBox.Ok)
            return self.check_box
        if self.out_salenumber_LE.text().strip() == "":
            self.check_box = QMessageBox.information(self, '提示', "请输入销售单号", QMessageBox.Ok)
            return self.check_box
        if self.out_trackingnumber_LE.text().strip() == "":
            self.check_box = QMessageBox.information(self, '提示', "请输入运单号", QMessageBox.Ok)
            return self.check_box

        # 一次性获取IEMI表中的数据
    def save_to_db(self):
        self.error_list = []
        row1_item = self.IEMItableWidget.item(0, 0)
        try:
            self.statusbar.showMessage("状态栏.....")
            if row1_item == None:
                self.statusbar.showMessage("录入数据为空.....")
            else:
                result = self.get_data()
                print(result)
                # print("input_table_rows",self.input_table_rows)
                try:
                    if self.input_table_rows != 0:
                        for i in range(self.input_table_rows):
                            values_list = list(result)
                            print(values_list)
                            input_table_rows_values = self.input_table.iloc[[i]]
                            input_table_rows_values_array = np.array(input_table_rows_values)
                            self.input_table_rows_values_list = input_table_rows_values_array.tolist()
                            print(self.input_table_rows_values_list)
                            for j in range(self.input_table_columns):
                                input_table_items_list = self.input_table_rows_values_list
                                ###==============将遍历的元素添加到tablewidget中并显示=======================
                                table_items = str(input_table_items_list[0][0])
                                values_list.insert(1, table_items)
                                values = tuple(values_list)
                                print(values)
                                error = self.db.insert_data(values)
                                print(error)
                                if error == None:
                                    continue
                                else:
                                    self.error_list.append(str(error).split()[4])
                        self.show_warning(self.input_table_rows)
                    else:
                        pass
                except:
                    IEMI_list = []
                    for i in range(self.IEMItableWidget.rowCount()):
                        if self.IEMItableWidget.item(i, 0):
                            IEMI = self.IEMItableWidget.item(i, 0).text()
                            IEMI_list.append(IEMI)
                            values_list = list(result)
                            print(values_list)
                            values_list.insert(1, IEMI)
                            values = tuple(values_list)
                            print(values)
                            error = self.db.insert_data(values)
                            print(error)
                            if error == None:
                                continue
                            else:
                                self.error_list.append(str(error).split()[4])
                        else:
                            continue
                    self.show_warning(len(IEMI_list))
                    print(IEMI_list)

        except Exception as e:
            print(e)
            self.statusbar.showMessage("参数错误.....")

    def show_warning(self, all_count):
        ###show warning===================================================================
        all_count = all_count
        fail_count = len(self.error_list)
        if fail_count == 0:
            self.message = f"添加成功：{all_count - fail_count} 条。"
        else:
            IEMI_str = ''
            for IEMI in self.error_list:
                IEMI_str = IEMI_str + IEMI + "\n"
            self.message = f"添加成功：{all_count - fail_count} 条;\n添加失败：{fail_count} 条;\n失败IEMI：\n{IEMI_str}"

        QMessageBox.information(self, '提示', self.message, QMessageBox.Ok | QMessageBox.Close)

    # Page3
    def search_get_data(self):
        IEMI = self.search_IEMI_LE.text()
        type = self.search_type_CB.currentText()
        color = self.search_color_CB.currentText()
        istorage = self.search_sotrage_CB.currentText()
        incompany = self.search_incompany_CB.currentText()
        bstorage = self.search_bsotrage_CB.currentText()
        remark = self.search_remark_LE.text()
        productlines = self.search_lines_CB.currentText()

        return IEMI, type, color, istorage, incompany, bstorage, remark, productlines

    def change_warning(self, result):
        if result == None:
            self.message = f"修改成功"
        else:
            self.message = f"修改失败"

        QMessageBox.information(self, '提示', self.message, QMessageBox.Ok | QMessageBox.Close)

    def search_show_data(self, IEMI):
        if IEMI:
            i = 0
            table_name_list = []
            self.info_list = []
            # 将输入的IEMI同步
            self.search_IEMI_LE.setText(IEMI)
            table_name_tuple = self.classciffication.get_iphone_type()
            for table_name in table_name_tuple:
                table_name_list.append(list(table_name)[0])
            print(table_name_list)
            for table_name in table_name_list:
                iphone_info_list = []
                self.iphone_info = self.search_db.get_iphone_info(table_name.replace(' ', '').lower(), IEMI)
                print(self.iphone_info)

                if self.iphone_info:
                    for x in range(len(self.iphone_info[0])):
                        iphone_info_list.append(self.iphone_info[0][x])
                    iphone_info_list.insert(0, IEMI)
                    iphone_info_list.insert(1, table_name)
                    print(iphone_info_list)
                    for j, input_table_items in enumerate(iphone_info_list):
                        # 判断是否为时间数据类型
                        if type(input_table_items) == type("") or input_table_items == None:
                            input_table_items = input_table_items
                        else:
                            input_table_items = str(input_table_items.date())
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.search_Info_TW.setItem(i, j, newItem)

                    self.table_name = table_name
                    self.IMEI = IEMI
                    info_tuple = (self.table_name, self.IMEI)
                    self.info_list.append(info_tuple)
                    i += 1
            print(self.info_list)
            # if self.info_list == []:
                # self.show_warning()

    def product_info_change(self):
        IEMI = self.search_IEMI_LE.text()

        if IEMI.strip():
            type = self.search_type_CB.currentText()
            color = self.search_color_CB.currentText()
            istorage = self.search_storage_CB.currentText()
            incompany = self.search_incompany_CB.currentText()
            bstorage = self.search_bsotrage_CB.currentText()
            remark = self.search_remark_LE.text()
            productlines = self.search_lines_CB.currentText()
            time = self.search_time_DE.text()

            values1 = (type.replace(" ", "").lower(), IEMI, istorage, color, incompany, productlines, bstorage, remark)

            if self.info_list == []:
                # 系统中不存在，直接添加
                result = self.search_db.insert_data(values1)

            else:
                if self.table_name.replace(" ", "").lower() == type.replace(" ", "").lower():
                    # 判断是否属于在相同的表中，如果是则修改该表的参数
                    values2 = (
                        self.table_name.replace(" ", "").lower(), istorage, color, incompany, productlines, bstorage,
                        remark,
                        IEMI)
                    result = self.search_db.change_data(values2)

                else:
                    # 如果不在同一张表中，删除原始数据，添加新的数据
                    values3 = (self.table_name.replace(" ", "").lower(), IEMI)
                    del_result = self.search_db.delete_data(values3)
                    result = self.search_db.insert_data(values1)

            # self.change_warning(result)
        self.search_show_data(IEMI)


    # page4
    def class_show_data(self):
        self.info_list = []
        table_name_list = self.get_iphone_type()
        print(table_name_list)
        for table_name in table_name_list:
            for i in range(self.input_table_rows):
                input_table_rows_values = self.input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)
                self.input_table_rows_values_list = input_table_rows_values_array.tolist()
                for IEMI in self.input_table_rows_values_list:
                    self.iphone_info = self.classciffication.get_iphone_info(table_name.replace(' ', '').lower(), str(IEMI[0]))
                    if self.iphone_info:
                        input_table_items = str(IEMI)
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.class_info_TW.setItem(i, 0, newItem)

                        input_table_items = table_name
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.class_info_TW.setItem(i, 1, newItem)

                        input_table_items = list(self.iphone_info[0])[0]
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.class_info_TW.setItem(i, 2, newItem)

                        input_table_items = input_table_items = list(self.iphone_info[0])[1]
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.class_info_TW.setItem(i, 3, newItem)

                        input_table_items = input_table_items = list(self.iphone_info[0])[2]
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.class_info_TW.setItem(i, 4, newItem)



                        self.table_name = table_name
                        self.IMEI = str(IEMI[0])
                        info_tuple = (self.table_name, self.IMEI)
                        self.info_list.append(info_tuple)
                    else:
                        # 将系统中不存在的IMEI列出
                        input_table_items = str(IEMI[0])
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.class_info_TW.setItem(i, 0, newItem)

    def show_scan_data(self, IEMI, currentRow, db, TW_name):
        self.currentRow = currentRow
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            self.iphone_info = db.get_iphone_info(table_name.replace(' ', '').lower(), IEMI)
            if self.iphone_info:
                if db == self.tranfer_db:
                    list_info = list(self.iphone_info[0])
                    list_info.insert(0, IEMI)
                    list_info.insert(1, table_name)

                    grade = list_info.pop()

                    for x, item in enumerate(list_info):
                        newItem = QTableWidgetItem(item)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        TW_name.setItem(currentRow - 1, x, newItem)

                    self.table_name = table_name
                    self.IMEI = IEMI
                    info_tuple = (self.table_name, self.IMEI)
                    self.info_list.append(info_tuple)

                    info_list = [table_name, list_info[2], list_info[3], grade]
                    self.all_info_list.append(info_list)
                if db == self.classciffication:
                    print(self.iphone_info)
                    iphone_info_list = list(self.iphone_info[0])
                    iphone_info_list.insert(1, table_name)
                    print(iphone_info_list)
                    for i, item in enumerate(iphone_info_list):
                        input_table_items = str(item)
                        newItem = QTableWidgetItem(input_table_items)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        TW_name.setItem(currentRow - 1, i, newItem)

                    self.table_name = table_name
                    self.IMEI = IEMI
                    info_tuple = (self.table_name, self.IMEI)
                    self.info_list.append(info_tuple)

                if db == self.out_db:
                    # 显示IEMI
                    newItem = QTableWidgetItem(IEMI)
                    # 设置显示居中
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    TW_name.setItem(currentRow-1, 0, newItem)

                    # 显示type
                    newItem = QTableWidgetItem(table_name)
                    # 设置显示居中
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    TW_name.setItem(currentRow-1, 2, newItem)

                    # 显示Grade
                    grade = list(self.iphone_info[0])[2]
                    newItem = QTableWidgetItem(grade)
                    # 设置显示居中
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    TW_name.setItem(currentRow-1, 1, newItem)

                    # 显示内存
                    storage = list(self.iphone_info[0])[0]
                    newItem = QTableWidgetItem(storage)
                    # 设置显示居中
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    TW_name.setItem(currentRow-1, 3, newItem)

                    # 显示颜色
                    color = list(self.iphone_info[0])[1]
                    newItem = QTableWidgetItem(color)
                    # 设置显示居中
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    TW_name.setItem(currentRow-1, 4, newItem)

                    self.table_name = table_name
                    self.IMEI = IEMI
                    info_tuple = (self.table_name, self.IMEI)
                    self.info_list.append(info_tuple)

                    info_list = [table_name, storage, color, grade]
                    self.all_info_list.append(info_list)

                    info_list_with_IEMI = [table_name, IEMI]
                    self.all_info_list_with_IEMI.append(info_list_with_IEMI)

                if db == self.inventory_db:
                    # 更改状态
                    print("sssssssss")
                    db.change_status_single(table_name.replace(" ", "").lower(), IEMI)
                    iphone_info_no_IEMI = list(self.iphone_info[0])
                    iphone_info_no_IEMI.pop()
                    iphone_info_no_IEMI.insert(1, table_name)
                    self.actual_count.append(iphone_info_no_IEMI)

                    self.iphone_info_list = list(self.iphone_info[0])
                    self.iphone_info_list.insert(0, IEMI)
                    self.iphone_info_list.insert(2, table_name)
                    print(self.iphone_info_list)
                    for x, item in enumerate(self.iphone_info_list):
                        newItem = QTableWidgetItem(item)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        TW_name.setItem(currentRow-1, x, newItem)

                    self.table_name = table_name
                    self.IMEI = IEMI
                    info_tuple = (self.table_name, self.IMEI)
                    self.info_list.append(info_tuple)

            else:
                # 将系统中不存在的IMEI列出
                input_table_items = IEMI
                newItem = QTableWidgetItem(input_table_items)
                # 设置显示居中
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                TW_name.setItem(currentRow-1, 0, newItem)
        print(self.info_list)

    def class_get_data(self):
        grade = self.class_grade_CB.currentText()
        remark = self.class_remark_LE.text()
        return grade, remark

    def submit_class(self):
        grade = list(self.class_get_data())[0]
        remark = list(self.class_get_data())[1]
        self.error_list = []
        for item in self.info_list:
            print(self.info_list)
            table_name = list(item)[0].replace(' ', '').lower()
            IEMI = list(item)[1]
            values = (table_name, grade, remark, IEMI)

            error = self.classciffication.submit_class(values)

            if error == None:
                continue
            else:
                self.error_list.append(str(error).split()[4])

        self.class_show_warning()

    def class_show_warning(self):
        ###show warning===================================================================
        try:
            all_count = self.input_table_rows
            fail_count = len(self.error_list)
            success_count = len(self.info_list)
            if fail_count == 0:
                self.message = f"修改成功：{int(success_count/2)} 条。"
            else:
                IEMI_str = ''
                for IEMI in self.error_list:
                    IEMI_str = IEMI_str + IEMI + "\n"
                self.message = f"修改成功：{all_count - fail_count} 条;\n修改失败：{fail_count} 条;\n失败IEMI：\n{IEMI_str}"

            QMessageBox.information(self, '提示', self.message, QMessageBox.Ok | QMessageBox.Close)
        except:
            all_count = self.currentRow
            fail_count = len(self.error_list)
            success_count = len(self.info_list)
            if fail_count == 0:
                self.message = f"修改成功：{int(success_count)} 条。"
            else:
                IEMI_str = ''
                for IEMI in self.error_list:
                    IEMI_str = IEMI_str + IEMI + "\n"
                self.message = f"修改成功：{all_count - fail_count} 条;\n修改失败：{fail_count} 条;\n失败IEMI：\n{IEMI_str}"

            QMessageBox.information(self, '提示', self.message, QMessageBox.Ok | QMessageBox.Close)

        finally:
            pass


    # page5
    def page5_get_data(self):
        product_line_from = self.transfer_fromline_CB.currentText()
        product_line_to = self.transfer_toline_CB.currentText()
        # change_time = self.transfer_time_DE.text()

        return product_line_from, product_line_to

    def page5_showData(self):
        self.info_list = []
        self.all_info_list = []
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            for i in range(self.input_table_rows):
                input_table_rows_values = self.input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)

                self.input_table_rows_values_list = input_table_rows_values_array.tolist()

                for IEMI in self.input_table_rows_values_list:
                    self.iphone_info = self.tranfer_db.get_iphone_info(table_name.replace(' ', '').lower(), str(IEMI[0]))

                    if self.iphone_info:
                        list_info = list(self.iphone_info[0])
                        list_info.insert(0, str(IEMI[0]))
                        list_info.insert(1, table_name)

                        grade = list_info.pop()

                        for x, item in enumerate(list_info):
                            newItem = QTableWidgetItem(item)
                            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.transfer_search_TW.setItem(i, x, newItem)

                        self.table_name = table_name
                        self.IMEI = str(IEMI[0])
                        info_tuple = (self.table_name, self.IMEI)
                        self.info_list.append(info_tuple)

                        info_list = [table_name, list_info[2],list_info[3], grade]
                        self.all_info_list.append(info_list)

                    else:
                        # 将系统中不存在的IMEI列出
                        input_table_items = str(IEMI[0])
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.transfer_search_TW.setItem(i, 0, newItem)

    def sum_transfer(self):
        self.transfer_sumresult_TW.clearContents()
        i = 0
        start_time = self.transfer_fromtime_DE.text().replace("/", "-")
        search_start_time = start_time + " 00:00:00"
        end_time = self.transfer_totime_DE.text().replace("/", "-")
        search_end_time = end_time + " 23:59:59"
        self.transfer_sumresult_TW.setRowCount(len(self.line_dict))
        for line, table_name in self.line_dict.items():
            result = self.tranfer_db.check_transfer_sum_count(table_name, search_start_time, search_end_time)
            result_list = [line, start_time, end_time, list(result[0])[0]]
            result_list_str = [ str(item) for item in result_list]
            print(result_list_str)

            for j, item in enumerate(result_list_str):
                output = QTableWidgetItem(item)
                output.setTextAlignment(QtCore.Qt.AlignCenter)
                self.transfer_sumresult_TW.setItem(i, j, output)

            i += 1

    def show_result(self, iphone_info_list, widget_name):
        print(iphone_info_list)
        print(widget_name)
        widget_name.clearContents()
        i = 0
        if iphone_info_list:
            all_info_list = [str(item) for item in iphone_info_list]
            count = dict(pd.Series(all_info_list).value_counts())
            widget_name.setRowCount(len(count))
            try:
                for key, value in count.items():
                    if 'None' in key:
                        key = key.replace("None", "''")
                    else:
                        key = key
                    for j, items in enumerate(key[2:-2].split("', '")):
                        output = QTableWidgetItem(items)
                        output.setTextAlignment(QtCore.Qt.AlignCenter)
                        widget_name.setItem(i, j, output)
                    output = QTableWidgetItem(str(value))
                    output.setTextAlignment(QtCore.Qt.AlignCenter)
                    widget_name.setItem(i, 4, output)
                    i += 1
            except:
                for key, value in count.items():
                    for j, items in enumerate(key[2:-2].split('", "')):
                        output = QTableWidgetItem(items)
                        output.setTextAlignment(QtCore.Qt.AlignCenter)
                        widget_name.setItem(i, j, output)
                    output = QTableWidgetItem(str(value))
                    output.setTextAlignment(QtCore.Qt.AlignCenter)
                    widget_name.setItem(i, 4, output)
                    i += 1
            return count

    def submit_transfer(self):
        product_line_from = list(self.page5_get_data())[0]
        product_line_to = list(self.page5_get_data())[1]
        from_table = self.line_dict[product_line_from]
        to_table = self.line_dict[product_line_to]
        self.error_list = []
        print(self.info_list)
        if self.info_list:
            for item in self.info_list:
                table_name = list(item)[0].replace(' ', '').lower()
                IEMI = list(item)[1]
                # 用于修改主表
                values = (table_name, product_line_to, IEMI)
                error = self.tranfer_db.submit_transfer(values)
                self.tranfer_db.transfer_line_table(from_table, to_table, IEMI)
                if error == None:
                    continue
                else:
                    self.error_list.append(str(error).split()[4])

            self.show_result(self.all_info_list, self.transfer_result_TW)

    # page6
    def page6_showData(self):
        self.info_list = []
        self.actual_count = []
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            for i in range(self.input_table_rows):
                input_table_rows_values = self.input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)
                self.input_table_rows_values_list = input_table_rows_values_array.tolist()
                for IEMI in self.input_table_rows_values_list:
                    self.iphone_info = self.inventory_db.get_iphone_info(table_name.replace(' ', '').lower(), str(IEMI[0]))

                    if self.iphone_info:
                        # 更改状态
                        self.inventory_db.change_status_single(table_name.replace(" ", "").lower(), str(IEMI[0]))
                        iphone_info_no_IEMI = list(self.iphone_info[0])
                        iphone_info_no_IEMI.pop()
                        iphone_info_no_IEMI.insert(1, table_name)
                        self.actual_count.append(iphone_info_no_IEMI)

                        self.iphone_info_list = list(self.iphone_info[0])
                        self.iphone_info_list.insert(0, str(IEMI[0]))
                        self.iphone_info_list.insert(2, table_name)
                        for x, item in enumerate(self.iphone_info_list):
                            newItem = QTableWidgetItem(item)
                            # 设置显示居中
                            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.inventory_search_TW.setItem(i, x, newItem)

                        self.table_name = table_name
                        self.IMEI = str(IEMI[0])
                        info_tuple = (self.table_name, self.IMEI)
                        self.info_list.append(info_tuple)
                    else:
                        # 将系统中不存在的IMEI列出
                        input_table_items = str(IEMI[0])
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.inventory_search_TW.setItem(i, 0, newItem)

    def get_theory_count(self):
        iphone_info_list = []
        product_line = self.inventory_lines_CB.currentText()
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            iphone_info = self.inventory_db.get_iphone_info_theory(table_name.replace(" ", "").lower(), product_line)
            if iphone_info:
                # iphone_info_list = [item.insert(1, table_name) for list(item) in iphone_info]
                for item in iphone_info:
                    info = list(item)
                    info.insert(1, table_name)
                    iphone_info_list.append(info)

        theory_count = self.show_count(iphone_info_list, self.inventory_result_page_1_TW)

        return theory_count

    def get_actual_count(self):
        actual_count = self.show_count(self.actual_count, self.inventory_result_page_2_TW)

        return actual_count

    def get_all_theory_count(self):
        iphone_info_list = []
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            iphone_info = self.inventory_db.get_iphone_info_all_theory(table_name.replace(" ", "").lower())
            if iphone_info:
                # iphone_info_list = [item.insert(1, table_name) for list(item) in iphone_info]
                for item in iphone_info:
                    info = list(item)
                    info.insert(1, table_name)
                    iphone_info_list.append(info)

        all_theory_count = self.show_count(iphone_info_list, self.inventory_sum_search_4_TW)

        return all_theory_count

    def get_all_actual_count(self):
        iphone_info_list = []
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            iphone_info = self.inventory_db.get_iphone_info_all_actual(table_name.replace(" ", "").lower())
            if iphone_info:
                # iphone_info_list = [item.insert(1, table_name) for list(item) in iphone_info]
                for item in iphone_info:
                    info = list(item)
                    info.insert(1, table_name)
                    iphone_info_list.append(info)

        all_actual_count = self.show_count(iphone_info_list, self.inventory_sum_search_3_TW)

        return all_actual_count

    def check_list(self):
        self.inventory_result_page_1_TW.clearContents()
        self.inventory_result_page_2_TW.clearContents()
        self.inventory_result_page_3_TW.clearContents()
        self.inventory_result_page_4_TW.clearContents()

        differ_theory_dict = {}
        differ_actual_dict = {}

        theory_count = self.get_theory_count()
        actual_count = self.get_actual_count()
        try:
            different = set(theory_count.items()) ^ set(actual_count.items())
            for item in different:
                if item in set(theory_count.items()):
                    # self.show_count()
                    differ_theory_dict[list(item)[0]] = list(item)[1]

                else:
                    differ_actual_dict[list(item)[0]] = list(item)[1]
        except:
            pass

        self.show_differ_count(differ_theory_dict, self.inventory_result_page_3_TW)
        self.show_differ_count(differ_actual_dict, self.inventory_result_page_4_TW)

    def show_count(self, iphone_info_list, widget_name):
        i = 0
        if iphone_info_list:
            all_info_list = [str(item) for item in iphone_info_list]
            count = dict(pd.Series(all_info_list).value_counts())
            widget_name.setRowCount(len(count))
            try:
                for key, value in count.items():
                    for j, items in enumerate(key[2:-2].split("', '")):
                        output = QTableWidgetItem(items)
                        output.setTextAlignment(QtCore.Qt.AlignCenter)
                        widget_name.setItem(i, j, output)
                    output = QTableWidgetItem(str(value))
                    output.setTextAlignment(QtCore.Qt.AlignCenter)
                    widget_name.setItem(i, 4, output)
                    i += 1
            except:
                for key, value in count.items():
                    for j, items in enumerate(key[2:-2].split('", "')):
                        output = QTableWidgetItem(items)
                        output.setTextAlignment(QtCore.Qt.AlignCenter)
                        widget_name.setItem(i, j, output)
                    output = QTableWidgetItem(str(value))
                    output.setTextAlignment(QtCore.Qt.AlignCenter)
                    widget_name.setItem(i, 4, output)
                    i += 1
            return count

    def show_differ_count(self, info_dict, widget_name):
        i = 0
        widget_name.setRowCount(len(info_dict))
        if info_dict:
            try:
                for key, value in info_dict.items():
                    for j, items in enumerate(key[2:-2].split("', '")):
                        output = QTableWidgetItem(items)
                        output.setTextAlignment(QtCore.Qt.AlignCenter)
                        widget_name.setItem(i, j, output)
                    output = QTableWidgetItem(str(value))
                    output.setTextAlignment(QtCore.Qt.AlignCenter)
                    widget_name.setItem(i, 4, output)

                    i += 1
            except:
                for key, value in info_dict.items():
                    for j, items in enumerate(key[2:-2].split('", "')):
                        output = QTableWidgetItem(items)
                        output.setTextAlignment(QtCore.Qt.AlignCenter)
                        widget_name.setItem(i, j, output)
                    output = QTableWidgetItem(str(value))
                    output.setTextAlignment(QtCore.Qt.AlignCenter)
                    widget_name.setItem(i, 4, output)

                    i += 1

    def check_status(self):
        if self.FLAG:
            if self.inventory_start_RB.isChecked():
                self.message = "是否确认初始化盘点？"
                clicked = QMessageBox.information(self, '提示', self.message, QMessageBox.Ok | QMessageBox.Cancel)
                # 判断是否选择初始化
                if clicked == QMessageBox.Ok:
                    try:
                        table_name_list = self.get_iphone_type()
                        for table_name in table_name_list:
                            result = self.inventory_db.change_status(table_name.replace(" ", "").lower())
                            self.FLAG = False
                    except:
                        print("执行出错")
                        pass
                else:
                    self.inventory_complete_RB.setChecked(True)

        if self.inventory_complete_RB.isChecked():
            self.FLAG = True

    def all_check(self):
        self.inventory_sum_search_1_TW.clearContents()
        self.inventory_sum_search_2_TW.clearContents()
        self.inventory_sum_search_3_TW.clearContents()
        self.inventory_sum_search_4_TW.clearContents()

        differ_theory_dict = {}
        differ_actual_dict = {}

        theory_count = self.get_all_theory_count()
        actual_count = self.get_all_actual_count()

        try:
            different = set(theory_count.items()) ^ set(actual_count.items())
            for item in different:
                if item in set(theory_count.items()):
                    # self.show_count()
                    differ_theory_dict[list(item)[0]] = list(item)[1]

                else:
                    differ_actual_dict[list(item)[0]] = list(item)[1]
        except:
            pass

        self.show_differ_count(differ_theory_dict, self.inventory_sum_search_1_TW)
        self.show_differ_count(differ_actual_dict, self.inventory_sum_search_2_TW)

    # page7
    def page7_get_iphone_type(self):
        iphone_type_list = []
        self.iphone_type = self.checkcount_db.get_iphone_type()
        for item in self.iphone_type:
            iphone_type_list.append(list(item)[0])

        return iphone_type_list

    def page7_set_iphone_type(self):
        iphone_type_list = self.page7_get_iphone_type()

        for i in range(len(iphone_type_list)):
            self.checkcount_type_CB.addItem(iphone_type_list[i])

    def page7_get_iphone_storage(self):
        iphone_storage_list = []
        self.iphone_storage = self.checkcount_db.get_iphone_storage()
        for item in self.iphone_storage:
            iphone_storage_list.append(list(item)[0])

        return iphone_storage_list

    def page7_set_iphone_storage(self):
        iphone_storage_list = self.page7_get_iphone_storage()

        # for i in range(len(iphone_storage_list)):
        #     self.TypeCB.addItem(iphone_storage_list[i])

    def page7_get_iphone_color(self):
        iphone_color_list = []
        self.iphone_color = self.checkcount_db.get_iphone_color()
        for item in self.iphone_color:
            iphone_color_list.append(list(item)[0])

        return iphone_color_list

    def page7_set_iphone_color(self):
        iphone_color_list = self.page7_get_iphone_color()
        # for i in range(len(iphone_color_list)):
        #     self.TypeCB.addItem(iphone_color_list[i])

    def check_count(self):
        self.checkcount_result_treeWidget.clear()
        iphone_type = self.checkcount_type_CB.currentText()
        table_name = iphone_type.replace(" ", "").lower()
        # 设置主节点
        iphone_type_item = QtWidgets.QTreeWidgetItem(self.checkcount_result_treeWidget)
        self.checkcount_result_treeWidget.topLevelItem(0).setData(0, 0, iphone_type)
        # iphone_type_item.topLevelItem(0).setText(0, iphone_type)
        all_count = list(self.all_count()[0])[0]
        # self.treeWidget.set
        self.checkcount_result_treeWidget.topLevelItem(0).setData(1, 0, all_count)

        for x, condition in enumerate(self.page7_condition):

            if condition not in self.page7_lines_condition:
                self.para = "grade"
            else:
                self.para = "productlines"
            condition_count = list(self.checkcount_db.get_all_count_condition(table_name, self.para, condition)[0])[0]
            self.checkcount_result_treeWidget.topLevelItem(0).setData(2 + x, 0, condition_count)

        # 设置次节点
        iphone_storage = self.get_iphone_storage()
        iphone_color = self.get_iphone_color()

        # 显示节点
        for i, storage in enumerate(iphone_storage):
            storage_child = QtWidgets.QTreeWidgetItem()

            storage_count = str(list(self.storage_count(storage)[0])[0])

            # 设置查找后对应内存的数量
            iphone_type_item.addChild(storage_child)
            self.checkcount_result_treeWidget.topLevelItem(0).child(i).setText(0, storage)
            self.checkcount_result_treeWidget.topLevelItem(0).child(i).setText(1, storage_count)

            for x, condition in enumerate(self.page7_condition):

                if condition not in self.page7_lines_condition:
                    self.para = "grade"
                else:
                    self.para = "productlines"
                storage_count_condition = str(
                    list(self.checkcount_db.get_storage_count_condition(table_name, storage, self.para, condition)[0])[0])

                self.checkcount_result_treeWidget.topLevelItem(0).child(i).setText(2 + x, storage_count_condition)

            for j, color in enumerate(iphone_color):
                color_child = QtWidgets.QTreeWidgetItem()

                color_count = str(list(self.color_count(storage, color)[0])[0])
                storage_child.addChild(color_child)
                self.checkcount_result_treeWidget.topLevelItem(0).child(i).child(j).setText(0, color)
                self.checkcount_result_treeWidget.topLevelItem(0).child(i).child(j).setText(1, color_count)
                for x, condition in enumerate(self.page7_condition):

                    if condition not in self.page7_lines_condition:
                        self.para = "grade"
                    else:
                        self.para = "productlines"
                    condition_count_condition = str(
                        list(self.checkcount_db.get_color_count_condition(table_name, storage, color, self.para, condition)[0])[0])
                    self.checkcount_result_treeWidget.topLevelItem(0).child(i).child(j).setText(2 + x, condition_count_condition)

    def all_count(self):
        table_name = self.checkcount_type_CB.currentText().replace(" ", "").lower()

        all_count = self.checkcount_db.get_all_count(table_name)

        return all_count

    def storage_count(self, storage):
        table_name = self.checkcount_type_CB.currentText().replace(" ", "").lower()
        storage_count = self.checkcount_db.get_storage_count(table_name, storage)

        return storage_count

    def color_count(self, storage, color):
        table_name = self.checkcount_type_CB.currentText().replace(" ", "").lower()
        color_count = self.checkcount_db.get_color_count(table_name, storage, color)

        return color_count

    # page8
    def page8_showData(self):
        self.info_list = []
        self.all_info_list = []
        self.all_info_list_with_IEMI = []
        table_name_list = self.get_iphone_type()
        for table_name in table_name_list:
            for i in range(self.input_table_rows):
                input_table_rows_values = self.input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)
                self.input_table_rows_values_list = input_table_rows_values_array.tolist()
                for IEMI in self.input_table_rows_values_list:
                    self.iphone_info = self.out_db.get_iphone_info(table_name.replace(' ', '').lower(), str(IEMI[0]))
                    if self.iphone_info:

                        # 显示IEMI
                        IEMI = str(IEMI[0])
                        newItem = QTableWidgetItem(IEMI)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.out_search_TW.setItem(i, 0, newItem)

                        # 显示type
                        newItem = QTableWidgetItem(table_name)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.out_search_TW.setItem(i, 2, newItem)

                        # 显示Grade
                        grade = list(self.iphone_info[0])[2]
                        newItem = QTableWidgetItem(grade)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.out_search_TW.setItem(i, 1, newItem)

                        # 显示内存
                        storage = list(self.iphone_info[0])[0]
                        newItem = QTableWidgetItem(storage)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.out_search_TW.setItem(i, 3, newItem)

                        # 显示颜色
                        color = list(self.iphone_info[0])[1]
                        newItem = QTableWidgetItem(color)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.out_search_TW.setItem(i, 4, newItem)

                        self.table_name = table_name
                        self.IMEI = str(IEMI[0])
                        info_tuple = (self.table_name, self.IMEI)
                        self.info_list.append(info_tuple)

                        info_list = [table_name, storage, color, grade]
                        self.all_info_list.append(info_list)

                        info_list_with_IEMI = [table_name, IEMI]
                        self.all_info_list_with_IEMI.append(info_list_with_IEMI)

                    else:
                        # 将系统中不存在的IMEI列出
                        input_table_items = str(IEMI[0])
                        newItem = QTableWidgetItem(input_table_items)
                        # 设置显示居中
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.out_search_TW.setItem(i, 0, newItem)

    def submit_out(self):

        # 修改参数，完成入库
        check_box = self.out_check_input_info()
        if check_box == QMessageBox.Ok:
            pass
        else:
            OutTimeDE = self.out_time_DE.text()
            Seller = self.out_seller_CB.currentText()
            BoolStorage = self.out_bstorage_CB.currentText()
            ToCompany = self.out_tocompany_LE.text()
            SaleNumber = self.out_salenumber_LE.text()
            TrackNumber = self.out_trackingnumber_LE.text()
            Remark = self.out_remarks_LE.text()

            error_list = []
            if self.all_info_list_with_IEMI:
                for item in self.all_info_list_with_IEMI:
                    # outtime = '%s', selller = '%s', bstorage = '%s', tocompany = '%s', tracknumber = '%s', salenumber = '%s', remarks = '%s'
                    values = (item[0].replace(" ", "").lower(), Seller, BoolStorage, ToCompany, TrackNumber,
                              SaleNumber, Remark, item[1])
                    result = self.out_db.insert_sell_info(values)
                    if result:
                        error_list.append(item)
            else:
                pass

            self.show_result(self.all_info_list, self.out_result_TW)






if __name__ == "__main__":
    import sys
    import os

    if hasattr(sys, '_MEIPASS'):
        # PyInstaller会创建临时文件夹temp
        # 并把路径存储在_MEIPASS中
        appPath = os.path.dirname(os.path.realpath(sys.executable))
    else:
        appPath, filename = os.path.split(os.path.abspath(__file__))

    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ComFunction()
    MainWindow.show()

    monitorObj = eventMonitor()  # 创建事件刷选监视对象
    monitorObj.EnterKeyPressed.connect(MainWindow.enterKeyPressed)  # 连接自定义信号和槽
    monitorObj.EnterKeyPressed.connect(MainWindow.get_current_text)  # 连接自定义信号和槽
    MainWindow.IEMItableWidget.installEventFilter(monitorObj)  # 对tableWidget安装事件监控

    sys.exit(app.exec_())
