from fastapi.testclient import TestClient

from main import app 

client = TestClient(app)


valid_payload = {
    "message": "This is a test",
    "to": "Juan Perez",
    "from": "Rita Asturia",
    "timeToLifeSec": 45
}


def test_missing_security_headers():
    response = client.post("/DevOps", json=valid_payload)
    assert response.status_code in [401, 403, 422]


def test_valid_request():

    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "token_falso_de_prueba" 
    }
    
    response = client.post("/DevOps", json=valid_payload, headers=headers)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}


def test_wrong_method():
    response = client.get("/DevOps")
    assert response.text == '"ERROR"' 