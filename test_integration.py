"""Интеграционные тесты: программа запускается целиком (main.py),
данные подаются на вход как с клавиатуры, проверяется вывод.
"""
import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "main.py")


def run(text):
    """Запуск main.py с заданным вводом. Возвращает (код, вывод)."""
    result = subprocess.run(
        [sys.executable, MAIN],
        input=text.encode("utf-8"),
        capture_output=True,
        cwd=HERE,
        timeout=10,
    )
    return result.returncode, result.stdout.decode("utf-8")


def matrix_input(rows):
    """Формирует ввод одного массива: строки, столбцы, элементы."""
    lines = [str(len(rows)), str(len(rows[0]))]
    lines += [" ".join(map(str, r)) for r in rows]
    return "\n".join(lines) + "\n"


class IntegrationTests(unittest.TestCase):

    def test_1_normal(self):
        """Обычный случай: в A две подходящие строки, в B ни одной."""
        a = [[1, 2, 3, 4],
             [2, 3, 4, 5],
             [1, 1, 2, 3]]
        b = [[2, 2, 2],
             [1, 2, 3]]
        code, out = run(matrix_input(a) + matrix_input(b))
        self.assertEqual(code, 0)
        self.assertIn("Массив A: подходящих строк - 2 (номера: 1, 2)", out)
        self.assertIn("Массив B: подходящих строк - 0", out)
        self.assertNotIn("Ни в одном", out)

    def test_2_negative_numbers(self):
        """Обычный случай с отрицательными числами и нулём."""
        a = [[-3, -2, -1, 0],
             [0, -1, 2, -3]]
        b = [[-4, -4]]
        code, out = run(matrix_input(a) + matrix_input(b))
        self.assertIn("Массив A: подходящих строк - 2 (номера: 1, 2)", out)
        self.assertIn("Массив B: подходящих строк - 0", out)

    def test_3_min_size_1x1(self):
        """Граничный случай: массивы 1x1 - чередования нет."""
        code, out = run("1\n1\n5\n1\n1\n4\n")
        self.assertEqual(code, 0)
        self.assertIn("Массив A: подходящих строк - 0", out)
        self.assertIn("Ни в одном из массивов нет строк", out)

    def test_4_max_size_10x10(self):
        """Граничный случай: массивы 10x10."""
        a = []
        for i in range(1, 11):
            first = 1 if i % 2 else 2  # в чётных строках второй - нечётный
            a.append([first if j % 2 == 0 else 3 - first for j in range(10)])
        b = [[0] * 10 for _ in range(10)]
        code, out = run(matrix_input(a) + matrix_input(b))
        self.assertIn("Массив A: подходящих строк - 10", out)
        self.assertIn("Массив B: подходящих строк - 0", out)

    def test_5_even_row_second_even(self):
        """Граничный: чётная строка чередуется, но второй элемент чётный."""
        a = [[1, 2], [3, 4]]  # строка 2: 3 4 - второй чётный
        b = [[5, 5], [2, 1]]  # строка 2: 2 1 - подходит
        code, out = run(matrix_input(a) + matrix_input(b))
        self.assertIn("Массив A: подходящих строк - 1 (номера: 1)", out)
        self.assertIn("Массив B: подходящих строк - 1 (номера: 2)", out)

    def test_6_wrong_input(self):
        """Ошибочный ввод: буквы, размер вне диапазона, не то число элементов."""
        text = ("abc\n11\n0\n1\n"   # строки: abc, 11, 0 - ошибки, потом 1
                "2\n"               # столбцы
                "1 2 3\n1 x\n1 2\n"  # 3 числа, буква - ошибки, потом верно
                "1\n2\n2 1\n")       # массив B
        code, out = run(text)
        self.assertEqual(code, 0)
        self.assertIn("Ошибка: нужно ввести целое число.", out)
        self.assertIn("Ошибка: размер должен быть от 1 до 10.", out)
        self.assertIn("Ошибка: нужно ровно 2 чисел через пробел.", out)
        self.assertIn("Ошибка: элементы должны быть целыми числами.", out)
        self.assertIn("Массив A: подходящих строк - 1 (номера: 1)", out)

    def test_7_empty_input(self):
        """Ошибочный ввод: данные не введены (конец ввода)."""
        code, out = run("")
        self.assertEqual(code, 1)
        self.assertIn("ввод прерван", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
