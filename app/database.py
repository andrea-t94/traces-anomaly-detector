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
    """Insert initial data into the database during boot."""
    conn = get_connection()
    cursor = conn.cursor()
    for i in range(1, 101):  # Insert 100 rows
        cursor.execute("INSERT INTO performance_table (data) VALUES (%s)", (f"Sample Data {i}",))
    conn.commit()
    cursor.close()
    conn.close()

def read_data():
    """Fetch a random record from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM performance_table")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
