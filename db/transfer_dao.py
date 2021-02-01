from db.common_dao import CommonDao


class TransferDao:
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
            sql = "SELECT istorage, color, productlines, grade FROM trillion.%s WHERE IEMI=%s;" % (table_name, IEMI)
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

    def submit_transfer(self, values):
        try:
            sql = "UPDATE trillion.%s SET productlines='%s' WHERE IEMI='%s';" % values
            iphone_info = CommonDao.change_option(self, sql)

            return iphone_info
        except:
            pass

    def transfer_line_table(self, from_table, to_table, IEMI):
        # 修改转出表
        result = self.change_line(from_table, IEMI, "0")
        # 修改转入表
        result = self.change_line(to_table, IEMI, "1")

        return result

    def change_line(self, table_name, IEMI, bool):
        try:
            sql = f"INSERT INTO trillion.{table_name} (IEMI, changetime, bool) VALUES ({IEMI}, CURRENT_TIMESTAMP, {bool})"
            results = CommonDao.change_option(self, sql)

            return results
        except:
            pass

    def check_transfer_sum_count(self, table_name, start_time, end_time):
        try:
            sql = f"SELECT COUNT(IEMI) FROM trillion.{table_name} WHERE bool='0' AND changetime BETWEEN  '{start_time}'  AND '{end_time}';"
            result = CommonDao.search_option(self, sql)

            return result
        except:
            pass



