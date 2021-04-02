from connection import connect_db
import cx_Oracle
from data.Classes.Employees import Employee

# get all employees
def get_employees():
    conn = connect_db()
    c = conn.cursor()
    list = []

    c.execute("SELECT * FROM EMPLOYEES")

    for row in c:
        employee = Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        list.append(employee)
    # close connection
    conn.close()

    return list

# get a single employee
def get_employee(id):
    return null
    ## TODO: select by id
