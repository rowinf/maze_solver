from tkinter import Tk, BOTH, Canvas


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
        line.draw(self.canvas, "red")


def main():
    win = Window(800, 600)
    line1 = Line(Point(10, 0), Point(10,100))
    line2 = Line(Point(0, 10), Point(100, 10))
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")
    win.wait_for_close()

main()
