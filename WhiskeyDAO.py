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
        sql="insert into whiskey (name, distillery, age, price, country_id) values (%s, %s,%s, %s,%s)"
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

    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from whiskey where id = %s'
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, whiskey):
       cursor = self.db.cursor()
       sql = "update whiskey set name = %s, distillery = %s, age = %s, price=%s, country_id=%s where id = %s"
       values = [
            whiskey["id"],
            whiskey["name"],
            whiskey["distillery"],
            whiskey["age"],
            whiskey["price"],
            whiskey["country_id"]
       ]
       cursor.execute(sql, values)
       self.db.commit()
       return whiskey

    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'delete from books where id = %s'
       values = [id]
       cursor.execute(sql, values)
       
       return {}


    def convertToDict(self, result):
        colnames = ["id", "name", "distillery", "age", "price", "country_id"]
        whiskey = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                whiskey[colName] = value
        return whiskey

WhiskeyDAO = WhiskeyDAO()