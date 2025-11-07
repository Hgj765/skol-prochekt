
from tkinter import *
from random import *

window = Tk()
window.title('Game Of Life')

def create_grid(window):
    width = 800
    height = 600
    canvas = Canvas(window, background='white', width=width, height=height)


    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)

create_grid(window)
window.mainloop()