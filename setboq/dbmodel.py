import sqlite3

loc = "C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\familydb.sqlite3"
loc2 = "C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\db.sqlite3"

con = sqlite3.connect(loc)
cursor = con.cursor()

con2 = sqlite3.connect(loc2)
cursor2 = con2.cursor()

def get_category():
    cursor.execute("SELECT * FROM category")
    data = cursor.fetchall()
    return data

def get_material():
    cursor.execute("SELECT * FROM material")
    data = cursor.fetchall()
    return data

def get_all_from_db():
    cursor2.execute("SELECT * FROM setboq_setboq")
    data = cursor2.fetchall()
    return data
