import numpy as np


def init_weights(length):
    """
    Инициализирует веса случайными числами от -0.3 до 0.3
    """
    weights = []
    for i in range(length):
        init_weight = np.random.uniform(-0.3, 0.3)
        weights.append(init_weight)
    return weights
