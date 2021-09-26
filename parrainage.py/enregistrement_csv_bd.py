import pandas as pd
import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="parrainage"
)

data = pd.read_csv("L1", sep=";")


mycursor = mydb.cursor()


sql = "INSERT INTO l1_new (matricule, nom, prenoms) VALUES (%s, %s, %s)"

for i in data.values:
    mycursor.execute(sql, tuple(i))


mydb.commit()

print(mycursor.rowcount, "record inserted.")
