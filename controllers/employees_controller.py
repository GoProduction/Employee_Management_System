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


# get max id
def get_latest_id():
    max_id_sql = "SELECT NVL(MAX(EMPLOYEE_ID), 0) AS MAX_ID FROM EMPLOYEES"
    conn = connect_db()
    c = conn.cursor()
    max_id = c.execute(max_id_sql)

    return max_id


# add employee and employee info
def add_employee(self, employee, info):
    emp_sql = """ INSERT INTO EMPLOYEES(DEPARTMENT_ID, FIRST_NAME, LAST_NAME, TITLE, PHONE, EMAIL)
                    VALUES(:deptID, :fName, :lName, :title, :phone, :email)"""
    emp_info_sql = """ INSERT INTO EMPLOYEE_INFO(EMPLOYEE_ID, STREET_ADDRESS, CITY, STATE, ZIP_CODE, LICENSE_ID, SS_NUMBER)
                        VALUES(:empID, :address, :city, :state, :zipcode, :licenseID, :ssn)"""
    try:
        conn = connect_db()
        c = conn.cursor()
    
        c.execute(emp_sql, [employee.deptID, employee.fName, employee.lName, 
                        employee.title, employee.phone, employee.email])

        c.execute(emp_info_sql, [info.empID, info.address, info.city, 
                             info.state, info.zipcode, info.licenseID, info.ssn])

        conn.close()
    except ValueError:
        print("Value error on add_employee()")


# check for email
def email_is_taken(email):
    found_email = []
    sql = "SELECT NVL(EMAIL, 'empty') AS EMAIL FROM EMPLOYEES WHERE EMAIL = :email"

    conn = connect_db()
    c = conn.cursor()

    c.execute(sql, [email])
    for row in c:
        print("Row: ", row)
        found_email.append(row)

    if (found_email == []):
        print("Provided email is open")
        return False
    else:
        return True