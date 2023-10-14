from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def draw(self):
        if self.has_top_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            p1 = Point(self.__x2, self.__y2)
            p2 = Point(self.__x1, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")
        if self.has_left_wall:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            line = Line(p1, p2)
            self.__win.draw_line(line, "black")

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

    cell = Cell(win, 0, 0, 50, 50, False, True, True, False)
    cell.draw()
    cell1 = Cell(win, 0, 50, 50, 100, False, True, True, False)
    cell1.draw()
    cell2 = Cell(win, 50, 50, 100, 100, True, True, True, True)
    cell2.draw()
    cell3 = Cell(win, 150, 150, 200, 200, True, True, True, True)
    cell3.draw()

    win.wait_for_close()

main()
