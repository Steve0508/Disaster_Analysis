import mysql.connector

# Database connection for auth
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='05102004pk',
    database='disaster'
)
cursor = conn.cursor()

def signup(username, password):
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        return False  # User already exists
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    return True

def login(username, password):
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    return cursor.fetchone() is not None
