import mysql.connector
from mysql.connector import cursor
import dbconfigs as cfg

class SuppliersDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql["host"],
            user= cfg.mysql["username"],
            password = cfg.mysql["password"],
            database = cfg.mysql["database"]
        )
        print ("connection made")

    def create(self, supplier):
        cursor = self.db.cursor()
        sql="insert into supplier (snr, name, country) values (%s, %s,%s)"
        values = [
            supplier['snr'],
            supplier['name'],
            supplier['country'],
            
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from supplier'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, snr):
        cursor = self.db.cursor()
        sql = 'select * from supplier where snr = %s'
        values = [ snr ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, supplier):
       cursor = self.db.cursor()
       sql = "update supplier set name = %s, country = %s where snr = %s"
       values = (
            supplier["name"],
            supplier["country"],
            supplier["snr"]
        )
       cursor.execute(sql, values)
       self.db.commit()
       cursor.close()
       return supplier
      
       

    def delete(self, snr):
       cursor = self.db.cursor()
       sql = 'delete from supplier where snr = %s'
       values = [snr]
       cursor.execute(sql, values)
       
       return {}


    def convertToDict(self, result):
        colnames = ["snr", "name", "country"]
        supplier = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                supplier[colName] = value
        return supplier

SuppliersDAO = SuppliersDAO()