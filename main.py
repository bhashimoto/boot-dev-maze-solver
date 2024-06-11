from graphics import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(50,50, 10, 12, 50, 50, win, seed=0)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()


    win.wait_for_close()



if __name__ == "__main__":
    main()
