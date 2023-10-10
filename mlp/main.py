# Предсказываем, машина импортированная или нет
# Dataset
# https://www.kaggle.com/datasets/talhabarkaatahmad/pakistan-used-car-prices-2023
import pandas
import keras
import numpy as np
import matplotlib.pyplot as plt
from func import to_category_dict

file_name = "pakwheels_used_cars.csv"
data_frame = pandas.read_csv(file_name)
data_frame.dropna(subset=["price"], inplace=True)
input_names = ["body", "make", "price"]
output_names = ["assembly"]  # Импортирована или нет

print(to_category_dict(data_frame["body"]))

max_price = data_frame["price"].max()
encoders = {"price": lambda price: [price/max_price],
            "body": lambda body: to_category_dict(data_frame["body"]).get(body),
            "make": lambda make: to_category_dict(data_frame["make"]).get(make),
            "assembly": lambda assembly: {"Imported": [1], np.NaN: [0]}.get(assembly)}


def data_frame_to_dict(df):
    result = dict()
    for column in df.columns:
        values = data_frame[column].values
        result[column] = values
    return result


def make_supervised(df):
    """
    Разделение на входные и выходные данные
    :param df: data frame
    :return:
    """
    raw_input_data = df[input_names]
    raw_output_data = df[output_names]
    return {"inputs": data_frame_to_dict(raw_input_data),
            "outputs": data_frame_to_dict(raw_output_data)}


def encode(data):
    """
    Кодирует данные в векторы
    :param data:
    :return:
    """
    vectors = []
    for data_name, data_values in data.items():
        encoded = list(map(encoders[data_name], data_values))
        vectors.append(encoded)
    formatted = []
    for vector_raw in list(zip(*vectors)):
        vector = []
        for element in vector_raw:
            for e in element:
                vector.append(e)
        formatted.append(vector)
    return formatted


supervised = make_supervised(data_frame)
encoded_inputs = np.array(encode(supervised["inputs"]))
encoded_outputs = np.array(encode(supervised["outputs"]))

train_x = encoded_inputs[:600]
train_y = encoded_outputs[:600]

test_x = encoded_inputs[600:]
test_y = encoded_outputs[600:]

model = keras.Sequential()
# Dence - полносвязанная сеть
# units - кол-во
model.add(keras.layers.Dense(units=5, activation="relu"))  # TODO: кол-во units = кол-во столбцов во входных данных
model.add(keras.layers.Dense(units=1, activation="sigmoid"))  # TODO: units=1, тк выход 0 или 1
# Компиляция
# lass - функция потерь. mse - среднеквадратичная ошибка
# optimizer: sgd - стахостический градиентный спуск
# metrics - метрики для отслеживания
model.compile(loss="mse", optimizer="sgd", metrics=["accuracy"])
# load_weights вместо fit, чтобы не тренеровать заново модель, а использовать сохраненные веса
# model.load_weights("weights.h5")
# Тренеровка
# validation_split означает 80% данных на тренировку и 20% на валидацию
fit_results = model.fit(x=train_x, y=train_y, epochs=10, validation_split=0.2)

plt.title("Losses train/validation")
plt.plot(fit_results.history["loss"], label="Train")
plt.plot(fit_results.history["val_loss"], label="Validation")
plt.legend()
plt.show()

plt.title("Accuracies train/validation")
plt.plot(fit_results.history["accuracy"], label="Train")
plt.plot(fit_results.history["val_accuracy"], label="Validation")
plt.legend()
plt.show()

predicted_test = model.predict(test_x)
# iloc - берем срез по определенному индексу
real_data = data_frame.iloc[600:][input_names + output_names]
real_data["PAssembly"] = predicted_test
print(real_data)

# Чтобы каждый раз не тренеровать, можно сохранить веса
# h5 - формат данных для сохранения весов
model.save_weights("weights.h5")
