"""Модуль обработки (участник Б).

Строка массива подходит, если:
1) чётность соседних элементов чередуется (чёт/нечёт/чёт... или наоборот);
2) в чётных по номеру строках (2, 4, 6, ...) второй элемент нечётный.
"""


def is_good_row(row, row_number):
    """Процедура проверки строки.

    row        - все элементы текущей строки;
    row_number - номер строки, начиная с 1.
    """
    if len(row) < 2:
        return False  # в строке из одного элемента нечему чередоваться
    for i in range(len(row) - 1):
        if row[i] % 2 == row[i + 1] % 2:
            return False
    if row_number % 2 == 0 and row[1] % 2 == 0:
        return False
    return True


def find_good_rows(matrix):
    """Возвращает список номеров подходящих строк (нумерация с 1)."""
    good = []
    for number, row in enumerate(matrix, start=1):
        if is_good_row(row, number):
            good.append(number)
    return good
