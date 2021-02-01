from db.common_dao import CommonDao


class CheckCountDao:
    def __init__(self):
        self.com_db = CommonDao()

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

    def get_all_count(self, table_name):
        try:
            sql = "SELECT COUNT(IEMI) FROM trillion.%s WHERE bstorage='1';" % table_name
            print(sql)
            all_count = CommonDao.search_option(self, sql)

            return all_count
        except:
            pass

    def get_all_count_condition(self, table_name, para, condition):
        try:
            if condition == "":
                sql = f"SELECT COUNT(IEMI) FROM trillion.{table_name} WHERE  bstorage='1' AND grade is Null;"
            else:
                sql = "SELECT COUNT(IEMI) FROM trillion.%s WHERE bstorage='1' AND %s='%s';" % (table_name, para, condition)
            print(sql)
            all_count_condition = CommonDao.search_option(self, sql)

            return all_count_condition
        except:
            pass

    def get_storage_count(self, table_name, storage):
        try:
            sql = "SELECT COUNT(IEMI) FROM trillion.%s WHERE bstorage='1' AND istorage='%s';" % (table_name, storage)
            print(sql)
            storage_count = CommonDao.search_option(self, sql)

            return storage_count
        except:
            pass

    def get_storage_count_condition(self, table_name, storage, para, condition):
        try:
            if condition == "":
                sql = f"SELECT COUNT(IEMI) FROM trillion.{table_name} WHERE  bstorage='1' AND istorage='{storage}' AND grade is Null;"
            else:
                sql = f"SELECT COUNT(IEMI) FROM trillion.{table_name} WHERE bstorage='1' AND istorage='{storage}' AND {para}='{condition}';"
            storage_count_condition = CommonDao.search_option(self, sql)

            return storage_count_condition
        except:
            pass

    def get_color_count(self, table_name, storage, color):
        try:
            sql = "SELECT COUNT(IEMI) FROM trillion.%s WHERE bstorage='1' AND istorage='%s' AND color='%s';" % (table_name, storage, color)
            color_count = CommonDao.search_option(self, sql)

            return color_count
        except:
            pass

    def get_color_count_condition(self, table_name, storage, color, para, condition):
        try:
            if condition == "":
                sql = f"SELECT COUNT(IEMI) FROM trillion.{table_name} WHERE bstorage='1' AND istorage='{storage}' AND color='{color}' AND grade is Null;"
            else:
                sql = f"SELECT COUNT(IEMI) FROM trillion.{table_name} WHERE bstorage='1' AND istorage='{storage}' AND color='{color}' AND {para}='{condition}';"
            print(sql)
            color_count_condition = CommonDao.search_option(self, sql)

            return color_count_condition
        except:
            pass

