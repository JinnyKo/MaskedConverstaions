import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456789",
        database="masked_conversations"
    )
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(255),
        date VARCHAR(255),
        age INT,
        address VARCHAR(255),
        masked_text TEXT,
        encrypted_text TEXT
    )
    """)
    connection.commit()

def insert_data(connection, customer_name, date, age, address, masked_text, encrypted_text):
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO conversations (customer_name, date, age, address, masked_text, encrypted_text)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (customer_name, date, age, address, masked_text, encrypted_text))
    connection.commit()
