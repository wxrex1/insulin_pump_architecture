# services/sensor/sensor.py

import random
import time
from .config import SensorConfig

class InsulinPumpSensor:
    def __init__(self, config: SensorConfig):
        self.config = config
        self.is_active = False

    def start(self):
        """Démarre le capteur."""
        self.is_active = True
        print("Capteur démarré.")

    def stop(self):
        """Arrête le capteur."""
        self.is_active = False
        print("Capteur arrêté.")

    def read_data(self):
        """Simule la lecture des données du capteur."""
        if not self.is_active:
            raise RuntimeError("Le capteur n'est pas actif.")
        
        glucose_level = random.uniform(self.config.min_glucose, self.config.max_glucose)
        return {"timestamp": time.time(), "glucose_level": glucose_level}
