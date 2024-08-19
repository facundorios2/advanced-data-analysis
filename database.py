import mysql.connector

class DatabaseConnect():
    def __init__(self, host, name,password, database):
        self.host = host
        self.name = name
        self.password = password
        self.database = database

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.name,
            password=self.password,
            database=self.database
        )

    def close(self):
        self.conn.close()
    