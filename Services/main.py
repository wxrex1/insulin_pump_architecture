from services.sensor.sensor import generate_sensor_data, send_data_to_receiver

if __name__ == "__main__":
    # Génération et envoi de données
    data = generate_sensor_data()
    print("Données générées :", data)
    send_data_to_receiver(data)
