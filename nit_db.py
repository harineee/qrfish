import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """ Create a table for storing product information """
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                product_name TEXT NOT NULL,
                                packaging_date TEXT,
                                expiration_date TEXT,
                                batch_number TEXT,
                                supplier_info TEXT,
                                calories INTEGER,
                                protein INTEGER,
                                fat INTEGER,
                                ingredients TEXT,
                                allergens TEXT,
                                dietary_suitability TEXT,
                                certifications TEXT,
                                origin_info TEXT,
                                processing_history TEXT,
                                spoilage_indicator TEXT
                              );"""
        conn.execute(sql_create_table)
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection('database.db')
    if conn:
        create_table(conn)
