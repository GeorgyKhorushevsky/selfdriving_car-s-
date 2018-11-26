from db_initializer import *
import sqlite3


class Database:
    def __init__(self, db=None):
        self.conn = None
        self.cursor = None

        if db:
            self.open(db)

    def open(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()

        except sqlite3.Error as error:
            print("Cannot connect to database.")

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = []
        rows = self.cursor.fetchall()
        for row in rows:
            if row[0] != 'sqlite_sequence':
                result.append(row[0])
        return result

    def get_table_columns(self, table):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM %s WHERE 1=0" % table)
        names = list(map(lambda x: x[0], cursor.description))
        return names

    def get_data(self, table):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM %s;" % table)

        rows = cursor.fetchall()
        result = []
        for row in rows:
            # print(row)
            result.append(row)
        return result

    def insert(self, table, columns, data):
        query = "INSERT INTO {0} ({1}) VALUES ({2});".format(table, columns, data)
        self.cursor.execute(query)

    def query(self, query):
        self.cursor.execute(query)

    def get_result(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)

        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row)
        return result
