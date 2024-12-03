from services.cloud.db import init_db, insert_data, fetch_data

def store_data(data):
    """Stocke les données reçues."""
    insert_data(data["glucose_level"], data["status"])
    print("Données stockées :", data)

def get_history():
    """Récupère l'historique des données."""
    return fetch_data()

if __name__ == "__main__":
    init_db()
    print("Historique :", get_history())
