from tkinter import *

_background_color = 'white'
_draw_color = 'black'

_left_mouse_key = '<B1-Motion>'
_right_mouse_key = '<B3-Motion>'

_result_text = "Результат: "


class App(Tk):
    def __init__(self, size, get_result_callback, scale=14):
        """
        Инициализация приложения для рисования на сетке
        :param size: Размер сетки
        :param scale: Масштабирование одной ячейки
        """
        super().__init__()

        self.get_result = get_result_callback
        self.title("Распознавание")
        self.width = size
        self.height = size
        self.scale = scale

        self.columnconfigure(size, weight=1)
        self.rowconfigure(size, weight=1)

        self.colors = [[0 for i in range(self.width)] for j in range(self.height)]
        self.pixel_colors = []
        self.pixels = []

        self.create_canvas()
        self.create_pixels()
        self.create_controls()
        self.create_info()
        self.bindKeys()

    def create_canvas(self):
        """
        Создание канваса для рисования
        """
        scale_width = self.width * self.scale
        scale_height = self.height * self.scale
        self.canvas = Canvas(self, width=scale_width, height=scale_height, bg=_background_color)
        self.canvas.grid(column=0, row=1, sticky=E + W + S + N)

    def create_pixels(self):
        """
        Создание массива пикселей, которые хранят прямоугольники, отображаемые на канвасе
        """
        for i in range(self.width):
            self.pixels.append([])
            for j in range(self.height):
                color = self.get_color(self.colors[i][j])
                x = i * self.scale
                y = j * self.scale
                pixel = self.canvas.create_rectangle(
                    x, y,
                    x + self.scale, y + self.scale,
                    fill=color
                )
                self.pixels[i].append(pixel)

    def bindKeys(self):
        """
        Привязываение клавишей
        """
        self.canvas.bind(_left_mouse_key, self.draw)
        self.canvas.bind(_right_mouse_key, self.clear)

    def draw(self, event):
        """
        Закрашивает на канвасе пиксели
        :param event: Событие
        """
        self.paint(event, mouse_button='left')

    def clear(self, event):
        """
        Очищает на канвасе пиксели
        :param event: Событие
        """
        self.paint(event, mouse_button='right')

    def paint(self, event, mouse_button):
        """
        Закрашивает пиксели в определенный цвет
        :param event: Событие
        :param mouse_button: Нажатая кнопка мыши
        """
        x = event.x // self.scale
        y = event.y // self.scale
        if x >= len(self.colors):
            return
        if y >= len(self.colors[x]):
            return
        if mouse_button == 'left':
            self.colors[x][y] = 1
            self.canvas.itemconfigure(self.pixels[x][y], fill=self.get_color(self.colors[x][y]))
        elif mouse_button == 'right':
            self.colors[x][y] = 0
            self.canvas.itemconfigure(self.pixels[x][y], fill=self.get_color(self.colors[x][y]))

    def clear_canvas(self):
        """
        Очищает канвас
        """
        for i in range(self.width):
            for j in range(self.height):
                self.canvas.itemconfigure(self.pixels[i][j], fill=self.get_color(0))

    def get_color(self, value):
        """
        Возвращает цвет в зависимости от значения.
        :param value: Значение
        :return: 0 - белый, 1 - черный
        """
        if value == 0:
            return 'white'
        else:
            return 'black'

    def get_answer(self):
        result_text = self.get_result()
        self.result_label

    def create_controls(self):
        """
        Создает кнопки управления
        """
        buttons_frame = Frame(master=self)
        buttons_frame.grid(column=0, row=0)
        Button(
            master=buttons_frame,
            text="Очистить",
            command=self.clear_canvas
        ).grid(column=0, row=0, padx=16, pady=8)
        Button(
            master=buttons_frame,
            text="Получить ответ",
            command=self.get_answer
        ).grid(column=1, row=0, padx=16, pady=8)

    def create_info(self):
        """
        Создает заголовок для отображения ответа персептрона
        """
        self.result_label = Label(text=_result_text).grid(column=1, row=0)
