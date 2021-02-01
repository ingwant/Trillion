from db.common_dao import CommonDao


class InventoryDao:
    def __init__(self):
        self.com_db = CommonDao()

    def get_product_lines(self):
        try:
            sql = "SELECT productlines FROM trillion.productlines;"
            product_lines = CommonDao.search_option(self, sql)
            if isinstance(product_lines, list):
                return product_lines
            else:
                product_lines = self.com_db.get_local_data("productlines")
                return product_lines
        except:
            product_lines = self.com_db.get_local_data("productlines")
            return product_lines

    def get_iphone_info(self, table_name, IEMI):
        try:
            sql = "SELECT productlines, istorage, color, bstorage FROM trillion.%s WHERE IEMI=%s;" % (table_name, IEMI)
            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
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

    def get_iphone_info_theory(self, table_name, product_line):
        try:
            sql = f"SELECT productlines, istorage, color FROM trillion.{table_name} WHERE productlines='{product_line}' and bstorage='1';"
            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
        except:
            pass

    def get_iphone_info_actual(self, table_name, product_line):
        try:
            sql = f"SELECT productlines, istorage, color FROM trillion.{table_name} WHERE productlines='{product_line}' and forinventory='1';"

            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
        except:
            pass

    def change_status(self, table_name):
        try:
            sql = f"UPDATE trillion.{table_name} SET forinventory='0';"

            results = CommonDao.change_option(self, sql)

            return results
        except:
            pass

    def change_status_single(self, table_name, IEMI):
        try:
            sql = f"UPDATE trillion.{table_name} SET forinventory='1' WHERE IEMI='{IEMI}';"

            results = CommonDao.change_option(self, sql)

            return results
        except:
            pass

    def get_iphone_info_all_theory(self, table_name):
        try:
            sql = f"SELECT productlines, istorage, color FROM trillion.{table_name} WHERE bstorage='1';"

            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
        except:
            pass

    def get_iphone_info_all_actual(self, table_name):
        try:
            sql = f"SELECT productlines, istorage, color FROM trillion.{table_name} WHERE forinventory='1';"

            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
        except:
            pass
