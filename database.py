import sqlite3

def init_db():
    conn = sqlite3.connect("economic_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS indicators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT,
            indicator TEXT,
            year INTEGER,
            value REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_data(country, indicator, year, value):
    conn = sqlite3.connect("economic_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO indicators (country, indicator, year, value)
        VALUES (?, ?, ?, ?)
    """, (country, indicator, year, value))
    conn.commit()
    conn.close()

def get_data(country, indicator):
    conn = sqlite3.connect("economic_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT year, value FROM indicators
        WHERE country = ? AND indicator = ?
        ORDER BY year ASC
    """, (country, indicator))
    rows = cursor.fetchall()
    conn.close()
    return rows