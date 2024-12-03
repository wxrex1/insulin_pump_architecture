from src.sensor.sensor import send_data_to_receiver

if __name__ == "__main__":
    print("=== DÉMARRAGE DU SYSTÈME ===")
    print("Simulation des données depuis le capteur CGM...")

    # Simule l'envoi des données par le capteur
    send_data_to_receiver()

    print("=== SYSTÈME ARRÊTÉ ===")
