
import tkinter as tk
from Game_of_life import *



#a tkinter gui for Game_of_life.py


class App():
    #the class for the tkinter gui

    def __init__(self,root=tk.Tk()):
        #it is just a tkinter window

        self.root = root
        self.grid = Grid()

        super().__init__()
        self.grid_dict = {}

        self.spela=False
        self.task_id = None

        self.screen_width = self.root.winfo_screenwidth()#fråga inte ordet var kortare
        self.screen_height = self.root.winfo_screenheight()


        self.tw = tk.IntVar(value=self.grid.width)
        self.th = tk.IntVar(value=self.grid.height)
        self.multi_generations_step =tk.StringVar()
        tk.Grid.columnconfigure(root, 1, weight=1)
        tk.Grid.rowconfigure(root, 0, weight=1)
        tk.Grid.rowconfigure(root, 1, weight=1)
        self.frame1 = tk.LabelFrame(self.root)
        self.frame1.grid(row=0,column=0,sticky="NW")
        self.frame2 = tk.LabelFrame(self.root)
        self.frame2.grid(row=1, column=0, sticky="Nw")
        self.frame_grid = tk.LabelFrame(self.root)
        self.frame_grid.grid(row=0, column=1, sticky="NW", rowspan=2)

        self.extend_init()

        self.new_grid()
    def extend_init(self):
        #this functions only exists becus there is a rule about the length of functions
        #it is just an extention of __init__
        self.btn_n = tk.Button(self.frame1, text="Next step", width=16, command=self.next_step)
        self.btn_n.grid(row=1, sticky="nw")
        self.btn_c = tk.Button(self.frame1, text="Clear bord", width=16, command=self.clear)
        self.btn_c.grid(row=2, sticky="nw")
        self.btn_p = tk.Button(self.frame1, text="Play", width=16, command=self.toggle_play)
        self.btn_p.grid(row=3, sticky="nw")

        self.name = tk.Label(self.frame1, text="Antalet generations steg")
        self.name.grid(row=4)
        self.name_entry = tk.Entry(self.frame1, textvariable=self.multi_generations_step)
        self.name_entry.grid(row=5)
        self.btn = tk.Button(self.frame1, text="Gå frammåt flera steg", width=16, command=self.new_grid)
        self.btn.grid(row=6, sticky="nw")

        self.btn_s = tk.Button(self.frame1, text="Save ", width=16, command=self.save)
        self.btn_s.grid(row=7, sticky="nw")
        self.btn_s = tk.Button(self.frame1, text="Exit", width=16, command=self.stop)
        self.btn_s.grid(row=8, sticky="nw")

        self.name = tk.Label(self.frame2, text="Update grid size", bg="blue", fg="white")
        self.name.grid(row=0)
        self.name = tk.Label(self.frame2, text="Width")
        self.name.grid(row=1)
        self.name_entry = tk.Entry(self.frame2, textvariable=self.tw)
        self.name_entry.grid(row=2)
        self.name = tk.Label(self.frame2, text="Hight")
        self.name.grid(row=3)
        self.name_entry = tk.Entry(self.frame2, textvariable=self.th)
        self.name_entry.grid(row=4)
        self.btn = tk.Button(self.frame2, text="Update grid", width=16, command=self.new_grid)
        self.btn.grid(row=5, sticky="nw")
    def stop(self):
        #quit the program by closing the window
        self.root.destroy()
    def save(self):
        #calls upon the grid method to save the cells to a file
        self.grid.spara(self.grid.cells)
    def select_cell(self, button):
        #a cell when clicked is either added to the list of cells or removed from it
        #Input: "button" the button that was clicked, dont ask how it works it is weard as shit
        #Output: nothing but changes the color of the button and changes the list of cells

        current_color = button.cget("bg")
        vald_cell = Cell(int(button.grid_info()['column']),int(button.grid_info()['row']))

        if current_color == "SystemButtonFace":
            new_color = "green"
            self.grid.cells.append(vald_cell)
        else:
            new_color = "SystemButtonFace"
            for cell in self.grid.cells:#den ville inte funka annars men de här suger
                if cell.x == vald_cell.x and cell.y == vald_cell.y:
                    self.grid.cells.remove(cell)
        button.config(bg=new_color)
    def new_grid(self):
        #first it clears the grid and then it updates it with the new size and cells
        #also creates the original grid the same way
        self.grid.height = int(self.th.get())
        self.grid.width = int(self.tw.get())
        for c in range(0, len(self.grid.cells)):  # c for coordinate but that is to long

            if self.grid.cells[c].x > self.grid.width:
                self.tw.set(self.grid.cells[c].x)

            if self.grid.cells[c].y > self.grid.height:
                self.th.set(self.grid.cells[c].y)

        self.grid_dict = {}

        for widget in self.frame_grid.winfo_children():
            widget.destroy()

        self.frame_grid = tk.LabelFrame(self.root)
        self.frame_grid.grid(row=0, column=1, sticky="NSEW", rowspan=2)


        for h in range(int(self.th.get())+1):
            self.frame_grid.rowconfigure(h, weight=1)
            for w in range(int(self.tw.get())+1):
                self.frame_grid.columnconfigure(w, weight=1)
                self.grid_dict[f"[{w},{h}]"] = tk.Button(self.frame_grid,
                                                    text="",
                                                    width=int((self.screen_width / 700) ),
                                                    height=int((self.screen_height / 700) ),)
                                                    #lambra function is maid with insperation from internet

                self.grid_dict[f"[{w},{h}]"].config(command=lambda b=self.grid_dict[f"[{w},{h}]"]: self.select_cell(b))
                self.grid_dict[f"[{w},{h}]"].grid(row=h, column=w, sticky="NSEW")


        for cell in self.grid.cells:
            self.grid_dict[str(cell)].config(bg="green")
    def next_step(self):
        #just like save calls the grids save method this calls the update method then changes the coulprs to show the new grid
        #Input: nothing
        #Output: new gen grid
        self.grid.update()

        for cell in self.grid_dict.keys():
            self.grid_dict[cell].config(bg="SystemButtonFace")

        for cell in self.grid.cells:

            self.grid_dict[str(cell)].config(bg="green")
    def toggle_play(self):
        #toggles the play button between start and pause and while it is in play the play method is runing
        #Input: from button
        #Output: runs or stops the play method
        if self.spela:
            self.spela = False
            self.btn_p.config(text="Start")

        else:
            self.spela = True
            self.btn_p.config(text="Pause")
            self.play()
    def play(self):
        #calls upen next step and then runs itself again after 500ms
        #it is realy weard on this level of programing but it runs in paralell with the rest of the program
        #Input: a toggle in toggle_play
        #Output: Runs the game continuesly untill toggled off

        if self.spela:
            self.next_step()
            self.task_id = self.root.after(500, self.play)
    def clear(self):
        #removes all cells from the grid and clears the list
        #input: nothing
        #output: clears the grid and list
        for cell in self.grid.cells:
            self.grid_dict[str(cell)].config(bg="SystemButtonFace")
        self.grid.cells = []




if __name__ == "__main__":

    app = App()
    app.root.mainloop()




