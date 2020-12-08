import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class WhiskeyDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql["host"],
            user= cfg.mysql["username"],
            password = cfg.mysql["password"],
            database = cfg.mysql["database"]
        )
        print ("connection made")

    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into whiskey (codenr, name, country, age, price) values (%s, %s,%s, %s,%s)"
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from whiskey'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, codenr):
        cursor = self.db.cursor()
        sql = 'select * from whiskey where codenr = %s'
        values = [ codenr ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, whiskey):
       cursor = self.db.cursor()
       sql = "update whiskey set codenr = %s, name = %s, country = %s, age = %s, price = %s where codenr = %s"
       values = [
            whiskey["codenr"],
            whiskey["name"],
            whiskey["country"],
            whiskey["age"],
            whiskey["price"],
            
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return whiskey

    def delete(self, codenr):
       cursor = self.db.cursor()
       sql = 'delete from whiskey where codenr = %s'
       values = [codenr]
       cursor.execute(sql, values)
       
       return {}


    def convertToDict(self, result):
        colnames = ["codenr", "name", "country", "age", "price"]
        whiskey = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                whiskey[colName] = value
        return whiskey

WhiskeyDAO = WhiskeyDAO()