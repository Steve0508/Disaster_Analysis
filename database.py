import mysql.connector

def get_connection():
    try:
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='05102004pk',
            database='disaster'
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_user(username, password):
    db = get_connection()
    if db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        cursor.close()
        db.close()

def validate_user(username, password):
    db = get_connection()
    if db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        db.close()
        return user
    return None

def get_all_table_names():
    db = get_connection()
    if db:
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        cursor.close()
        db.close()
        return [table[0] for table in tables]
    return []
