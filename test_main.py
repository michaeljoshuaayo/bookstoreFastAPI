from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_welcome_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Bookstore API!"}

def test_create_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Tester"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Tester"
    assert "id" in data

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book_by_id():
    book = client.post("/books/", json={"title": "Single", "author": "Author"}).json()
    book_id = book["id"]
    
    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == "Single"
