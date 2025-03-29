import pytest
from fastapi.testclient import TestClient
from main import app #This comes from main.py


import io 
from PIL import Image 

client = TestClient(app)

def create_test_image():
    img = Image.new("RGB", (100, 50), color=(255, 255, 255))  # Create a white image
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)
    return img_byte_array


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI with Groq and Tesseract is running!"}

    

def test_extract_txt():
    img_data = cv2.imread('/home/jabuan/BlasterHacks/blaster25-backend/src/test-images/test.png')
    
    files = {"file": ("test_image.png", img_data, "image/png")}
    response = client.post("/extract-text/", files = files)

    assert response.status_code == 200
    assert "extracted_text" in response.json()

