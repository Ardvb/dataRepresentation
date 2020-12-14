import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg

class WhiskeyDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect( #Connect the database
            host = cfg.mysql["host"],
            user= cfg.mysql["username"],
            password = cfg.mysql["password"],
            database = cfg.mysql["database"]
        )
        print ("connection made") #Just to check it is working

    def create(self, whiskey): #Create a new whiskey
        cursor = self.db.cursor()
        sql="insert into whiskey (codenr, name, country, age, price) values (%s, %s,%s, %s,%s)"
        values = [
            whiskey['codenr'],
            whiskey['name'],
            whiskey['country'],
            whiskey['age'],
            whiskey['price'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

    def getAll(self): # Show info of all whiskeys
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

    def findById(self, codenr): # Find a whiskey by entered the codenr
        cursor = self.db.cursor()
        sql = 'select * from whiskey where codenr = %s'
        values = [ codenr ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, whiskey): # Update info of certain whiskey with selected codenr
       cursor = self.db.cursor()
       sql = "update whiskey set name = %s, country = %s, age = %s, price = %s where codenr = %s"
       values = (
            whiskey["name"],
            whiskey["country"],
            whiskey["age"],
            whiskey["price"],
            whiskey["codenr"]
        )
       cursor.execute(sql, values)
       self.db.commit()
       cursor.close()
       return whiskey
      
       

    def delete(self, codenr): # Delete whiskey with selected codenr
       cursor = self.db.cursor()
       sql = 'delete from whiskey where codenr = %s'
       values = [codenr]
       cursor.execute(sql, values)
       
       return {}


    def convertToDict(self, result): # convert whiskey into JSON dictionary
        colnames = ["codenr", "name", "country", "age", "price"]
        whiskey = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                whiskey[colName] = value
        return whiskey

WhiskeyDAO = WhiskeyDAO()