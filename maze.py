import random
from time import sleep
from graphics import Window
from graphics import Point
from cell import Cell

class Maze:
    def __init__(
        self,
        x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win:Window|None = None,
        seed=None
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win:Window|None = win

        if seed:
            random.seed(seed)

        self._cells:list[list[Cell]] = []
        self._create_cells()


    def _create_cells(self):
        for j in range(self._num_cols):
            col = []
            for i in range(self._num_rows):
                top_left = Point(self._x1 + j*self._cell_size_x, self._y1 + i*self._cell_size_y)
                bottom_right = Point(self._x1 + (j+1) * self._cell_size_x, self._y1 + (i+1) * self._cell_size_y)
                new_cell = Cell(top_left, bottom_right, self._win)
                col.append(new_cell)
            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win:
            self._cells[i][j].draw()
            self._animate()


    def _animate(self):
        if self._win:
            self._win.redraw()
            sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0]._has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1]._has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    def _break_walls_r(self, i, j):
        current_cell:Cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []

            if i-1 >= 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i+1 < len(self._cells) and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j+1 < len(self._cells[0]) and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if len(to_visit) == 0:
                current_cell.draw()
                return
            
            direction = random.choice(to_visit)

            next_cell:Cell = self._cells[direction[0]][direction[1]]

            if direction[0] == i + 1:
                current_cell._has_right_wall = False
                next_cell._has_left_wall = False
            if direction[0] == i - 1:
                current_cell._has_left_wall = False
                next_cell._has_right_wall = False
            if direction[1] == j + 1:
                current_cell._has_bottom_wall = False
                next_cell._has_top_wall = False
            if direction[1] == j - 1:
                current_cell._has_top_wall = False
                next_cell._has_bottom_wall = False


            self._break_walls_r(direction[0], direction[1])
            

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        self._solve_r(0,0)


    def _solve_r(self, i, j):
        self._animate()
        cell:Cell = self._cells[i][j]
        cell.visited = True
        if i == self._num_cols - 1 and j ++ self._num_rows - 1:
            return True
        
        if i > 0 and not cell._has_left_wall and not self._cells[i-1][j].visited:
            cell.draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                cell.draw_move(self._cells[i-1][j], undo=True)
        if i < self._num_cols - 1 and not cell._has_right_wall and not self._cells[i+1][j].visited:
            cell.draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                cell.draw_move(self._cells[i+1][j], undo=True)
        if j > 0 and not cell._has_top_wall and not self._cells[i][j-1].visited:
            cell.draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                cell.draw_move(self._cells[i][j-1], undo=True)
        if i < self._num_rows - 1 and not cell._has_bottom_wall and not self._cells[i][j+1].visited:
            cell.draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                cell.draw_move(self._cells[i][j+1], undo=True)
