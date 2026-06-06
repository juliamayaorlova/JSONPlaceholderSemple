import requests

def test_get_todos():
    """Тест проверяет GET-запрос к /todos."""
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_get_albums():
    """Тест проверяет GET-запрос к /albums."""
    response = requests.get('https://jsonplaceholder.typicode.com/albums')
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

