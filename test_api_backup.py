import requests

def test_get_posts():
    """Тест проверяет, что GET-запрос к /posts возвращает статус 200."""
    print("\n=== Test: test_get_posts ===")
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200

def test_post_data_structure():
    """Тест проверяет структуру данных в ответе от /posts/1."""
    print("\n=== Test: test_post_data_structure ===")
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    print(f"Response JSON: {data}")
    assert 'userId' in data
    assert 'id' in data
    assert 'title' in data
    assert 'body' in data

def test_post_title_contains_word():
    """Тест проверяет, что заголовок поста содержит слово."""
    print("\n=== Test: test_post_title_contains_word ===")
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}")
    assert len(data['title']) > 0
