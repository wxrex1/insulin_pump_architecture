from services.receiver.receiver import process_data

def test_process_data():
    data = {"glucose_level": 90, "status": "normal"}
    response = process_data(data)
    assert "alert" in response
    assert response["alert"] == "Glucose level normal."
