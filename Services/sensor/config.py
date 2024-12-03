# services/sensor/config.py

class SensorConfig:
    def __init__(self, min_glucose=70, max_glucose=180, read_interval=5):
        self.min_glucose = min_glucose  # Niveau de glucose minimum simulé
        self.max_glucose = max_glucose  # Niveau de glucose maximum simulé
        self.read_interval = read_interval  # Intervalle de lecture en secondes
