from db.common_dao import CommonDao


class ClassificationDao:

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


    def get_iphone_info(self, table_name, IEMI):
        try:
            sql = "SELECT IEMI, istorage, color, productlines FROM trillion.%s WHERE IEMI=%s and bstorage='1';" % (table_name, IEMI)
            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
        except:
            pass


    def submit_class(self, values):
        try:
            sql = "UPDATE trillion.%s SET " \
                  "grade='%s', remarks='%s' WHERE IEMI='%s';" % values
            # print(sql)
            iphone_info = CommonDao.change_option(self, sql)

            return iphone_info
        except:
            pass
