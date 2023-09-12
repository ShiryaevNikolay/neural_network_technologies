from app.app import App
from perseptron import Perseptron
from utils.activate_func import treshold
from train import train_perseptron

_size = 28

perseptron = Perseptron(length=_size, shift=0.5, activate_fun=treshold)


def get_perseptron_result():
    pass


while True:
    info_text = """
    Что планируется сделать?
    1. Обучить персептрон
    2. Открыть приложение, чтобы нарисовать фигуру
    
    Введите цифру: 
    """
    try:
        action = int(input(info_text))
    except:
        continue
    if action == 1 or action == 2:
        break

if action == 1:
    train_perseptron(perseptron)
elif action == 2:
    app = App(size=_size, get_result_callback=get_perseptron_result)
    app.mainloop()
