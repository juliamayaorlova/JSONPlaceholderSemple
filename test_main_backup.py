import main
from io import StringIO
import sys

def test_main_prints_hello():
    """Тест проверяет, что функция main() выводит приветственное сообщение."""
    captured_output = StringIO()
    sys.stdout = captured_output
    main.main()
    sys.stdout = sys.__stdout__
    assert "Hello from main.py!" in captured_output.getvalue()

def test_main_exists():
    """Тест проверяет, что функция main() определена в модуле."""
    assert hasattr(main, 'main')
    assert callable(main.main)
