 # from irctc import Irctc
def create_table(cursor):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if cursor.fetchone() is None:
            cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT UNIQUE);""")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='questions'")
        if cursor.fetchone() is None:
            cursor.execute("""
                CREATE TABLE questions (
                    user_id INTEGER,
                    question TEXT,
                    answer TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (id));""")
    except Exception as e:
        print(f"Error creating tables: {e}")