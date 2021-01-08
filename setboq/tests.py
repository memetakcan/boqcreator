
import sqlite3
liste=[]




loc = "C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\familydb.sqlite3"
loc2 = "C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\db.sqlite3"

con = sqlite3.connect(loc)
cursor = con.cursor()

con2 = sqlite3.connect(loc2)
cursor2 = con2.cursor()

"""
def ekle(codes,material_name):

    cursor.execute("INSERT INTO material (material_name) VALUES(?,?)",(material_name))
    con.commit()

def deger_al():
    cursor.execute("SELECT * FROM material")
    data = cursor.fetchall()
    for i in data:
        liste.append(i[0]+":"+i[1])




deger_al()
print(liste)

catlist=[]


for v,i in enumerate(catlist):
    ekle(i)"""


def get_all_from_db():
    cursor2.execute("SELECT * FROM setboq_setboq")
    data = cursor2.fetchall()
    return data

for i in get_all_from_db():
    print(i[5])
