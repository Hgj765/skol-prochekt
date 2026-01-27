

#Daniel wickleus
#personligt prochekt till dd1310

#kriterier
    #basicly game of life
    #grid med celler
    #en cell överlever om den har 2 eller 3 grannar annars dör den
    #en tom cell som har 3 granar föder en ny cell


#VARNING: olika variabler som heter samma ord kan variera i stavning, jag är dyslektiker. samma variebel har korekt stavning men olika variabler kan variera även om de är samma ord
class Cell:
    #klassen är igentligen inte nödvendig men den är såpass integrerad i programet att ta bort den skulle ta massa tid och liksom orka
    #klassen är legit bara kordinater med x och y atribut
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'[{self.x},{self.y}]'
    __repr__ = __str__





class Grid:
    #klassen skapar och hanterar matrisen med celler
    def __init__(self, width=10, height=10, cells = []):

        self.width = width
        self.height = height

        self.cells = cells
        self.grann_lista = {}

        try:#läser in förvalda celler från fil
            with open("glidare.txt", "r") as f:
                file_c=f.readlines()
            try:
                for cell in range(0,len(file_c)):
                    file_c[cell]=file_c[cell].replace("\n","").split()

                for c in range(0, len(file_c)):  # c för cordinate men de blev oläsbart
                    if int(file_c[c][0]) > self.width:
                        self.width=(int(file_c[c][0]))
                    if int(file_c[c][1]) > self.height:
                        self.height=(int(file_c[c][1]))



                    self.cells.append(Cell(int(file_c[c][0]), int(file_c[c][1])))
            except:
                pass
        except:
            pass




    def make_grid(self):
        #skapar en string som ska visa hur griden ser ut, borde mergas med print_grid
        grid = []
        for height in range(self.height+1):
            grid.append([])
            for width in range(self.width+1):

                grid[height].append("-")

        for cell in self.cells:
            grid[cell.y][cell.x]="*"






        return grid

    def print_grid(self):
        #printar ut en fin grid så att de går att se den i consolen
        for width in range(self.width+1):
            print("   ",width, end="")
        print()
        for i in range(self.height+1):
            print(i, self.grid[i])

    def grannar(self,cells):
        #skapar en dict med celler och gämför sen om avståndet till andra celler är 1 aka är ett steg ifrån
        #metoden måste inte vara i klassen men orkar inte flyta den och de funkar lika bra oavsät
        granceller ={}
        for cello in cells:#cello= cell one
            granceller[cello] = 0
            for cellt in cells:#cellt = cell two
                if str(cello) != str(cellt):
                    #debuging prints
                    """print(cello, cellt,
                          cellt.y % (self.height ) ,
                          cello.y % (self.height),
                          cellt.x % (self.width ) ,
                          cello.x % (self.width ),
                          abs(int(cellt.y % (self.height +1)) - int(cello.y % (self.height+1))) <= 1,
                           abs(int(cellt.x % (self.width +1))- int(cello.x % (self.width +1))) <= 1,

                          (abs(int(cellt.y % (self.height +1)) - int(cello.y % (self.height+1)))%self.height <= 1 and
                           (abs(int(cellt.x % (self.width +1))- int(cello.x % (self.width +1))))%self.width <= 1),

                          granceller[cello])"""


                    if (abs(int(cellt.y % (self.height +1)) - int(cello.y % (self.height+1)))%self.height <= 1 and
                           (abs(int(cellt.x % (self.width +1))- int(cello.x % (self.width +1))))%self.width <= 1):
                        granceller[cello]+=1




        return(granceller)

        #räkna antalet grannar cellen har

    def födas(self):
        #om tom ruta har mer än 3 grannar ska den födas, funktionen klollar alla relevanta rutor och ser om de ska födas
        #jag hatar den här funktionen men den funkar
        for cell in self.grann_lista:
                for width in range(-1,2):
                    for hight in range(-1, 2):
                        curent_cell = Cell((cell.x+width)%(self.width+1),(cell.y+hight)%(self.height+1))#curent cell som i den som är relevant för tilfelet

                        if not (hight == 0 and width == 0):                                                                         #if looparna skulle kunna vara i en med and mellan sig men de blev oläsligt och blev marginelt bättre
                            if not (str(curent_cell) in list(str(i) for i in self.grann_lista.keys())):                                                         #ser till så cellen inte fins i grann_lista
                                    if str(curent_cell) not in str(self.cells):

                                        födas_alternativ = self.grannar( list(self.grann_lista.keys())+[curent_cell])
                                        födas_alternativ_granar = födas_alternativ[list(födas_alternativ.keys()-self.grann_lista.keys())[0]]

                                        if födas_alternativ_granar ==3:
                                            self.cells.append(list(födas_alternativ.keys()-self.grann_lista.keys())[0])

    def dö(self):
        #om antalet grannar är mindre än mindre än 2 eller mer än 3 ska de dö
        for cell in self.grann_lista:
            if not (2 == self.grann_lista[cell] or self.grann_lista[cell]== 3) or not 0<=cell.x<= self.width or not 0<=cell.y<= self.height:
                self.cells.remove(cell)

    def update(self):
        #borde igentligen heta stega eller next_step
        #funktionen går till nästa generation i spelet

        self.grid = self.make_grid()  # inte perfekt sätt att göra det men nu görs de så


        self.grann_lista = self.grannar(self.cells)
        self.dö()
        self.födas()

    def spara(self,x):#metoden behöver varken vara i en klass och andvends egentligen bara från Gui klassen men de kändes mer lämpligt att metoden som sparar griden var i samma klass som den skapas och hanteras i
        #funktionen sparar de valda cellerna
        with open("glidare.txt", "w") as f:
            for rad in x:
                skriv=str(int(rad.x))+" "+str(int(rad.y))+"\n"
                f.write(skriv)

    def ui(self):
        #text interfacet genom basic input och if satser
        self.grid=self.make_grid()
        self.print_grid()
        self.kör=True
        while self.kör:
            print("""Vill du
\t(1)-Gå till nästa generation
\t(2)-Rensa bort alla celler
\t(3)-Gå fram ett satt antal generationer
\t(4)-Spara de celler du har och avsluta programmet
                    """)
            try:
                val=int(input())
                if val==1:
                    self.update()
                    self.grid=self.make_grid()
                    self.print_grid()

                elif val==2:
                    self.cells = []
                    self.grid=self.make_grid()
                    self.print_grid()
                elif val==3:
                    antal=int(input("hur många generationer framåt vill du gå"))
                    try:
                        for i in range(antal):
                            self.update()
                        self.grid=self.make_grid()
                        self.print_grid()
                    except:
                        print("måste vara ett nummer")

                elif val==4:
                    self.spara(self.cells)
                else:
                    print("inte ett alternativ, måste vara inom 1-4")
            except:
                print("inte ett alternativ, måste vara en sifra")




if __name__ == "__main__":
    test_grid = Grid()
    test_grid.ui()





