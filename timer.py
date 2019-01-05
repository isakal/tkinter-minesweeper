import tkinter as tk
root = tk.Tk()
screen = tk.Canvas(root)
screen.grid()


offsets = (
    (0, 0, 1, 0),  # top line
    (1, 0, 1, 1),  # upper right line
    (1, 1, 1, 2),  # lower right line
    (0, 2, 1, 2),  # bottom line
    (0, 1, 0, 2),  # lower left line
    (0, 0, 0, 1),  # upper left line
    (0, 1, 1, 1),  # middle line
)

digits = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1)   # 9
)


class Digit:
    def __init__(self, canvas, *, x=5, y=5, length=10, width=3):
        self.canvas = canvas
        l = length
        self.segments = []
        for x0, y0, x1, y1 in offsets:
            self.segments.append(canvas.create_line(
                x + x0*l, y + y0*l, x + x1*l, y + y1*l,
                width=width,state = 'hidden'))
    def show(self, num):
        for iid, on in zip(self.segments, digits[num]):
            self.canvas.itemconfigure(iid, state = 'normal' if on else 'hidden')



dig = Digit(screen)
n = 0
def update():
    global n
    dig.show(n)
    n = (n+1) % 10
    root.after(1000, update)
root.after(1000, update)
root.mainloop()

#TODO: implement this into an actual file