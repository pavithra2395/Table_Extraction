import requests
import json
import cx_Oracle

def main():

    try:
        # con = cx_Oracle.connect("COROTF_DEV/COROTF_DEV@IBSorcl/122.166.157.90")
        dsn = cx_Oracle.makedsn(host='122.166.157.90', port=1521, sid='IBSorcl')
        con = cx_Oracle.connect(user="ACCORD", password="ACCORD",
                                dsn= dsn,
                                encoding="UTF-8")
        # print(con)
        # con.close()

    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database:', er)

    else:
        pass

    try:
        cur = con.cursor()
        table ="AIFStmtMaster"
        sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table)
            # valid in Python 3
        r=cur.execute(sql, list())



    except cx_Oracle.DatabaseError as er:
        print('There is an error in Oracle database 2:', er)

    except Exception as er:
        print(er)

    else:
        con.commit()
        print('Multiple records are inserted successfully')