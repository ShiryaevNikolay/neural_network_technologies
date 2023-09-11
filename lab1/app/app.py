from tkinter import *

_size = 28
_scale = 20
_background_color = 'white'
_draw_color = 'black'
_brush_size = 10

_left_mouse_key = '<B1-Motion>'
_right_mouse_key = '<B3-Motion>'

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Распознавание")
        self.width = _size
        self.height = _size
        self.scale = _scale

        self.columnconfigure(_size, weight=1)
        self.rowconfigure(_size, weight=1)

        self.colors = [[0 for i in range(self.width)] for j in range(self.height)]
        self.pixel_colors = []
        self.pixels = []

        self.create_canvas()
        self.create_pixels()
        self.bindKeys()

    def create_canvas(self):
        scale_width = self.width * self.scale
        scale_height = self.height * self.scale
        self.canvas = Canvas(self, width=scale_width, height=scale_height, bg=_background_color)
        self.canvas.grid(row=2, column=0, sticky=E + W + S + N)
        # self.canvas.grid(row=2, column=0)

    def create_pixels(self):
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
        self.canvas.bind(_left_mouse_key, self.draw)
        self.canvas.bind(_right_mouse_key, self.clear)
    
    def draw(self, event):
        self.paint(event, mouse_button='left')

    def clear(self, event):
        self.paint(event, mouse_button='right')

    def paint(self, event, mouse_button):
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
        self.canvas.delete('all')
        self.canvas['bg'] = _background_color

    def get_color(self, value):
        if value == 0:
            return 'white'
        else:
            return 'black'
