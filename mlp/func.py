from keras.utils import to_categorical


def to_category_dict(data):
    """
    Преобразует кортеж данных в словарь с категорией
    :param data:
    :return:
    """
    set_element_data = [element for _, element in enumerate(list(dict.fromkeys(data)))]
    set_index_data = [index for index, _ in enumerate(list(dict.fromkeys(data)))]
    category_data = [[int(element) for element in list_data] for list_data in to_categorical(set_index_data)]
    return dict(zip(set_element_data, category_data))
