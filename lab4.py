# Namn Daniel wickleus och Erik guve
# Datum 2025-09-18
# Kurskod DD1310

# En kort beskrivning av programmet.
#tre i rad
from random import randint

def skriv_ut_spelplan(spelplan):
    """Skriver ut spelplanen
    Använder sig av "Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character
    Inparameter: spelplan (matris)
    Returvärde: Inget
    """

    print('    A   B   C  ')
    print('  ┏━━━┳━━━┳━━━┓')
    rad_räknare = 0
    for rad in spelplan:
        rad_räknare += 1
        print(str(rad_räknare) + ' ┃', end=' ')
        for ruta in rad:
            print('' + ruta, end=' ')
            print('┃', end=' ')
        print()
        if rad_räknare < 3:  # Efter sista raden vill vi inte göra detta
            print('  ┣━━━╋━━━╋━━━┫')
    print('  ┗━━━┻━━━┻━━━┛')  # Utan istället detta            if "" not in rad:


def kontrollera_rader(spelplan):
    for rad in spelplan:
        if ' ' not in rad:  # Vi vill inte att tre tomma rutor ska räknas som vinst
            if rad[0] == rad[1] == rad[2]:
                return True

    return False


def kontrollera_kolumner(spelplan):
    """Kontrollerar om det finns tre likadana tecken på någon kolumn och returnerar då True, annars False
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    for kolumn in range(0,len(spelplan)):

        if spelplan[0][kolumn] == spelplan[1][kolumn] == spelplan[2][kolumn] and ' ' not in [spelplan[2][kolumn], spelplan[1][kolumn], spelplan[0][kolumn]]:
            return True

    return False



def kontrollera_diagonaler(spelplan):
    if ' ' not in [spelplan[2][0], spelplan[1][1], spelplan[0][2]] and spelplan[2][0] == spelplan[1][1] == spelplan[0][2] or ' ' not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]] and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]:
        return True
    else:
        return False


def är_oavgjort(spelplan):
    if kontrollera_rader(spelplan) or kontrollera_diagonaler(spelplan) or kontrollera_kolumner(spelplan):
        return False
    for rad in spelplan:
        for element in rad:
            if element == ' ':
                return False
    return True


def tolka_inmatning(inmatning):
    """
    Tar emot en sträng som anger en position på spelplanen och returnerar
    rad och kolumn som vi kan indexera med i vår spelplan, exempel:
    A1 -> 0,0
    B3 -> 2,1
    Inparameter: spelplan (matris)
    Returvärde: rad, kolumn (heltal, heltal)
    """
    bokstav = inmatning[0].upper()
    if 1<= int(inmatning[1]) <=3:
        rad = int(inmatning[1]) - 1

    if bokstav == 'A':
        kolumn = 0
    elif bokstav == 'B':
        kolumn = 1
    elif bokstav == 'C':
        kolumn = 2
    return rad, kolumn



def playerinput(inmatning, spelplan):
    #taks the input from the player and makes sure it is corect and the chosen spot alrady taken
    while True:
        try:
            rad, kolumn = tolka_inmatning(inmatning)
            break
        except:
            inmatning = input("Inte en ruta i spelet Välj igen (A-C)(1-3)")



    if spelplan[rad][kolumn] == " ":
        return rad, kolumn

    elif spelplan[rad][kolumn]!= " ":
        inmatning = input("rutan är redan vald välj igen")
        rad, kolumn = playerinput(inmatning, spelplan)
        return rad, kolumn



def spela(spelarnamn_1, spelarnamn_2):
    #startar och kör spelet

    print("Då kör vi!")
    print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
    spelplan = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    spelarlista = [spelarnamn_1, spelarnamn_2]
    vems_tur = randint(0,3)


    while True:
        vems_tur = (vems_tur + 1) % 2  # vems_tur ska aldrig bli 2, utan börja om igen på 0, %-är modul dvs resten vid heltals division.

        skriv_ut_spelplan(spelplan)
        if vems_tur == 0:
            markör = 'X'
        else:
            markör = 'O'

        inmatning = input(str(spelarlista[vems_tur]) + "s tur att spela: ")
        rad, kolumn = playerinput(inmatning,spelplan)

        spelplan[rad][kolumn] = markör#rediskerar dicten


        if kontrollera_rader(spelplan) or kontrollera_diagonaler(spelplan) or kontrollera_kolumner(spelplan):
            skriv_ut_spelplan(spelplan)
            print(str(spelarlista[vems_tur]) + " är vinnare!! ")
            break
        elif är_oavgjort(spelplan):
            print(är_oavgjort(spelplan))
            skriv_ut_spelplan(spelplan)
            print("Det blev är_oavgjort!")
            break




def huvudfunktion():
    #tar input och startar den faktiska huvud funktionen
    print("Hej och väkommen till Tre-i-rad!")
    spelarnamn_1 = input("Vad heter spelare 1? ")

    spelarnamn_2 = input("Vad heter spelare 2? ")

    spela(spelarnamn_1, spelarnamn_2)

huvudfunktion()