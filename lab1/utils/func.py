def net(values, weights):
    """
    Сумма произведений входного веркора на веса
    :param values: Входной вектор данных
    :param weights: Веса
    :return: Сумма произведений векторов
    """
    return sum(value * weight for value, weight in zip(values, weights))
