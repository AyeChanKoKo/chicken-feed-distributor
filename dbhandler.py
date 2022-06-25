#   This class is for the database connection and
#   CRUD operations.
#   Class's function should be called with 2 parameters:
#   "table_name" and " VALUES"
#    Author : "Ayechan Koko"

import mysql.connector as db
dbc = ("localhost", "root", "G0dM0d3", "sales")


class DataHandler:
    connection = None
    cursor = None

    # Initializing the Database connection and cursor
    def __init__(self):
        if DataHandler.connection is None:
            try:
                DataHandler.connection = db.connect(host="127.0.0.1", user="root", password="G0dM0d3",
                                                    database="sales")
                DataHandler.cursor = DataHandler.connection.cursor()
            except Exception as error:
                print("Error: Connection not established {}".format(error))
            else:
                print("Connection established")

        self.connection = DataHandler.connection
        self.cursor = DataHandler.cursor

    def query(self, entity):
        sql = "SELECT * FROM " + entity + " ;"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
        self.connection.commit()

    def specific_select(self, entity, tgt):
        sql = "SELECT DISTINCT "+tgt+" FROM " + entity + " ;"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
        self.connection.commit()

    def insert(self, entity, val):
        select = selection(entity)
        print(entity)
        print(select)
        target = select.count(",")
        counter = ""
        i = 0
        while i < (target+1):
            if i == target:
                counter = counter+"%s"
            else:
                counter = counter+"%s, "
            i += 1
        counter = " VALUES (" + counter + ")"
        sql = "INSERT INTO " + entity + " " + select + counter
        self.cursor.execute(sql, val)
        cid = self.cursor.lastrowid
        self.connection.commit()
        return cid
        # print(self.cursor.rowcount, " record inserted")

    def update(self, tgt, val):
        sql = "UPDATE " + tgt + "(name, phone, address) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, val)
        self.connection.commit()

    def show_all(self):
        sql = "show tables"
        self.cursor.execute(sql)
        self.connection.commit()



def selection(tgt):
    mapping = {"voucher": "(item_id, sale_id, t_charge", "customer": "(name, phone, address)",
               "items": "(item_name, item_type)","feed":"(item_id, code, price, package)",
               "med": "(item_id, package, price)", "imp_voucher":"(date)"}
    select = mapping.get(tgt)
    return select


if __name__ == '__main__':
    db = DataHandler()
    table = "customer"
    values = ("ခင်မောင်ထူး", "0943012445", "မရမ်းခုံ")
    db.insert(table, values)
    ans = db.query(table)
    for row in ans:
        print(row)