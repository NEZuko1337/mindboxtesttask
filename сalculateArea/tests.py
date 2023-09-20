import unittest
from AreaCalculation import triangle_area, calculate_circle_area
from RightTriangle import triangle_check


class MyTestCase(unittest.TestCase):
    def test_triangle_area_and_triangle_check(self):
        # Правильный тест
        self.assertEqual(triangle_area(2, 3, 4), 2.9047375096555625, "Площадь вычисляется неправильно")
        # Неправильный тест
        self.assertEqual(triangle_area(2, 3, 4), 2, "Площадь вычисляется неправильно")
        # Ниже будут еще пару тестов
        self.assertEqual(triangle_area(3, 4, 5), 6.0, "Площадь вычисляется неправильно")
        self.assertEqual(triangle_area(23, 22, 21), 208.71032557111303, "Площадь вычисляется неправильно")
        # Тесты на прямоугольность треугольника
        self.assertEqual(triangle_check(3, 4, 5), True, "Треугольник не прямоугольный")
        self.assertEqual(triangle_check(4, 5, 6), False, "Треугольник не прямоугольный")

    def test_circle_area(self):
        # Правильный тест
        self.assertEqual(calculate_circle_area(9), 254.46900494077323, "Площадь вычисляется неправильно")
        # Неправильный тест
        self.assertEqual(calculate_circle_area(9), 120, "Площадь вычисляется неправильно")
        # Ниже будут еще пару тестов
        self.assertEqual(calculate_circle_area(3), 28.274333882308138, "Площадь вычисляется неправильно")
        self.assertEqual(calculate_circle_area(2), 12.566370614359172, "Площадь вычисляется неправильно")


if __name__ == '__main__':
    unittest.main()
