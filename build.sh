#!/usr/bin/env bash
# Сборка и проверка проекта из командной строки (Git Bash):
#   bash build.sh
set -e
PY=${PYTHON:-python}

echo "=== 1. Сборка: компиляция всех модулей ==="
$PY -m py_compile input_module.py processing.py output.py main.py
echo "Ошибок компиляции нет"

echo
echo "=== 2. Интеграционное тестирование ==="
$PY -m unittest -v test_integration
