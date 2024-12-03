from services.sensor.sensor import generate_sensor_data

def test_generate_sensor_data():
    data = generate_sensor_data()
    assert "glucose_level" in data
    assert "status" in data
    assert data["glucose_level"] >= 0
