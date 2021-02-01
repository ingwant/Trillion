from db.common_dao import CommonDao


class ProductSearchDao:

    def get_iphone_info(self, table_name, IEMI):
        try:
            sql = "SELECT istorage, color, company, intime, productlines, remarks, grade, outtime, bstorage, selller, tocompany FROM trillion.%s WHERE IEMI=%s;" % (table_name, IEMI)
            iphone_info = CommonDao.search_option(self, sql)

            return iphone_info
        except:
            pass

    def insert_data(self, values):
        try:
            sql = "INSERT INTO trillion.%s (IEMI, istorage, color, intime, company, productlines, bstorage, remarks)  VALUES ('%s','%s','%s',CURRENT_TIMESTAMP,'%s','%s','%s','%s');" % values
            results = CommonDao.change_option(self, sql)

            return results
        except:
            pass

    def change_data(self, values):
        try:
            sql = "UPDATE trillion.%s SET istorage='%s', color='%s', intime=CURRENT_TIMESTAMP, company='%s', productlines='%s', bstorage='%s', remarks='%s' WHERE IEMI='%s';" % values
            results = CommonDao.change_option(self, sql)

            return results
        except:
            pass

    def delete_data(self, values):
        try:
            sql = "DELETE FROM trillion.%s WHERE IEMI='%s';" % values
            results = CommonDao.change_option(self, sql)

            return results
        except:
            pass
