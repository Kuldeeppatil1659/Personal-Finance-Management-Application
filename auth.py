import sqlite3
from models import create_connection
from utils import hash_password, verify_password

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    hashed_password = hash_password(password)
    
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Try again.")
    
    conn.close()

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    if result:
        user_id = result[0]  
        stored_password = result[1]
        
        if verify_password(password, stored_password):
            print("Login successful!")
            return user_id  
        else:
            print("Invalid password.")
            return None
    else:
        print("User not found.")
        return None
    
    conn.close()