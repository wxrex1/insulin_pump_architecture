import sqlite3

DB_FILE = "cloud_data.db"

def init_db():
    """Initialise la base de données."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS glucose_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    glucose_level REAL,
                    status TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

def insert_data(glucose_level, status):
    """Insère des données dans la base de données."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO glucose_data (glucose_level, status) VALUES (?, ?)",
              (glucose_level, status))
    conn.commit()
    conn.close()

def fetch_data():
    """Récupère toutes les données de la base."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM glucose_data")
    rows = c.fetchall()
    conn.close()
    return rows
