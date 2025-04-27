# database.py
import sqlite3

class ExpenseDatabase:
    def __init__(self, db_name="expenses.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)
        self.connection.commit()

    def add_expense(self, name, amount):
        self.cursor.execute("""
            INSERT INTO expenses (name, amount) VALUES (?, ?)
        """, (name, amount))
        self.connection.commit()

    def get_all_expenses(self):
        self.cursor.execute("SELECT * FROM expenses")
        return self.cursor.fetchall()

    def get_total_amount(self):
        self.cursor.execute("SELECT SUM(amount) FROM expenses")
        result = self.cursor.fetchone()[0]
        return result if result is not None else 0

    def close(self):
        self.connection.close()
        
