import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 5  # seconds

def test_predict_get():
    response = requests.get(f"{BASE_URL}/predict", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert "y_pred" in data
    assert isinstance(data["y_pred"], (int, float))


def test_predict_post():
    payload = {
        "size": 100,
        "nb_rooms": 3,
        "garden": 1
    }
    response = requests.post(f"{BASE_URL}/predict", json=payload, timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert "y_pred" in data
    assert isinstance(data["y_pred"], (int, float))


if __name__ == "__main__":
    print("---------- Running tests ----------")
    print("Testing /predict GET endpoint 🕚")
    test_predict_get()
    print("Testing /predict POST endpoint 🕚")
    test_predict_post()
    print("All tests passed ✅")
