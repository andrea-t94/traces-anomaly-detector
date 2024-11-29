import mariadb
import random

conn_params = {
    "user": "root",
    "password": "password",
    "host": "db",
    "port": 3306,
    "database": "performance_db"
}

def get_connection():
    try:
        conn = mariadb.connect(**conn_params)
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None

def insert_data():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO performance_table (data) VALUES (?)", (random.randint(1, 1000),))
            conn.commit()
        except mariadb.Error as e:
            print(f"Error writing to database: {e}")
        finally:
            conn.close()

def read_data():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT data FROM performance_table ORDER BY RAND() LIMIT 1")
            cursor.fetchall()
        except mariadb.Error as e:
            print(f"Error reading from database: {e}")
        finally:
            conn.close()
