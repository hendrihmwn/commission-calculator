from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_file():
    file_path = "frontend/public/sample_data.xlsx"
    
    # Open the file in binary mode
    with open(file_path, "rb") as f:
        # Provide the file for upload
        file = {"file": (file_path, f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        response = client.post("/read-file", files=file)
    
    assert response.status_code == 200

def test_read_file_invalid():
    invalid_file_content = b"dummy invalid file content"
    file = {"file": ("test.txt", invalid_file_content, "text/plain")}
    
    response = client.post("/read-file", files=file)
    
    assert response.status_code == 400

def test_calculate_incentives():
    response = client.post("/calculate-incentives", 
                           json=[{
                               "so": "123", 
                               "sp": "JAJA", 
                               "sm": "JIJI",
                               "gm": "JOJO",
                               "item": "yellow"
                               }])
    
    assert response.status_code == 200

def test_calculate_incentives_invalid():
    response = client.post("/calculate-incentives", 
                           json=[{
                               "so": "123", 
                               "sp": "JAJA", 
                               "sm": "JIJI",
                               "gm": "JOJO"
                               }])
    
    assert response.status_code == 422
    