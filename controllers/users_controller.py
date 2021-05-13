from connection import connect_db
import cx_Oracle


def get_user(username, password):
    found_user = []
    sql = "select * from admin.users where user_name = :username and user_pass = :password"
    conn = connect_db()
    c = conn.cursor()

    c.execute(sql, [username, password])
    for row in c:
        found_user.append(row)

    if(found_user == []):
        return False
    else:
        print("User was found")
        return True