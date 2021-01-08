
import sqlite3



loc="C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\familydb.sqlite3"

con = sqlite3.connect(loc)
cursor = con.cursor()

def ekle(codes,material_name):

    cursor.execute("INSERT INTO material (codes,material_name) VALUES(?,?)",(codes,material_name))
    con.commit()

def deger_al():
    cursor.execute("SELECT * FROM category")
    data = cursor.fetchall()
    print(data)


deger_al()

catlist=[]

"""
for v,i in enumerate(catlist):
    ekle(v+1,i)"""
