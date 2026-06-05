import requests

def test_get_comments_by_post():
    """Тест проверяет получение комментариев к посту."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_get_comments_structure():
    """Тест проверяет структуру комментариев."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
    data = response.json()
    comment = data[0]
    assert 'postId' in comment
    assert 'id' in comment
    assert 'name' in comment
    assert 'email' in comment
    assert 'body' in comment
