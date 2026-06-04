import requests

def test_get_users():
    """Тест проверяет, что GET-запрос к /users возвращает статус 200."""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    assert response.status_code == 200

def test_users_list_is_not_empty():
    """Тест проверяет, что список пользователей не пустой."""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    data = response.json()
    assert len(data) > 0

def test_user_data_structure():
    """Тест проверяет структуру данных пользователя."""
    response = requests.get('https://jsonplaceholder.typicode.com/users/1')
    data = response.json()
    assert 'id' in data
    assert 'name' in data
    assert 'username' in data
    assert 'email' in data
