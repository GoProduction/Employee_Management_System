from connection import connect_db
import cx_Oracle
from data.Classes.Status import Status

# get all status'
def get_status():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM ADMIN.STATUS")

    for row in c:
        status = Status(row[0], row[1])
        list.append(status)

    # close connection
    conn.close()

    return list