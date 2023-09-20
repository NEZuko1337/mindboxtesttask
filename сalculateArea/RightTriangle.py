def triangle_check(a: float, b: float, c:float) ->bool:
    # Создаю массив со значениями
    list_of_numbers: list = [a, b, c]
    # Беру из него максимум и сразу жу удаляю его
    max_of_numbers: float = max(list_of_numbers)
    list_of_numbers.remove(max_of_numbers)
    # После смотрю, выполняется ли теорема пифагора, т.е
    # Если сумма квадратов длин двух меньших сторон равна квадрату самой большой стороны,
    # то треугольник является прямоугольным.Ниже возвращаю условие теоремы пифагора
    return max_of_numbers**2 == list_of_numbers[0] ** 2 + list_of_numbers[-1] ** 2
