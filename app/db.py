import mariadb

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

def reset_database():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS performance_table")
            cursor.execute("CREATE TABLE performance_table (id INT AUTO_INCREMENT PRIMARY KEY, data INT)")
            conn.commit()
        except mariadb.Error as e:
            print(f"Error resetting database: {e}")
        finally:
            conn.close()
