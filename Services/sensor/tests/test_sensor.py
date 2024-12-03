# services/sensor/tests/test_sensor.py

import unittest
from services.sensor.sensor import InsulinPumpSensor
from services.sensor.config import SensorConfig

class TestInsulinPumpSensor(unittest.TestCase):
    def setUp(self):
        self.config = SensorConfig(min_glucose=80, max_glucose=150)
        self.sensor = InsulinPumpSensor(self.config)

    def test_sensor_initialization(self):
        self.assertFalse(self.sensor.is_active)

    def test_start_stop_sensor(self):
        self.sensor.start()
        self.assertTrue(self.sensor.is_active)
        self.sensor.stop()
        self.assertFalse(self.sensor.is_active)

    def test_read_data_active_sensor(self):
        self.sensor.start()
        data = self.sensor.read_data()
        self.assertIn("glucose_level", data)
        self.assertGreaterEqual(data["glucose_level"], self.config.min_glucose)
        self.assertLessEqual(data["glucose_level"], self.config.max_glucose)

    def test_read_data_inactive_sensor(self):
        with self.assertRaises(RuntimeError):
            self.sensor.read_data()

if __name__ == "__main__":
    unittest.main()
