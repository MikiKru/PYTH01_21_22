# pip install pymysql
# pip install cryptography
import pymysql
from mysql_connector.data_model import DataModel
import datetime

class ConnectionConfig:
    def connection(self, user="pyth01_user", passwd="qwe123"):
        self.conn = pymysql.connect(host="localhost", user=user, password=passwd, db="pyth01")
        if(self.conn):
            print("...połączono z bazą danych...")
            self.cursor = self.conn.cursor()  # obiekt na którym wykonujemy polecenia native SQL
        else:
            print("błąd połączenia")
        return self.conn
    def insert_data_to_db(self, path):
        with open(path, "r", encoding="utf-8") as file:
            for i, row in enumerate(file.readlines()):
                if not i:
                    continue
                data = row.strip().replace('"', "").split(";")
                model = DataModel(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12])
                SQL = "INSERT INTO odczyty VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                self.cursor.execute(SQL, (model.meter_id, model.meter_object_id, model.cap_time, model.acq_time, model.flags, model.scale, model.unit, model.reason, model.value, model.user_id, model.data, model.dep_time, model.expression))
        self.conn.commit()
    def get_data_from_db(self):
        SQL = "select meter_id, cap_time, acq_time from odczyty"
        self.cursor.execute(SQL)
        result = self.cursor.fetchall()
        for row in result:
            print(f"{row[0]:50} | {row[1]:50} | {row[2]:50} |")
    def closeConnection(self):
        self.conn.close()
        print("...połączenie zakmniete...")


cc = ConnectionConfig()
cc.connection()
# cc.insert_data_to_db(r'export.dsv')
cc.get_data_from_db()


import time
unix_timestamp = 1636498800000
# local_time = time.localtime(unix_timestamp)
print(datetime.datetime.fromtimestamp(1636498800).strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime("%Y-%m-%d",local_time))