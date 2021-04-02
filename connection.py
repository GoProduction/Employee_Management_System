import os
import cx_Oracle

# connection properties for Oracle Cloud DB
db_username = "ADMIN"
db_password = "nb9QRpFzHEQgbV3"
db_connection_string = "tcps://adb.us-ashburn-1.oraclecloud.com:1522/sdxlk72ygu0rs6u_db202104011218_medium.adb.oraclecloud.com?wallet_location=network/wallet"
    
# DB connector
def connect_db():
        conn = cx_Oracle.connect(db_username, db_password, db_connection_string)
        c = conn.cursor()
        print('Successful connection')
        c.execute("SELECT * FROM EMPLOYEES")

        # test code to make sure this shit works
        for row in c:
            print('Employee First Name: ', row[2], 'Employee Last Name: ', row[3])
        conn.close()


