"""Главный модуль (участник А).

ЛР 5, вариант 6. Связывает модули ввода, обработки и вывода.
"""
import sys

from input_module import read_matrix
from processing import find_good_rows
from output import print_matrix, print_result, print_no_rows


def setup_console():
    """Русский текст и мгновенный вывод в Git Bash, cmd и PyCharm."""
    try:
        sys.stdin.reconfigure(encoding="utf-8")
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    except (AttributeError, ValueError):
        pass


def main():
    setup_console()
    print("ЛР 5, вариант 6: строки с чередующейся чётностью элементов")

    try:
        matrix_a = read_matrix("A")
        matrix_b = read_matrix("B")
    except EOFError:
        print("\nОшибка: ввод прерван, данные не получены.")
        return 1

    print_matrix("A", matrix_a)
    print_matrix("B", matrix_b)

    rows_a = find_good_rows(matrix_a)
    rows_b = find_good_rows(matrix_b)

    print("\nРезультат:")
    print_result("A", rows_a)
    print_result("B", rows_b)
    if not rows_a and not rows_b:
        print_no_rows()
    return 0


if __name__ == "__main__":
    sys.exit(main())
