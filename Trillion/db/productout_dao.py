from db.common_dao import CommonDao


class ProductOutDao:
    def __init__(self):
        self.com_db = CommonDao()

    def get_iphone_info(self, table_name, IEMI):
        try:
            sql = "SELECT istorage, color, grade FROM trillion.%s WHERE IEMI=%s AND bstorage='1';" % (table_name, IEMI)
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


    def insert_sell_info(self, values):
        try:
            sql = "UPDATE trillion.%s SET " \
                  "outtime=CURRENT_TIMESTAMP, selller='%s', bstorage='%s', tocompany='%s', tracknumber='%s', salenumber='%s', remarks='%s' WHERE IEMI='%s';" % values
            # print(sql)
            results = CommonDao.change_option(self, sql)
            print(results)

            return results
        except:
            pass