from AreaCalculation import calculate_circle_area, triangle_area
from RightTriangle import triangle_check


def main():
    # Вычисление площади круга и площади треугольника
    circle_area = calculate_circle_area(9)
    area_of_triangle = triangle_area(2, 3, 4)
    print(f"Площадь круга равна: {circle_area}, а площадь треугольника равна: {area_of_triangle}")
    print(f"Проверяю является ли треугольник со сторонами 3,4,5 прямоугольным: {triangle_check(3, 4, 5)}")


if __name__ == '__main__':
    main()


