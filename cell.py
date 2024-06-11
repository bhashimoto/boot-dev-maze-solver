from graphics import Line, Point, Window

class Cell:
    def __init__(self, top_left:Point, bottom_right:Point, win:Window|None=None, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self._x1:int = top_left._x
        self._y1:int = top_left._y
        self._x2:int = bottom_right._x
        self._y2:int = bottom_right._y
        self._has_left_wall = has_left_wall
        self._has_right_wall = has_right_wall
        self._has_top_wall = has_top_wall
        self._has_bottom_wall = has_bottom_wall
        self._win = win
        self.visited = False

    def draw(self):
        if self._win:
            if self._has_left_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color="black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color="white")

            if self._has_right_wall:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color="black")
            else:
                self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color="white")
            
            if self._has_top_wall:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color="black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color="white")
            
            if self._has_bottom_wall:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color="black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color="white")

    def draw_move(self, to_cell, undo=False):
        if self._win:
            fill_color = "gray" if undo else "red"
            center_from = Point((self._x1 + self._x2)//2,(self._y1 + self._y2)//2)
            center_to = Point((to_cell._x1 + to_cell._x2)//2,(to_cell._y1 + to_cell._y2)//2)
            self._win.draw_line(Line(center_from, center_to), fill_color)
