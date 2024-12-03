from services.cloud.cloud import store_data

def process_data(data):
    """Traite les données reçues du capteur."""
    alert = "Glucose level normal."
    if data['status'] == 'hypoglycemia':
        alert = "ALERT: Low glucose level detected!"
    elif data['status'] == 'hyperglycemia':
        alert = "ALERT: High glucose level detected!"
    print(f"Traitement des données : {data}")
    store_data(data)
    return {"alert": alert}
