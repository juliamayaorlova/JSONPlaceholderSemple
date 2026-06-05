import requests

def test_create_post():
    """Тест проверяет создание нового поста через POST-запрос."""
    payload = {
        'title': 'Тестовый пост',
        'body': 'Это тело тестового поста',
        'userId': 1
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data['title'] == 'Тестовый пост'

def test_update_post():
    """Тест проверяет обновление поста через PUT-запрос."""
    payload = {
        'id': 1,
        'title': 'Обновленный заголовок',
        'body': 'Обновленное тело',
        'userId': 1
    }
    response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'Обновленный заголовок'

def test_delete_post():
    """Тест проверяет удаление поста через DELETE-запрос."""
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
