
#Daniel wickleus
#personligt prochekt till dd1310

#kriteria
    #its just a game of life
    #grid with cells
    #a cell lives if it has 2 or 3 neighbours and dies otherwise
    #an empty cell is born if it has 3 neighbours


#warning: my spelling is shit so variebles might have the same word as names but with difrent spellings
#the vatieble gran_lista is in swedish becus the english version was to hard to spell and i dont like it so deal with it
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
    def __init__(self, width=10, height=10, cells = [],file="glidare.txt"):
        #Atribut: file,width, height(the size of the grid) and cells(the list of licing cells in the curent game)
        #innit creates the base structure of the grid
            #definites width and height
            #reading the file and adding saved cells
            #checks if there are cells outside of the grid and makes the grid larger if there are

        self.width = width
        self.height = height
        self.FILE = file

        self.cells = cells
        self.gran_list = {}

        #this sould be a function but when i tryed to make it a function everything blow up so maby later
        try:  # reads the file and adds the cells to self.cells
            with open(self.FILE, "r") as f:
                file_c = f.readlines()

            try:#makes sure that the grid is big enough to contain all the cells
                for cell in range(0, len(file_c)):
                    file_c[cell] = file_c[cell].replace("\n", "").split()

                for c in range(0, len(file_c)):  # c for coordinate but that is to long
                    if int(file_c[c][0]) > self.width:
                        self.width = (int(file_c[c][0]))
                    if int(file_c[c][1]) > self.height:
                        self.height = (int(file_c[c][1]))
                    new_cell=Cell(int(file_c[c][0]), int(file_c[c][1]))

                    if not any(str(new_cell) == str(i) for i in self.cells):
                        self.cells.append(new_cell)

            except:
                print("Error: somthing went wrong with the file")
        except:
            print("Error: No file found")

    def make_print_grid(self):
        # Prints the grid in the console in a nice way
        # Input: self.grid self.width self.height
        # Output: nothing but prints the grid
        #the name is realy weard becous it used to be 2 methods
        grid = []
        for height in range(self.height + 1):
            grid.append([])
            for width in range(self.width + 1):
                grid[height].append("-")

        for cell in self.cells:
            grid[cell.y][cell.x] = "*"

        for width in range(self.width + 1):
            print("", width, end="")
        print()

        for i in range(self.height+1):
            print(i, end=" ")
            for j in range(self.width + 1):
                print(grid[i][j], end=" ")
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
        #improvment potential: make a list so the boxes that have alrady been checke is not checked again(optimisation)

        #How it works: first there is a for loop for all the cells alive, then two foor loops from -1 to 1. ther is no point in checking boxes that dosent have neigbours so the boxes around the living cells are the only ones checked
            #then we define the new cell candidate as a cell obiect with the coordinates of the cell we are checking around plus width_add /hight_add
            #in the if staments it is first checked if the new cell has the same coordinates as the original cell, wich it is not alowed to have
                #then we ckeck if the new cell alrady exists in self.grann_lista
                #and we ckeck if it is in self.cells (i dont understand why it is needed to ckeck both self.cells and self.grann_lista bur if one of them is removed thing that souldnt be there start apearing)
            #then finaly, we add the new cell to a list coppy of self.grann_lista and then send it in to self.neighbours, the new list means we can use an alrady existing function to do the ckeck
            #when the ckeck is done ew simply extrackt the number from the list and see if it == 3
            #if it dose we add it to self.cells
        for cell in self.gran_list:
                for width_add in range(-1,2):
                    for hight_add in range(-1, 2):
                        curent_cell = Cell((cell.x+width_add)%(self.width+1),(cell.y+hight_add)%(self.height+1))

                        if not (hight_add == 0 and width_add == 0):  #the if statements sould be one but that is unreadeble
                            if not (str(curent_cell) in list(str(i) for i in self.gran_list.keys())):
                                    if str(curent_cell) not in str(self.cells):

                                        birth_alternativ = self.neighbours(list(self.gran_list.keys()) + [curent_cell])
                                        birth_alternativ_granar = birth_alternativ[list(birth_alternativ.keys() - self.gran_list.keys())[0]]

                                        if birth_alternativ_granar ==3:
                                            self.cells.append(list(birth_alternativ.keys() - self.gran_list.keys())[0])

    def die(self):
        #if cells naibour amount somthing other than 2 or 3 it is removed
        #also if the cell is outside of the grid it is removed but that sould be imposible so dont worry about it
        #Input: self.cells self.grann_lista self.width self.height
        #Output: nothing but removes cells that are to die
        for cell in self.gran_list:
            if not (2 == self.gran_list[cell] or self.gran_list[cell] == 3) or not 0 <= cell.x <= self.width or not 0 <= cell.y <= self.height:
                self.cells.remove(cell)

    def update(self):
        #sould be called next_spet or next_gen but this is good enough
        #function goes to the next generation of the game
        #Input: self.cells self.grann_lista self.width self.height
        #Output: nothing but updates self.cells
        #self.grann_lista is created so birth and die isnt effected by each other and can workin paralel
        #so there is a original state and a curent satte they can work with

        self.gran_list = self.neighbours(self.cells)

        self.die()
        self.birth()

    def save(self, cell_list):
        #function saves the curent cells to a file
        #Input: cell_list
        #Output: saves the cells to a file in the dum format we are told to use
        #I WHANT TO USE JSON, WHAT IS THIS SHIT FORMAT!!! >:(

        with open(self.FILE, "w") as f:
            for row in cell_list:
                f.write(str(int(row.x))+" "+str(int(row.y))+"\n")

def main_menue():
    #the main menue of the game
    #self is inputed so i dont have to change all the code that used to be in a class
    #Input: self
    #Output: runs the game
    self = Grid()
    self.make_print_grid()

    while True:
        print("""
\t(1)-Run game
\t(2)-Resice grid
\t(3)-Save current grid
\t(4)-Exit without saving
                """)
        try:
            chois=int(input())

            if chois==1:
                game_menue(self)
            elif chois==2:
                print("If there are cells outside of the grid the grid will be resized automaticly")
                w=input("How wide do you want the grid to be ")
                h=input("How high do you want the grid to be ")
                self.save(self.cells)
                self = Grid(int(w),int(h))
            elif chois==3:
                self.save(self.cells)
                print("Saved")
            elif chois==4:
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
    self.make_print_grid()


    print("""
    How many generations do you want to go forward per click(runing is very slow)
    
    """)
    try:
        choice_go ="somthing that isnt empty"
        chois_gen = int(input())
        while choice_go != "stop":
            for i in range(chois_gen):
                self.update()

            self.make_print_grid()
            choice_go = input("""whright stop if you whant to stop otherwise press enter
            """)

        else:
            print(
                "Not an alternative, must be number betwean 1-3")  # if the number they wright is not an alternative
    except:  # this is if they try to whight a somthing that is not a number
        print("Not an alternative, must be number")






if __name__ == "__main__":

    main_menue()





