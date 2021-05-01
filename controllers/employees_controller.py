from connection import connect_db
import cx_Oracle
from data.Classes.Employees import Employee
from data.Classes.EmployeeInfo import EmployeeInfo

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

# get all employees by only name and id; used for drop-down field
def get_employees_short():
    sql = "SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME FROM EMPLOYEES"
    list = []

    conn = connect_db()
    c = conn.cursor()
    c.execute(sql)

    for row in c:
        list.append(row)

    return list

# get a single employee
def get_employee(id):
    empid = int(id)
    emp_sql = """ SELECT * FROM EMPLOYEES WHERE EMPLOYEE_ID = :empid """
    info_sql = """ SELECT * FROM EMPLOYEE_INFO WHERE EMPLOYEE_ID = :empid """ 
    list = []

    conn = connect_db()
    c = conn.cursor()
    
    # execute query for employees table
    c.execute(emp_sql, [empid])
    for row in c:
        employee = Employee(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        list.append(employee)

    # execute query for employee info table
    c.execute(info_sql, [empid])
    for row in c:
        info = EmployeeInfo(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        list.append(info)

    # close connection
    conn.close()

    return list


# get max id
def get_latest_id():
    max_id_sql = "SELECT NVL(MAX(EMPLOYEE_ID), 0) AS MAX_ID FROM EMPLOYEES"
    conn = connect_db()
    c = conn.cursor()
    c.execute(max_id_sql)
    max_id = 0
    max = c.fetchone()

    for num in max:
        max_id = num

    #debug
    print("MaxID: ", max_id)
    return max_id


# add employee and employee info
def add_employee(data_list):
    emp_sql = """ INSERT INTO EMPLOYEES(DEPARTMENT_ID, FIRST_NAME, LAST_NAME, TITLE, PHONE, EMAIL)
                    VALUES(:depID, :f2ame, :l2ame, :title, :phone, :email)"""
    emp_info_sql = """ INSERT INTO EMPLOYEE_INFO(EMPLOYEE_ID, STREET_ADDRESS, CITY, STATE, ZIP_CODE, LICENSE_ID, SS_NUMBER)
                        VALUES(:empID, :address, :city, :state, :zipcode, :licenseID, :ssn)"""
    try:
        # since cx_Oracle does not support tuples, the properties need to be
            # instantiated separately. It's kind of ugly, but it is what it is...
        depID = int(data_list[0])
        title = str(data_list[1])
        fname = str(data_list[2])
        lname = str(data_list[3])
        phone = int(data_list[4])
        email = str(data_list[5])
        address = str(data_list[6])
        city = str(data_list[7])
        state = str(data_list[8])
        zip = int(data_list[9])
        licenseID = str(data_list[10])
        ssn = int(data_list[11])

        conn = connect_db()
        c = conn.cursor()
        
        # insert new Employee
        c.execute(emp_sql, [depID, fname, lname, title, phone, email])
        conn.commit()

        # get latest ID
        latest_empID = get_latest_id()

        # insert new EmployeeInfo
        c.execute(emp_info_sql, [latest_empID, address, city, state, zip, licenseID, ssn])
        conn.commit()

        conn.close()
    except (RuntimeError, TypeError, NameError):
        print("error on add_employee()")


# removes employee after providing employee id
def remove_employee(id):
    try:
        sql = """ DELETE FROM EMPLOYEES WHERE EMPLOYEE_ID = :id """
        conn = connect_db()
        c = conn.cursor()

        c.execute(sql, [id])
        conn.commit()
        conn.close()
        print("Removed employee with id: ", id)
    except (RuntimeError, TypeError, NameError):
        print("error on remove_employee()")

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