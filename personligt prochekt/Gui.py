import time
import tkinter as tk
from Game_of_life import *




class App(tk.Tk):
    #klassen är för tkinter fönstret som visar spel planen
    def __init__(self):

        super().__init__()
        self.grid_dict = {}
        self.width = grid.width
        self.height = grid.height


        self.screen_width = self.winfo_screenwidth()#fråga inte ordet var kortare
        self.screen_height = self.winfo_screenheight()


        self.tw = tk.IntVar(value=self.width)
        self.th = tk.IntVar(value=self.height)



        self.frame1 = tk.LabelFrame(self)
        self.frame1.grid(row=0,column=0,sticky="NW")

        self.frame2 = tk.LabelFrame(self)
        self.frame2.grid(row=1, column=0, sticky="Nw")

        self.frame_grid = tk.LabelFrame(self)
        self.frame_grid.grid(row=0, column=1, sticky="NW", rowspan=2)



        self.btn = tk.Button(self.frame1, text="Next step", width=16,command=self.next_step)
        self.btn.grid(row=1, sticky="nw")
        self.btn = tk.Button(self.frame1, text="Save and exit", width=16,command=self.stop)
        self.btn.grid(row=3, sticky="nw")





        self.name = tk.Label(self.frame2, text="Bred")
        self.name.grid(row=0)

        self.name_entry = tk.Entry(self.frame2, textvariable=self.tw)
        self.name_entry.grid(row=1)

        self.name = tk.Label(self.frame2, text="Höjd")
        self.name.grid(row=2)

        self.name_entry = tk.Entry(self.frame2, textvariable=self.th)
        self.name_entry.grid(row=3)
        self.btn = tk.Button(self.frame2, text="Update grid", width=16, command=self.new_grid)
        self.btn.grid(row=5, sticky="nw")






        self.new_grid()

    def stop(self):
        fil((grid.cells))
        App.destroy(self)

    def select_cell(self, button):
        current_color = button.cget("bg")

        vald_cell = Cell(int(button.grid_info()['column']),int(button.grid_info()['row']))


        if current_color == "SystemButtonFace":
            new_color = "green"
            grid.cells.append(vald_cell)

        else:
            new_color = "SystemButtonFace"

            for cell in grid.cells:#den ville inte funka annars men de här suger
                if cell.x == vald_cell.x and cell.y == vald_cell.y:
                    grid.cells.remove(cell)
        button.config(bg=new_color)

    def new_grid(self):
        for c in range(0, len(grid.cells)):  # c för cordinate men de blev oläsbart
            print(str(grid.cells[c]))
            if grid.cells[c].x > self.width:
                self.tw.set(grid.cells[c].x)

            if grid.cells[c].y > self.height:
                self.th.set(grid.cells[c].y)


        self.grid_dict = {}


        # Iterate through every widget inside the frame
        for widget in self.frame_grid.winfo_children():
            widget.destroy()

        grid.height  = int(self.th.get())
        grid.width = int(self.tw.get())
        self.width = grid.width
        self.height = grid.height

        self.frame_grid = tk.LabelFrame(self)
        self.frame_grid.grid(row=0, column=1, sticky="NW", rowspan=2)

        for h in range(int(self.th.get())+1):
            for w in range(int(self.tw.get())+1):
                self.grid_dict[f"[{w},{h}]"] = tk.Button(self.frame_grid,
                                                    text="",
                                                    width=int((self.screen_width / 30) / self.width),
                                                    height=int((self.screen_height / 30) / self.height),

                                                    )

                self.grid_dict[f"[{w},{h}]"].config(command=lambda b=self.grid_dict[f"[{w},{h}]"]: self.select_cell(b))
                self.grid_dict[f"[{w},{h}]"].grid(row=h, column=w, sticky="nw")

        print(int(self.tw.get()),int(self.th.get()),"dojfnbsojdfnodkfbn")
        for cell in grid.cells:
            self.grid_dict[str(cell)].config(bg="green")


    def next_step(self):

        grid.update()

        for cell in self.grid_dict.keys():
            self.grid_dict[cell].config(bg="SystemButtonFace")

        for cell in grid.cells:

            self.grid_dict[str(cell)].config(bg="green")

    def play(self):

        self.next_step()
        time.sleep(1)
    def clear(self):
        for cell in grid.cells:
            self.grid_dict[str(cell)].config(bg="SystemButtonFace")
        grid.cells = []

grid = Grid()
if __name__ == "__main__":
    app = App()
    app.mainloop()




