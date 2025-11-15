#daniel wickleus
#personligt prochekt till dd1310

#kriterier
#basicly game of life
#grid med celler
#en cell överlever om den har 2 eller 3 grannar annars dör den
#en tom cell som har 3 granar föder en ny cell


#VARNING: variabler som heter samma ord kan variera i stavning, jag är dyslektiker. samma variebel har korekt stavning men olika variabler kan variera
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
    __repr__ = __str__





class Grid:
    def __init__(self, width = 0, height=0, cells=[]):

        self.width = width
        self.height = height

        self.cells = cells
        self.grann_lista = {}




    def make_grid(self):
        #skapar en string som ska visa hur griden ser ut, borde mergas med print_grid
        grid = []
        for height in range(self.height):
            grid.append([])
            for width in range(self.width):

                grid[height].append("-")

        for cell in self.cells:
            grid[cell.y][cell.x]="*"





        return grid

    def print_grid(self):
        #printar ut en fin grid så att de går att se den
        for width in range(self.width):
            print("  ",width, end=" ")
        print()
        for i in range(self.width):
            print(i, self.grid[i])


    def grannar(self,cells):
        #skapar en dict med celler och gämför sen om avståndet till andra celler är 1 aka är ett steg ifrån
        #metoden måste inte vara i klassen men orkar inte flyta den och de funkar lika bra oavsät
        granceller ={}
        for cello in cells:#cello= cell one
            granceller[cello] = 0
            for cellt in cells:#cellt = cell two
                if abs(cello.y - cellt.y) <= 1 and abs(cello.x - cellt.x) <= 1 and(cello.y!=cellt.y or cello.x!=cellt.x) :
                    granceller[cello]+=1


        return(granceller)

        #räkna antalet grannar cellen har

    def födas(self):
        for cell in self.grann_lista:

                for hight in range(-1,2):
                    for width in range(-1, 2):

                        if not (hight == 0 and width == 0):#if looparna skulle kunna vara i en med and mellan sig men de blev oläsligt och de här är lite bättre
                            if not str(Cell(cell.x+width, cell.y+hight)) in list(str(i) for i in self.grann_lista.keys()):
                                if 0<cell.x+width< self.width and 0<=cell.y+hight< self.height:
                                    if not str(Cell(cell.x+width, cell.y+hight)) in str(self.cells):

                                        födas_alternativ = self.grannar(set(list(self.grann_lista.keys())+ [Cell(cell.x+width, cell.y+hight)]))
                                        födas_alternativ_granar = födas_alternativ[next(iter(set(födas_alternativ).difference(set(list(self.grann_lista.keys())))))]

                                        if födas_alternativ_granar ==3:
                                            self.cells.append(next(iter(set(födas_alternativ).difference(set(list(self.grann_lista.keys()))))))



                #döds alternativ tar dubleter och de måste fixas för annars ses sama ruta flera gånger

        # om tom ruta har mer än 3 grannar ska den födas

    def dö(self):
        for cell in self.grann_lista:
            if not (2 == self.grann_lista[cell] or self.grann_lista[cell]== 3) or not 0<=cell.x<= self.width or not 0<=cell.y<= self.height:
                self.cells.remove(cell)




        # om antalet grannar är mindre än mindre än 2 eller mer än 3 ska de dö

    def update(self):


        self.grann_lista = self.grannar(self.cells)
        self.dö()
        self.födas()

if __name__ == "__main__":
    test_grid = Grid(10,
                10,
                [

                    Cell(0,0),
                    Cell(0,1),
                    Cell(1,0),
                    Cell(1,1)
                ]
                )


    for i in range(5):
        test_grid.update()
        print(test_grid.cells)
        test_grid.grid = test_grid.make_grid()  # inte perfekt sätt att göra det men nu görs de så
        test_grid.print_grid()



