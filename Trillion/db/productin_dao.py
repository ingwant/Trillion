# coding=utf-8
from db.common_dao import CommonDao
from UI.TrillionV2 import Ui_MainWindow


class ProductInDao:
    # 存入数据
    def __init__(self):
        self.com_db = CommonDao()
        self.UI = Ui_MainWindow()

    def insert_data(self, values):
        try:
            sql = "INSERT INTO trillion.%s" \
                  "(IEMI, istorage, color, intime, company, productlines, bstorage, remarks, lotNo)" \
                  "VALUES" \
                  "('%s','%s','%s',CURRENT_TIMESTAMP,'%s','%s' ,'%s','%s', '%s');" % values
            results = CommonDao.change_option(self, sql)
            return results
        except:
            pass

    def get_iphone_type(self):
        try:
            sql = "SELECT iphonetype FROM trillion.iphonetype;"
            iphone_type = CommonDao.search_option(self, sql)
            if isinstance(iphone_type, list):
                return iphone_type
            else:
                iphone_type = self.com_db.get_local_data("iphonetype")
                return iphone_type
        except:
            iphone_type = self.com_db.get_local_data("iphonetype")
            return iphone_type

    def get_iphone_color(self):
        try:
            sql = "SELECT iphonecolor FROM trillion.iphonecolor;"
            iphone_color = CommonDao.search_option(self, sql)
            if isinstance(iphone_color, list):
                return iphone_color
            else:
                iphone_color = self.com_db.get_local_data("iphonecolor")
                return iphone_color
        except:
            iphone_color = self.com_db.get_local_data("iphonecolor")
            return iphone_color

    def get_iphone_storage(self):
        try:
            sql = "SELECT iphonestorage FROM trillion.iphonestorage;"
            iphone_storage = CommonDao.search_option(self, sql)
            if isinstance(iphone_storage, list):
                return iphone_storage
            else:
                iphone_storage = self.com_db.get_local_data("iphonestorage")
                return iphone_storage
        except:
            iphone_storage = self.com_db.get_local_data("iphonestorage")
            return iphone_storage

    def get_product_lines(self):
        try:
            sql = "SELECT productlines FROM trillion.productlines;"
            product_lines = CommonDao.search_option(self, sql)
            if isinstance(product_lines, list):
                return product_lines
            else:
                product_lines = self.com_db.get_local_data("productlines")
                return product_lines
        except Exception:
            product_lines = self.com_db.get_local_data("productlines")
            return product_lines

    def get_in_company(self):
        try:
            sql = "SELECT incompany FROM trillion.incompany;"
            in_company = CommonDao.search_option(self, sql)
            if isinstance(in_company, list):
                return in_company
            else:
                in_company = self.com_db.get_local_data("incompany")
                return in_company
        except:
            in_company = self.com_db.get_local_data("incompany")
            return in_company



