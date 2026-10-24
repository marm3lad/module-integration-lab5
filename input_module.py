"""Модуль ввода данных (участник А).

Ввод двумерного массива целых чисел с клавиатуры
и проверка размеров (не более 10x10).
"""

MAX_SIZE = 10


def read_size(prompt):
    """Ввод размера массива от 1 до MAX_SIZE с повтором при ошибке."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        if 1 <= value <= MAX_SIZE:
            return value
        print(f"Ошибка: размер должен быть от 1 до {MAX_SIZE}.")


def read_row(number, cols):
    """Ввод одной строки массива: ровно cols целых чисел через пробел."""
    while True:
        parts = input(f"  Строка {number}: ").split()
        if len(parts) != cols:
            print(f"Ошибка: нужно ровно {cols} чисел через пробел.")
            continue
        try:
            return [int(p) for p in parts]
        except ValueError:
            print("Ошибка: элементы должны быть целыми числами.")


def read_matrix(name):
    """Ввод массива с именем name. Возвращает список строк."""
    print(f"\nВвод массива {name}")
    rows = read_size("Количество строк (1-10): ")
    cols = read_size("Количество столбцов (1-10): ")
    print(f"Введите {rows} строк(и) по {cols} целых чисел через пробел:")
    return [read_row(i, cols) for i in range(1, rows + 1)]
