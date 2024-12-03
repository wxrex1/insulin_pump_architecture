from src.cloud.db import init_db, insert_data, fetch_all_data
from src.platform.platform import process_and_redirect

def store_data(data):
    """Stocke les données dans le cloud et les redirige vers la plateforme."""
    insert_data(data["glucose_level"], data["status"])
    print(f"Données stockées dans le cloud : {data}")
    process_and_redirect(data)

if __name__ == "__main__":
    init_db()
