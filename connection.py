import sys
from sys import platform
import os
import cx_Oracle


# connection properties for Oracle Cloud DB
db_username = "app_user"
db_password = "oY@@flS7kGRV"
db_connection_string = "tcps://adb.us-ashburn-1.oraclecloud.com:1522/sdxlk72ygu0rs6u_db202104011218_medium.adb.oraclecloud.com?wallet_location=network/wallet"

# for macOS users
if sys.platform.startswith("darwin"):
    cx_Oracle.init_oracle_client(lib_dir=r"/Users/francisbui/Desktop/instantclient_19_8")


# DB connector
def connect_db():
    try:
        conn = cx_Oracle.connect(db_username, db_password, db_connection_string)
        print('Successful connection')
        return conn
    except (RuntimeError, TypeError, NameError):
        print('Cannot connect to DB')

