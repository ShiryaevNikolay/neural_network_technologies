import math


def net(values, weights):
    """
    Сумма произведений входного веркора на веса
    :param values: Входной вектор данных
    :param weights: Веса
    :return: Сумма произведений векторов
    """
    return sum(value * weight for value, weight in zip(values, weights))


def dist(x1, y1, x2, y2):
    """
    Вычисляет длину между двумя точками
    :param x1: X координата первой точки
    :param y1: Y координата первой точки
    :param x2: X координата второй точки
    :param y2: Y координата второй точки
    :return: Длину между двумя точками
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def make_ring(matrix, center_x, center_y, outer_radius, inner_radius):
    """
    Рисует круг в матрице
    :param matrix: Исходная нулевая матрица
    :param center_x: центр по оси X
    :param center_y: центр по оси Y
    :param outer_radius: радиус круга
    """
    for x in range(center_x - outer_radius, center_x + outer_radius):
        for y in range(center_y - outer_radius, center_y + outer_radius):
            if inner_radius <= dist(center_x, center_y, x, y) <= outer_radius:
                matrix[x][y] = 1


_size = 28
center_x = _size // 2
center_y = _size // 2

radius = min(center_x, center_y) - 1
matrix = [[0 for _ in range(_size)] for _ in range(_size)]

make_ring(matrix, center_x, center_y, radius, radius - 2)

print("\n".join("".join(map(str, i)) for i in matrix))
