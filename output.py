"""Модуль вывода (участник Б).

Форматированный вывод массивов и результатов.
"""


def print_matrix(name, matrix):
    """Вывод массива в виде таблицы."""
    print(f"\nМассив {name}:")
    for row in matrix:
        print("  " + " ".join(f"{x:5d}" for x in row))


def print_result(name, good_rows):
    """Вывод количества и номеров подходящих строк массива."""
    if good_rows:
        numbers = ", ".join(str(n) for n in good_rows)
        print(f"Массив {name}: подходящих строк - {len(good_rows)} (номера: {numbers})")
    else:
        print(f"Массив {name}: подходящих строк - 0")


def print_no_rows():
    """Сообщение, если подходящих строк нет ни в одном массиве."""
    print("\nНи в одном из массивов нет строк, удовлетворяющих условию.")
