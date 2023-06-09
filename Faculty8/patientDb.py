#patient database
import sqlite3

class Patient_Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS patient(
            id Integer Primary Key,
            name text,
            address text,
            birthday text,
            age text,
            contact text,
            martial text,
            height text, 
            weight text,
            pulse text,
            bodytemp text,
            home text,
            work text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, address, birthday, age, contact, martial, height, weight, pulse, bodytemp,home, work):
        self.cur.execute("INSERT into patient values (NULL,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (name, address , birthday , age, contact, martial, height, weight, pulse, bodytemp, home, work))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from patient")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from patient where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, address , birthday , age, contact, martial, height, weight, pulse, bodytemp):
        self.cur.execute(
            "update patient set name=?, address=?, birthday=?, age=?, contact=?, martial=?, heigth=?, weight=?, pulse=?, bodytemp=? where id=?",
            (name,address, birthday, age, contact, martial, height, weight, pulse, bodytemp, id))
        self.con.commit()


    def updateMeds(self, home, work):
        self.cur.execute( 
            "update patient set  home=?, work=? where id=?",
            (home, work, id))
        self.con.commit()
