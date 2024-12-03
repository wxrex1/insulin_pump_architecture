from services.cloud.cloud import init_db, store_data, fetch_data

def test_store_and_fetch_data():
    init_db()
    store_data({"glucose_level": 110, "status": "normal"})
    data = fetch_data()
    assert len(data) > 0
