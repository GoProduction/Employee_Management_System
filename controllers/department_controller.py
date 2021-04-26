from connection import connect_db
import cx_Oracle
from data.Classes.Department import Department


# get all departments
def get_departments():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM DEPARTMENT")

    for row in c:
        department = Department(row[0], row[1])
        list.append(department)
    # close connection
    conn.close()

    return list
