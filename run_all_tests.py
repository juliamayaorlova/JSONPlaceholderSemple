#!/usr/bin/env python
"""Скрипт для запуска всех автотестов."""

import sys
import subprocess

def run_tests():
    """Запускает все тесты из папки JSONPlaceholder/test/."""
    print("Запуск автотестов...")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "JSONPlaceholder/test/", "-v"],
        cwd="d:/Julia/Omni/rumyant"
    )
    return result.returncode

if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)
