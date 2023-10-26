import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)

def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def create_products(conn):
    create_product(conn, ('Albeni', 52.5, 10))
    create_product(conn, ('Lays', 140, 50))
    create_product(conn, ('Mojito', 80.5, 65))
    create_product(conn, ('RedBull', 110, 10))
    create_product(conn, ('Nitro', 65.4, 78))
    create_product(conn, ('Sandwich', 75, 15))
    create_product(conn, ('Flint', 40, 20))
    create_product(conn, ('Flovell', 90, 10))
    create_product(conn, ('Yokobaby', 495, 5))
    create_product(conn, ('Snickers', 50.5, 90))
    create_product(conn, ('Mars', 50.3, 90))
    create_product(conn, ('Bounty', 45.5, 90))
    create_product(conn, ('KitKat', 52.5, 60))
    create_product(conn, ('AlpenGold', 65.5, 100))
    create_product(conn, ('Raffaelo', 340.2, 36))

def update_product_quantity(conn, product: tuple):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def update_product_price(conn, product: tuple):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)

def delete_product_by_id(conn, id: int):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)

def print_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)

def print_all_products_by_price_and_quntity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.0 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)

def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)

connection = create_connection(db_name='Products.db')

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''
if connection is not None:
    # create_table(connection, create_products_table)
    # create_products(connection)
    update_product_quantity(connection, (47, 2))
    update_product_price(connection, (60, 1))
    delete_product_by_id(connection, (4))
    print_all_products(connection)
    print_all_products_by_price_and_quntity(connection)
    search_by_word(connection, ('Kit' or 'Alpen'))