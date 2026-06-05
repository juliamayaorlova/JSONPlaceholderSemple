import requests

def test_get_posts():
    """Тест проверяет, что GET-запрос к /posts возвращает статус 200."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200

def test_post_data_structure():
    """Тест проверяет структуру данных в ответе от /posts/1."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    assert 'userId' in data
    assert 'id' in data
    assert 'title' in data
    assert 'body' in data

def test_post_title_contains_word():
    """Тест проверяет, что заголовок поста содержит слово."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    assert len(data['title']) > 0
