from utils.init import init_weights
from utils.func import net


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
        self.weights = init_weights(length)

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
