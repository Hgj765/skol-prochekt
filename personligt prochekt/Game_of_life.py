
#Daniel wickleus
#personligt prochekt till dd1310

#kriteria
    #its just a game of life
    #grid with cells
    #a cell lives if it has 2 or 3 neighbours and dies otherwise
    #an empty cell is born if it has 3 neighbours


#warning: my spelling is shit so variebles might have the same word as names but with difrent spellings
class Cell:
    #this class in compleatly useless but cant be bothers removing it
    #it is just to create obiects with x and y coordinates
    #Atritbutes: x,y

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x},{self.y}]'
    __repr__ = __str__

class Grid:
    #the class creates the grid and manages the game
    #attributes: width, height, cells(a list of cell obiects that are just used as coordinates)
    def __init__(self, width=10, height=10, cells = []):
        #innit creates the base structure of the grid
            #definites width and height
            #reading the file and adding saved cells
            #checks if there are cells outside of the grid and makes the grid larger if there are

        self.width = width
        self.height = height

        self.cells = cells
        self.grann_lista = {}

        #this sould be a function but when i tryed to make it a function everything blow up so maby later
        try:  # reads the file and adds the cells to self.cells
            with open("glidare.txt", "r") as f:
                file_c = f.readlines()

            try:#makes sure that the grid is big enough to contain all the cells
                for cell in range(0, len(file_c)):
                    file_c[cell] = file_c[cell].replace("\n", "").split()

                for c in range(0, len(file_c)):  # c för cordinate men de blev oläsbart
                    if int(file_c[c][0]) > self.width:
                        self.width = (int(file_c[c][0]))
                    if int(file_c[c][1]) > self.height:
                        self.height = (int(file_c[c][1]))

                    self.cells.append(Cell(int(file_c[c][0]), int(file_c[c][1])))
            except:
                print("Error: något är fell med inläsningen från filen")
        except:
            print("Error: hitade ingen fil")


    def make_grid(self):
        #was meaning to merge this with print_grid but somthing broke catastrificly so i left it like this
        # makes a list to show how the grid looks like
        #Input: self.grid self.width self.height
        #Output: a list of lists with the grid
        grid = []
        for height in range(self.height + 1):
            grid.append([])
            for width in range(self.width + 1):
                grid[height].append("-")

        for cell in self.cells:

            grid[cell.y][cell.x] = "*"

        return grid

    def print_grid(self):
        # Prints the grid in the console in a nice way
        # Input: self.grid self.width self.height
        # Output: nothing but prints the grid

        for width in range(self.width + 1):
            print("", width, end="")
        print()

        for i in range(self.height+1):
            print(i, end=" ")
            for j in range(self.width + 1):
                print(self.grid[i][j], end=" ")
            print("")

    def neighbours(self, cells):

        #creates a dict with the number of neighbours a cell has
        #finds the number of neighbours a cell has by taking the cell and checking if another cell has the same x and y coordinate +-1 (so 2,2 would chech 1,1 2,1 3,1 1,2 3,2 1,3 2,3 3,3)
        #Input: cells a list of cells
        #Output: a dict with the key being the cordinates of the cell and the value being the number of neighbours

        granceller ={}#neighbour_cells is to long is use swedish insted
        for cell_1 in cells:
            granceller[cell_1] = 0
            for cell_2 in cells:
                if str(cell_1) != str(cell_2):
                    #debuging prints
                    """print(cell_1, cell_2,
                          cell_2.y % (self.height ) ,
                          cell_1.y % (self.height),
                          cell_2.x % (self.width ) ,
                          cell_1.x % (self.width ),
                          abs(int(cell_2.y % (self.height +1)) - int(cell_1.y % (self.height+1))) <= 1,
                           abs(int(cell_2.x % (self.width +1))- int(cell_1.x % (self.width +1))) <= 1,

                          (abs(int(cell_2.y % (self.height +1)) - int(cell_1.y % (self.height+1)))%self.height <= 1 and
                           (abs(int(cell_2.x % (self.width +1))- int(cell_1.x % (self.width +1))))%self.width <= 1),

                          granceller[cell_1])"""


                    if (abs(int(cell_2.y % (self.height +1)) - int(cell_1.y % (self.height+1)))%self.height <= 1 and
                           (abs(int(cell_2.x % (self.width +1))- int(cell_1.x % (self.width +1))))%self.width <= 1):
                        granceller[cell_1]+=1




        return(granceller)

    def birth(self):
        #checks if an empty cell has 3 neighbours
        #this method sucks but it works
        #Input: self.cells self.grann_lista self.width self.height
        #Output: nothing but adds the new cells to self.cells

        for cell in self.grann_lista:
                for width in range(-1,2):
                    for hight in range(-1, 2):
                        curent_cell = Cell((cell.x+width)%(self.width+1),(cell.y+hight)%(self.height+1))

                        if not (hight == 0 and width == 0):
                            if not (str(curent_cell) in list(str(i) for i in self.grann_lista.keys())):
                                    if str(curent_cell) not in str(self.cells):

                                        födas_alternativ = self.neighbours(list(self.grann_lista.keys()) + [curent_cell])
                                        födas_alternativ_granar = födas_alternativ[list(födas_alternativ.keys()-self.grann_lista.keys())[0]]

                                        if födas_alternativ_granar ==3:
                                            self.cells.append(list(födas_alternativ.keys()-self.grann_lista.keys())[0])

    def die(self):
        #if cell not 2<=naiburs<=3 then it dies (removes it from cells)
        #Input: self.cells self.grann_lista self.width self.height
        #Output: nothing but removes cells that are to die
        for cell in self.grann_lista:
            if not (2 == self.grann_lista[cell] or self.grann_lista[cell]== 3) or not 0<=cell.x<= self.width or not 0<=cell.y<= self.height:
                self.cells.remove(cell)

    def update(self):
        #sould be called next_spet or next_gen but this is good enough
        #function goes to the next generation of the game
        #Input: self.cells self.grann_lista self.width self.height
        #Output: nothing but updates self.cells

        self.grid = self.make_grid()  # inte perfekt sätt att göra det men nu görs de så


        self.grann_lista = self.neighbours(self.cells)
        self.die()
        self.birth()

    def spara(self, cell_list):
        #function saves the curent cells to a file
        #Input: cell_list
        #Output: saves the cells to a file in the dum format we are told to use
        #I WHANT TO USE JSON, WHAT IS THIS SHIT!!! >:(

        with open("glidare_1.txt", "w") as f:
            for rad in cell_list:
                skriv=str(int(rad.x))+" "+str(int(rad.y))+"\n"
                f.write(skriv)

def main_menue(self):
    #the main menue of the game
    #self is inputed so i dont have to change all the code that used to be in a class
    #Input: self
    #Output: runs the game
    self.grid = self.make_grid()
    self.print_grid()

    while True:
        print("""
\t(1)-Run game
\t(2)-Save current grid
\t(3)-Exit without saving
                """)
        try:
            chois=int(input())

            if chois==1:
                game_menue(self)
            elif chois==2:
                self.spara(self.cells)
                print("Saved")
            elif chois==3:
                print("Exiting")
                break

            else:
                print("Not an alternative, must be number betwean 1-3") #if the number they wright is not an alternative
        except:                                                         #this is if they try to whight a somthing that is not a number
            print("Not an alternative, must be number")

def game_menue(self):
    #text ui for the game
    #Input: self
    #Output: runs the game
    self.grid = self.make_grid()
    self.print_grid()


    print("""
    How many generations do you want to go forward per click(runing is very slow)
    
    """)
    try:
        choice_go ="asd"
        chois_gen = int(input())
        while choice_go != "stop":
            for i in range(chois_gen):
                self.update()

            self.grid = self.make_grid()
            self.print_grid()
            choice_go = input("""whright stop if you whant to stop otherwise press enter
            """)

        else:
            print(
                "Not an alternative, must be number betwean 1-3")  # if the number they wright is not an alternative
    except:  # this is if they try to whight a somthing that is not a number
        print("Not an alternative, must be number")






if __name__ == "__main__":
    test_grid = Grid()
    main_menue(test_grid)





