import mysql.connector
class GameDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
        host="StephenCaulfield.mysql.pythonanywhere-services.com",
        user="StephenCaulfield",
        password="DataRep2022",
        database="StephenCaulfield$datarepresentation"
        )


    def create(self, values):
        cursor = self.db.cursor()
        sql="INSERT INTO Games (name, platform, developer, publisher, price) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="SELECT * FROM Games"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="SELECT * FROM Games WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="UPDATE Games SET name= %s,platform=%s,developer=%s,publisher=%s,price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql="DELETE FROM Games WHERE id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("Deleted")

    def convertToDictionary(self, result):
        colnames=['id','Name','Platform',"Developer","Publisher","Price"]
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

GameDAO = GameDAO()