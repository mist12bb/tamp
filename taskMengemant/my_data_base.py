import pymysql
from datetime import datetime as date

coon = pymysql.connect(host = "localhost",
    user = "nac12",
    password = "EFFECTorAF%FECT54,504",
    db = "economy",
    cursorclass = pymysql.cursors.DictCursor)



cursor = coon.cursor()
SQL = "SELECT * FROM entering;"; cursor.execute(SQL);
entering_dict = cursor.fetchall()

def new_enterign(amount, ACK, from_ ,date_ = None):
    SQL = f"INSERT INTO entering(amount, ACK, froms, point_data) VALUES({amount}, {ACK}, '{from_}', '{date_}')"
    global cursor, coon
    cursor.execute(SQL);coon.commit()
    SQL = f"SELECT * FROM entering where amount = {amount}"
    return cursor.fetchall()

print(entering_dict)