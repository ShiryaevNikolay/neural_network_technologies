from utils.init import init_weights
from utils.func import net
from utils.read_data import read_weights
from utils.write_data import save_weights

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
        sum_value = net(values, self.weights) + self.shift
        return self.activate_fun(sum_value)

    def train(self, values):
        pass
