class CheckCount(QWidget):
    def __init__(self):
        super(CheckCount, self).__init__()
        self.checkcount = Ui_CheckCount()
        self.checkcount.setupUi(self)
        self.setWindowIcon(QIcon("./static/icon/parallel-tasks-256.ico"))

        self.TypeCB = self.checkcount.TypeCB
        self.SearchPB = self.checkcount.SearchPB
        self.checkcount_search_PB.clicked.connect(self.check_count)

        self.treeWidget = self.checkcount.treeWidget

        self.db = CheckCountDao()

        # 设置iphone类型
        self.page7_set_iphone_type()
        self.page7_set_iphone_storage()
        self.page7_set_iphone_color()

        # 查询条件
        self.condition = ["A+", "A", "AB", "B", "", "仓库", "测试", "维修", "换屏", "返修", "打磨"]
        self.lines_condition = ["仓库", "测试", "维修", "换屏", "返修", "打磨"]

        self.search_table = self.checkcount_type_CB.currentText().replace(" ", "").lower()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./static/img/search-13-64.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchPB.setIcon(icon)

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
        iphone_type_item = QtWidgets.QTreeWidgetItem(self.treeWidget)
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