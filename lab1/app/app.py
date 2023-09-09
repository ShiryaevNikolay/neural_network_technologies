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

        self.create_canvas()
        self.bindKeys()

    def create_canvas(self):
        scale_width = self.width * self.scale
        scale_height = self.height * self.scale
        self.canvas = Canvas(self, width=scale_width, height=scale_height, bg=_background_color)
        # self.canvas.grid(row=2, column=0, sticky=E + W + S + N)
        self.canvas.grid(row=2, column=0)

    def bindKeys(self):
        self.canvas.bind(_left_mouse_key, self.draw)
        self.canvas.bind(_right_mouse_key, self.clear)
    
    def draw(self, event):
        x1, y1 = (event.x - _brush_size), (event.y - _brush_size)
        x2, y2 = (event.x + _brush_size), (event.y + _brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=_draw_color, width=0)

    def clear(self, event):
        x1, y1 = (event.x - _brush_size), (event.y - _brush_size)
        x2, y2 = (event.x + _brush_size), (event.y + _brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=_background_color, width=0)

    def clear_canvas(self):
        self.canvas.delete('all')
        self.canvas['bg'] = _background_color
