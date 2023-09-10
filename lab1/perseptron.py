from utils.init import init_weights
from utils.func import net
from utils.read_data import read_weights
from utils.write_data import save_weights
import numpy as np

_file_name = 'weights.xlsx'
_sheet_name = 'weigths'

class Perseptron:
    def __int__(self, length, shift, activate_fun):
        """
        Инициализация персептрона
        :param length: Длина вектора входных данных
        :param shift: Сдвиг, смещение
        :param activate_fun: Активационная функция
        """
        self.shift = shift
        self.learn_speed = np.random.uniform(0.5, 0.7)  # Скорость обучения
        self.activate_fun = activate_fun
        weights = read_weights(length, file_name=_file_name, sheet_name=_sheet_name)
        if len(weights) == 0:
            weights = init_weights(length)
            save_weights(weights, sheet_name=_sheet_name, file_name=_file_name)
        self.weights = weights

    def result(self, values):
        """
        Вычиялет результат работы персептрона
        :param values: Вектор входных данных
        :return: Результат активационной функции
        """
        weights = self.weights.flatten()
        input_data = values.flatten()
        sum_value = net(input_data, weights) + self.shift
        return self.activate_fun(sum_value)

    def train(self, values):
        result = self.result(values)
        error = target - result
        column_length = len(self.weights)
        for i in range(column_length):
            row_length = len(self.weights[i])
            for j in range(row_length):
                self.weights[i][j] += error * values[i][j] * self.learn_speed
