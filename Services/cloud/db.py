import sqlite3

DB_FILE = "cloud_data.db"  # Nom du fichier de la base de données

def init_db():
    """
    Initialise la base de données SQLite.
    Crée la table 'glucose_data' si elle n'existe pas.
    """
    conn = sqlite3.connect(DB_FILE)  # Connexion à la base de données
    c = conn.cursor()
    # Création de la table
    c.execute('''
        CREATE TABLE IF NOT EXISTS glucose_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            glucose_level REAL,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()  # Sauvegarde les modifications
    conn.close()  # Ferme la connexion


def insert_data(glucose_level, status):
    """
    Insère un enregistrement dans la table 'glucose_data'.

    :param glucose_level: Niveau de glucose (float)
    :param status: État du glucose (str : 'normal', 'hypoglycemia', 'hyperglycemia')
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO glucose_data (glucose_level, status)
        VALUES (?, ?)
    ''', (glucose_level, status))
    conn.commit()
    conn.close()


def fetch_all_data():
    """
    Récupère tous les enregistrements de la table 'glucose_data'.

    :return: Liste des enregistrements sous forme de tuples.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM glucose_data')
    rows = c.fetchall()
    conn.close()
    return rows


def fetch_data_by_status(status):
    """
    Récupère les enregistrements correspondant à un statut donné.

    :param status: Statut à filtrer (str : 'normal', 'hypoglycemia', 'hyperglycemia')
    :return: Liste des enregistrements sous forme de tuples.
    """
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM glucose_data WHERE status = ?', (status,))
    rows = c.fetchall()
    conn.close()
    return rows
