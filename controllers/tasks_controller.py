from connection import connect_db
import cx_Oracle
from data.Classes.Tasks import Tasks

# get all employees
def get_tasks():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM TASKS")

    for row in c:
        task = Tasks(row[0], row[1], row[2], row[3], row[4])
        list.append(task)

    # close connection
    conn.close()

    return list