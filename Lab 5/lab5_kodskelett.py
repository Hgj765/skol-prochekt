# skriven av daniel wikcleus och erika erwin 2025-09-23
#tar en input från filen "lab5_in_felfri.txt och bästemer top 3 höksta poäng

"""
Lab 5 - Läser in resultat från en pilkastningstävling som finns lagrade på en fil och hanterar fel som kan finnas där.
"""
from types import NoneType


def hantera_rad(rad_sträng):
    """ Tar emot en rad i form av en sträng och returnerar en tupel bestående av ett namn (sträng) 
        och ett resultat (int) i den ordningen, alternativt returnerar den None, om raden är ogiltig.

        Alla rader som inte består av ett namn (minst ett tecken) och ett heltal med komma emellan är ogiltiga 

        Inparameter:    rad_sträng (str)
        Returvärde:     None eller en tupel med namn och poäng (tuple)
    """
    try:

        uppdelad_rad = rad_sträng.split(",")

        if (uppdelad_rad[0]) == "\n":
            print("Rad ignorerad pga:", "Tom rad")
            raise NoneType
        elif len(uppdelad_rad) != 2 :
            print("Rad ignorerad pga:", "Fel antal delar")
            raise ValueError

        namn = uppdelad_rad[0].strip()
        poäng_sträng = int(uppdelad_rad[1].strip())

        if not 0 <= poäng_sträng <=50 :
            print("Rad ignorerad pga:", "Ogiltig poäng")
            raise ValueError
        if namn == "":
            print("Rad ignorerad pga", "Namn saknas")
            raise ValueError


        return (namn, int(poäng_sträng))
    except NoneType:
        pass
    except ValueError:
        pass
    except IndexError:
        print ("Rad ignorerad pga", "Namn eller Poäng saknas")






def läs_resultat_från_fil(filnamn):
    resultat=[]
    """ Läser ifrån en fil och returnerar en lista av tupler som innehåller alla giltiga resultat från filen.
        Ska använda sig av funktionen hantera_rad()

        Inparameter:    ett filnamn (str)
        Returvärde:     en lista av tupler (list)
    """
    with open(filnamn, "r") as fil:
        for rad in fil:
            try:
                resultat.append(hantera_rad(rad))
            except:
                pass
    return resultat

def ta_ut_top_3(resultat):
    """ Tar emot en lista som sorteras. Därefter returneras de tre bästa resultaten.

        Inparameter:    lista av tupler (list)
        Returvärde:     en potentiellt kortare lista av tupler (list)
    """
    return sorted(resultat, key = lambda namn_poäng_par : namn_poäng_par[1], reverse = True)[:3]

def skriv_resultat_till_fil(top_3):
    """ Skriver ut top 3 till en annan textfil

        Inparameter:    lista av tupler (list)
    """
    with open("top3.txt", "w") as fil:
        for rad in top_3:
            fil.write(f"{rad[0]}, {rad[1]}\n")

def main():
    """ Huvudfunktion"""

    filnamn = "lab5_in_felfri.txt"
    resultat = läs_resultat_från_fil(filnamn)

    top_3 = ta_ut_top_3(resultat)
    skriv_resultat_till_fil(top_3)

    print()
    print("Top 3:")
    for par in top_3:
        print(par[0],":",par[1])

#main()
with open("lab5_in_felfri.txt", "r") as fil:
    text=fil.readlines()

for i in text:
    print(i.strip())