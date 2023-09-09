def treshold(value):
    """
    Пороговая (Хевисайда) функция активации
    :param value: Сумма произведений
    :return: 0, если value < 0, иначе 1
    """
    return 0 if value < 0 else 1
