import sqlite3

loc="C:\\Users\\Mehmet.BOLD\\Desktop\\BOQ\\familydb.sqlite3"

con = sqlite3.connect(loc)
cursor = con.cursor()

def get_category():
    cursor.execute("SELECT * FROM category")
    data = cursor.fetchall()
    return data

def get_material():
    cursor.execute("SELECT * FROM material")
    data = cursor.fetchall()
    return data