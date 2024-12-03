import random
import json

def generate_sensor_data():
    """Génère des données aléatoires de glucose."""
    glucose_level = random.uniform(50, 250)
    status = "normal"
    if glucose_level < 70:
        status = "hypoglycemia"
    elif glucose_level > 180:
        status = "hyperglycemia"
    return {
        "glucose_level": round(glucose_level, 2),
        "status": status
    }

def send_data_to_receiver(data):
    """Simule l'envoi de données au récepteur."""
    from services.receiver.receiver import process_data
    response = process_data(data)
    print("Réponse du récepteur :", response)

if __name__ == "__main__":
    data = generate_sensor_data()
    print("Données générées :", data)
    send_data_to_receiver(data)
