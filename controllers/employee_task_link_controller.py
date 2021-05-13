from connection import connect_db
import cx_Oracle
from data.Classes.EmployeeTaskLink import EmployeeTaskLink

# get all links
def get_link():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM ADMIN.EMPLOYEE_TASK_LINK")

    for row in c:
        link = EmployeeTaskLink(row[0], row[1], row[2])
        list.append(link)

    # close connection
    conn.close()

    return list
