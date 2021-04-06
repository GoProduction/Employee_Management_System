from connection import connect_db
import cx_Oracle
from data.Classes.EmployeeInfo import EmployeeInfo

# get all employee info
def get_info():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM EMPLOYEE_INFO")

    for row in c:
        info = EmployeeInfo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        list.append(info)

    # close connection
    conn.close()

    return list