from tkinter import Tk, BOTH, Canvas
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = list()
        self._create_cells()

    def _create_cells(self):
        for i in range(0, self.__num_cols):
            column = list()
            self._cells.append(column)
            for j in range(0, self.__num_rows):
                x1 = i * self.__cell_size_x + self.__x1
                y1 = j * self.__cell_size_y + self.__y1
                x2 = x1 + self.__cell_size_x
                y2 = y1 + self.__cell_size_y
                cell = Cell(self.__win, x1, y1, x2, y2, True, True, True, True)
                self._cells[i].append(cell)
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.__win is None:
            return
        cell.draw()
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

class Cell:
    def __init__(self, win, x1, y1, x2, y2, has_top_wall, has_right_wall, has_bottom_wall, has_left_wall):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.has_left_wall =has_left_wall
        self.has_right_wall=has_right_wall
        self.has_top_wall=has_top_wall
        self.has_bottom_wall=has_bottom_wall

    def mid_point(self):
        x_mid = (self.__x1 + self.__x2) / 2
        y_mid = (self.__y1 + self.__y2) / 2
        return Point(x_mid, y_mid)


    def draw_move(self, to_cell, undo=False):
        p1 = self.mid_point()
        p2 = to_cell.mid_point()
        self.__win.draw_line(Line(p1, p2), 'grey' if undo else 'red')

    def draw_wall(self, x1, y1, x2, y2):
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        line = Line(p1, p2)
        self.__win.draw_line(line, "black")

    def draw(self):
        if self.has_top_wall:
            self.draw_wall(self.__x1, self.__y1, self.__x2, self.__y1)
        if self.has_right_wall:
            self.draw_wall(self.__x2, self.__y1, self.__x2, self.__y2)
        if self.has_bottom_wall:
            self.draw_wall(self.__x2, self.__y2, self.__x1, self.__y2)
        if self.has_left_wall:
            self.draw_wall(self.__x1, self.__y1, self.__x1, self.__y2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        p1 = self.p1
        p2 = self.p2
        canvas.create_line(
            p1.x, p1.y, p2.x, p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)
        

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 10, 14, 50, 50, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()
