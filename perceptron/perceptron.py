from utils.init_data import init_weights
from utils.func import net
from utils.read_data import read_weights
from utils.write_data import save_weights
import numpy as np

_file_name = 'weights.xlsx'
_sheet_name = 'weights'


class Perceptron:
    def __init__(self, length, activate_fun):
        """
        Инициализация персептрона
        :param length: Длина вектора входных данных
        :param activate_fun: Активационная функция
        """
        self.learn_speed = 0.5  # Скорость обучения
        self.activate_fun = activate_fun
        self.shift, self.weights = read_weights(
            length,
            file_name=_file_name,
            sheet_name=_sheet_name,
        )
        if len(self.weights) == 0:
            self.weights = init_weights(length)
            save_weights(
                shift=self.shift,
                weights=self.weights,
                sheet_name=_sheet_name,
                file_name=_file_name,
            )

    def result(self, values):
        """
        Вычисление результата работы персептрона
        :param values: Вектор входных данных
        :return: Результат активационной функции
        """
        weights = np.array(self.weights).flatten()
        input_data = np.array(values).flatten()
        sum_value = np.dot(input_data, weights) + self.shift
        return self.activate_fun(sum_value)

    def train(self, values, target):
        """
        Обуает персептрон
        :param values: Матрица входных значений
        :param target: Эталонный результат
        """
        result = self.result(values)
        error = target - result
        self.shift += error * self.learn_speed
        column_length = len(self.weights)
        for i in range(column_length):
            row_length = len(self.weights[i])
            for j in range(row_length):
                delta = error * values[i][j] * self.learn_speed
                self.weights[i][j] += delta

    def save_weights(self):
        """
        Сохраняет веса в файл
        """
        save_weights(
            shift=self.shift,
            weights=self.weights,
            sheet_name=_sheet_name,
            file_name=_file_name
        )
