import time
import tkinter as tk
from Game_of_life import *

#guit är till stor del åter andvänt från en gymnasie upgift,
#om strukturen värkar skit konstig fins de en risk att de är därför


class App():
    #klassen är för tkinter fönstret som visar spel planen
    def __init__(self,root=tk.Tk()):
        #de skumaste guit jag någonsin gort
        #basicly de är bara ett tkinter gui till Game_of_life
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


        self.frame1 = tk.LabelFrame(self.root)
        self.frame1.grid(row=0,column=0,sticky="NW")

        self.frame2 = tk.LabelFrame(self.root)
        self.frame2.grid(row=1, column=0, sticky="Nw")

        self.frame_grid = tk.LabelFrame(self.root)
        self.frame_grid.grid(row=0, column=1, sticky="NW", rowspan=2)

        self.bygg_fönstret()

        self.new_grid()
    def bygg_fönstret(self):
        #den här funktionen fins enbart för att korta ned init
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

        self.btn_s = tk.Button(self.frame1, text="Save and exit", width=16, command=self.stop)
        self.btn_s.grid(row=7, sticky="nw")

        self.name = tk.Label(self.frame2, text="updatera grid stolek", bg="blue", fg="white")
        self.name.grid(row=0)
        self.name = tk.Label(self.frame2, text="Bred")
        self.name.grid(row=1)
        self.name_entry = tk.Entry(self.frame2, textvariable=self.tw)
        self.name_entry.grid(row=2)
        self.name = tk.Label(self.frame2, text="Höjd")
        self.name.grid(row=3)
        self.name_entry = tk.Entry(self.frame2, textvariable=self.th)
        self.name_entry.grid(row=4)
        self.btn = tk.Button(self.frame2, text="Update grid", width=16, command=self.new_grid)
        self.btn.grid(row=5, sticky="nw")

    def stop(self):
        #sparar de valda cellerna och avslutar programmet
        self.grid.spara(self.grid.cells)
        self.root.destroy()

    def select_cell(self, button):
        #när en cell klickas blir den antingen vald eller avvald, den här funktionen holler koll på de
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
        #funktionen skapar eller skalar om griden genom att först ta bort allt som redan är där och lägger in de igen
        for c in range(0, len(self.grid.cells)):  # c för cordinate men de blev oläsbart

            if self.grid.cells[c].x > self.grid.width:
                self.tw.set(self.grid.cells[c].x)

            if self.grid.cells[c].y > self.grid.height:
                self.th.set(self.grid.cells[c].y)


        self.grid_dict = {}



        for widget in self.frame_grid.winfo_children():
            widget.destroy()

        self.grid.height  = int(self.th.get())
        self.grid.width = int(self.tw.get())


        self.frame_grid = tk.LabelFrame(self.root)
        self.frame_grid.grid(row=0, column=1, sticky="NW", rowspan=2)

        for h in range(int(self.th.get())+1):
            for w in range(int(self.tw.get())+1):
                self.grid_dict[f"[{w},{h}]"] = tk.Button(self.frame_grid,
                                                    text="",
                                                    width=int((self.screen_width / 30) / self.grid.width),
                                                    height=int((self.screen_height / 30) / self.grid.height),
                                                    )
                                                    #lambda funktionen är gord med insperation från internet
                self.grid_dict[f"[{w},{h}]"].config(command=lambda b=self.grid_dict[f"[{w},{h}]"]: self.select_cell(b))
                #self.grid_dict[f"[{w},{h}]"].config(command=self.select_cell(self.grid_dict[f"[{w},{h}]"]))
                self.grid_dict[f"[{w},{h}]"].grid(row=h, column=w, sticky="nw")


        for cell in self.grid.cells:
            self.grid_dict[str(cell)].config(bg="green")


    def next_step(self):

        self.grid.update()

        for cell in self.grid_dict.keys():
            self.grid_dict[cell].config(bg="SystemButtonFace")

        for cell in self.grid.cells:

            self.grid_dict[str(cell)].config(bg="green")





    def toggle_play(self):
        #togglar om spelet fortsäter frammåt(kallar på next_step)
        if self.spela:
            self.spela = False
            self.btn_p.config(text="Start")

        else:
            self.spela = True
            self.btn_p.config(text="Pause")
            self.play()


    def play(self):
        #kallar på next_step och sen sig sielv med 0.5s delay
            #kör bara om self.spela == True
        #med insperation från internet
        if self.spela:
            self.next_step()
            self.task_id = self.root.after(500, self.play)



    def clear(self):
        #tar bort alla valda celler
        for cell in self.grid.cells:
            self.grid_dict[str(cell)].config(bg="SystemButtonFace")
        self.grid.cells = []




if __name__ == "__main__":

    app = App()
    app.root.mainloop()




