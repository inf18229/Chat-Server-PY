import sqlite3
class SQLServer:
    def __init__(self):
        self.userDB_Connection = sqlite3.connect("db/User.db")
        self.userDB_Cursor = self.userDB_Connection.cursor()
        # Create Basic Tables in SQL Database
        self.userDB_Cursor.execute("""
        SELECT count(name)
        FROM sqlite_master
        WHERE type='table' AND name='users'
        """)
        if self.userDB_Cursor.fetchall()[0]!=0:

            sql_CreateTables = """
                CREATE TABLE users (
                UName VARCHAR(20),
                Vorname VARCHAR(20),
                NACHNAME VARCHAR(20),
                PASSWORD VARCHAR(64)
                );"""
            self.userDB_Cursor.execute(sql_CreateTables)
            self.userDB_Connection.commit()
        self.userDB_Connection.close()
    def createUserinDB(self, userName, vName,nName,password):
        DB_con = sqlite3.connect("db/User.db")
        DB_curs = DB_con.cursor()
        DB_curs.execute("""
        INSERT INTO users 
                VALUES (?,?,?,?)
        """,
        (userName, vName, nName,password))
        DB_con.commit()
        DB_con.close()
    def getallUsers(self):
        DB_con = sqlite3.connect("db/User.db")
        DB_curs = DB_con.cursor()
        DB_curs.execute("""
        SELECT UName, NACHNAME, PASSWORD
        FROM users
        """)
        print(DB_curs.fetchall())
        DB_con.close()
    def getUserName(self,userName):
        DB_con = sqlite3.connect("db/User.db")
        DB_curs = DB_con.cursor()
        DB_curs.execute("""
        SELECT Vorname, NACHNAME
        FROM users
        WHERE UName = (?)
        """,
        (userName,))
        print(DB_curs.fetchall())
        DB_con.close()
    def closeConnection(self):
        #Only for destruction
        self.userDB_Connection.close()