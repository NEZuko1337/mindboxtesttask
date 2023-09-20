from math import pi, sqrt


def calculate_circle_area(radius: float) -> float:
    # s = pi * r^2
    area: float = pi * (radius**2)
    return area


# Буду все делать по формуле Герона
def triangle_area(a: float, b: float, c: float) -> float:
    # Периметр
    perimeter: float = (a + b + c)
    # Половина от периметра
    half_perimeter: float = perimeter / 2
    # Сама формула герона
    area: float = sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))
    return area


