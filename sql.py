import sqlite3

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except sqlite3.Error as e:
       print(e)
   return conn

def create_tables(conn):
    """
    Create contacts and present tables
    :param conn: Connection object
    :return:
    """
    contacts_table = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            mail TEXT NOT NULL
        );
    """

    present_table = """
        CREATE TABLE IF NOT EXISTS present (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            preferences TEXT NOT NULL,
            FOREIGN KEY (contact_id) REFERENCES contacts (id)
        );
    """

    try:
        c = conn.cursor()
        c.execute(contacts_table)
        c.execute(present_table)
    except sqlite3.Error as e:
        print(e)

def add_contact(conn, contact):
   """
   Create a new contact into the contacts table
   :param conn:
   :param contact:
   :return: contact id
   """
   sql = '''INSERT INTO contacts(name, phone, mail)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, contact)
   conn.commit()
   return cur.lastrowid

def add_present(conn, present):
   """
   Create a new present into the present table
   :param conn:
   :param present:
   :return: present id
   """
   sql = '''INSERT INTO present(contact_id, name, birthday, preferences)
         VALUES(?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, present)
   conn.commit()
   return cur.lastrowid

contact = ('Mother','095632563','mama@gmail.com')
contact = ('Dad', '0366955454','tato@gmail.com')

conn = create_connection("database.db")
create_tables(conn)

pr_id = add_contact(conn, contact)
present = (
    pr_id,
    'Mother',
    '20.09.1974',
    'flowers'
)

pr_id = add_contact(conn, contact)
present = (
    pr_id,
    'Dad',
    '19.02.1975',
    'cars'
)
present_id = add_present(conn, present)
print(pr_id, present_id)
conn.close()
