from app.app import App
from perceptron import Perceptron
from utils.activate_func import treshold

_size = 30

perseptron = Perceptron(length=_size, activate_fun=treshold)


def get_perseptron_result(values):
    global perseptron

    return perseptron.result(values)


def train_perseptron(values):
    global perseptron

    current_result = perseptron.result(values)
    target = 1 if current_result == 0 else 0
    perseptron.train(values, target)
    perseptron.save_weights()


app = App(
    size=_size,
    get_result_callback=get_perseptron_result,
    train_callback=train_perseptron
)
app.mainloop()

'''
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
    app = App(
        size=_size,
        get_result_callback=get_perseptron_result,
        train_callback=train_perseptron
    )
    app.mainloop()
'''
