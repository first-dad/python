# coding: utf-8
    
import sqlite3

def add_row(sqlite_file):
    
    sqlite_file = 'my_first_db.sqlite'
    id_first = 'my_table_id'
    id_second = 'my_1st_column'
    id_third = 'my_2nd_column'
    
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    
    try:
        c.execute("INSERT INTO products VALUES ({id}, '{Name}', {price})".\
            format(id = id_first, Name = id_second, price = id_third))
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_second))
    
    conn.commit()
    conn.close()