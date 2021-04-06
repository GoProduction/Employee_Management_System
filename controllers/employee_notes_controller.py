from connection import connect_db
import cx_Oracle
from data.Classes.EmployeeNotes import EmployeeNotes

# get all employee notes
def get_notes():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM EMPLOYEE_NOTES")

    for row in c:
        note = EmployeeNotes(row[0], row[1], row[2], row[3])
        list.append(note)

    # close connection
    conn.close()

    return list
