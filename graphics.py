from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

class Line:
    def __init__(self, p1:Point, p2:Point):
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas:Canvas, fill:str):
        canvas.create_line(self._p1._x, self._p1._y, self._p2._x, self._p2._y, fill=fill, width=2)

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._root = Tk()
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        self._root.wm_title("Maze Solver")
        self._canvas = Canvas(height=height, width=width, background="white")
        self._canvas.pack()

        self.running = False

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line:Line, fill_color:str):
        line.draw(self._canvas, fill=fill_color)
