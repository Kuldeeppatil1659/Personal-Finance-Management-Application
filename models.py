import sqlite3

def create_connection():
    return sqlite3.connect('database/finance.db')

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            type TEXT CHECK(type IN ('income', 'expense')),
            category TEXT,
            date TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                month TEXT,
                year TEXT,
                category TEXT,
                amount REAL,
                FOREIGN KEY (user_id) REFERENCES users(id),
                UNIQUE(user_id, month, year, category)
            )
        ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
