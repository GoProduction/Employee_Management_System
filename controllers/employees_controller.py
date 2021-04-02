import connection
import cx_Oracle

def get_employees():
    c = connection.connect_db()
    list = []
    c.execute("SELECT * FROM EMPLOYEES")
    for row in c:
        list.append(row)
        print(row)
    
    return list