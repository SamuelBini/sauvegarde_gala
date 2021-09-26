import mysql.connector
import random


r = 0.43

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="parrainage"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT label FROM l2_new")
l2 = mycursor.fetchall()

mycursor.execute("SELECT nom, prenoms FROM l1_new")
l1 = mycursor.fetchall()

mycursor.execute("SELECT nom, prenoms, niveau FROM presence_winter_night")
presents = mycursor.fetchall()


l2_n = []


for i in l2:
    h = i[0].split(" ")
    l2_n.append(tuple([h[0], i[0][i[0].index(" ") + 1:]]))


l1_pres = []
l2_pres = []


for i in presents:
    if i[2] == "L1":
        l1_pres.append(i)
    else:
        if i[2] == "L2":
            l2_pres.append(i)


random.shuffle(l1_pres)
random.shuffle(l2_pres)
random.shuffle(l2_n)


sql = "INSERT INTO new_parrainage (nom_l1, prenoms_l1, nom_l2, prenoms_l2) VALUES (%s, %s, %s, %s)"


for i in zip(l1_pres, l2_pres):
    h = [i[0][0], i[0][1], i[1][0], i[1][1]]
    mycursor.execute(sql, tuple(h))


if len(l1_pres) > len(l2_pres):
    for i in zip(l1_pres[len(l2_pres):], l2_n):
        h = [i[0][0], i[0][1], i[1][0], i[1][1]]
        mycursor.execute(sql, tuple(h))



mydb.commit()


print("LE PARRAINAGE A BEL ET BIEN ETE EFFECTUÉ")
