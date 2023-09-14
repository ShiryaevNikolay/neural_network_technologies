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


def make_ring(matrix, padding=0, width=1):
    """
    Рисует круг в матрице
    :param matrix: Исходная нулевая матрица
    :param padding: Отступ кольца от края
    :param width: Ширина отступа
    :return:
    """
    center_x = len(matrix) // 2
    center_y = len(matrix) // 2
    outer_radius = min(center_x, center_y) - padding
    inner_radius = outer_radius - width
    for x in range(center_x - outer_radius, center_x + outer_radius):
        for y in range(center_y - outer_radius, center_y + outer_radius):
            if inner_radius <= dist(center_x, center_y, x, y) <= outer_radius:
                matrix[x][y] = 1


def make_cross(matrix, padding=0):
    """
    Рисует крестик в матрице
    :param matrix: Исходная нулевая матрица
    :param padding: Отступ крестика от края
    :return:
    """
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 1
        matrix[i][size - i - 1] = 1


_size = 28
matrix_ring = [[0 for _ in range(_size)] for _ in range(_size)]
matrix_cross = [[0 for _ in range(_size)] for _ in range(_size)]

make_ring(matrix_ring, padding=1, width=2)
make_cross(matrix_cross)

print("\n".join("".join(map(str, i)) for i in matrix_ring))
print("\n".join("".join(map(str, i)) for i in matrix_cross))
