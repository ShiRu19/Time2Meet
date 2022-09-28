import pymysql
import json

class SQL:
    def __init__(self):
        self.connection = None

    def conn(self):
        self.connection = pymysql.connect(host="127.0.0.1", user="SIRU", password="asdfjkl", db="Time2Meet")
        print("Connection succeeded.")

    def select(self, data):
        cursor = self.connection.cursor()

        sql = "SELECT * FROM PROJECT WHERE PROJECT_NAME = %s AND USER_NAME = %s"
        cursor.execute(sql, (data["project"], data["userName"]))
        result = cursor.rowcount

        cursor.close()
        self.connection.commit()

        return result

    def insert(self, insertData):
        if(type(insertData)!=dict):
            insertData = json.loads(insertData)
        
        cursor = self.connection.cursor()
        sql = "INSERT INTO PROJECT VALUES (%s, %s, %s)"
        #print(insertData['project'] + " " + insertData['userName'] + " " +insertData['userTime'])
        #cursor.execute(sql, ("test1", "user1", "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"))
        cursor.execute(sql, (insertData["project"], insertData["userName"], insertData["userTime"]))
        print("Insertion secceeded.")

        cursor.close()
        self.connection.commit()

    def update(self, data):
        if(type(data) != dict):
            data = json.loads(data)

        cursor = self.connection.cursor()
        sql = "UPDATE `PROJECT` SET `USER_TIME`=%s WHERE `PROJECT_NAME`=%s AND `USER_NAME`=%s"
        cursor.execute(sql, (data['userTime'], data['project'], data['userName']))
        print("Update secceeded.")

        cursor.close()
        self.connection.commit()