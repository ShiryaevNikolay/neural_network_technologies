from openpyxl import *


def read_weights(length, file_name='../weights.xlsx', sheet_name='weights'):
    """
    Считывает веса из файла таблицы
    :param length: Размер данных в одной строке/столбце
    :param file_name: Имя файла
    :param sheet_name: Название страницы с весами
    :return: Матрицу весов размером length
    """
    weights_file = load_workbook(file_name)
    weigths = []
    try:
        sheet = weights_file.get_sheet_by_name(sheet_name)
        for i in range(length):
            weigths.append([])
            for j in range(length):
                weight_value = sheet.cell(column=i + 1, row=j + 1).value
                weigths[i].append(weight_value)
        return weigths
    except:
        return weigths
