#daniel wickleus
#personligt prochekt till dd1310

#kriterier
#basicly game of life
#grid med celler
#en cell överlever om den har 2 eller 3 grannar annars dör den
#en tom cell som har 3 granar föder en ny cell

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
    __repr__ = __str__
    """def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))"""




class Grid:
    def __init__(self, width, height, cells):

        self.width = width
        self.height = height

        self.cells = cells




    def make_grid(self):
        grid = []
        for height in range(self.height):
            grid.append([])
            for width in range(self.width):

                grid[height].append("-")

        for cell in self.cells:
            grid[cell.y][cell.x]="*"



        return grid

    def print_grid(self):
        for width in range(self.width):
            print("  ",width, end=" ")
        print()
        for i in range(self.width):
            print(i, self.grid[i])


    def grannar(self,cells):
        granceller ={}
        for cello in cells:#cello= cell one
            for cellt in cells:#cellt = cell two
                if abs(cello.y - cellt.y) <= 1 and abs(cello.x - cellt.x) <= 1 and(cello.y!=cellt.y or cello.x!=cellt.x) :

                    granceller[cello] = granceller.get(cello,0)+1
        return(granceller)

        #räkna antalet grannar cellen har

    def födas(self):
        for cell in self.grannlista:
            for hight in range(-1,2):
                for width in range(-1, 2):

                    if not (hight == 0 and width == 0):#if looparna skulle kunna vara i en med and mellan sig men de blev oläsligt och de här är lite bättre
                        if not str(Cell(cell.x+width, cell.y+hight)) in list(str(i) for i in self.grannlista.keys()):


                            if not str(Cell(cell.x+width, cell.y+hight)) in str(self.cells):

                                döds_alternativ = self.grannar(set(list(self.grannlista.keys())+ [Cell(cell.x+width, cell.y+hight)]))
                                döds_alternativ_granar = döds_alternativ[next(iter(set(döds_alternativ).difference(set(list(self.grannlista.keys())))))]

                                if döds_alternativ_granar >=3:
                                    self.cells.add(next(iter(set(döds_alternativ).difference(set(list(self.grannlista.keys()))))))
        print("\n\n\n")

                #döds alternativ tar dubleter och de måste fixas för annars ses sama ruta flera gånger

        # om tom ruta har mer än 3 grannar ska den födas

    def dö(self):
        for cell in self.grannlista:
            if not 2<=self.grannlista[cell] <=3:
                self.cells.remove(cell)




        # om antalet grannar är mindre än mindre än 2 eller mer än 3 ska de dö
grid = Grid(10,
            10,
            {
                Cell(2,3),
                Cell(3,3),
                Cell(3,2),
                Cell(2,2),
                Cell(1,2),
                Cell(9,9)
            }
            )


for i in range(10):
    print(grid.cells)
    grid.grid = grid.make_grid()  # inte perfekt sätt att göra det men nu görs de så
    grid.print_grid()


    grid.grannlista = grid.grannar(grid.cells)
    grid.dö()
    grid.födas()
print(grid.cells)
grid.grid = grid.make_grid()  # inte perfekt sätt att göra det men nu görs de så
grid.print_grid()



