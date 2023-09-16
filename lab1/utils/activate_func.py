def treshold(value):
    """
    Пороговая (Хевисайда) функция активации
    :param value: Сумма произведений
    :return: 1, если value > 0, иначе 0
    """
    return 0 if value < 0.5 else 1

def sigmoid(values):
    pass