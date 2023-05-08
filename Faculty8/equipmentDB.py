#equipment database
import sqlite3


class Equipment_Database:
    def __init__(self, equipment_db):
        self.con = sqlite3.connect(equipment_db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS equip(
            id Integer Primary Key,
            name text,
            quantity Interger
        )
        """

        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, quantity):
        self.cur.execute("INSERT into equip values (NULL,?,?)",
                         (name, quantity))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from equip")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("DELETE from equip where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, quantity):
        self.cur.execute(
            "UPDATE equip set name=?, quantity=? where id=?",
            (name, quantity, id))
        self.con.commit()
